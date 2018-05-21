"""NIM REST API Python Client"""

from __future__ import absolute_import

from netease_im import (
    components,
    util,
)

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class ImClient(util.ApiClient):
    """NIM REST API Python Client"""

    """Base URL for NIM API"""
    BASE_URI = 'https://api.netease.im/nimserver'

    def __init__(
            self, api_key, api_secret, timeout=15):
        """Create a new NIM client

        :param api_key: The NIM API key
        :param api_secret: The NIM API secret
        :param timeout: The time out to use for API requests
        """
        super(ImClient, self).__init__(
            base_uri=ImClient.BASE_URI, timeout=timeout)

        # Setup the config details
        self.config = {
            'api_key': api_key,
            'api_secret': api_secret,
        }

        # Register all of the components
        self.components = {
            'user': components.user.UserComponent(
                base_uri=ImClient.BASE_URI, config=self.config),
            'friend': components.friend.FriendComponent(
                base_uri=ImClient.BASE_URI, config=self.config),
            'message': components.message.MessageComponent(
                base_uri=ImClient.BASE_URI, config=self.config),
            'team': components.team.TeamComponent(
                base_uri=ImClient.BASE_URI, config=self.config),
            'chatroom': components.chatroom.ChatroomComponent(
                base_uri=ImClient.BASE_URI, config=self.config),
            'history': components.history.HistoryComponent(
                base_uri=ImClient.BASE_URI, config=self.config),
            'event': components.event.EventComponent(
                base_uri=ImClient.BASE_URI, config=self.config),
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    @property
    def api_key(self):
        """The NIM api_key"""
        return self.config.get('api_key')

    @api_key.setter
    def api_key(self, value):
        """Set the api_key"""
        self.config['api_key'] = value

    @property
    def api_secret(self):
        """The NIM api_secret"""
        return self.config.get('api_secret')

    @api_secret.setter
    def api_secret(self, value):
        """Set the api_secret"""
        self.config['api_secret'] = value

    @property
    def user(self):
        """Get the user component"""
        return self.components.get('user')

    @property
    def friend(self):
        """Get the friend component"""
        return self.components.get('friend')

    @property
    def message(self):
        """Get the message component"""
        return self.components.get('message')

    @property
    def team(self):
        """Get the team component"""
        return self.components.get('team')

    @property
    def chatroom(self):
        """Get the chatroom component"""
        return self.components.get('chatroom')

    @property
    def history(self):
        """Get the history component"""
        return self.components.get('history')

    @property
    def event(self):
        """Get the event component"""
        return self.components.get('event')
