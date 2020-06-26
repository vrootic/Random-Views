import json
import logging

from django.views.generic import TemplateView

import requests

logger = logging.getLogger(__name__)

class CurrencyView(TemplateView):
    template_name = "currency.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.warning('in get_context_data')
        try:
            r = requests.get('https://tw.rter.info/capi.php')
            result = {
                'USDJPY': r.json()['USDJPY'], 
                'USDTWD': r.json()['USDTWD']
            }
        except requests.HttpError as e:
            logger.exception(e)
            logger.debug("Could not get additional data", exc_info=True)
            return None

        context['result'] = json.dumps(result)
        return context

