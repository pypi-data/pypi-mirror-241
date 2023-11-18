"""
The HEA Server AWS Accounts Microservice provides ...
"""
import logging
from asyncio import gather, get_running_loop
from heaserver.service.heaobjectsupport import type_to_resource_url
from heaserver.service.oidcclaimhdrs import SUB
from heaserver.service.runner import init_cmd_line, routes, start, web
from heaserver.service.db import aws, awsservicelib
from heaserver.service.wstl import builder_factory, action
from heaserver.service import response, client
from heaserver.service.appproperty import HEA_DB
from heaserver.service.heaobjectsupport import new_heaobject_from_type
from heaobject.account import AWSAccount
from heaobject.bucket import AWSBucket
from heaobject.storage import AWSStorage
from heaobject.folder import AWSS3BucketItem
from heaobject.root import DesktopObjectDict
from heaobject.volume import AWSFileSystem
from yarl import URL
from aiohttp import hdrs
from aiohttp.web import Request, Response
from typing import Awaitable
from botocore.exceptions import ClientError as BotoClientError
from aiohttp.client_exceptions import ClientError, ClientResponseError
from heaserver.service.activity import DesktopObjectActionLifecycle, Status
from heaserver.service.messagebroker import publish_desktop_object



@routes.get('/ping')
async def ping(request: web.Request) -> web.Response:
    """
    For testing whether the service is up.

    :param request: the HTTP request.
    :return: Always returns status code 200.
    """
    return response.status_ok(None)


@routes.get('/awsaccounts/{id}')
@action('heaserver-accounts-awsaccount-get-open-choices', rel='hea-opener-choices hea-context-menu', path='awsaccounts/{id}/opener')
@action('heaserver-accounts-awsaccount-get-properties', rel='hea-properties hea-context-menu')
@action('heaserver-accounts-awsaccount-get-create-choices', rel='hea-creator-choices hea-context-menu', path='awsaccounts/{id}/creator')
@action('heaserver-accounts-awsaccount-get-trash', rel='hea-trash hea-context-menu', path='volumes/{volume_id}/awss3trash')
@action('heaserver-accounts-awsaccount-get-self', rel='self hea-account', path='awsaccounts/{id}')
@action(name='heaserver-accounts-awsaccount-get-volume', rel='hea-volume', path='volumes/{volume_id}')
async def get_awsaccount(request: web.Request) -> web.Response:
    """
    Gets the AWS account with the given id. IIf no AWS credentials can be found, it uses any credentials found by the
    AWS boto3 library.

    :param request: the HTTP request.
    :return: a Response object with the requested AWS account or Not Found.
    ---
    summary: The user's AWS account.
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        id_ = request.match_info['id']
    except KeyError as e:
        return response.status_bad_request(str(e))
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting AWS account {id_}',
                                                activity_cb=publish_desktop_object) as activity:
        account, volume_id = await _get_account_by_id(request)
        logger = logging.getLogger(__name__)
        logger.debug('Got account %s and volume %s', account, volume_id)
        request.match_info['volume_id'] = volume_id
        if account is None:
            raise response.status_not_found()
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_object_id = id_
        activity.new_object_uri = f'awsaccounts/{id_}'
        activity.new_volume_id = volume_id
        return await response.get(request, account.to_dict())


@routes.get('/awsaccounts/byname/{name}')
@action('heaserver-accounts-awsaccount-get-self', rel='self hea-account', path='awsaccounts/{id}')
@action(name='heaserver-accounts-awsaccount-get-volume', rel='hea-volume', path='volumes/{volume_id}')
async def get_awsaccount_by_name(request: web.Request) -> web.Response:
    """
    Gets the AWS account with the given id. If no AWS credentials can be found, it uses any credentials found by the
    AWS boto3 library.

    :param request: the HTTP request.
    :return: a Response object with the requested AWS account or Not Found.
    ---
    summary: The user's AWS account.
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - $ref: '#/components/parameters/name'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        name = request.match_info['name']
    except KeyError as e:
        return response.status_bad_request(str(e))
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting AWS account {name}',
                                                activity_cb=publish_desktop_object) as activity:
        account, volume_id = await _get_account_by_name(request)
        request.match_info['volume_id'] = volume_id
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_object_id = name
        activity.new_object_uri = f'awsaccounts/{name}'
        return await response.get(request, account.to_dict() if account is not None else None)


@routes.get('/awsaccounts')
@routes.get('/awsaccounts/')
@action('heaserver-accounts-awsaccount-get-open-choices', rel='hea-opener-choices hea-context-menu', path='awsaccounts/{id}/opener')
@action('heaserver-accounts-awsaccount-get-properties', rel='hea-properties hea-context-menu')
@action('heaserver-accounts-awsaccount-get-create-choices', rel='hea-creator-choices hea-context-menu', path='awsaccounts/{id}/creator')
@action('heaserver-accounts-awsaccount-get-self', rel='self', path='awsaccounts/{id}')
async def get_awsaccounts(request: web.Request) -> web.Response:
    """
    Gets all AWS accounts. If no AWS credentials can be found, it uses any credentials found by the AWS boto3 library.

    :param request: the HTTP request.
    :return: a Response object with the requested AWS accounts or the empty list
    ---
    summary: The user's AWS accounts.
    tags:
        - heaserver-accounts-awsaccount
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting all AWS accounts',
                                                activity_cb=publish_desktop_object) as activity:
        aws_accounts = await _get_all_accounts(request)
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_object_uri = 'awsaccounts/'
        return await response.get_all(request, [account.to_dict() for account in aws_accounts])


@routes.get('/volumes/{volume_id}/awsaccounts/me')
@action('heaserver-accounts-awsaccount-get-open-choices', rel='hea-opener-choices hea-context-menu',
        path='volumes/{volume_id}/awsaccounts/me/opener')
@action('heaserver-accounts-awsaccount-get-properties', rel='hea-properties hea-context-menu')
@action('heaserver-accounts-awsaccount-get-create-choices', rel='hea-creator-choices hea-context-menu', path='awsaccounts/{id}/creator')
@action('heaserver-accounts-awsaccount-get-trash', rel='hea-trash hea-context-menu', path='volumes/{volume_id}/awss3trash')
@action('heaserver-accounts-awsaccount-get-self', rel='self hea-account', path='awsaccounts/{id}')
@action(name='heaserver-accounts-awsaccount-get-volume', rel='hea-volume', path='volumes/{volume_id}')
async def get_awsaccount_by_volume_id(request: web.Request) -> web.Response:
    """
    Gets the AWS account associated with the given volume id. If the volume's credentials are None, it uses any
    credentials found by the AWS boto3 library.

    :param request: the HTTP request.
    :return: the requested AWS account or Not Found.
    ---
    summary: The user's AWS account.
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the user's AWS volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting my AWS account',
                                                activity_cb=publish_desktop_object) as activity:
        try:
            volume_id = request.match_info['volume_id']
        except KeyError as e:
            return response.status_bad_request(str(e))
        resp = await _get_account(request, volume_id)
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_volume_id = volume_id
        activity.new_object_uri = f'volumes/{volume_id}/awsaccounts/me'
        return resp


@routes.get('/awsaccounts/{id}/opener')
@action('heaserver-accounts-awsaccount-open-buckets',
        rel=f'hea-opener hea-context-aws hea-default {AWSBucket.get_mime_type()}', path='volumes/{volume_id}/bucketitems/')
@action('heaserver-accounts-awsaccount-open-storage',
        rel=f'hea-opener hea-context-aws {AWSStorage.get_mime_type()}', path='volumes/{volume_id}/storage/')
async def get_awsaccount_opener(request: web.Request) -> web.Response:
    """
    Gets choices for opening an AWS account.

    :param request: the HTTP Request.
    :return: A Response object with a status of Multiple Choices or Not Found.
    ---
    summary: AWS account opener choices
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '300':
        $ref: '#/components/responses/300'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        id_ = request.match_info['id']
    except KeyError as e:
        return response.status_bad_request(str(e))
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Accessing AWS account {id_}',
                                                activity_cb=publish_desktop_object) as activity:
        volume_id = await awsservicelib.get_volume_id_for_account_id(request)
        if volume_id is None:
            activity.status = Status.FAILED
            return response.status_not_found()
        request.match_info['volume_id'] = volume_id  # Needed to make the actions work.
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_object_uri = f'awsaccounts/{id_}'
        activity.new_object_id = id_
        activity.new_volume_id = volume_id
        return await response.get_multiple_choices(request)


@routes.get('/volumes/{volume_id}/awsaccounts/me/opener')
@action('heaserver-accounts-awsaccount-open-buckets',
        rel=f'hea-opener hea-context-aws hea-default {AWSBucket.get_mime_type()}', path='volumes/{volume_id}/bucketitems/')
@action('heaserver-accounts-awsaccount-open-storage',
        rel=f'hea-opener hea-context-aws {AWSStorage.get_mime_type()}', path='volumes/{volume_id}/storage/')
async def get_awsaccount_opener_by_volume_id(request: web.Request) -> web.Response:
    """
    Gets choices for opening an AWS account.

    :param request: the HTTP Request.
    :return: A Response object with a status of Multiple Choices or Not Found.
    ---
    summary: AWS account opener choices
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the user's AWS volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
    responses:
      '300':
        $ref: '#/components/responses/300'
      '404':
        $ref: '#/components/responses/404'
    """
    volume_id = request.match_info['volume_id']
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting my AWS account',
                                                activity_cb=publish_desktop_object) as activity:
        resp = await _account_opener(request, volume_id)
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_object_uri = f'volumes/{volume_id}/awsaccounts/me'
        activity.new_volume_id = volume_id
        return resp


# @routes.post('/volumes/{volume_id}/awsaccounts/me')
# async def post_account_awsaccounts(request: web.Request) -> web.Response:
#     """
#     Posts the awsaccounts information given the correct access key and secret access key.
#
#     :param request: the HTTP request.
#     :return: the requested awsaccounts or Not Found.
#
#     FIXME: should only be permitted by an AWS organization administrator, I would think. Need to sort out what the call looks like.
#     """
#     return await awsservicelib.post_account(request)


@routes.put('/volumes/{volume_id}/awsaccounts/me')
async def put_account_awsaccounts(request: web.Request) -> web.Response:
    """
    Puts the awsaccounts information given the correct access key and secret access key.

    :param request: the HTTP request.
    :return: the requested awsaccounts or Not Found.
    """
    try:
        volume_id = request['volume_id']
    except KeyError as e:
        return response.status_bad_request(str(e))
    alt_contact_type = request.match_info.get("alt_contact_type", None)
    email_address = request.match_info.get("email_address", None)
    name = request.match_info.get("name", None)
    phone = request.match_info.get("phone", None)
    title = request.match_info.get("title", None)

    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-delete',
                                                description=f'Updating my AWS account',
                                                activity_cb=publish_desktop_object) as activity:
        activity.old_object_type_name = AWSAccount.get_type_name()
        activity.old_object_uri = f'volumes/{volume_id}/awsaccounts/me'
        activity.old_volume_id = volume_id
        try:
            async with aws.AccountClientContext(request, volume_id) as acc_client:
                async with aws.STSClientContext(request, volume_id) as sts_client:
                    def do():
                        account_id = sts_client.get_caller_identity().get('Account')
                        acc_client.put_alternate_contact(AccountId=account_id, AlternateContactType=alt_contact_type,
                                                        EmailAddress=email_address, Name=name, PhoneNumber=phone, Title=title)
                    await get_running_loop().run_in_executor(None, do)
                    activity.new_object_type_name = AWSAccount.get_type_name()
                    activity.new_object_uri = f'volumes/{volume_id}/awsaccounts/me'
                    activity.new_volume_id = volume_id
            return web.HTTPNoContent()
        except BotoClientError as e:
            activity.status = Status.FAILED
            return web.HTTPBadRequest()


@routes.delete('/volumes/{volume_id}/awsaccounts/me')
async def delete_account_awsaccounts(request: web.Request) -> web.Response:
    """
    Deletes the awsaccounts information given the correct access key and secret access key.

    :param request: the HTTP request.
    :return: the requested awsaccounts or Not Found.

    FIXME: should only be permitted by an AWS organization administrator, I would think. Need to sort out what the call looks like.
    """
    return response.status_not_found()


@routes.get('/awsaccounts/{id}/creator')
@action('heaserver-accounts-awsaccount-create-bucket', rel='hea-creator hea-default application/x.bucket',
        path='awsaccounts/{id}/newbucket')
async def get_account_creator(request: web.Request) -> web.Response:
    """
        Gets account creator choices.

        :param request: the HTTP Request.
        :return: A Response object with a status of Multiple Choices or Not Found.
        ---
        summary: Account creator choices
        tags:
            - heaserver-accounts-awsaccount
        parameters:
            - $ref: '#/components/parameters/id'
        responses:
          '300':
            $ref: '#/components/responses/300'
          '404':
            $ref: '#/components/responses/404'
        """
    try:
        id_ = request.match_info['id']
    except KeyError as e:
        return response.status_bad_request(str(e))
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting AWS account {id_}',
                                                activity_cb=publish_desktop_object) as activity:
        volume_id = await awsservicelib.get_volume_id_for_account_id(request)
        if volume_id is None:
            activity.status = Status.FAILED
            return response.status_not_found()
        activity.new_object_id = id_
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_object_uri = f'awsaccounts/{id_}'
        activity.new_volume_id = volume_id
        return await response.get_multiple_choices(request)


@routes.get('/volumes/{volume_id}/awsaccounts/me/creator')
@action('heaserver-accounts-awsaccount-create-bucket', rel='hea-creator hea-default application/x.bucket',
        path='volumes/{volume_id}/awsaccounts/me/newbucket')
async def get_account_creator_by_volume_id(request: web.Request) -> web.Response:
    """
    Gets account creator choices.

    :param request: the HTTP Request.
    :return: A Response object with a status of Multiple Choices or Not Found.
    ---
    summary: Account creator choices
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
        - $ref: '#/components/parameters/id'
    responses:
      '300':
        $ref: '#/components/responses/300'
      '404':
        $ref: '#/components/responses/404'
    """
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting my AWS account',
                                                activity_cb=publish_desktop_object) as activity:
        volume_id = request.match_info["volume_id"]
        resp = await _account_opener(request, volume_id)
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_object_uri = f'volumes/{volume_id}/awsaccounts/me'
        activity.new_volume_id = volume_id
        return resp


@routes.get('/volumes/{volume_id}/awsaccounts/me/newbucket')
@routes.get('/volumes/{volume_id}/awsaccounts/me/newbucket/')
@action('heaserver-accounts-awsaccount-new-bucket-form')
async def get_new_bucket_form_by_volume_id(request: web.Request) -> web.Response:
    """
    Gets form for creating a new bucket in this account.

    :param request: the HTTP request. Required.
    :return: the current bucket, with a template for creating a child folder or Not Found if the requested item does not
    exist.
    ---
    summary: An account.
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting my AWS account',
                                                activity_cb=publish_desktop_object) as activity:
        volume_id = request.match_info["volume_id"]
        resp = await _get_account(request, volume_id)
        return resp


@routes.get('/awsaccounts/{id}/newbucket')
@routes.get('/awsaccounts/{id}/newbucket/')
@action('heaserver-accounts-awsaccount-new-bucket-form')
async def get_new_bucket_form(request: web.Request) -> web.Response:
    """
    Gets form for creating a new bucket in this account.

    :param request: the HTTP request. Required.
    :return: the current bucket, with a template for creating a child folder or Not Found if the requested item does not
    exist.
    ---
    summary: An account.
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        id_ = request.match_info['id']
    except KeyError as e:
        return response.status_bad_request(str(e))
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-get',
                                                description=f'Getting AWS account {id_}',
                                                activity_cb=publish_desktop_object) as activity:
        account, _ = await _get_account_by_id(request)
        activity.new_object_id = id_
        activity.new_object_type_name = AWSAccount.get_type_name()
        activity.new_object_uri = f'awsaccounts/{id_}'
        return await response.get(request, account.to_dict() if account is not None else None)


@routes.post('/volumes/{volume_id}/awsaccounts/me/newbucket')
@routes.post('/volumes/{volume_id}/awsaccounts/me/newbucket/')
async def post_new_bucket_by_volume_id(request: web.Request) -> web.Response:
    """
    Gets form for creating a new bucket in this account.

    :param request: the HTTP request. Required.
    :return: the current account, with a template for creating a bucket or Not Found if the requested account does not
    exist.
    ---
    summary: An account.
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - name: volume_id
          in: path
          required: true
          description: The id of the volume.
          schema:
            type: string
          examples:
            example:
              summary: A volume id
              value: 666f6f2d6261722d71757578
    requestBody:
        description: A new bucket.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: Folder example
                  value: {
                    "template": {
                      "data": [
                      {
                        "name": "display_name",
                        "value": "my-bucket"
                      },
                      {
                        "name": "type",
                        "value": "heaobject.bucket.AWSBucket"
                      },
                      {
                        "name": "region",
                        "value": "us-west-1"
                      }]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: Item example
                  value: {
                    "display_name": "my-bucket",
                    "type": "heaobject.bucket.AWSBucket",
                    "region": "us-west-1"
                  }
    responses:
      '201':
        $ref: '#/components/responses/201'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-create',
                                                description=f'Creating a new bucket in my AWS account',
                                                activity_cb=publish_desktop_object) as activity:
        logger = logging.getLogger(__name__)
        volume_id = request.match_info['volume_id']
        bucket_url = await type_to_resource_url(request, AWSBucket, file_system_type_or_type_name=AWSFileSystem)
        if bucket_url is None:
            raise ValueError('No AWSBucket service registered')
        headers = {SUB: request.headers[SUB]} if SUB in request.headers else None
        resource_base = str(URL(bucket_url) / volume_id / 'buckets')
        bucket = await new_heaobject_from_type(request, type_=AWSBucket)
        try:
            id_ = await client.post(request.app, resource_base, data=bucket, headers=headers)
            activity.new_object_id = id_
            activity.new_object_type_name = AWSBucket.get_type_name()
            activity.new_volume_id = volume_id
            activity.new_object_uri = f'volumes/{volume_id}/buckets/{id_}'
            return await response.post(request, id_, resource_base)
        except ClientResponseError as e:
            activity.status = Status.FAILED
            return response.status_generic(status=e.status, body=str(e))
        except ClientError as e:
            activity.status = Status.FAILED
            return response.status_generic(status=500, body=str(e))



@routes.post('/awsaccounts/{id}/newbucket')
@routes.post('/awsaccounts/{id}/newbucket/')
async def post_new_bucket(request: web.Request) -> web.Response:
    """
    Gets form for creating a new bucket in this account.

    :param request: the HTTP request. Required.
    :return: the current account, with a template for creating a bucket or Not Found if the requested account does not
    exist.
    ---
    summary: An account.
    tags:
        - heaserver-accounts-awsaccount
    parameters:
        - $ref: '#/components/parameters/id'
    requestBody:
        description: A new bucket.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: Folder example
                  value: {
                    "template": {
                      "data": [
                      {
                        "name": "display_name",
                        "value": "my-bucket"
                      },
                      {
                        "name": "type",
                        "value": "heaobject.bucket.AWSBucket"
                      },
                      {
                        "name": "region",
                        "value": "us-west-1"
                      }]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: Item example
                  value: {
                    "display_name": "my-bucket",
                    "type": "heaobject.bucket.AWSBucket",
                    "region": "us-west-1"
                  }
    responses:
      '201':
        $ref: '#/components/responses/201'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    try:
        id_ = request.match_info['id']
    except KeyError as e:
        return response.status_bad_request(str(e))
    async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-create',
                                                description=f'Creating a new bucket in AWS account',
                                                activity_cb=publish_desktop_object) as activity:
        logger = logging.getLogger(__name__)
        volume_id = await awsservicelib.get_volume_id_for_account_id(request)
        if volume_id is None:
            activity.status = Status.FAILED
            return response.status_bad_request(f'Invalid account id {request.match_info["id"]}')
        bucket_url = await type_to_resource_url(request, AWSBucket, file_system_type_or_type_name=AWSFileSystem)
        if bucket_url is None:
            raise ValueError('No AWSBucket service registered')
        headers = {SUB: request.headers[SUB]} if SUB in request.headers else None
        resource_base = str(URL(bucket_url) / volume_id / 'buckets')
        bucket = await new_heaobject_from_type(request, type_=AWSBucket)
        try:
            id_ = await client.post(request.app, resource_base, data=bucket, headers=headers)
            activity.new_object_id = id_
            activity.new_object_type_name = AWSBucket.get_type_name()
            activity.new_volume_id = volume_id
            activity.new_object_uri = f'volumes/{volume_id}/buckets/{id_}'
            return await response.post(request, id_, resource_base)
        except ClientResponseError as e:
            activity.status = Status.FAILED
            return response.status_generic(status=e.status, body=e.message)
        except ClientError as e:
            activity.status = Status.FAILED
            return response.status_generic(status=500, body=str(e))


def main() -> None:
    config = init_cmd_line(description='Manages account information details',
                           default_port=8080)
    start(package_name='heaserver-accounts', db=aws.S3Manager,
          wstl_builder_factory=builder_factory(__package__), config=config)


async def _account_opener(request: Request, volume_id: str) -> Response:
    """
    Gets choices for opening an account object.

    :param request: the HTTP request. Required. If an Accepts header is provided, MIME types that do not support links
    will be ignored.
    :param volume_id: the id string of the volume containing the requested HEA object. If None, the root volume is
    assumed.
    :return: a Response object with status code 300, and a body containing the HEA desktop object and links
    representing possible choices for opening the HEA desktop object; or Not Found.
    """
    if not await request.app[HEA_DB].has_account(request, volume_id):
        return response.status_not_found()
    return await response.get_multiple_choices(request)


async def _get_account(request: Request, volume_id: str) -> Response:
    """
    Gets the AWS account associated with the provided volume id.

    Only get since you can't delete or put id information
    currently being accessed. If organizations get included, then the delete, put, and post will be added for name,
    phone, email, ,etc.
    NOTE: maybe get email from the login portion of the application?

    :param request: the aiohttp Request (required).
    :param volume_id: the id string of the volume representing the user's AWS account.
    :return: an HTTP response with an AWSAccount object in the body.
    FIXME: a bad volume_id should result in a 400 status code; currently has status code 500.
    """
    aws_object = await request.app[HEA_DB].get_account(request, volume_id)
    return await response.get(request, aws_object.to_dict())


async def _get_account_by_id(request: web.Request) -> tuple[AWSAccount | None, str | None]:
    """
    Gets an account by its id and the account's volume id. The id is expected to be the request object's match_info
    mapping, with key 'id'.

    :param request: an aiohttp Request object (required).
    :return: a two-tuple containing an AWSAccount dict and volume id.
    """

    async def get_account_and_volume_id(account_getter: Awaitable[AWSAccount | None],
                                        volume_id_: str | None) -> tuple[AWSAccount | None, str | None]:
        """
        This function serves as a pass-through for volume ids so we can return the volume id along with the account
        dict.

        :param account_getter: the actual coroutine to get the account.
        :param volume_id_: the volume id.
        :return: a two-tuple containing the account dict and the volume id.
        """
        return await account_getter, volume_id_

    account, volume_id = next((a for a in await gather(
        *[get_account_and_volume_id(request.app[HEA_DB].get_account(request, v.id), v.id) async for v in
          request.app[HEA_DB].get_volumes(request, AWSFileSystem)])
                               if a[0].id == request.match_info['id']), (None, None))
    return account, volume_id


async def _get_account_by_name(request: web.Request) -> tuple[AWSAccount | None, str | None]:
    """
    Gets an account by its id and the account's volume id. The id is expected to be the request object's match_info
    mapping, with key 'id'.

    :param request: an aiohttp Request object (required).
    :return: a two-tuple containing an AWSAccount and volume id.
    """

    async def get_account_and_volume_id(account_getter: Awaitable[AWSAccount | None],
                                        volume_id_: str | None) -> tuple[AWSAccount | None, str | None]:
        """
        This function serves as a pass-through for volume ids so we can return the volume id along with the account
        dict.

        :param account_getter: the actual coroutine to get the account.
        :param volume_id_: the volume id.
        :return: a two-tuple containing the account dict and the volume id.
        """
        return await account_getter, volume_id_

    db = request.app[HEA_DB]
    account, volume_id = next((a for a in await gather(
        *[get_account_and_volume_id(db.get_account(request, v.id), v.id) async for v in
          db.get_volumes(request, AWSFileSystem)])
                               if a[0].id == request.match_info['name']), (None, None))
    return account, volume_id


async def _get_all_accounts(request: web.Request) -> list[AWSAccount]:
    """
    Gets all AWS accounts for the current user.

    In order for HEA to access an AWS account, there must be a volume accessible to the user through the volumes
    microservice with an AWSFileSystem for its file system, and credentials must either be stored in the keychain
    microservice and associated with the volume, or stored on the server's file system in a location searched by the
    AWS boto3 library.

    :param request: an aiohttp Request object (required).
    :return: a list of AWSAccount objects, or the empty list of the current user has no accounts.
    """
    db = request.app[HEA_DB]
    return [a for a in await gather(
        *[db.get_account(request, v.id) async for v in db.get_volumes(request, AWSFileSystem)])]


async def _post_account(request: Request) -> Response:
    """
    Called this create since the put, get, and post account all handle information about accounts, while create and delete handle creating/deleting new accounts

    account_email (str)     : REQUIRED: The email address of the owner to assign to the new member account. This email address must not already be associated with another AWS account.
    account_name (str)      : REQUIRED: The friendly name of the member account.
    account_role (str)      : If you don't specify this parameter, the role name defaults to OrganizationAccountAccessRole
    access_to_billing (str) : If you don't specify this parameter, the value defaults to ALLOW

    source: https://github.com/aws-samples/account-factory/blob/master/AccountCreationLambda.py

    Note: Creates an AWS account that is automatically a member of the organization whose credentials made the request.
    This is an asynchronous request that AWS performs in the background. Because CreateAccount operates asynchronously,
    it can return a successful completion message even though account initialization might still be in progress.
    You might need to wait a few minutes before you can successfully access the account
    The user who calls the API to create an account must have the organizations:CreateAccount permission

    When you create an account in an organization using the AWS Organizations console, API, or CLI commands, the information required for the account to operate as a standalone account,
    such as a payment method and signing the end user license agreement (EULA) is not automatically collected. If you must remove an account from your organization later,
    you can do so only after you provide the missing information.
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/organizations.html#Organizations.Client.create_account

    You can only close an account from the Billing and Cost Management Console, and you must be signed in as the root user.
    """
    try:
        volume_id = request.match_info.get("volume_id", None)
        account_email = request.match_info.get("account_email", None)
        account_name = request.match_info.get("account_name", None)
        account_role = request.match_info.get("account_role", None)
        access_to_billing = request.match_info.get("access_to_billing", None)
        if not volume_id:
            return web.HTTPBadRequest(body="volume_id is required")
        async with aws.OrganizationsClientContext(request, volume_id) as org_client:
            org_client.create_account(Email=account_email, AccountName=account_name, RoleName=account_role,
                                    IamUserAccessToBilling=access_to_billing)
            return web.HTTPAccepted()
            # time.sleep(60)        # this is here as it  takes some time to create account, and the status would always be incorrect if it went immediately to next lines of code
            # account_status = org_client.describe_create_account_status(CreateAccountRequestId=create_account_response['CreateAccountStatus']['Id'])
            # if account_status['CreateAccountStatus']['State'] == 'FAILED':    # go to boto3 link above to see response syntax
            #     web.HTTPBadRequest()      # the response syntax contains reasons for failure, see boto3 link above to see possible reasons
            # else:
            #     return web.HTTPCreated()  # it may not actually be created, but it likely isn't a failure which means it will be created after a minute or two more, see boto3 docs
    except BotoClientError as e:
        return web.HTTPBadRequest()  # see boto3 link above to see possible  exceptions
