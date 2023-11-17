from __future__ import annotations

import contextlib
import functools
import json
from dataclasses import dataclass, field
from functools import cached_property
from http.cookiejar import LWPCookieJar
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import urljoin

from requests import Session

from .common import bs4_html, get_all_values_from_form

if TYPE_CHECKING:
    from requests import Response

    from .credentials import Credentials


def handle_cookies_and_login(func):
    @functools.wraps(func)
    def inner(self: SmartSchool, *args, **kwargs):
        if self.creds is None:
            raise RuntimeError("Please start smartschool first via: `SmartSchool.start(PathCredentials())`")

        resp = func(self, *args, **kwargs)

        did_a_login = False
        if resp.url.endswith("/login") and not self.already_logged_on:
            self.already_logged_on = True  # Prevent loops
            resp = self._do_login(resp)
            did_a_login = True

        assert not resp.url.endswith("/login"), "Still login?"

        if did_a_login:
            resp = func(self, *args, **kwargs)

        self._session.cookies.save(ignore_discard=True)

        return resp

    return inner


@dataclass
class SmartSchool:
    creds: Credentials = None

    already_logged_on: bool = field(init=False, default=False)
    _session: Session = field(init=False, default_factory=Session)

    @classmethod
    def start(cls, creds: Credentials) -> None:
        global session

        creds.validate()
        session.creds = creds

    def __post_init__(self):
        self._session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"

        cookie_jar = LWPCookieJar(Path.cwd() / "cookies.txt")
        with contextlib.suppress(FileNotFoundError):
            cookie_jar.load(ignore_discard=True)

        self._session.cookies = cookie_jar

    def create_url(self, url: str) -> str:
        return urljoin(self._url, url)

    @handle_cookies_and_login
    def post(self, url, *args, **kwargs) -> Response:
        return self._session.post(self.create_url(url), *args, **kwargs)

    @handle_cookies_and_login
    def get(self, url, *args, **kwargs) -> Response:
        return self._session.get(self.create_url(url), *args, **kwargs)

    def json(self, url, *args, method: str = "get", **kwargs) -> dict:
        """Sometimes this is double json-encoded. So we keep trying until it isn't a string anymore."""
        if method.lower() == "post":
            r = self.post(url, *args, **kwargs)
        else:
            r = self.get(url, *args, **kwargs)

        json_ = r.text

        while isinstance(json_, str):
            json_ = json.loads(json_)

        return json_

    def _do_login(self, response: Response) -> Response:
        html = bs4_html(response)
        inputs = get_all_values_from_form(html, 'form[name="login_form"]')

        final = 0
        data = {}
        for input_ in inputs:
            if "username" in input_["name"]:
                data[input_["name"]] = self.creds.username
                final |= 1
            elif "password" in input_["name"]:
                data[input_["name"]] = self.creds.password
                final |= 2
            else:
                data[input_["name"]] = input_["value"]

        assert final == 3, "We're missing something here!"

        return self.post(response.url, data=data)

    @cached_property
    def _url(self) -> str:
        return "https://" + self.creds.main_url

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(for: {self.creds.username})"


session: SmartSchool = SmartSchool()
