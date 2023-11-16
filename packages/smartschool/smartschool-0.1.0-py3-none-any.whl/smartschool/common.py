from __future__ import annotations

import contextlib
import functools
import inspect
import json
import operator
import platform
import re
import smtplib
import sys
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum, auto
from pathlib import Path
from typing import Callable, Literal

from bs4 import BeautifulSoup, FeatureNotFound
from requests import Response

CACHE = Path(__file__).parent / ".cache"


__all__ = [
    "send_email",
    "CACHE",
    "capture_and_email_all_exceptions",
    "save",
    "IsSaved",
    "bs4_html",
    "get_all_values_from_form",
    "make_filesystem_safe",
    "as_float",
]

_used_bs4_option = None


class IsSaved(Enum):
    NEW = auto()
    UPDATED = auto()
    SAME = auto()


def save(
    type_: Literal["agenda", "punten", "todo"], course_name: str, id_: str, data: dict | str, is_eq: Callable = operator.eq, extension: str = "json"
) -> IsSaved | dict:
    save_as = CACHE / f"_{type_}/{course_name}/{id_}.{extension}"
    save_as.parent.mkdir(exist_ok=True, parents=True)
    data_was_dict = isinstance(data, dict)

    if data_was_dict:
        to_write = json.dumps(data, indent=4)
    else:
        to_write = data

    if not save_as.exists():
        save_as.write_text(to_write, encoding="utf8")
        return IsSaved.NEW

    old_data = save_as.read_text(encoding="utf8")
    if data_was_dict:
        old_data = json.loads(old_data)

    if is_eq(data, old_data):
        return IsSaved.SAME

    save_as.write_text(to_write, encoding="utf8")
    return old_data


def send_email(
    subject: str,
    text: str,
    email_to: list[str] | str,
    email_from: str,
):
    if isinstance(email_to, str):
        email_to = [email_to]

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = email_from
    message["To"] = ", ".join(email_to)
    message.attach(MIMEText(text, "plain", "utf8"))

    print(f"Sending email >> {subject}")

    if platform.system() == "Windows":
        print("=================== On Linux we would have sent this: ===================")
        print(message.as_string())
        print("=========================================================================")
        return  # I put this here, so I can still debug 'message.as_string()'

    with smtplib.SMTP("localhost") as server:
        server.sendmail(
            from_addr=email_from,
            to_addrs=email_to,
            msg=message.as_string(),
        )


def capture_and_email_all_exceptions(func, email_from: str | list[str], email_to: str | list[str]) -> Callable:
    @functools.wraps(func)
    def inner(*args, **kwargs):
        frm = inspect.stack()[1]
        module_name = Path(frm.filename)
        function_signature = f"{module_name.stem}.{func.__name__}"

        print(f"[{function_signature}] Start")
        try:
            result = func(*args, **kwargs)
        except Exception as ex:
            print(f"[{function_signature}] An exception happened: {ex}")

            send_email(
                email_to=email_to,
                email_from=email_from,
                subject="Salco parser: something went wrong!!",
                text="".join(traceback.format_exception(None, ex, ex.__traceback__)),
            )

            sys.exit(1)

        print(f"[{function_signature}] Finished")
        return result

    return inner


def bs4_html(html: str | bytes | Response) -> BeautifulSoup:
    global _used_bs4_option

    if isinstance(html, Response):
        html = html.text

    possible_options = [
        _used_bs4_option,
        {"parser": "html.parser", "features": "lxml"},
        {"features": "html5lib"},
        {"features": "html.parser"},
    ]

    for kw in possible_options:
        if kw is None:
            continue

        with contextlib.suppress(FeatureNotFound):
            parsed = BeautifulSoup(html, **kw)
            _used_bs4_option = kw
            return parsed

    _used_bs4_option = {}
    return BeautifulSoup(html)


def get_all_values_from_form(html, form_selector):
    form = html.select(form_selector)
    assert len(form) == 1, f"We should have only 1 form. We got {len(form)}!"
    form = form[0]

    # action = form.attrs.get("action").lower()
    # method = form.attrs.get("method", "get").lower()
    all_inputs = form.find_all(["input", "button", "textarea", "select"])

    inputs = []
    for input_tag in all_inputs:
        tag_name = input_tag.name.lower()
        attrs = input_tag.attrs

        if "name" not in attrs:
            continue

        if tag_name != "select":
            inputs.append(
                {
                    "name": attrs.get("name"),
                    "value": attrs.get("value", ""),
                }
            )
        else:  # select
            raise ValueError("Check if this code works. Possible issue with getting the value if the value tag isn't set.")

            select_options = []
            value = ""
            for select_option in input_tag.find_all("option"):
                option_value = select_option.attrs.get("value")
                if option_value:
                    select_options.append(option_value)
                    if "selected" in select_option.attrs:
                        value = option_value
            if not value and select_options:
                # if the default is not set, and there are options, take the first option as default
                value = select_options[0]
            # add the select to the inputs list
            inputs.append({"name": attrs.get("name"), "values": select_options, "value": value})

    return inputs


def make_filesystem_safe(name: str) -> str:
    return re.sub("[^-_a-z0-9.]+", "", name, flags=re.IGNORECASE)


def as_float(txt: str) -> float:
    return float(txt.replace(",", "."))
