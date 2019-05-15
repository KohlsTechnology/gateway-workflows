# Copyright 2019 BlueCat Networks (USA) Inc. and its affiliates
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
# Date: 2018-12-12
# Gateway Version: 18.12.1
# Description: Example Cisco ACI Workflows


# pylint: disable=redefined-builtin,missing-docstring
type = 'ui'
sub_pages = [
    {
        'name'        : 'cisco_aci_example_page',
        'title'       : u'Cisco ACI',
        'endpoint'    : 'cisco_aci_example/cisco_aci_example_endpoint',
        'description' : u'cisco_aci_example'
    },
]
