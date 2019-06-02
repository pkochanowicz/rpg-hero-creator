"""
Settings used for the live site.

(This demo project doesn't use this file anywhere, it's just as an illustration.)
"""
import requests
from .base import *
from django.core.exceptions import ImproperlyConfigured

########## ALLOWED_HOSTS
from requests.exceptions import ConnectionError

url = "http://169.254.169.254/latest/meta-data/public-ipv4"
try:
    r = requests.get(url)
    instance_ip = r.text
    ALLOWED_HOSTS += [instance_ip]
except ConnectionError:
    error_msg = "You can only run production settings on an AWS EC2 instance"
    raise ImproperlyConfigured(error_msg)
########## END ALLOWED_HOSTS

DEBUG = False
