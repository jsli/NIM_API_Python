# NIM_API_Python

网易云信服务端API封装(python)

[![](https://secure.travis-ci.org/jsli/NIM_API_Python.png?branch=master "Build Status")](http://travis-ci.org/jsli/NIM_API_Python)
[![](https://pypip.in/py_versions/NIM_API_Python/badge.svg "Supported Python versions")](https://pypi.python.org/pypi/NIM_API_Python/)
[![](https://pypip.in/status/NIM_API_Python/badge.svg "Development Status")](https://pypi.python.org/pypi/NIM_API_Python/)
[![](https://pypip.in/version/NIM_API_Python/badge.svg "Latest Version")](https://pypi.python.org/pypi/NIM_API_Python/)
[![](https://pypip.in/license/NIM_API_Python/badge.svg "License")](https://pypi.python.org/pypi/NIM_API_Python/)


Installation
------------

### The production way

```sh
pip install NIM-API-Python
```

### The developer way

```sh
git clone https://github.com/jsli/NIM_API_Python.git
cd NIM_API_Python
git checkout -b develop origin/develop
python setup.py install
```

Compatability
-------------

NIM-API-Python has been tested for Python 2.6, 3.2, 3.3, 3.4, and pypy using [Travis CI](https://travis-ci.org/jsli/NIM_API_Python)

Example Usage
-------------

### Create the client

```python
from im import ImClient

client = ImClient('API_KEY', 'API_SECRET')
client.user.create(...)
```

### Using with a manage context

```python
with ZoomClient('API_KEY', 'API_SECRET') as client:
    client.user.create(...)
    ...
```


Available methods
-----------------

> 具体参数请参考：[网易云信 服务端API文档](http://dev.netease.im/docs/product/IM即时通讯/服务端API文档/接口概述)

### user
* client.user.create(...)
* client.user.update(...)
* client.user.refresh_token(...)
* client.user.block(...)
* client.user.unblock(...)
* client.user.update_info(...)
* client.user.get_info(...)
* client.user.set_donnop(...)
* client.user.set_special_relation(...)
* client.user.list_black_and_mute(...)

### team
* client.team.create(...)
* client.team.add(...)
* client.team.kick(...)
* client.team.remove(...)
* client.team.update(...)
* client.team.query(...)
* client.team.query_detail(...)
* client.team.get_mark_read_info(...)
* client.team.change_owner(...)
* client.team.add_manager(...)
* client.team.remove_manager(...)
* client.team.join_teams(...)
* client.team.update_team_nick(...)
* client.team.mute_team(...)
* client.team.mute_tlist(...)
* client.team.leave(...)
* client.team.mute_tlist_all(...)
* client.team.list_team_mute(...)

### message
* client.message.send_msg(...)
* client.message.send_batch_msg(...)
* client.message.send_attach_msg(...)
* client.message.send_batch_attach_msg(...)
* client.message.upload(...)
* client.message.upload_file(...)
* client.message.recall(...)
* client.message.broadcast_msg(...)


### history
* client.history.query_session_msg(...)
* client.history.query_team_msg(...)
* client.history.query_chatroom_msg(...)
* client.history.query_user_events(...)
* client.history.delete_media_file(...)
* client.history.query_broadcast_msg(...)
* client.history.query_broadcast_msg_by_id(...)

### friend
* client.friend.add(...)
* client.friend.update(...)
* client.friend.delete(...)
* client.friend.get(...)

### event
* client.event.subscribe_add(...)
* client.event.subscribe_delete(...)
* client.event.subscribe_batch_delete(...)
* client.event.subscribe_query(...)

### chatroom
* client.chatroom.create(...)
* client.chatroom.get(...)
* client.chatroom.get_batch(...)
* client.chatroom.update(...)
* client.chatroom.toggle_close_stat(...)
* client.chatroom.set_member_role(...)
* client.chatroom.update_my_room_role(...)
* client.chatroom.request_addr(...)
* client.chatroom.send_msg(...)
* client.chatroom.add_robot(...)
* client.chatroom.remove_robot(...)
* client.chatroom.temporary_mute(...)
* client.chatroom.queue_offer(...)
* client.chatroom.queue_poll(...)
* client.chatroom.queue_drop(...)
* client.chatroom.queue_init(...)
* client.chatroom.mute_room(...)
* client.chatroom.topn(...)
* client.chatroom.members_by_page(...)
* client.chatroom.query_members(...)
* client.chatroom.delete_history_msg(...)


Running the Tests
-----------------

### Simple

First, make sure to install the testing requirements

```sh
pip install -r requirements-tests.txt
```

Then run the tests via nose

```sh
nosetests -v -s
```
