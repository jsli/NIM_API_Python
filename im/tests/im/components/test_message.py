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

    def test_can_send_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.message.send_msg(**{
            'from': 'jingyuxiaoban_accid',
            'ope': MESSAGE_OPE_USER,
            'to': 'jingyuxiaoban_accid1',
            'type': MESSAGE_TYPE_TEXT,
            'body': {
                'msg': 'hello, manson'
            },
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_send_batch_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.message.send_batch_msg(**{
            'fromAccid': 'jingyuxiaoban_accid',
            'toAccids': ['jingyuxiaoban_accid1'],
            'type': MESSAGE_TYPE_TEXT,
            'body': {
                'msg': 'hello, manson'
            },
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_send_attach_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.message.send_attach_msg(**{
            'from': 'jingyuxiaoban_accid',
            'to': 'jingyuxiaoban_accid1',
            'msgtype': ATTACH_MESSAGE_TYPE_USER,
            'attach': {
                'msg': 'hello, manson'
            },
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_send_batch_attach_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.message.send_batch_attach_msg(**{
            'fromAccid': 'jingyuxiaoban_accid',
            'toAccids': ['jingyuxiaoban_accid1', 'xxxxdfdsafe'],
            'attach': {
                'msg': 'hello, manson'
            },
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_upload(self):
        client = ImClient(KEY, SECRET)
        res = client.message.upload(**{
            'content': 'data:image/png;base64,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',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_upload_file(self):
        client = ImClient(KEY, SECRET)
        res = client.message.upload_file(**{
            'content': 'data:image/png;base64,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',
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_recall(self):
        client = ImClient(KEY, SECRET)
        res = client.message.recall(**{
            'deleteMsgid': '257097856041',
            'timetag': '148152815574',
            'from': 'jingyuxiaoban_accid',
            'to': 'jingyuxiaoban_accid1',
            'type': RECALL_TYPE_USER
        }).json()
        print res
        self.assertEqual(res['code'], 200)

    def test_can_broadcast_msg(self):
        client = ImClient(KEY, SECRET)
        res = client.message.broadcast_msg(**{
            'body': 'abcd',
            'targetOs': ["ios", "aos", "pc", "web", "mac"],
        }).json()
        print res
        self.assertEqual(res['code'], 200)


if __name__ == '__main__':
    unittest.main()
