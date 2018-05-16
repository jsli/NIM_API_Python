# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- Team component"""

from __future__ import absolute_import

from im import util
from im.components import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class TeamComponent(base.BaseComponent):
    """Component dealing with all user related matters"""

    def create(self, **kwargs):
        """
        创建群
        """
        util.require_keys(kwargs, ['tname', 'owner', 'members', 'msg', 'magree', 'joinmode'])
        return self.post_request('/team/create.action', data=kwargs)

    def add(self, **kwargs):
        """
        拉人入群
        """
        util.require_keys(kwargs, ['tid', 'owner', 'members', 'msg', 'magree'])
        return self.post_request('/team/add.action', data=kwargs)

    def kick(self, **kwargs):
        """
        踢人出群
        """
        util.require_keys(kwargs, ['tid', 'owner', 'member'])
        return self.post_request('/team/kick.action', data=kwargs)

    def remove(self, **kwargs):
        """
        解散群
        """
        util.require_keys(kwargs, ['tid', 'owner'])
        return self.post_request('/team/remove.action', data=kwargs)

    def update(self, **kwargs):
        """
        编辑群资料
        """
        util.require_keys(kwargs, ['tid', 'owner'])
        return self.post_request('/team/update.action', data=kwargs)

    def query(self, **kwargs):
        """
        群信息与成员列表查询
        """
        util.require_keys(kwargs, ['tids', 'ope'])
        return self.post_request('/team/query.action', data=kwargs)

    def query_detail(self, **kwargs):
        """
        获取群组详细信息
        """
        util.require_keys(kwargs, 'tid')
        return self.post_request('/team/queryDetail.action', data=kwargs)

    def get_mark_read_info(self, **kwargs):
        """
        获取群组已读消息的已读详情信息
        """
        util.require_keys(kwargs, ['tid', 'msgid', 'fromAccid'])
        return self.post_request('/team/getMarkReadInfo.action', data=kwargs)

    def change_owner(self, **kwargs):
        """
        移交群主
        """
        util.require_keys(kwargs, ['tid', 'owner', 'newowner', 'leave'])
        return self.post_request('/team/changeOwner.action', data=kwargs)

    def add_manager(self, **kwargs):
        """
        任命管理员
        """
        util.require_keys(kwargs, ['tid', 'owner', 'members'])
        return self.post_request('/team/addManager.action', data=kwargs)

    def remove_manager(self, **kwargs):
        """
        移除管理员
        """
        util.require_keys(kwargs, ['tid', 'owner', 'members'])
        return self.post_request('/team/removeManager.action', data=kwargs)

    def join_teams(self, **kwargs):
        """
        获取某用户所加入的群信息
        """
        util.require_keys(kwargs, ['accid'])
        return self.post_request('/team/joinTeams.action', data=kwargs)

    def update_team_nick(self, **kwargs):
        """
        修改群昵称
        """
        util.require_keys(kwargs, ['tid', 'owner', 'accid', 'nick'])
        return self.post_request('/team/updateTeamNick.action', data=kwargs)

    def mute_team(self, **kwargs):
        """
        修改消息提醒开关
        """
        util.require_keys(kwargs, ['tid', 'accid', 'ope'])
        return self.post_request('/team/muteTeam.action', data=kwargs)

    def mute_tlist(self, **kwargs):
        """
        禁言群成员
        """
        util.require_keys(kwargs, ['tid', 'owner', 'accid', 'mute'])
        return self.post_request('/team/muteTeam.action', data=kwargs)

    def leave(self, **kwargs):
        """
        主动退群
        """
        util.require_keys(kwargs, ['tid', 'accid'])
        return self.post_request('/team/leave.action', data=kwargs)

    def mute_tlist_all(self, **kwargs):
        """
        将群组整体禁言
        """
        util.require_keys(kwargs, ['tid', 'owner'])
        return self.post_request('/team/muteTlistAll.action', data=kwargs)

    def list_team_mute(self, **kwargs):
        """
        获取群组禁言列表
        """
        util.require_keys(kwargs, ['tid', 'owner'])
        return self.post_request('/team/listTeamMute.action', data=kwargs)
