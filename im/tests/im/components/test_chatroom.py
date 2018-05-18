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

    def test_can_delete_history_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.history.delete_history_msg(**{
            'roomid': 1234,
            'fromAcc': 'jingyuxiaoban_accid',
            'msgTimetag': 144359963111,
        }).json()
        print res
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()
