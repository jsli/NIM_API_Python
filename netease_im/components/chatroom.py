# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- Chatroom component"""

from __future__ import absolute_import

import json

from netease_im import util
from netease_im.components import base
from netease_im.util import is_str_type

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class ChatroomComponent(base.BaseComponent):
    """Component dealing with all user related matters"""

    def create(self, **kwargs):
        """
        创建聊天室
        """
        util.require_keys(kwargs, ['creator', 'name'], False)
        return self.post_request('/chatroom/create.action', data=kwargs)

    def get(self, **kwargs):
        """
        查询聊天室信息
        """
        util.require_keys(kwargs, ['roomid'], False)
        return self.post_request('/chatroom/get.action', data=kwargs)

    def get_batch(self, **kwargs):
        """
        批量查询聊天室信息
        """
        util.require_keys(kwargs, ['roomids'], False)
        # JSONArray对应的accid串，如：["zhangsan"]
        if not is_str_type(kwargs['roomids']):
            kwargs['roomids'] = json.dumps(kwargs['roomids'])
        return self.post_request('/chatroom/getBatch.action', data=kwargs)

    def update(self, **kwargs):
        """
        更新聊天室信息
        """
        util.require_keys(kwargs, ['roomid'], False)
        return self.post_request('/chatroom/update.action', data=kwargs)

    def toggle_close_stat(self, **kwargs):
        """
        修改聊天室开/关闭状态
        """
        util.require_keys(kwargs, ['roomid', 'operator', 'valid'], False)
        return self.post_request('/chatroom/toggleCloseStat.action', data=kwargs)

    def set_member_role(self, **kwargs):
        """
        设置聊天室内用户角色
        """
        util.require_keys(kwargs, ['roomid', 'operator', 'target', 'opt', 'optvalue'], False)
        return self.post_request('/chatroom/setMemberRole.action', data=kwargs)

    def update_my_room_role(self, **kwargs):
        """
        变更聊天室内的角色信息
        """
        util.require_keys(kwargs, ['roomid', 'accid'], False)
        return self.post_request('/chatroom/updateMyRoomRole.action', data=kwargs)

    def request_addr(self, **kwargs):
        """
        请求聊天室地址
        """
        util.require_keys(kwargs, ['roomid', 'accid'], False)
        return self.post_request('/chatroom/requestAddr.action', data=kwargs)

    def send_msg(self, **kwargs):
        """
        发送聊天室消息
        """
        util.require_keys(kwargs, ['roomid', 'msgId', 'fromAccid', 'msgType'], False)
        return self.post_request('/chatroom/sendMsg.action', data=kwargs)

    def add_robot(self, **kwargs):
        """
        往聊天室内添加机器人
        """
        util.require_keys(kwargs, ['roomid', 'accids'], False)
        # JSONArray对应的accid串，如：["zhangsan"]
        if not is_str_type(kwargs['accids']):
            kwargs['accids'] = json.dumps(kwargs['accids'])
        return self.post_request('/chatroom/addRobot.action', data=kwargs)

    def remove_robot(self, **kwargs):
        """
        从聊天室内删除机器人
        """
        util.require_keys(kwargs, ['roomid', 'accids'], False)
        # JSONArray对应的accid串，如：["zhangsan"]
        if not is_str_type(kwargs['accids']):
            kwargs['accids'] = json.dumps(kwargs['accids'])
        return self.post_request('/chatroom/removeRobot.action', data=kwargs)

    def temporary_mute(self, **kwargs):
        """
        设置临时禁言状态
        """
        util.require_keys(kwargs, ['roomid', 'operator', 'target', 'muteDuration'], False)
        return self.post_request('/chatroom/temporaryMute.action', data=kwargs)

    def queue_offer(self, **kwargs):
        """
        往聊天室有序队列中新加或更新元素
        """
        util.require_keys(kwargs, ['roomid', 'key', 'value'], False)
        return self.post_request('/chatroom/queueOffer.action', data=kwargs)

    def queue_poll(self, **kwargs):
        """
        从队列中取出元素
        """
        util.require_keys(kwargs, ['roomid'], False)
        return self.post_request('/chatroom/queuePoll.action', data=kwargs)

    def queue_list(self, **kwargs):
        """
        排序列出队列中所有元素
        """
        util.require_keys(kwargs, ['roomid'], False)
        return self.post_request('/chatroom/queueList.action', data=kwargs)

    def queue_drop(self, **kwargs):
        """
        删除清理整个队列
        """
        util.require_keys(kwargs, ['roomid'], False)
        return self.post_request('/chatroom/queueDrop.action', data=kwargs)

    def queue_init(self, **kwargs):
        """
        初始化队列
        """
        util.require_keys(kwargs, ['roomid', 'sizeLimit'], False)
        return self.post_request('/chatroom/queueInit.action', data=kwargs)

    def mute_room(self, **kwargs):
        """
        将聊天室整体禁言
        """
        util.require_keys(kwargs, ['roomid', 'operator', 'mute'], False)
        return self.post_request('/chatroom/muteRoom.action', data=kwargs)

    def topn(self, **kwargs):
        """
        查询聊天室统计指标TopN
        """
        return self.post_request('/stats/chatroom/topn.action', data=kwargs)

    def members_by_page(self, **kwargs):
        """
        分页获取成员列表
        """
        util.require_keys(kwargs, ['roomid', 'type', 'endtime', 'limit'], False)
        return self.post_request('/chatroom/membersByPage.action', data=kwargs)

    def query_members(self, **kwargs):
        """
        批量获取在线成员信息
        """
        util.require_keys(kwargs, ['roomid', 'accids'], False)
        # JSONArray对应的accid串，如：["zhangsan"]
        if not is_str_type(kwargs['accids']):
            kwargs['accids'] = json.dumps(kwargs['accids'])
        return self.post_request('/chatroom/queryMembers.action', data=kwargs)

    def delete_history_msg(self, **kwargs):
        """
        删除聊天室云端历史消息
        """
        util.require_keys(kwargs, ['roomid', 'fromAcc', 'msgTimetag'], False)
        return self.post_request('/chatroom/deleteHistoryMessage.action', data=kwargs)
