import re

from django.conf import settings

default_headers = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding',
)

default_methods = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
)


class CorsHeadersSettings(object):
    CORS_ALLOW_HEADERS = default_headers
    CORS_ALLOW_METHODS = default_methods
    CORS_ALLOW_CREDENTIALS = False
    CORS_PREFLIGHT_MAX_AGE = 86400
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = ()
    CORS_ORIGIN_REGEX_WHITELIST = ()
    CORS_EXPOSE_HEADERS = ()
    CORS_URLS_REGEX = '^.*$'
    CORS_MODEL = None
    CORS_REPLACE_HTTPS_REFERER = False

    def __init__(self, config, override=None):
        if override is None:
            override = {}
        fields = [
            field
            for field in dir(CorsHeadersSettings)
            if field.startswith('CORS_')]
        for field in fields:
            if hasattr(config, field):
                setattr(self, field, getattr(config, field))
        for field, value in override.items():
            if field in fields:
                setattr(self, field, value)


def get_active_settings(request):
    override = None
    endpoint_overrides = getattr(settings, 'CORS_ENDPOINT_OVERRIDES', [])
    for regex, overrides in endpoint_overrides:
        if re.match(regex, request.path):
            override = overrides
            break
    return CorsHeadersSettings(settings, override)
