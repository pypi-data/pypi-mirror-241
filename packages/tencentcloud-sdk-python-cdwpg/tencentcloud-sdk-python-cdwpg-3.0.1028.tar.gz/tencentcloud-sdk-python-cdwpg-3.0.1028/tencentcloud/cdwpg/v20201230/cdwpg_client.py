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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cdwpg.v20201230 import models


class CdwpgClient(AbstractClient):
    _apiVersion = '2020-12-30'
    _endpoint = 'cdwpg.tencentcloudapi.com'
    _service = 'cdwpg'


    def CreateInstanceByApi(self, request):
        """创建集群

        :param request: Request instance for CreateInstanceByApi.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.CreateInstanceByApiRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CreateInstanceByApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceByApi", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceByApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        """根据实例ID查询某个实例的具体信息

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceInfo(self, request):
        """获取集群信息

        :param request: Request instance for DescribeInstanceInfo.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceInfoRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceState(self, request):
        """集群详情页中显示集群状态、流程进度等

        :param request: Request instance for DescribeInstanceState.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceStateRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """获取云原生实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSimpleInstances(self, request):
        """获取集群实例列表

        :param request: Request instance for DescribeSimpleInstances.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeSimpleInstancesRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeSimpleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSimpleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSimpleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyInstanceByApi(self, request):
        """销毁集群

        :param request: Request instance for DestroyInstanceByApi.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DestroyInstanceByApiRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DestroyInstanceByApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstanceByApi", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstanceByApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        """修改实例信息，目前为实例名称

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))