# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- History component"""

from __future__ import absolute_import

from netease_im import util
from netease_im.components import base
from netease_im.util import is_str_type

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class HistoryComponent(base.BaseComponent):
    """Component dealing with all user related matters"""

    def query_session_msg(self, **kwargs):
        """
        单聊云端历史消息查询
        """
        util.require_keys(kwargs, ['from', 'to', 'begintime', 'endtime', 'limit'], False)
        if 'type' in kwargs and not is_str_type(kwargs['type']):
            tmp = []
            for i in kwargs['type']:
                tmp.append(str(i))
            kwargs['type'] = ','.join(tmp)
        return self.post_request('/history/querySessionMsg.action', data=kwargs)

    def query_team_msg(self, **kwargs):
        """
        群聊云端历史消息查询
        """
        util.require_keys(kwargs, ['tid', 'accid', 'begintime', 'endtime', 'limit'], False)
        return self.post_request('/history/queryTeamMsg.action', data=kwargs)

    def query_chatroom_msg(self, **kwargs):
        """
        聊天室云端历史消息查询
        """
        util.require_keys(kwargs, ['roomid', 'accid', 'timetag', 'limit'], False)
        return self.post_request('/history/queryChatroomMsg.action', data=kwargs)

    def query_user_events(self, **kwargs):
        """
        用户登录登出事件记录查询
        """
        util.require_keys(kwargs, ['accid', 'begintime', 'endtime', 'limit'], False)
        return self.post_request('/history/queryUserEvents.action', data=kwargs)

    def delete_media_file(self, **kwargs):
        """
        删除音视频/白板服务器录制文件
        """
        util.require_keys(kwargs, ['channelid'], False)
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
        util.require_keys(kwargs, ['broadcastId'], False)
        return self.post_request('/history/queryBroadcastMsgById.action', data=kwargs)
