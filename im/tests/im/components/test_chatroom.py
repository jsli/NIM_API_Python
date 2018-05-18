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

    def test_can_create(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.create(**{
            'creator': 'jingyuxiaoban_accid',
            'name': u'测试聊天室',
            'queuelevel': CHATROOM_QUEUE_LEVEL_PERM_ADMIN,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_get(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.get(**{
            'roomid': 24938834,
            'needOnlineUserCount': True,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_get_batch(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.get_batch(**{
            'roomids': [24938834],
            'needOnlineUserCount': True,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_update(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.update(**{
            'roomid': 24938834,
            'name': u'你的',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_toggle_close_stat(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.toggle_close_stat(**{
            'roomid': 24938834,
            'operator': 'jingyuxiaoban_accid',
            'valid': True
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_set_member_role(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.set_member_role(**{
            'roomid': 24938834,
            'operator': 'jingyuxiaoban_accid',
            'target': 'jingyuxiaoban_accid',
            'opt': CHATROOM_OPT_ADMIN,
            'optvalue': True
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_update_my_room_role(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.update_my_room_role(**{
            'roomid': 24938834,
            'accid': 'jingyuxiaoban_accid',
            'save': True,
            'name': 'manson',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_request_addr(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.request_addr(**{
            'roomid': 24938834,
            'accid': 'jingyuxiaoban_accid',
            'clienttype': CHATROOM_CLIENT_TYPE_MP,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_send_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.send_msg(**{
            'roomid': 24938834,
            'msgId': 'abcdouifewlkjf',
            'fromAccid': 'jingyuxiaoban_accid',
            'attach': 'abcdmanfkj',
            'msgType': MESSAGE_TYPE_TEXT
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_add_robot(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.add_robot(**{
            'roomid': 24938834,
            'accids': ['jingyuxiaoban_accid'],
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_remove_robot(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.remove_robot(**{
            'roomid': 24938834,
            'accids': ['jingyuxiaoban_accid'],
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_temporary_mute(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.temporary_mute(**{
            'roomid': 24938834,
            'operator': 'jingyuxiaoban_accid',
            'target': 'jingyuxiaoban_accid',
            'muteDuration': 300
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_delete_history_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.delete_history_msg(**{
            'roomid': 24938834,
            'fromAcc': 'jingyuxiaoban_accid',
            'msgTimetag': 144359963111,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_mute_room(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.mute_room(**{
            'roomid': 24938834,
            'operator': 'jingyuxiaoban_accid',
            'mute': True
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_topn(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.topn(**{
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_members_by_page(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.members_by_page(**{
            'roomid': 24938834,
            'type': CHATROOM_MEMBER_TYPE_FIX,
            'endtime': 0,
            'limit': 30
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_query_members(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.query_members(**{
            'roomid': 24938834,
            'accids': ['jingyuxiaoban_accid'],
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_queue_init(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.queue_init(**{
            'roomid': 24938834,
            'sizeLimit': 500,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_queue_drop(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.queue_drop(**{
            'roomid': 24938834,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_queue_list(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.queue_list(**{
            'roomid': 24938834,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_queue_poll(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.queue_poll(**{
            'roomid': 24938834,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_queue_offer(self):
        client = ImClient(KEY, SECRET)
        res = client.chatroom.queue_offer(**{
            'roomid': 24938834,
            'key': 'key',
            'value': 'value'
        }).json()
        print res
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()
