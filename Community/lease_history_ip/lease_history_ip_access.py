# Copyright 2020 BlueCat Networks (USA) Inc. and its affiliates
# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# By: BlueCat Networks
# Date: 2019-03-14
# Gateway Version: 18.10.2
# Description: Lease History IP Access

# Various Flask framework items.
import os
import sys
import codecs

import psycopg2

from flask import g, jsonify, request
from urllib.parse import urlparse

from main_app import app
from bluecat import route

from bluecat import util
import config.default_config as config

from bluecat.util import rest_exception_catcher
from bluecat.util import rest_workflow_permission_required
from bluecat.server_endpoints import empty_decorator
from bluecat.server_endpoints import get_result_template

def module_path():
    return os.path.dirname(os.path.abspath(str(__file__)))

def get_resource_text():
    return util.get_text(module_path(), config.language)

def get_configuration(api, config_name):
    configuration = api.get_configuration(config_name)
    return configuration


def raw_table_data(*args, **kwargs):
    """Returns table formatted data for display in the TableField component"""
    # pylint: disable=unused-argument

    text = get_resource_text()
    return {
        "columns": [
            {"title": text['title_mac_address']},
            {"title": text['title_lease_time']},
            {"title": text['title_expiry_time']},
            {"title": text['title_update_count']},
        ],
        "columnDefs": [
            {"className": "dt-body-right", "targets": [3]}
        ],
        "data": []
    }


def load_lease_history(config_id, ip_address):
    """
    Load Lease_Summary_TABLE as json format.
    :param ip_address: IP Address for query.
    :return: result
    """

    db_address = os.environ['BAM_IP']
    connector = psycopg2.connect(host=db_address, database="proteusdb", user="bcreadonly")
    cursor = connector.cursor()

    sql = \
    "select " \
    "long2mac(mac_address), " \
    "to_char(lease_time, 'YYYY/MM/DD HH24:MI:SS'), " \
    "to_char(expire_time, 'YYYY/MM/DD HH24:MI:SS'), " \
    "update_count " \
    "from " \
    "public.lease_summary " \
    "where " \
    "conf_id = %d and long2ip4(ip_address) = '%s'" \
    "order by expire_time desc" % (config_id, ip_address)

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    connector.close()

    text = get_resource_text()
    data = {
        "columns": [
            {"title": text['title_mac_address']},
            {"title": text['title_lease_time']},
            {"title": text['title_expiry_time']},
            {"title": text['title_update_count']},
        ],
        "columnDefs": [
            {"className": "dt-body-right", "targets": [3]}
        ],
        "data": []
    }

    for row in result:
        data['data'].append([row[0].upper(), row[1], row[2], row[3]])

    return data


def query_history_by_ip_endpoint(workflow_name, element_id, permissions, result_decorator=None):
    """Endpoint for retrieving the selected objects"""
    # pylint: disable=unused-argument
    endpoint = 'query_history_by_ip'
    function_endpoint = '%squery_history_by_ip' % workflow_name
    view_function = app.view_functions.get(function_endpoint)
    if view_function is not None:
        return endpoint
    if not result_decorator:
        result_decorator = empty_decorator

    g.user.logger.info('Creating endpoint %s', endpoint)

    @route(app, '/%s/%s' % (workflow_name, endpoint), methods=['POST'])
    @rest_workflow_permission_required(permissions)
    @rest_exception_catcher
    # pylint: disable=unused-variable
    def query_history_by_ip():
        """Retrieve a list of properties for the table"""
        # pylint: disable=broad-except
        try:
            configuration = get_configuration(g.user.get_api(), config.default_configuration)
            ip_address = request.form['ip_address']

            data = load_lease_history(configuration.get_id(), ip_address)

            # If no entities were found reutrn with failure state and message
            result = get_result_template()
            result['status'] = 'SUCCESS'
            result['data'] = {"table_field": data}
            return jsonify(result_decorator(result))

        except Exception as e:
            result = get_result_template()
            result['status'] = 'FAIL'
            result['message'] = str(e)
            return jsonify(result_decorator(result))

    return endpoint
