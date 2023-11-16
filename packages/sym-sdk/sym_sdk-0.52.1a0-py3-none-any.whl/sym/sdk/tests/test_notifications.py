import pytest
from pydantic import ValidationError

from sym.sdk.notifications import Notification
from sym.sdk.request_destination import SlackChannelName, SlackUser


class TestNotification:
    def test_destinations__at_least_one_required(self):
        with pytest.raises(ValidationError):
            Notification(destinations=[])

    def test_destinations__only_one_slack_destination_allowed(self):
        assert Notification(destinations=[SlackChannelName(channel_name="#general")])

        with pytest.raises(ValidationError):
            Notification(
                destinations=[
                    SlackChannelName(channel_name="#sym-errors"),
                    SlackChannelName(channel_name="#general"),
                ]
            )

        with pytest.raises(ValidationError):
            Notification(
                destinations=[
                    SlackChannelName(channel_name="#general"),
                    SlackUser(user_id="U12345"),
                ]
            )
