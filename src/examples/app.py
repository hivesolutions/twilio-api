#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Twilio API
# Copyright (c) 2008-2015 Hive Solutions Lda.
#
# This file is part of Hive Twilio API.
#
# Hive Twilio API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Twilio API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Twilio API. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import appier

from . import base

class TwilioApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(self, name = "twilio")

    @appier.route("/", "GET")
    def index(self):
        return self.usage()

    @appier.route("/usage", "GET")
    def usage(self):
        api = self.get_api()
        usage = api.usage_account()
        return usage

    @appier.route("/message", "GET")
    def message(self):
        sender = self.field("sender")
        receiver = self.field("receiver")
        body = self.field("body")
        api = self.get_api()
        result = api.send_message(sender, receiver, body)
        return result

    def get_api(self):
        return base.get_api()

if __name__ == "__main__":
    app = TwilioApp()
    app.serve()
