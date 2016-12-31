Provisioning a new site 
========================

# Required packages:

* nginx
* Python 3
* Git 
* pip
* virtualenv

To install on Ubuntu:
    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv


## Nginx Virtual Host Config

* see nginx.template.conf
* replace SITENAME with the name of the site you are deploying

## Upstart Job (Gunicorn)

* see gunicorn-upstart.template.conf
* replace SITENAME with the name of the site you are deploying

## Folder Structure
A user account, such as /home/zaid, is needed.

/home/zaid
└── sites        └── SITENAME             ├── database             ├── source             ├── static             └── virtualenv


## Other notes
* Caching on your local browser can stop the site from displaying correctly.
* Check for errors in your nginx configuration by running `sudo nginx t`.
* The virtualenv does not have to be activated, the executables within can be run from virtual/bin.


## Creating a user and SSH
* It's safest to disable password access and use ssh keys for logging in.

