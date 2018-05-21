# -*- coding: utf-8 -*-

"""NIM REST API Python Client"""

from __future__ import absolute_import

import hashlib
import os
import time

from netease_im import util

__author__ = "Manson Li"
__email__ = "manson.li3307@gmail.com"


class BaseComponent(util.ApiClient):
    """A base component"""

    def __init__(self, base_uri=None, config=None, timeout=15, **kwargs):
        """Setup a base component

        :param base_uri: The base URI to the API
        :param config: The config details
        :param timeout: The timeout to use for requests
        :param \*\*kwargs: Any other attributes. These will be added as
                           attributes to the ApiClient object.
        """
        super(BaseComponent, self).__init__(
            base_uri=base_uri, timeout=timeout, config=config, **kwargs)

    def post_request(
            self, endpoint, params=None, data=None, headers=None, cookies=None):
        """Helper function for POST requests

        Since the NIM API only uses POST requests and each post request
        must include all of the config data, this method ensures that all
        of that data is there

        :param endpoint: The endpoint
        :param params: The URL parameters
        :param data: The data (either as a dict or dumped JSON string) to
                     include with the POST
        :param headers: request headers
        :param cookies: request cookies
        :return: The :class:``requests.Response`` object for this request
        """

        # 增加公共header
        headers = headers or {}
        headers.update(self.im_header())
        if 'Content-Type' not in headers:
            headers.update({
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
            })

        return super(BaseComponent, self).post_request(
            endpoint, params=params, data=data, headers=headers,
            cookies=cookies)

    def im_header(self):
        """
        根据NIM文档，每个请求header中，都需要携带校验相关的信息
        :return: common header
        """

        # 开发者平台分配的appkey
        api_key = self.config['api_key']

        # 32随机数（最大长度128个字符）
        nonce = ''.join(map(lambda xx: (hex(ord(xx))[2:]), os.urandom(16)))

        # 当前UTC时间戳，从1970年1月1日0点0 分0 秒开始到现在的秒数(String)
        curtime = str(int(time.time()))

        # SHA1(AppSecret + Nonce + CurTime),三个参数拼接的字符串，进行SHA1哈希计算，转化成16进制字符(String，小写)
        sha = hashlib.sha1('%s%s%s' % (self.config['api_secret'], nonce, curtime))
        checksum = sha.hexdigest()

        return {
            'AppKey': api_key,
            'Nonce': nonce,
            'CurTime': curtime,
            'CheckSum': checksum,
        }
