#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import local
from datetime import datetime


def do_pack():
    """packages all contents from web_static into .tgz archive
    """
    local('mkdir -p versions')
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    result = local('tar -czvf versions/web_static_{}.tgz web_static'
                   .format(date))

    if result.failed:
        return None
    else:
        return result
