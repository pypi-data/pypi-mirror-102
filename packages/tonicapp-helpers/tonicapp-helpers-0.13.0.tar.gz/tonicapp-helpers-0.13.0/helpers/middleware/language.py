import re
import requests
import logging
import json

from django.conf import settings

logger = logging.getLogger()


class LanguageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        content_string = response.content
        keys = re.findall(r'(\*\*.*?\*\*)', content_string)

        if len(keys) == 0:
            return response

        locale = request.locale

        params = {
            'language_code': locale,
            'feature': settings.LANGUAGE["feature"],
            'keys': ",".join(keys)
        }
        headers = {
            'Accept-Language': locale,
            'Authorization': f'TWT {settings.AUTHENTICATION["TONIC_WEB_TOKEN"]}'
        }
        language_response = requests.get(
            settings.LANGUAGE["url"],
            params=params,
            headers=headers
        )

        if language_response.status_code != 200:
            logger.error(f'Error getting the translations for this response, code: {language_response.status_code}, response: {str(language_response.content)}')
            return response

        json_response = json.loads(
            str(language_response.content)
            .replace('b', '')
            .replace('\'', '')
        )
        if json_response['count'] == 0:
            logger.warning(f'No keys were found in language service with this params: {params}.')
            return response

        for result in json_response['results']:
            response.content = response.content.replace(result['key'], result['value'])
        return response
