site = 'site_name'

##
# Assumes project is inside virtual env
#
command = '/opt/{0}/bin/gunicorn'.format(site)
pythonpath = '/opt/{0}/{0}'.format(site)
bind = '127.0.0.1:8001'

preload_app = True
workers = 3

