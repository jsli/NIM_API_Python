# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- Message component"""

from __future__ import absolute_import

from im import util
from im.components import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class MessageComponent(base.BaseComponent):
    """Component dealing with all Message related matters"""

    def send_msg(self, **kwargs):
        """
        发送普通消息
        """
        util.require_keys(kwargs, ['from', 'ope', 'to', 'type', 'body'])
        return self.post_request('/msg/sendMsg.action', data=kwargs)

    def send_batch_msg(self, **kwargs):
        """
        批量发送点对点普通消息
        """
        util.require_keys(kwargs, ['fromAccid', 'toAccids', 'type', 'body'])
        return self.post_request('/msg/sendBatchMsg.action', data=kwargs)

    def send_attach_msg(self, **kwargs):
        """
        发送自定义系统通知
        """
        util.require_keys(kwargs, ['from', 'msgtype', 'to', 'attach'])
        return self.post_request('/msg/sendAttachMsg.action', data=kwargs)

    def send_batch_attach_msg(self, **kwargs):
        """
        批量发送点对点自定义系统通知
        """
        util.require_keys(kwargs, ['fromAccid', 'toAccids', 'attach'])
        return self.post_request('/msg/sendBatchAttachMsg.action', data=kwargs)

    def upload(self, **kwargs):
        """
        文件上传
        """
        util.require_keys(kwargs, 'content')
        return self.post_request('/msg/upload.action', data=kwargs)

    def upload_file(self, **kwargs):
        """
        文件上传（multipart方式）
        """
        # TODO:
        pass

    def recall(self, **kwargs):
        """
        消息撤回
        """
        util.require_keys(kwargs, ['deleteMsgid', 'timetag', 'type', 'from', 'to', 'msg', 'ignoreTime'])
        return self.post_request('/msg/recall.action', data=kwargs)

    def broadcast_msg(self, **kwargs):
        """
        发送广播消息
        """
        util.require_keys(kwargs, 'body')
        return self.post_request('/msg/broadcastMsg.action', data=kwargs)
