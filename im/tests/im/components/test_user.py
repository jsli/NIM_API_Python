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
        res = client.user.create(**{
            'accid': 'jingyuxiaoban_accid',
            'name': 'jingyuxiaoban_name',
            'icon': '',
            'token': '',
            'props': '',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_update(self):
        client = ImClient(KEY, SECRET)
        res = client.user.update(**{
            'accid': 'jingyuxiaoban_accid',
            'token': '',
            'props': '',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_refresh_token(self):
        client = ImClient(KEY, SECRET)
        res = client.user.refresh_token(**{
            'accid': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_block(self):
        client = ImClient(KEY, SECRET)
        res = client.user.block(**{
            'accid': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_unblock(self):
        client = ImClient(KEY, SECRET)
        res = client.user.unblock(**{
            'accid': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_update_info(self):
        client = ImClient(KEY, SECRET)
        res = client.user.update_info(**{
            'accid': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_get_info(self):
        client = ImClient(KEY, SECRET)
        res = client.user.get_info(**{
            'accids': ['jingyuxiaoban_accid'],
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_set_donnop(self):
        client = ImClient(KEY, SECRET)
        res = client.user.set_donnop(**{
            'accid': 'jingyuxiaoban_accid',
            'donnopOpen': True
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_set_special_relation(self):
        client = ImClient(KEY, SECRET)
        res = client.user.set_special_relation(**{
            'accid': 'jingyuxiaoban_accid',
            'targetAcc': 'jingyuxiaoban_accid1',
            'relationType': RELATION_TYPE_BLACK,
            'value': OP_VALUE_ADD
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_list_black_and_mute(self):
        client = ImClient(KEY, SECRET)
        res = client.user.list_black_and_mute(**{
            'accid': 'jingyuxiaoban_accid',
        }).json()
        print res
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()
