# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CreateWeappQRUrlRequest(AbstractModel):
    """CreateWeappQRUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionKey: 代理角色临时密钥的Token
        :type SessionKey: str
        """
        self._SessionKey = None

    @property
    def SessionKey(self):
        return self._SessionKey

    @SessionKey.setter
    def SessionKey(self, SessionKey):
        self._SessionKey = SessionKey


    def _deserialize(self, params):
        self._SessionKey = params.get("SessionKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWeappQRUrlResponse(AbstractModel):
    """CreateWeappQRUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 渠道备案小程序二维码
        :type Url: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Url = None
        self._RequestId = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._RequestId = params.get("RequestId")


class DescribeGetAuthInfoRequest(AbstractModel):
    """DescribeGetAuthInfo请求参数结构体

    """


class DescribeGetAuthInfoResponse(AbstractModel):
    """DescribeGetAuthInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsTenPayMasked: 实名认证状态：0未实名，1已实名
        :type IsTenPayMasked: str
        :param _IsAuthenticated: 实名认证类型：0个人，1企业
        :type IsAuthenticated: str
        :param _Type: 认证类型，个人0，企业1
        :type Type: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsTenPayMasked = None
        self._IsAuthenticated = None
        self._Type = None
        self._RequestId = None

    @property
    def IsTenPayMasked(self):
        return self._IsTenPayMasked

    @IsTenPayMasked.setter
    def IsTenPayMasked(self, IsTenPayMasked):
        self._IsTenPayMasked = IsTenPayMasked

    @property
    def IsAuthenticated(self):
        return self._IsAuthenticated

    @IsAuthenticated.setter
    def IsAuthenticated(self, IsAuthenticated):
        self._IsAuthenticated = IsAuthenticated

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsTenPayMasked = params.get("IsTenPayMasked")
        self._IsAuthenticated = params.get("IsAuthenticated")
        self._Type = params.get("Type")
        self._RequestId = params.get("RequestId")


class SyncIcpOrderWebInfoRequest(AbstractModel):
    """SyncIcpOrderWebInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IcpOrderId: 备案ICP订单号
        :type IcpOrderId: str
        :param _SourceWebId: 订单里的webId
        :type SourceWebId: str
        :param _TargetWebIds: 订单里的webId 数组(如果传入的webIds含有 订单中不包含的webId，会自动跳过)
        :type TargetWebIds: list of str
        :param _SyncFields: 网站信息字段名 数组
        :type SyncFields: list of str
        :param _CheckSamePerson: 是否先判断同步的网站负责人是否一致 (这里会判断 sitePersonName, sitePersonCerType,sitePersonCerNum三个字段完全一致)  默认:true. 非必要 不建议关闭修改该参数默认值
        :type CheckSamePerson: bool
        """
        self._IcpOrderId = None
        self._SourceWebId = None
        self._TargetWebIds = None
        self._SyncFields = None
        self._CheckSamePerson = None

    @property
    def IcpOrderId(self):
        return self._IcpOrderId

    @IcpOrderId.setter
    def IcpOrderId(self, IcpOrderId):
        self._IcpOrderId = IcpOrderId

    @property
    def SourceWebId(self):
        return self._SourceWebId

    @SourceWebId.setter
    def SourceWebId(self, SourceWebId):
        self._SourceWebId = SourceWebId

    @property
    def TargetWebIds(self):
        return self._TargetWebIds

    @TargetWebIds.setter
    def TargetWebIds(self, TargetWebIds):
        self._TargetWebIds = TargetWebIds

    @property
    def SyncFields(self):
        return self._SyncFields

    @SyncFields.setter
    def SyncFields(self, SyncFields):
        self._SyncFields = SyncFields

    @property
    def CheckSamePerson(self):
        return self._CheckSamePerson

    @CheckSamePerson.setter
    def CheckSamePerson(self, CheckSamePerson):
        self._CheckSamePerson = CheckSamePerson


    def _deserialize(self, params):
        self._IcpOrderId = params.get("IcpOrderId")
        self._SourceWebId = params.get("SourceWebId")
        self._TargetWebIds = params.get("TargetWebIds")
        self._SyncFields = params.get("SyncFields")
        self._CheckSamePerson = params.get("CheckSamePerson")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncIcpOrderWebInfoResponse(AbstractModel):
    """SyncIcpOrderWebInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")