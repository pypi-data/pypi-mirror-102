# pylint: skip-file
import asyncio
import os

import django
from django.conf import settings
from unimatrix.ext import secrets



settings.configure(
    INSTALLED_APPS=['unimatrix.ext.secrets'],
    SECRET_STORAGE_BACKENDS={
        'default': {
            'class': 'unimatrix.ext.secrets.loaders.google.GoogleSecretLoader',
            'prefetch': True,
            'options': {
                'project': os.getenv('GOOGLE_TEST_PROJECT')
            }
        }
    }
)


if __name__ == '__main__':
    django.setup()
    print(secrets.get_sync('default-signing-key'))
