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

    def test_can_subscribe_add(self):
        client = ImClient(KEY, SECRET)
        res = client.event.subscribe_add(**{
            'accid': 'jingyuxiaoban_accid',
            'publisherAccids': ['jingyuxiaoban_accid1'],
            'eventType': EVENT_TYPE_SUBSCRIBE,
            'ttl': SUBSCRIBE_TTL_30_DAYS,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_subscribe_delete(self):
        client = ImClient(KEY, SECRET)
        res = client.event.subscribe_delete(**{
            'accid': 'jingyuxiaoban_accid',
            'publisherAccids': ['jingyuxiaoban_accid1'],
            'eventType': EVENT_TYPE_SUBSCRIBE,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_subscribe_batch_delete(self):
        client = ImClient(KEY, SECRET)
        res = client.event.subscribe_batch_delete(**{
            'accid': 'jingyuxiaoban_accid',
            'eventType': EVENT_TYPE_SUBSCRIBE,
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_subscribe_query(self):
        client = ImClient(KEY, SECRET)
        res = client.event.subscribe_query(**{
            'accid': 'jingyuxiaoban_accid',
            'publisherAccids': ['jingyuxiaoban_accid1'],
            'eventType': EVENT_TYPE_SUBSCRIBE,
        }).json()
        print res
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()
