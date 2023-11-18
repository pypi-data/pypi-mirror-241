# SPDX-FileCopyrightText: 2023 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from fedora_messaging import message

SCHEMA_URL = "http://fedoraproject.org/message-schema/"


class MaubotFedoraMessage(message.Message):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by Maubot Fedora.
    """

    @property
    def app_name(self):
        return "Maubot Fedora"

    @property
    def app_icon(self):
        return "https://apps.fedoraproject.org/img/icons/maubot-fedora.png"
