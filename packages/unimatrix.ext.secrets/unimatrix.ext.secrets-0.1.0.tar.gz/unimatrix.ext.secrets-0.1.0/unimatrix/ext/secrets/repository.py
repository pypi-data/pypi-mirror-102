"""Declares :class:`SecretRepository`."""
import collections

import ioc

from .provider import DEFAULT_LOADER


class SecretRepository:
    """Provides an abstraction for the secret storage layer. This repository
    implementation uses a dictionary to maintain local state of secrets. It is
    populated using concrete :class:`~unimatrix.ext.secrets.loaders.BaseLoader`
    implementations.
    """
    __module__ = 'unimatrix.ext.secrets'
    SecretDoesNotExist = type('SecretDoesNotExist', (LookupError,), {})

    def __init__(self):
        self.__secrets = collections.defaultdict(dict)

    def _add_secret(self, using, name, version, payload):
        pass

    def get_sync(self, name, version=None, using=DEFAULT_LOADER):
        """Lookup a :class:`~unimatrix.ext.secrets.Secret` instance from the
        local storage backend, or try the remote storage backend identified
        by `using`.
        """
        try:
            return self.__secrets[using][name][version]
        except LookupError:
            # Get the specified loader from the provider and try to look up
            # the secret.
            self.fetch_sync(using, name, version)
            return self.get_sync(name, version, using)

    @ioc.inject('provider', 'SecretLoaderProvider')
    def fetch_sync(self, using, name, version, provider):
        """Lookup the named secrets provider and retrieve the secret from
        the storage backend.
        """
        loader = provider.get(using)
        for name, version, payload in loader.fetch_sync(name):
            self._add_from_loader(loader, name, version, payload)

    @ioc.inject('provider', 'SecretLoaderProvider')
    async def prefetch(self, provider):
        """Run all configured secret loaders and ensure that the secrets are
        locally available through the repository.
        """
        for loader in provider.prefetching():
            await self.run_loader(loader)

    async def run_loader(self, loader):
        """Invoke the :meth:`~unimatrix.ext.secrets.loader.BaseLoader.prefetch`
        method to lookup all secrets from the storage backend and populate the
        internal state of the :class:`SecretRepository`.
        """
        async for name, version, payload in loader.prefetch():
            self._add_from_loader(loader, name, version, payload)

    def _add_from_loader(self, loader, name, version, payload):
            if name not in self.__secrets[loader.name]:
                self.__secrets[loader.name][name] = collections.defaultdict(
                    lambda: payload
                )
            self.__secrets[loader.name][name][version] = payload
