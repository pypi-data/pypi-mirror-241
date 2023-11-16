#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : utils
# @Time         : 2023/11/6 15:25
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 

from meutils.pipe import *

from xchat.schemas.msg import Message


@decorator
def msg_filter(reply_fn, chatroom_regexp: Optional[str] = None, *msgs):
    """
        过滤群聊、私聊
    """
    msg = Message(**obj_to_dict(msgs[0]))

    # msg.FromUserName

    if (
            msg.CreateTime > time.time() - 5
            and (re.search(chatroom_regexp, msg.chatroom_name) if chatroom_regexp else True)  # 群匹配
            and "user"  # 人匹配

    ):
        return reply_fn(msg)


@decorator
def friendchat_msg(reply_fn, chatroom_regexp: Optional[str] = None, *msgs):
    """
        过滤群聊、私聊
    """
    msg = Message(**obj_to_dict(msgs[0]))



    # msg.FromUserName

    if (
            msg.CreateTime > time.time() - 5
            and (re.search(chatroom_regexp, msg.chatroom_name) if chatroom_regexp else True)  # 群匹配
            and "user"  # 人匹配

    ):
        return reply_fn(msg)