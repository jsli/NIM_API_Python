# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- Friend component"""

from __future__ import absolute_import

from im import util
from im.components import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class FriendComponent(base.BaseComponent):
    """Component dealing with all Friend related matters"""

    def add(self, **kwargs):
        """
        加好友
        """
        util.require_keys(kwargs, ['accid', 'faccid', 'type'])
        return self.post_request('/friend/add.action', data=kwargs)

    def update(self, **kwargs):
        """
        更新好友相关信息
        """
        util.require_keys(kwargs, ['accid', 'faccid'])
        return self.post_request('/friend/update.action', data=kwargs)

    def delete(self, **kwargs):
        """
        删除好友
        """
        util.require_keys(kwargs, ['accid', 'faccid'])
        return self.post_request('/friend/delete.action', data=kwargs)

    def get(self, **kwargs):
        """
        获取好友关系
        """
        util.require_keys(kwargs, ['accid', 'updatetime'])
        return self.post_request('/friend/get.action', data=kwargs)

    def set_special_relation(self, **kwargs):
        """
        拉黑/取消拉黑；设置静音/取消静音
        """
        util.require_keys(kwargs, ['accid', 'targetAcc', 'relationType', 'value'])
        return self.post_request('/friend/setSpecialRelation.action', data=kwargs)

    def list_black_and_mute(self, **kwargs):
        """
        查看指定用户的黑名单和静音列表
        """
        util.require_keys(kwargs, 'accid')
        return self.post_request('/friend/listBlackAndMuteList.action', data=kwargs)
