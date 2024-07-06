import asyncio
from django.conf import settings
from django.core.management import BaseCommand

from bot.client import client


class Command(BaseCommand):
    help = 'Run discord bot.'

    def handle(self, *args, **options):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(client.run(settings.DISCORD_BOT_TOKEN))
