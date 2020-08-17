#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to my web servers, using the function do_deploy.
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo

"""my server's ip addresses"""
env.hosts = ['35.243.144.124', '3.91.55.208']
env.user = "ubuntu"

def do_deploy(archive_path):
    """do_deploy function."""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + file_name.split(".")[0])

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(file_name, new_folder))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True

    except:
        return False
