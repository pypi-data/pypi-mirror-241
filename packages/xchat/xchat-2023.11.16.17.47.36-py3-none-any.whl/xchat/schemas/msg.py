#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : msg
# @Time         : 2023/11/3 17:23
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :
import time

from pydantic import constr

from meutils.pipe import *


class RecommendInfo(BaseModel):
    UserName: str = ''
    NickName: str = ''
    QQNum: int = '0'
    Province: str = ''
    City: str = ''
    Content: str = ''
    Signature: str = ''
    Alias: str = ''
    Scene: int = '0'
    VerifyFlag: int = '0'
    AttrStatus: int = '0'
    Sex: int = '0'
    Ticket: str = ''
    OpCode: int = '0'


class Member(BaseModel):
    MemberList: list = []
    Uin: int = '0'
    UserName: str = ''
    NickName: str = ''
    AttrStatus: int = 0
    PYInitial: str = ''
    PYQuanPin: str = ''
    RemarkPYInitial: str = ''
    RemarkPYQuanPin: str = ''
    MemberStatus: int = 0
    DisplayName: str = ''
    KeyWord: str = ''


class Self(Member):
    """机器人属性"""


class User(BaseModel):
    """群属性"""
    MemberList: List[Member]

    Uin: int = '0'
    UserName: str = '@@...'
    NickName: constr(to_lower=True) = ''  # 群昵称
    HeadImgUrl: str = '/cgi-bin/mmwebwx-bin/webwxgetheadimg?seq=805036502&username=@@...&skey='
    ContactFlag: int = 0
    MemberCount: int = 0
    RemarkName: str = ''
    HideInputBarFlag: int = 0
    Sex: int = 0
    Signature: str = ''
    VerifyFlag: int = 0
    OwnerUin: int = 0
    PYInitial: str = ''  # 'XCHATCHATLLM'
    PYQuanPin: str = ''  # 'Xchatchatllm'
    RemarkPYInitial: str = ''
    RemarkPYQuanPin: str = ''
    StarFriend: int = 0
    AppAccountFlag: int = 0
    Statues: int = 1
    AttrStatus: int = 0
    Province: str = ''
    City: str = ''
    Alias: str = ''
    SnsFlag: int = 0
    UniFriend: int = 0
    DisplayName: str = ''
    ChatRoomId: int = 0
    KeyWord: str = ''
    EncryChatRoomId: str = '@...'
    IsOwner: int = '1'
    IsAdmin: str = None

    Self: Self = Self()  # 机器人微信信息


class Message(BaseModel):
    MsgId: str = ''
    FromUserName: str = '@...'
    ToUserName: str = '@@...'  # @@是接收信息的群ID
    MsgType: int = 49
    Content: str = ''
    Status: int = 3
    ImgStatus: int = 1
    CreateTime: int = Field(default_factory=lambda: int(time.time()))
    VoiceLength: int = 0
    PlayLength: int = 0
    FileName: str = ''  # 'xx.doc'
    FileSize: str = '633344'
    MediaId: str = '@crypt_...'
    Url: str = ''
    AppMsgType: int = 6
    StatusNotifyCode: int = 0
    StatusNotifyUserName: str = ''

    RecommendInfo: RecommendInfo = RecommendInfo()

    ForwardFlag: int = '0'
    AppInfo: dict = {'AppID': '', 'Type': 0}
    HasProductId: int = '0'
    Ticket: str = ''
    ImgHeight: int = '0'
    ImgWidth: int = '0'
    SubMsgType: int = '0'
    NewMsgId: int = '1316678251262129000'
    OriContent: str = ''
    EncryFileName: str = '%E8%80%B6%E8%B7%AF%E6%92%92%E5%86%B7%E4%B8%89%E5%8D%83%E5%B9%B4%2Edoc'
    ActualNickName: str = ''  # 群里展示的昵称

    IsAt: bool = False
    ActualUserName: str = '@...'

    # user: User = Field(alias='User')
    User: User

    Type: str = 'Attachment'
    Text: Any = '{}'  # 可能是函数

    # 增强
    chatroom_name: str = None
    chatroom_id: str = None

    user_name: str = None

    # download: Callable = None

    def __init__(self, **data: Any):
        super().__init__(**data)

        self.chatroom_name = self.User.NickName  # 已被转小写
        self.chatroom_id = self.User.UserName

        self.user_name = self.User.NickName  # 人昵称 不是机器人昵称


if __name__ == '__main__':
    d = {'MsgId': '1316678251262128814', 'FromUserName': '@74b453ddc9611c5493fdc787f577d4cf',
         'ToUserName': '@@c9591096040bc439437c36a1113348b063e2aa52bca6fd95b385cb2c0fd3a721', 'MsgType': 49,
         'Content': '', 'Status': 3, 'ImgStatus': 1, 'CreateTime': 1699002776, 'VoiceLength': 0, 'PlayLength': 0,
         'FileName': '耶路撒冷三千年.doc', 'FileSize': '633344',
         'MediaId': '@crypt_3f3d67af_b1a633396e70020d1b7aefa27523ba3543af6d310945d6e153ee9fea13f5f42f78c9fed6c09a9fb83ee2860948d457745fe78b1c7d85a108f7c7a7ae72d3af90809ac28e991f18992b1ce1cfed3accb671a427dc8318dc865cde8f06a5402d93119e165cc71d41f6659d55d287e687825187a7c1b2026e29076174c298e5f9ce54ebfb260ddcc62822d28c9fdff7f70c80fc2d732bb35c2f2c026735fc9ad508b8450c901cc92f32daf35d63dabe7c9efeb67bf2449611c5ce043106aa4ebe0d04275197943eb684c35f5300c9f58bd4fe2b71e0b5e2854587b12aa88bafe617',
         'Url': '', 'AppMsgType': 6, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '',
         'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 'City': '', 'Content': '',
                           'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0,
                           'Ticket': '', 'OpCode': 0}, 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0},
         'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0,
         'NewMsgId': 1316678251262128814, 'OriContent': '',
         'EncryFileName': '%E8%80%B6%E8%B7%AF%E6%92%92%E5%86%B7%E4%B8%89%E5%8D%83%E5%B9%B4%2Edoc',
         'ActualNickName': 'Bettermeeeeeee', 'IsAt': "False", 'ActualUserName': '@74b453ddc9611c5493fdc787f577d4cf',
         'User': {'MemberList': [{'MemberList': [], 'Uin': 0,
                                  'UserName': '@5398ace5532a6968cf8184a021ba490df3a7ee397a4d1225952dd31273741941',
                                  'NickName': 'firebot', 'AttrStatus': 102725, 'PYInitial': '', 'PYQuanPin': '',
                                  'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'MemberStatus': 0,
                                  'DisplayName': 'firebotqqqqqqq', 'KeyWord': ''},
                                 {'MemberList': [], 'Uin': 0, 'UserName': '@74b453ddc9611c5493fdc787f577d4cf',
                                  'NickName': 'Betterme', 'AttrStatus': 125031, 'PYInitial': '', 'PYQuanPin': '',
                                  'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'MemberStatus': 0,
                                  'DisplayName': 'Bettermeeeeeee', 'KeyWord': 'qq-'}, {'MemberList': [], 'Uin': 0,
                                                                                       'UserName': '@2ed8079bb83e67eb0f40309c1fa7aa204386e389f6d84632312301d8670bf64c',
                                                                                       'NickName': 'java严跃',
                                                                                       'AttrStatus': 104485,
                                                                                       'PYInitial': '', 'PYQuanPin': '',
                                                                                       'RemarkPYInitial': '',
                                                                                       'RemarkPYQuanPin': '',
                                                                                       'MemberStatus': 0,
                                                                                       'DisplayName': '',
                                                                                       'KeyWord': ''}], 'Uin': 0,
                  'UserName': '@@c9591096040bc439437c36a1113348b063e2aa52bca6fd95b385cb2c0fd3a721',
                  'NickName': 'Xchat chatllm',
                  'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgetheadimg?seq=805036502&username=@@c9591096040bc439437c36a1113348b063e2aa52bca6fd95b385cb2c0fd3a721&skey=',
                  'ContactFlag': 2050, 'MemberCount': 3, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 0,
                  'Signature': '', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'XCHATCHATLLM',
                  'PYQuanPin': 'Xchatchatllm', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0,
                  'AppAccountFlag': 0, 'Statues': 1, 'AttrStatus': 0, 'Province': '', 'City': '', 'Alias': '',
                  'SnsFlag': 0, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '',
                  'EncryChatRoomId': '@441ad7c99d89e58312bdd882a220096d', 'IsOwner': 1, 'IsAdmin': "None",
                  'Self': {'MemberList': [], 'Uin': 0, 'UserName': '@74b453ddc9611c5493fdc787f577d4cf',
                           'NickName': 'Betterme', 'AttrStatus': 125031, 'PYInitial': '', 'PYQuanPin': '',
                           'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'MemberStatus': 0,
                           'DisplayName': 'Bettermeeeeeee', 'KeyWord': 'qq-'}}, 'Type': 'Attachment', 'Text': {}

         }

    # r = d['User']['Self']
    # rprint(Self(**r))

    #########
    # r = d['User']['MemberList'][0]
    # rprint(r)
    # rprint(Member(**r).dict())

    # r = d['User']
    # rprint(r)
    # rprint(User(**r).dict()['MemberList'])
    # rprint(User(**r).dict()['Self'])

    rprint(Message(**d).dict())
    # rprint(Message(**d).dict())
    # rprint(Message(**d).dict())
