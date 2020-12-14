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
# Description: Lease History IP Page

# Various Flask framework items.
import os
import sys
import codecs

from flask import url_for, redirect, render_template, flash, g

from bluecat import route, util
from main_app import app

from .lease_history_ip_access import get_resource_text
from .lease_history_ip_form import GenericFormTemplate

# The workflow name must be the first part of any endpoints defined in this file.
# If you break this rule, you will trip up on other people's endpoint names and
# chaos will ensue.
@route(app, '/lease_history_ip/lease_history_ip_endpoint')
@util.workflow_permission_required('lease_history_ip_page')
@util.exception_catcher
def lease_history_ip_lease_history_ip_page():
    form = GenericFormTemplate()
    return render_template(
        'lease_history_ip_page.html',
        form=form,
        text=get_resource_text(),
        options=g.user.get_options(),
    )

@route(app, '/lease_history_ip/form', methods=['POST'])
@util.workflow_permission_required('lease_history_ip_page')
@util.exception_catcher
def lease_history_ip_lease_history_ip_page_form():
    form = GenericFormTemplate()
    if form.validate_on_submit():
        # Put form processing code here
        g.user.logger.info('SUCCESS')
        flash('success', 'succeed')
        return redirect(url_for('lease_history_iplease_history_ip_lease_history_ip_page'))
    else:
        g.user.logger.info('Form data was not valid.')
        return render_template(
            'lease_history_ip_page.html',
            form=form,
            text=get_resource_text(),
            options=g.user.get_options(),
        )
