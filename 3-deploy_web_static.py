#!/usr/bin/python3
"""
full deployment
"""
from fabric.contrib import files
from datetime import datetime
import os.path
from fabric.api import env, put, run, local
from fabric.operations import run, put, sudo


"""my server's ip addresses"""
env.hosts = ['35.243.144.124', '3.91.55.208']


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


def do_deploy(archive_path):
    """do_deploy function."""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + file_name.split(".")[0])

        put(archive_path, "/tmp")
        run("mkdir -p {}".format(new_folder))
        run("tar -xzf /tmp/{} -C {}".
            format(file_name, new_folder))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("rm -rf {}/web_static".format(new_folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(new_folder))
        return True

    except:
        return False


def deploy():
    """deploy function."""
    path = do_pack()

    if path is None:
        return False

    return do_deploy(path)
