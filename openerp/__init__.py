# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

""" OpenERP core library.

"""
# The hard-coded super-user id (a.k.a. administrator, or root user).
SUPERUSER_ID = 1

import addons
import conf
import cron
import loglevels
import modules
import netsvc
import osv
import pooler
import pychart
import release
import report
import run_tests
import service
import sql_db
import test
import tiny_socket
import tools
import wizard
import workflow
import wsgi

# Is the server running in multi-process mode (e.g. behind Gunicorn).
# If this is True, the processes have to communicate some events,
# e.g. database update or cache invalidation. Each process has also
# its own copy of the data structure and we don't need to care about
# locks between threads.
multi_process = False

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

