#!/usr/bin/python3

"""
    Lab02 Example
"""


import json
from compute_api_json import *


with open("auth_sample", "r") as sample:
    auth_response = json.load(sample)

compute_api_info = {"flavor_id":     None,
                    "image_id":      None}

update_cache(auth_response, type="auth_api_info")
update_cache(compute_api_info, type="compute_api_info")

print("Token: {}".format(get_token_id(auth_response)))
print("Tenant: {}".format(get_tenant_id(auth_response)))
print("Compute URLs: {}".format(get_compute_public_URL(auth_response)))
print("Image ID: {}".format(get_image_id()))
print("Flavor ID: {}".format(get_flavor()))
