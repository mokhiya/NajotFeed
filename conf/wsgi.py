

import os
import sys

from django.core.wsgi import get_wsgi_application
sys.path.append('/var/www/NajotFeed')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

application = get_wsgi_application()
