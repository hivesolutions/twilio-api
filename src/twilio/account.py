#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Twilio API
# Copyright (c) 2008-2024 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """


class AccountAPI(object):

    def usage_account(self, period="LastMonth"):
        url = self.account_url + "Usage/Records/%s.json" % period
        contents = self.get(url)
        return contents
