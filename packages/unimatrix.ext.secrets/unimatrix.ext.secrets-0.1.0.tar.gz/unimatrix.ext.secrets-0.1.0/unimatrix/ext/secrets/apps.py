# pylint: skip-file
import asyncio

from django.apps import AppConfig
from django.conf import settings

from . import __boot__ as boot


class SecretStorageConfig(AppConfig):
    name = 'secrets'
    verbose_name = "Secret Storage"

    def ready(self):
        boot.setup_ioc()
        asyncio.run(self.on_ready())

    async def on_ready(self):
        await boot.on_setup(settings=settings)
        await boot.boot()
