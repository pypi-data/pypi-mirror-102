# pylint: skip-file
import ioc

from .conf import setup
from .provider import DEFAULT_LOADER


__all__ = ['get', 'get_sync', 'setup']

default_app_config = 'unimatrix.ext.secrets.apps.SecretStorageConfig'


@ioc.inject('repo', 'SecretRepository')
async def get(name, version=None, using=DEFAULT_LOADER, repo=None):
    assert repo is not None
    return await repo.get(name, version, using=using)


@ioc.inject('repo', 'SecretRepository')
def get_sync(name, version=None, using=DEFAULT_LOADER, repo=None):
    """Like :func:`get`, but synchronous."""
    assert repo is not None
    return repo.get_sync(name, version, using=using)
