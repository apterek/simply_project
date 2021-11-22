import logging
import requests
from datetime import datetime
from django_rq import job
import time
import datetime
from core.models import ExchangeRate

logger = logging.getLogger(__name__)
CURRCOV_API_KEY = "37f1f0ad28d970fb8fd3"


# the task for update exchange rate
@job
def run_update_exchange_rate():
    url_usd = f"https://free.currconv.com/api/v7/convert?q=USD_BYN&compact=ultra&apiKey={CURRCOV_API_KEY}"
    url_eur = f"https://free.currconv.com/api/v7/convert?q=EUR_BYN&compact=ultra&apiKey={CURRCOV_API_KEY}"

    response_usd = requests.get(url_usd)
    time.sleep(5)
    response_eur = requests.get(url_eur)
    if response_usd.status_code != 200:
        logger.error("Something gone wrong, try again_USD")

    if response_eur.status_code != 200:
        logger.error("Something gone wrong, try again_EUR")

    exchange_rate_usd = response_usd.json().get("USD_BYN")
    exchange_rate_eur = response_eur.json().get("EUR_BYN")
    ExchangeRate.objects.create(exchange_rate_usd=exchange_rate_usd,
                                exchange_rate_eur=exchange_rate_eur,
                                created_at=datetime.datetime.now())
    logger.info(f"Exchange rate updated successfully: {datetime.datetime.now()}")
