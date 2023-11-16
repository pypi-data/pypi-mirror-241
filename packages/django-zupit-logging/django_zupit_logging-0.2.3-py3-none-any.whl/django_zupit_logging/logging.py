import json
import logging
from datetime import datetime

from django_zupit_logging.settings import lib_settings

logger = logging.getLogger(__name__)


def clean_sensitive_info(dictionary):
    sensitive_fields = lib_settings.SENSITIVE_FIELDS
    clean_dict = {
        k: "***" if k in sensitive_fields else v for (k, v) in dictionary.items()
    }
    return clean_dict


def parse_clean_json(myjson):
    if not myjson:
        return myjson

    try:
        return clean_sensitive_info(json.loads(myjson))
    except ValueError as ex:
        logger.error("Could not parse JSON", exc_info=ex)
        return None


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
        # Maybe it's the last, cfr. https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class ZupitLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url_is_not_blacklisted = all(
            url not in str(request.get_full_path())
            for url in lib_settings.BLACKLIST_URLS
        )

        if url_is_not_blacklisted:
            log_data = {
                "date_time": str(datetime.utcnow()),
                "remote_address": get_client_ip(request),
                "request_method": request.method,
                "request_path": request.path,
                "user_id": request.user.id if request.user and request.user.id else "",
                "request_id": request.headers.get(lib_settings.REQUEST_ID_HEADER, ""),
                "app_version": lib_settings.APP_VERSION,
                "params": json.dumps(request.GET),
            }

            logger.info(msg=log_data)

        response = self.get_response(request)

        if url_is_not_blacklisted:
            response_log_message = log_data

            response_log_message["status_code"] = response.status_code

            if 200 <= response.status_code < 400:
                logger.debug(response_log_message)
            elif 400 <= response.status_code < 500:
                logger.warning(response_log_message)
            elif response.status_code >= 500:
                logger.error(response_log_message)

        return response


def enable_zupit_logger(django_logging_config):
    if any(
        key not in django_logging_config
        for key in ("loggers", "formatters", "handlers")
    ):
        raise ValueError(
            "Could not find 'loggers', 'formatters' or 'handlers' "
            "in the given django django_logging_config conf."
        )

    if not lib_settings.APP_INSIGHTS_CONNECTION_STRING:
        raise ValueError("Error: APP_INSIGHTS_CONNECTION_STRING not set.")

    django_logging_config["formatters"]["azure"] = {
        "format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
    }

    django_logging_config["handlers"]["azure"] = {
        "formatter": "azure",
        "class": "opencensus.ext.azure.log_exporter.AzureLogHandler",
        "enable_local_storage": False,
        "connection_string": lib_settings.APP_INSIGHTS_CONNECTION_STRING
    }

    for logger_name in django_logging_config["loggers"]:
        django_logging_config["loggers"][logger_name]["handlers"].append("azure")
