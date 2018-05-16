# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- User component"""

from __future__ import absolute_import

from im import util
from im.components import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class UserComponent(base.BaseComponent):
    """Component dealing with all user related matters"""

    def create(self, **kwargs):
        """
        创建网易云通信ID
        """
        util.require_keys(kwargs, 'accid')
        return self.post_request('/user/create.action', data=kwargs)

    def update(self, **kwargs):
        """
        网易云通信ID更新
        """
        util.require_keys(kwargs, 'accid')
        return self.post_request('/user/update.action', data=kwargs)

    def refresh_token(self, **kwargs):
        """
        更新并获取新token
        """
        util.require_keys(kwargs, 'accid')
        return self.post_request('/user/refreshToken.action', data=kwargs)

    def block(self, **kwargs):
        """
        封禁网易云通信ID
        """
        util.require_keys(kwargs, 'accid')
        return self.post_request('/user/block.action', data=kwargs)

    def unblock(self, **kwargs):
        """
        解禁网易云通信ID
        """
        util.require_keys(kwargs, 'accid')
        return self.post_request('/user/unblock.action', data=kwargs)

    def update_info(self, **kwargs):
        """
        更新用户名片
        """
        util.require_keys(kwargs, 'accid')
        return self.post_request('/user/updateUinfo.action', data=kwargs)

    def get_info(self, **kwargs):
        """
        获取用户名片
        """
        util.require_keys(kwargs, 'accid')
        return self.post_request('/user/getUinfos.action', data=kwargs)

    def set_donnop(self, **kwargs):
        """
        设置桌面端在线时，移动端是否需要推送
        """
        util.require_keys(kwargs, ['accid', 'donnopOpen'])
        return self.post_request('/user/setDonnop.action', data=kwargs)
