__all__ = [
    'MeetingException',
]


import datetime
import functools

from typing import Optional

from .. import constants
from ..enums import SaveType
from .meeting_related import MeetingRelated


class MeetingException(MeetingRelated):
    """
    Class for handling Meeting Exceptions.
    """

    def save(self, **_) -> constants.SAVE_TYPE:
        """
        Meeting Exceptions are hidden attachments with no save behaviors. As
        such, for saving we literally just return the object and do nothing
        else.

        If you want something to happen for saving, you can call the save of a
        parent class or write your own code.
        """
        return (SaveType.NONE, None)

    @functools.cached_property
    def exceptionReplaceTime(self) -> Optional[datetime.datetime]:
        """
        The date and time within the recurrence pattern that the exception will
        replace. The value is specified in UTC.
        """
        return self._getNamedAs('8228', constants.ps.PSETID_APPOINTMENT)

    @functools.cached_property
    def fExceptionalBody(self) -> bool:
        """
        Indicates that the Exception Embedded Message object has a body that
        differs from the Recurring Calendar object. If True, the Exception MUST
        have a body.
        """
        return self._getNamedAs('8206', constants.ps.PSETID_APPOINTMENT, bool, False)

    @functools.cached_property
    def fInvited(self) -> bool:
        """
        Indicates if invitations have been sent for this exception.
        """
        return self._getNamedAs('8229', constants.ps.PSETID_APPOINTMENT, bool, False)
