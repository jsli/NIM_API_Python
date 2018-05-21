# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- Message component"""

from __future__ import absolute_import

import json

from netease_im import util
from netease_im.components import base
from netease_im.util import is_str_type

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class MessageComponent(base.BaseComponent):
    """Component dealing with all Message related matters"""

    def send_msg(self, **kwargs):
        """
        发送普通消息
        """
        util.require_keys(kwargs, ['from', 'ope', 'to', 'type', 'body'], False)
        # JSON串，如：{"msg":"hello"}
        if not is_str_type(kwargs['body']):
            kwargs['body'] = json.dumps(kwargs['body'])
        return self.post_request('/msg/sendMsg.action', data=kwargs)

    def send_batch_msg(self, **kwargs):
        """
        批量发送点对点普通消息
        """
        util.require_keys(kwargs, ['fromAccid', 'toAccids', 'type', 'body'], False)

        # JSON串，如：{"msg":"hello"}
        if not is_str_type(kwargs['body']):
            kwargs['body'] = json.dumps(kwargs['body'])
        # JSONArray对应的accid串，如：["zhangsan"]
        if not is_str_type(kwargs['toAccids']):
            kwargs['toAccids'] = json.dumps(kwargs['toAccids'])

        return self.post_request('/msg/sendBatchMsg.action', data=kwargs)

    def send_attach_msg(self, **kwargs):
        """
        发送自定义系统通知
        """
        util.require_keys(kwargs, ['from', 'msgtype', 'to', 'attach'], False)
        # JSON串，如：{"msg":"hello"}
        if not is_str_type(kwargs['attach']):
            kwargs['attach'] = json.dumps(kwargs['attach'])
        return self.post_request('/msg/sendAttachMsg.action', data=kwargs)

    def send_batch_attach_msg(self, **kwargs):
        """
        批量发送点对点自定义系统通知
        """
        util.require_keys(kwargs, ['fromAccid', 'toAccids', 'attach'], False)

        # JSON串，如：{"msg":"hello"}
        if not is_str_type(kwargs['attach']):
            kwargs['attach'] = json.dumps(kwargs['attach'])
        # JSONArray对应的accid串，如：["zhangsan"]
        if not is_str_type(kwargs['toAccids']):
            kwargs['toAccids'] = json.dumps(kwargs['toAccids'])

        return self.post_request('/msg/sendBatchAttachMsg.action', data=kwargs)

    def upload(self, **kwargs):
        """
        文件上传
        """
        util.require_keys(kwargs, 'content', False)
        return self.post_request('/msg/upload.action', data=kwargs)

    def upload_file(self, **kwargs):
        """
        文件上传（multipart方式）
        """
        print u'暂不支持multipart方式上传, 转换为普通文件上传'
        return self.upload(**kwargs)

    def recall(self, **kwargs):
        """
        消息撤回
        """
        util.require_keys(kwargs, ['deleteMsgid', 'timetag', 'type', 'from', 'to'], False)
        return self.post_request('/msg/recall.action', data=kwargs)

    def broadcast_msg(self, **kwargs):
        """
        发送广播消息
        """
        util.require_keys(kwargs, 'body', False)
        # JSONArray对应的accid串，如：["zhangsan"]
        if 'targetOs' in kwargs and not is_str_type(kwargs['targetOs']):
            kwargs['targetOs'] = json.dumps(kwargs['targetOs'])
        return self.post_request('/msg/broadcastMsg.action', data=kwargs)
