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

    def test_can_add(self):
        client = ImClient(KEY, SECRET)
        res = client.friend.add(**{
            'accid': 'jingyuxiaoban_accid',
            'faccid': 'jingyuxiaoban_accid1',
            'type': FRIEND_ADD_SILENTLY,
            'msg': '',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_update(self):
        client = ImClient(KEY, SECRET)
        res = client.friend.update(**{
            'accid': 'jingyuxiaoban_accid',
            'faccid': 'jingyuxiaoban_accid1',
            'alias': 'friend',
            'ex': '',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_delete(self):
        client = ImClient(KEY, SECRET)
        res = client.friend.delete(**{
            'accid': 'jingyuxiaoban_accid',
            'faccid': 'jingyuxiaoban_accid1',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_get(self):
        client = ImClient(KEY, SECRET)
        res = client.friend.get(**{
            'accid': 'jingyuxiaoban_accid',
            'updatetime': 1443599631111
        }).json()
        print res
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()
