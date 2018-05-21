# -*- coding: utf-8 -*-

"""NIM REST API Python Client -- Event component"""

from __future__ import absolute_import

import json

from netease_im import util
from netease_im.components import base
from netease_im.util import is_str_type

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class EventComponent(base.BaseComponent):
    """Component dealing with all user related matters"""

    def subscribe_add(self, **kwargs):
        """
        订阅在线状态事件
        """
        util.require_keys(kwargs, ['accid', 'eventType', 'publisherAccids', 'ttl'], False)
        if not is_str_type(kwargs['publisherAccids']):
            kwargs['publisherAccids'] = json.dumps(kwargs['publisherAccids'])
        return self.post_request('/event/subscribe/add.action', data=kwargs)

    def subscribe_delete(self, **kwargs):
        """
        取消在线状态事件订阅
        """
        util.require_keys(kwargs, ['accid', 'eventType', 'publisherAccids'], False)
        if not is_str_type(kwargs['publisherAccids']):
            kwargs['publisherAccids'] = json.dumps(kwargs['publisherAccids'])
        return self.post_request('/event/subscribe/delete.action', data=kwargs)

    def subscribe_batch_delete(self, **kwargs):
        """
        取消全部在线状态事件订阅
        """
        util.require_keys(kwargs, ['accid', 'eventType'], False)
        return self.post_request('/event/subscribe/batchdel.action', data=kwargs)

    def subscribe_query(self, **kwargs):
        """
        查询在线状态事件订阅关系
        """
        util.require_keys(kwargs, ['accid', 'eventType', 'publisherAccids'], False)
        return self.post_request('/event/subscribe/query.action', data=kwargs)
