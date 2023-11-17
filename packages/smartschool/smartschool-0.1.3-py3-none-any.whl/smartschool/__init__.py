import logging

from .agenda import SmartschoolHours, SmartschoolLessons, SmartschoolMomentInfos
from .courses import Courses, TopNavCourses
from .credentials import EnvCredentials, PathCredentials
from .logger import setup_logger
from .messages import Attachments, BoxType, Message, MessageHeaders, SortField, SortOrder
from .objects import FutureTasks
from .periods import Periods
from .results import Results
from .session import SmartSchool
from .student_support import StudentSupportLinks

__all__ = [
    "PathCredentials",
    "EnvCredentials",
    "SmartSchool",
    "logger",
    "Courses",
    "TopNavCourses",
    "Results",
    "Periods",
    "FutureTasks",
    "SortField",
    "SortOrder",
    "BoxType",
    "MessageHeaders",
    "StudentSupportLinks",
    "SmartschoolHours",
    "SmartschoolLessons",
    "SmartschoolMomentInfos",
    "Message",
    "Attachments",
]

logger = setup_logger(logging.DEBUG)
