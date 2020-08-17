#!/usr/bin/env bash
# Script for Nginx Installation.
# ------------------------------
# author: Ronnie B.M.
# github: ronniebm
# ------------------------------

# 1. install nginx if not exist.

if ! which nginx >/dev/null;
then
    Update & Install Nginx.
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# ------------------------------
# 2. creating folders.

mkdir -p /data/web_static/releases/test;
mkdir -p /data/web_static/shared;

# ------------------------------
# creating fake html website.

echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

# ------------------------------
# 3. re-creating soft links.

rm -f /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# ------------------------------
# 4. give ownership of '/data' folder to ubuntu user.

sudo chown -fR ubuntu:ubuntu "/data/"

# ------------------------------
# 5. Update Nginx config. to serve content of
#    /data/web_static/current/ to hbnb_static.

TEXT="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "/server_name localhost;/a $TEXT" /etc/nginx/sites-available/default

# ------------------------------
# 6. Restart Nginx service.

sudo service nginx restart
