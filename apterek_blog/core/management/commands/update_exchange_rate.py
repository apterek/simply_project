from django.core.management.base import BaseCommand
from core.task import run_update_exchange_rate


class Command(BaseCommand):
    help = "Update exchange rate in product model"

    def handle(self, *args, **options):
        run_update_exchange_rate.delay()
