# -*- coding: utf-8 -*-
from im.constants.params import *

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"

import unittest

from im import ImClient
from im import components

KEY = '271f99c2ad5a414459fc02071eb1e405'
SECRET = 'a44cfdc61f29'
BASE_URI = 'https://api.netease.im/nimserver'


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CreateTestCase))
    return suite


class CreateTestCase(unittest.TestCase):

    def setUp(self):
        self.component = components.user.UserComponent(
            base_uri=BASE_URI,
            config={
                'api_key': KEY,
                'api_secret': SECRET
            }
        )

    def test_can_query_session_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.history.query_session_msg(**{
            'from': 'jingyuxiaoban_accid',
            'to': 'jingyuxiaoban_accid1',
            'begintime': 144359963111,
            'endtime': 1443599639999,
            'limit': 20,
            'reverse': HISTORY_QUERY_REVERSE_ASE,
            'type': [MESSAGE_TYPE_TEXT, MESSAGE_TYPE_IMAGE]
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_query_team_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.history.query_team_msg(**{
            'tid': '487347499',
            'accid': 'jingyuxiaoban_accid',
            'begintime': 144359963111,
            'endtime': 1443599639999,
            'limit': 20,
            'reverse': HISTORY_QUERY_REVERSE_ASE,
            'type': [MESSAGE_TYPE_TEXT, MESSAGE_TYPE_IMAGE]
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_query_chatroom_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.history.query_chatroom_msg(**{
            'roomid': 1234,
            'accid': 'jingyuxiaoban_accid',
            'timetag': 144359963111,
            'limit': 20,
            'reverse': HISTORY_QUERY_REVERSE_ASE,
            'type': [MESSAGE_TYPE_TEXT, MESSAGE_TYPE_IMAGE]
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_query_user_events(self):
        client = ImClient(KEY, SECRET)
        res = client.history.query_user_events(**{
            'accid': 'jingyuxiaoban_accid',
            'begintime': 144359963111,
            'endtime': 144369963111,
            'limit': 50,
            'reverse': HISTORY_QUERY_REVERSE_DESC,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_delete_media_file(self):
        client = ImClient(KEY, SECRET)
        res = client.history.delete_media_file(**{
            'channelid': 144359963111,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_query_broadcast_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.history.query_broadcast_msg(**{
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_query_broadcast_msg_by_id(self):
        client = ImClient(KEY, SECRET)
        res = client.history.query_broadcast_msg_by_id(**{
            'broadcastId': 123,
        }).json()
        print res
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()
