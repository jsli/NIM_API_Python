# -*- coding: utf-8 -*-

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"

import unittest

from im import (
    components,
    ImClient)


KEY = '271f99c2ad5a414459fc02071eb1e405'
SECRET = 'a44cfdc61f29'


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ImClientTestCase))
    return suite


class ImClientTestCase(unittest.TestCase):

    def test_init_sets_config(self):
        client = ImClient(KEY, SECRET)
        self.assertEqual(
            client.config,
            {
                'api_key': KEY,
                'api_secret': SECRET,
            }
        )

    def test_init_sets_config_with_timeout(self):
        client = ImClient(KEY, SECRET, timeout=500)
        self.assertEqual(client.timeout, 500)

    def test_cannot_init_with_non_int_timeout(self):
        with self.assertRaises(ValueError) as context:
            ImClient(KEY, SECRET, timeout='bad')
            self.assertEqual(
                context.exception.message, "timeout value must be an integer")

    def test_init_creates_all_components(self):
        client = ImClient(KEY, SECRET)
        self.assertEqual(
            set(['user', 'friend', 'message', 'team', 'chatroom', 'history', 'event']),
            set(client.components.keys())
        )
        self.assertIsInstance(
            client.components['user'],
            components.user.UserComponent
        )
        self.assertIsInstance(
            client.components['friend'],
            components.friend.FriendComponent
        )
        self.assertIsInstance(
            client.components['message'],
            components.message.MessageComponent
        )
        self.assertIsInstance(
            client.components['team'],
            components.team.TeamComponent
        )
        self.assertIsInstance(
            client.components['chatroom'],
            components.chatroom.ChatroomComponent
        )
        self.assertIsInstance(
            client.components['history'],
            components.history.HistoryComponent
        )
        self.assertIsInstance(
            client.components['event'],
            components.event.EventComponent
        )

    def test_can_get_api_key(self):
        client = ImClient(KEY, SECRET)
        self.assertEqual(client.api_key, KEY)

    def test_can_set_api_key(self):
        client = ImClient(KEY, SECRET)
        client.api_key = 'NEW-KEY'
        self.assertEqual(client.api_key, 'NEW-KEY')

    def test_can_get_api_secret(self):
        client = ImClient(KEY, SECRET)
        self.assertEqual(client.api_secret, SECRET)

    def test_can_set_api_secret(self):
        client = ImClient(KEY, SECRET)
        client.api_secret = 'NEW-SECRET'
        self.assertEqual(client.api_secret, 'NEW-SECRET')

    def test_can_get_user_component(self):
        client = ImClient(KEY, SECRET)
        self.assertIsInstance(
            client.user,
            components.user.UserComponent
        )

    def test_can_get_friend_component(self):
        client = ImClient(KEY, SECRET)
        self.assertIsInstance(
            client.friend,
            components.friend.FriendComponent
        )

    def test_can_get_message_component(self):
        client = ImClient(KEY, SECRET)
        self.assertIsInstance(
            client.message,
            components.message.MessageComponent
        )

    def test_can_get_team_component(self):
        client = ImClient(KEY, SECRET)
        self.assertIsInstance(
            client.team,
            components.team.TeamComponent
        )

    def test_can_get_chatroom_component(self):
        client = ImClient(KEY, SECRET)
        self.assertIsInstance(
            client.chatroom,
            components.chatroom.ChatroomComponent
        )

    def test_can_get_history_component(self):
        client = ImClient(KEY, SECRET)
        self.assertIsInstance(
            client.history,
            components.history.HistoryComponent
        )

    def test_can_get_event_component(self):
        client = ImClient(KEY, SECRET)
        self.assertIsInstance(
            client.event,
            components.event.EventComponent
        )

    def test_can_use_client_with_context(self):
        with ImClient(KEY, SECRET) as client:
            self.assertIsInstance(
                client,
                ImClient
            )


if __name__ == '__main__':
    unittest.main()
