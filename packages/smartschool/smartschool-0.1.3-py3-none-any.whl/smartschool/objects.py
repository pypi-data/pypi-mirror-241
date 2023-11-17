from __future__ import annotations

import base64
from datetime import date, datetime
from typing import Annotated, Literal

from pydantic import BeforeValidator
from pydantic.dataclasses import Field, dataclass

from .common import as_float
from .session import session


def convert_to_datetime(x: str | datetime) -> datetime:
    if isinstance(x, datetime):
        if x.tzinfo is None:
            raise ValueError("No timezone information found in this date")
        return x

    try:
        return datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:  # 2023-11-16 08:24
        return datetime.strptime(x, "%Y-%m-%d %H:%M")


def convert_to_date(x: str | date | datetime) -> date:
    if isinstance(x, datetime):
        return x.date()
    if isinstance(x, date):
        return x

    return datetime.strptime(x, "%Y-%m-%d").date()


Url = Annotated[str, BeforeValidator(lambda x: session.create_url(x))]
Date = Annotated[date, BeforeValidator(convert_to_date)]
DateTime = Annotated[datetime, BeforeValidator(convert_to_datetime)]


@dataclass
class CourseGraphic:
    type: Literal["icon"]
    value: str


@dataclass
class ResultGraphic:
    type: Literal["percentage"]
    color: Literal["green", "red"]
    value: int
    description: str

    @property
    def achieved_points(self) -> float:
        return as_float(self.description.split("/")[0])

    @property
    def total_points(self) -> float:
        return as_float(self.description.split("/")[1])


@dataclass
class PersonDescription:
    startingWithFirstName: str = ""
    startingWithLastName: str = ""


@dataclass
class _User:
    id: str
    pictureHash: str
    pictureUrl: Url
    description: PersonDescription
    name: PersonDescription
    sort: str


@dataclass
class DateRange:
    start: DateTime
    end: DateTime


@dataclass
class SkoreWorkYear:
    id: int
    dateRange: DateRange


@dataclass
class Class_:
    identifier: str
    id: int
    platformId: int
    name: str
    type: str
    icon: str


@dataclass
class Period:
    id: int
    name: str
    icon: str
    skoreWorkYear: SkoreWorkYear
    isActive: bool
    class_: Class_ = Field(alias="class")


@dataclass
class Component:
    id: int
    name: str
    abbreviation: str


Teacher = _User
Student = _User


@dataclass
class Course:
    id: int
    name: str
    graphic: CourseGraphic
    teachers: list[Teacher]
    skoreClassId: int
    parentCourseId: None | int
    skoreWorkYear: SkoreWorkYear
    class_: Class_ = Field(alias="class")


@dataclass
class Feedback:
    text: str
    user: Teacher


@dataclass
class FeedbackFull:
    attachments: list[str]
    changedAt: DateTime
    createdAt: DateTime
    evaluationId: str
    id: str
    student: Student
    teacher: Teacher
    text: str


@dataclass
class Result:
    identifier: str
    type: Literal["normal"]
    name: str
    graphic: ResultGraphic
    date: DateTime

    gradebookOwner: Teacher
    component: Component
    courses: list[Course]
    period: Period
    feedback: list[Feedback]
    feedbacks: list[FeedbackFull]
    availabilityDate: DateTime
    isPublished: bool
    doesCount: bool


@dataclass
class ResultDetails:
    centralTendencies: list[str]
    teachers: list[Teacher]
    dateChanged: DateTime
    userChanged: Teacher
    class_: Class_ = Field(alias="class")


@dataclass
class ResultWithDetails(Result):
    details: ResultDetails


@dataclass
class CourseCondensed:
    name: str
    teacher: str
    url: Url

    descr: str = Field(repr=False, default="")
    icon: str = Field(repr=False, default="")


@dataclass
class FutureTaskOneTask:
    label: str
    description: str
    icon: str
    warning: bool
    click_handle: str
    activityID: int
    dateID: str
    assignmentID: str
    endMomentTS: None
    startMomentID: str
    endMomentID: str
    lessonID: str
    type: str
    classID: str
    course: str
    date: Date
    hourID: str


@dataclass
class FutureTaskOneItem:
    tasks: list[FutureTaskOneTask]
    materials: list[str]


@dataclass
class FutureTaskOneCourse:
    lessonID: str
    hourID: str
    classID: str
    course_title: str
    items: FutureTaskOneItem


@dataclass
class FutureTaskOneDay:
    date: Date
    pretty_date: str
    courses: list[FutureTaskOneCourse]


@dataclass
class FutureTasks:
    """
    Class that interfaces the retrieval of any task that needs to be made in the near future.

    Example:
    -------
    >>> for day in FutureTasks().days:
    >>>     for course in day.courses:
    >>>         print("Course:", course.course_title)
    >>>         for item in course.items:
    >>>             for task in item.tasks:
    >>>                 print("Task:", task.description)
    Course: 2 - AAR1, Lotte Peeters
    Task: Toets 3. De koolstofcyclus in het systeem aarde pagina 42 - 47
    """

    days: list[FutureTaskOneDay] = Field(default_factory=list)
    last_assignment_id: int = 0
    last_date: Date = Field(default_factory=date.today)

    def __post_init__(self):
        """I need to do this here because when I do it in Agenda, it'll not lazily load it. But in this way, I load it on construction."""
        json = session.json("/Agenda/Futuretasks/getFuturetasks")

        self.days = []
        for d in json["days"]:
            self.days.append(FutureTaskOneDay(**d))

        self.last_assignment_id = json["last_assignment_id"]
        self.last_date = convert_to_date(json["last_date"])


@dataclass
class AgendaHour:
    hourID: str
    start: str
    end: str
    title: str


@dataclass
class AgendaLesson:
    momentID: str
    lessonID: str
    hourID: str
    date: Date
    subject: str | None
    course: str
    courseTitle: str
    classroom: str
    classroomTitle: str
    teacher: str
    teacherTitle: str
    klassen: str
    klassenTitle: str
    classIDs: str
    bothStartStatus: str
    assignmentEndStatus: str
    testDeadlineStatus: str
    noteStatus: str
    note: str | None
    date_listview: str
    hour: str
    activity: str
    activityID: str | None
    color: str
    hourValue: str
    components_hidden: object
    freedayIcon: str
    someSubjectsEmpty: str | None

    @property
    def hour_details(self) -> AgendaHour:
        from .agenda import SmartschoolHours

        return SmartschoolHours().search_by_hourId(self.hourID)


@dataclass
class AgendaMomentInfoAssignment:
    startAssignment: str
    start: str
    end: str
    type: str
    description: str
    atdescription: str
    freedeadline: str
    warning: str
    assignmentInfo: str
    assignmentDeadline: str


@dataclass
class AgendaMomentInfo:
    className: str
    subject: str
    materials: str | None
    momentID: str
    assignments: list[AgendaMomentInfoAssignment]


@dataclass
class StudentSupportLink:
    id: str
    name: str
    description: str
    icon: str
    link: Url
    cleanLink: str
    isVisible: bool


@dataclass
class ShortMessage:
    id: int
    fromImage: Url
    subject: str
    date: DateTime
    status: int
    attachment: int
    unread: bool
    label: bool
    deleted: bool
    allowreply: bool
    allowreplyenabled: bool
    hasreply: bool
    hasForward: bool
    realBox: str
    sendDate: DateTime | None
    from_: str = Field(alias="from")


@dataclass
class FullMessage:
    id: int
    to: str | None
    subject: str
    date: DateTime
    body: str
    status: int
    attachment: int
    unread: bool
    label: bool
    receivers: list[str]
    ccreceivers: list[str]
    bccreceivers: list[str]
    senderPicture: str
    markedInLVS: None
    fromTeam: int
    totalNrOtherToReciviers: int
    totalnrOtherCcReceivers: int
    totalnrOtherBccReceivers: int
    canReply: bool
    hasReply: bool
    hasForward: bool
    sendDate: DateTime | None
    from_: str = Field(alias="from")


@dataclass
class Attachment:
    fileID: int
    name: str
    mime: str
    size: str
    icon: str
    wopiAllowed: bool
    order: int

    def download(self) -> bytes:
        resp = session.get(f"/?module=Messages&file=download&fileID={self.fileID}&target=0")
        return base64.b64decode(resp.content)
