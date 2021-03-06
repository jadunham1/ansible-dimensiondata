#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Dimension Data
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#   - Aimon Bustardo <aimon.bustardo@dimensiondata.com>
#
# Common methods to be used by versious module components
import os
import ConfigParser
from os.path import expanduser


# -------------------------
# This method will get user_id and key from environemnt or dot file.
# Environment takes priority.
#
# To set in environment:
# export DIDATA_USER='myusername'
# export DIDATA_PASSWORD='mypassword'
#
# To set in dot file place a file at ~/.dimensiondata with
# the following contents:
# [dimensiondatacloud]
# DIDATA_USER: myusername
# DIDATA_PASSWORD: mypassword
# -------------------------
def get_credentials():
    user_id = None
    key = None

    # Attempt to grab from environment
    if 'DIDATA_USER' in os.environ and 'DIDATA_PASSWORD' in os.environ:
        user_id = os.environ['DIDATA_USER']
        key = os.environ['DIDATA_PASSWORD']

    # Environment failed try dot file
    if user_id is None or key is None:
        home = expanduser('~')
        config = ConfigParser.SafeConfigParser()
        config.read("%s/.dimensiondata" % home)
        try:
            user_id = config.get("dimensiondatacloud", "DIDATA_USER")
            key = config.get("dimensiondatacloud", "DIDATA_PASSWORD")
        except:
            pass

    # Return False if either are not found
    if user_id is None or key is None:
        return False

    # Both found, return data
    return dict(user_id=user_id, key=key)
