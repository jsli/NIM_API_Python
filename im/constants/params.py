# -*- coding: utf-8 -*-

FRIEND_ADD_SILENTLY = 1  # 直接加好友
FRIEND_ADD_REQUEST = 2  # 请求加好友
FRIEND_ADD_AGREE = 3  # 同意加好友
FRIEND_ADD_REFUSE = 4  # 拒绝加好友


RELATION_TYPE_BLACK = 1  # 黑名单操作
RELATION_TYPE_MUTE = 2  # 静音列表操作

OP_VALUE_REMOVE = 0  # 取消黑名单或静音
OP_VALUE_ADD = 1  # 加入黑名单或静音

MESSAGE_OPE_USER = 0  # 点对点个人消息
MESSAGE_OPE_TEAM = 1  # 群消息

MESSAGE_TYPE_TEXT = 0  # 文本消息
MESSAGE_TYPE_IMAGE = 1  # 图片消息
MESSAGE_TYPE_AUDIO = 2  # 语音消息
MESSAGE_TYPE_VIDEO = 3  # 视频消息
MESSAGE_TYPE_LOCATION = 4  # 地理位置消息
MESSAGE_TYPE_FILE = 6  # 文件消息
MESSAGE_TYPE_CUSTOM = 100  # 自定义消息类型

ATTACH_MESSAGE_TYPE_USER = 0  # 点对点自定义系统通知
ATTACH_MESSAGE_TYPE_TEAM = 1  # 群消息自定义系统通知

RECALL_TYPE_USER = 7  # 点对点消息撤回
RECALL_TYPE_TEAM = 8  # 表示群消息撤回
