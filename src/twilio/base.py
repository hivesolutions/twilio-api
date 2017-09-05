#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Twilio API
# Copyright (c) 2008-2017 Hive Solutions Lda.
#
# This file is part of Hive Twilio API.
#
# Hive Twilio API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Twilio API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Twilio API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2017 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import account
from . import message

BASE_URL = "https://api.twilio.com/2010-04-01/"
""" The default base url to be used when no other
base url value is provided to the constructor """

BASE_TEMPLATE = "https://%s:%s@api.twilio.com/2010-04-01/"
""" The default base url template support that is
going to be used in the construction of the secure
url version of the url """

class API(
    appier.API,
    account.AccountAPI,
    message.MessageAPI
):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.sid = appier.conf("TWILIO_SID", None)
        self.auth_token = appier.conf("TWILIO_AUTH_TOKEN", None)
        self.base_url = kwargs.get("base_url", BASE_URL)
        self.base_template = kwargs.get("base_template", BASE_TEMPLATE)
        self.sid = kwargs.get("sid", self.sid)
        self.auth_token = kwargs.get("auth_token", self.auth_token)
        self._build_url()

    def _build_url(self):
        if not self.sid:
            raise appier.OperationalError(message = "No account sid provided")
        if not self.auth_token:
            raise appier.OperationalError(message = "No auth token provided")
        self.secure_url = self.base_template % (self.sid, self.auth_token)
        self.account_url = self.secure_url + "Accounts/%s/" % self.sid
