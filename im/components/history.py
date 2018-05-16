# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- History component"""

from __future__ import absolute_import

from im import util
from im.components import base


__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class HistoryComponent(base.BaseComponent):
    """Component dealing with all user related matters"""

    def query_session_msg(self, **kwargs):
        """
        单聊云端历史消息查询
        """
        util.require_keys(kwargs, ['from', 'to', 'begintime', 'endtime', 'limit'])
        return self.post_request('/history/querySessionMsg.action', data=kwargs)

    def query_team_msg(self, **kwargs):
        """
        群聊云端历史消息查询
        """
        util.require_keys(kwargs, ['tid', 'accid', 'begintime', 'endtime', 'limit'])
        return self.post_request('/history/queryTeamMsg.action', data=kwargs)

    def query_chatroom_msg(self, **kwargs):
        """
        聊天室云端历史消息查询
        """
        util.require_keys(kwargs, ['roomid', 'accid', 'timetag', 'limit'])
        return self.post_request('/history/queryChatroomMsg.action', data=kwargs)

    def delete_history_msg(self, **kwargs):
        """
        删除聊天室云端历史消息
        """
        util.require_keys(kwargs, ['roomid', 'fromAcc', 'msgTimetag'])
        return self.post_request('/history/deleteHistoryMessage.action', data=kwargs)

    def query_user_events(self, **kwargs):
        """
        用户登录登出事件记录查询
        """
        util.require_keys(kwargs, ['accid', 'begintime', 'endtime', 'limit'])
        return self.post_request('/history/queryUserEvents.action', data=kwargs)

    def delete_media_file(self, **kwargs):
        """
        删除音视频/白板服务器录制文件
        """
        util.require_keys(kwargs, ['channelid'])
        return self.post_request('/history/deleteMediaFile.action', data=kwargs)

    def query_broadcast_msg(self, **kwargs):
        """
        批量查询广播消息
        """
        return self.post_request('/history/queryBroadcastMsg.action', data=kwargs)

    def query_broadcast_msg_by_id(self, **kwargs):
        """
        查询单条广播消息
        """
        util.require_keys(kwargs, ['broadcastId'])
        return self.post_request('/history/queryBroadcastMsgById.action', data=kwargs)
