# pylint: skip-file
import ioc
from unimatrix.conf import settings
from unimatrix.lib import meta

from .conf import setup as setup_secret_loaders
from .provider import SecretLoaderProvider
from .repository import SecretRepository


def setup_ioc(*args, **kwargs):
    if not ioc.is_satisfied('SecretLoaderProvider'):
        ioc.provide('SecretLoaderProvider', SecretLoaderProvider())
    if not ioc.is_satisfied('SecretRepository'):
        ioc.provide('SecretRepository', SecretRepository())


@ioc.inject('repo', 'SecretRepository')
@ioc.inject('provider', 'SecretLoaderProvider')
async def on_setup(repo, provider, settings=settings):
    if hasattr(settings, 'SECRET_STORAGE_BACKENDS'):
        setup_secret_loaders(settings.SECRET_STORAGE_BACKENDS)


@ioc.inject('repo', 'SecretRepository')
async def boot(repo):
    await repo.prefetch()
