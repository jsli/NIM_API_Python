# -*- coding: utf-8 -*-

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"

import unittest

from netease_im import ImClient
from netease_im import components
from netease_im.constants.params import *

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
        res = client.team.create(**{
            'tname': u'测试群',
            'owner': 'jingyuxiaoban_accid',
            'members': ['jingyuxiaoban_accid', 'jingyuxiaoban_accid1'],
            'msg': u'欢迎加入',
            'magree': TEAM_CREATE_SILENTLY,
            'joinmode': TEAM_JOIN_MODE_OPEN,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_add(self):
        client = ImClient(KEY, SECRET)
        res = client.team.add(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'members': ['jingyuxiaoban_accid', 'jingyuxiaoban_accid1'],
            'msg': u'欢迎加入',
            'magree': TEAM_CREATE_SILENTLY,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_kick(self):
        client = ImClient(KEY, SECRET)
        res = client.team.kick(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'member': 'jingyuxiaoban_accid1',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_remove(self):
        client = ImClient(KEY, SECRET)
        res = client.team.remove(**{
            'tid': '487282750',
            'owner': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_update(self):
        client = ImClient(KEY, SECRET)
        res = client.team.update(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'tname': u'修改群名称'
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_query(self):
        client = ImClient(KEY, SECRET)
        res = client.team.query(**{
            'tids': ['487347499'],
            'ope': TEAM_QUERY_MESSAGE_MEMBERS
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_query_detail(self):
        client = ImClient(KEY, SECRET)
        res = client.team.query_detail(**{
            'tid': '487347499',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_get_mark_read_info(self):
        client = ImClient(KEY, SECRET)
        res = client.team.get_mark_read_info(**{
            'tid': '487347499',
            'msgid': 1232321321,
            'fromAccid': 'jingyuxiaoban_accid'
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_change_owner(self):
        client = ImClient(KEY, SECRET)
        res = client.team.change_owner(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'newowner': 'jingyuxiaoban_accid',
            'leave': TEAM_CHANGE_OWNER_NOT_LEAVE
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_add_manager(self):
        client = ImClient(KEY, SECRET)
        res = client.team.add_manager(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'members': ['jingyuxiaoban_accid'],
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_remove_manager(self):
        client = ImClient(KEY, SECRET)
        res = client.team.remove_manager(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'members': ['jingyuxiaoban_accid'],
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_join_teams(self):
        client = ImClient(KEY, SECRET)
        res = client.team.join_teams(**{
            'accid': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_update_team_nick(self):
        client = ImClient(KEY, SECRET)
        res = client.team.update_team_nick(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'accid': 'jingyuxiaoban_accid',
            'nick': 'manson',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_mute_team(self):
        client = ImClient(KEY, SECRET)
        res = client.team.mute_team(**{
            'tid': '487347499',
            'accid': 'jingyuxiaoban_accid',
            'ope': TEAM_MESSAGE_MUTE
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_mute_tlist(self):
        client = ImClient(KEY, SECRET)
        res = client.team.mute_tlist(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'accid': 'jingyuxiaoban_accid',
            'mute': TEAM_MEMBER_MUTE
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_leave(self):
        client = ImClient(KEY, SECRET)
        res = client.team.leave(**{
            'tid': '487347499',
            'accid': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_mute_tlist_all(self):
        client = ImClient(KEY, SECRET)
        res = client.team.mute_tlist_all(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
            'muteType': TEAM_MUTE_TYPE_MEMBERS_ONLY,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_list_team_mute(self):
        client = ImClient(KEY, SECRET)
        res = client.team.list_team_mute(**{
            'tid': '487347499',
            'owner': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()
