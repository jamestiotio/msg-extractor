#!/usr/bin/env python3
# -*- coding: latin-1 -*-
# Date Format: YYYY-MM-DD

"""
extract_msg:
    Extracts emails and attachments saved in Microsoft Outlook's .msg files.

https://github.com/TeamMsgExtractor/msg-extractor
"""

# --- LICENSE.txt --------------------------------------------------------------
#
#    Copyright 2013-2022 Matthew Walker and Destiny Peterson
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = 'Destiny Peterson & Matthew Walker'
__date__ = '2023-08-03'
__version__ = '0.44.0'

__all__ = [
    # Modules:
    'attachments',
    'enums',
    'exceptions',
    'msg_classes',
    'properties',

    # Classes:
    'Attachment',
    'AttachmentBase',
    'Message',
    'MSGFile',
    'Named',
    'NamedProperties',
    'OleWriter',
    'PropertiesStore',
    'Recipient',
    'SignedAttachment',

    # Functions:
    'openMsg',
    'openMsgBulk',
]


# Ensure these are imported before anything else.
from . import constants, enums, exceptions

from . import attachments, msg_classes, properties
from .attachments import Attachment, AttachmentBase, SignedAttachment
from .msg_classes import Message, MSGFile
from .ole_writer import OleWriter
from .open_msg import openMsg, openMsgBulk
from .properties import Named, NamedProperties, PropertiesStore
from .recipient import Recipient