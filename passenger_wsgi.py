# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1359646/data/www/kznprog.xyz/dartblog')
sys.path.insert(1, '/var/www/u1359646/data/djangoenv/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dartblog.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()