# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- Friend component"""

from __future__ import absolute_import

from netease_im import util
from netease_im.components import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class FriendComponent(base.BaseComponent):
    """Component dealing with all Friend related matters"""

    def add(self, **kwargs):
        """
        加好友
        """
        util.require_keys(kwargs, ['accid', 'faccid', 'type'], False)
        return self.post_request('/friend/add.action', data=kwargs)

    def update(self, **kwargs):
        """
        更新好友相关信息
        """
        util.require_keys(kwargs, ['accid', 'faccid'], False)
        return self.post_request('/friend/update.action', data=kwargs)

    def delete(self, **kwargs):
        """
        删除好友
        """
        util.require_keys(kwargs, ['accid', 'faccid'], False)
        return self.post_request('/friend/delete.action', data=kwargs)

    def get(self, **kwargs):
        """
        获取好友关系
        """
        util.require_keys(kwargs, ['accid', 'updatetime'], False)
        return self.post_request('/friend/get.action', data=kwargs)
