# pylint: skip-file
import asyncio
import os

import ioc
import unimatrix.runtime
import unimatrix.ext.secrets as secrets


if __name__ == '__main__':
    unimatrix.runtime.on.sync('boot')
    secrets.setup({
        'default': {
            'class': 'unimatrix.ext.secrets.loaders.google.GoogleSecretLoader',
            'prefetch': False,
            'options': {
                'project': os.getenv('GOOGLE_TEST_PROJECT')
            }
        }
    })

    repo = ioc.require('SecretRepository')
    print(repo.get_sync('default-signing-key'))

    # This does not trigger a lookup.
    print(repo.get_sync('default-signing-key'))
