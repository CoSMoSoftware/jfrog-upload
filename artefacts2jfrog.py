#!/usr/bin/env python3

import os
import re
import requests
import subprocess
import hashlib
import glob


patterns = os.environ["ARTEFACTS_PATTERNS"].split()
print(f"Looking for following patterns \n {patterns}")

def base_path(path_):
    while 1:
        path_ = os.path.split(path_)[0]
        if "*" not in path_:
            break
    return path_

def find_artefacts():
    artefacts = list()
    for pattern in patterns:
        for file_path in glob.iglob(pattern):
            artefacts += [file_path]

    return artefacts

def upload_artefacts(file_path):
    jfrog_url = os.environ["REGISTRY_URL"]
    jfrog_token = os.environ["ACCESS_TOKEN"]
    jfrog_user = os.environ["SERVICE_ACCOUNT"]

    file_name = os.path.split(file_path)[1]
    # add check of sha for downloads
    headers = {'content_type': 'application/octet-stream'}
    jfrog_url_ = os.path.join(jfrog_url, file_name)

    with open(file_path, 'rb') as f:
        r = requests.put(jfrog_url_,
                         auth=(jfrog_user,
                               jfrog_token),
                         data=f,
                         headers=headers)
    if r.status_code != 201:
        print("Something went wrong! Check response:")
        print(r.json())
        raise IOError("Download error")
    else:
        print(f"#### {file_name} download url:\n{r.json()['downloadUri']}")


if __name__ == '__main__':
    artefacts_ = find_artefacts()
    print("Found following artefacts:")
    print(artefacts_)
    for file_path in artefacts_:
        upload_artefacts(file_path)
