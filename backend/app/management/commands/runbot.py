import asyncio
import logging

from django.core.management.base import BaseCommand
from bot.main import main

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Запускает telegram бота"
    
    def handle(self, *args, **kwargs):
        logging.info("Запуск бота...")
        asyncio.run(main()) # запуск асинхронной фун-и
