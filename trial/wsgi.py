"""
WSGI config for trial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from trial.settings import MEDIA_ROOT

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trial.settings")

application = get_wsgi_application()
# application = WhiteNoise(application, root='/path/to/static/files')
application = WhiteNoise(application, root=MEDIA_ROOT)
application.add_files(MEDIA_ROOT, prefix='more-files/')
