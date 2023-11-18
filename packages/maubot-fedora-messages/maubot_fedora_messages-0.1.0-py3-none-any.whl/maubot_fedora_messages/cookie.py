# SPDX-FileCopyrightText: 2023 Contributors to the Fedora Project
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import typing

from .base import SCHEMA_URL, MaubotFedoraMessage


class GiveCookieV1(MaubotFedoraMessage):
    """
    A sub-class of a Fedora message that defines a message schema for messages
    published by Maubot Fedora when a cookie is given.
    """

    topic = "maubot.cookie.give.v1"

    body_schema: typing.ClassVar = {
        "id": SCHEMA_URL + topic,
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Schema for messages sent when a new thing is created",
        "type": "object",
        "properties": {
            "sender": {"type": "string"},
            "recipient": {"type": "string"},
            "total": {"type": "number"},
            "fedora_release": {"type": "string"},
            "count_by_release": {"type": "object"},
        },
        "required": ["sender", "recipient", "total", "fedora_release", "count_by_release"],
    }

    def __str__(self):
        """Return a complete human-readable representation of the message."""
        current_release = self.body["fedora_release"]
        return (
            f"{self.agent_name} gave a cookie to {self.body['recipient']}. They now "
            f"have {self.body['total']} cookie(s), {self.body['count_by_release'][current_release]}"
            f" of which were obtained in the Fedora {current_release} release cycle"
        )

    @property
    def summary(self):
        """Return a summary of the message."""
        return f"{self.agent_name} gave a cookie to {self.body['recipient']}"

    @property
    def agent_name(self):
        """The username of the user who initiated the action that generated this message."""
        return self.body["sender"]

    @property
    def usernames(self):
        """List of users affected by the action that generated this message."""
        return [self.agent_name, self.body["recipient"]]
