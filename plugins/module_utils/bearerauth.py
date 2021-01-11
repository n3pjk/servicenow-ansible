# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)

import requests


class BearerAuth(requests.auth.AuthBase):
    """A :class:`requests.auth` bearer token authentication method per https://2.python-requests.org/en/master/user/authentication/#new-forms-of-authentication

    :param token: Bearer token to use instead of user/pass or session
    """

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
