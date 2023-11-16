import dataclasses
from datetime import datetime
from unittest import mock
from unittest.mock import patch

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from django_zupit_logging.logging import ZupitLoggingMiddleware
from django_zupit_logging.settings import lib_settings


@dataclasses.dataclass
class MockResponse:
    status_code: int


class ZupitLoggingMiddlewareTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )
        self.anon_user = AnonymousUser()

    @patch("logging.Logger.info")
    def test_log_userful_request_info(self, info_logger_mock):
        request = self.factory.get("/")
        request.user = self.user
        time = datetime(1901, 12, 21)

        response = MockResponse(status_code=200)

        middleware = ZupitLoggingMiddleware(
            get_response=mock.MagicMock(return_value=response)
        )

        with patch(
            "django_zupit_logging.logging.datetime", wraps=datetime
        ) as mock_datetime:
            mock_datetime.utcnow.return_value = time
            middleware(request)
        info_logger_mock.assert_called_once_with(
            msg={
                "date_time": str(time),
                "remote_address": "127.0.0.1",
                "request_method": request.method,
                "request_path": request.path,
                "user_id": self.user.id,
                "request_id": "",
                "app_version": lib_settings.APP_VERSION,
                "params": "{}",
                "status_code": response.status_code,
            }
        )

    @patch("logging.Logger.info")
    def test_log_logged_user_request(self, info_logger_mock):
        request = self.factory.get("/")
        request.user = self.user

        middleware = ZupitLoggingMiddleware(
            get_response=mock.MagicMock(return_value=MockResponse(status_code=200))
        )
        middleware(request)

        _, kwargs = info_logger_mock.call_args
        msg = kwargs.get("msg")
        user_id = msg.get("user_id")

        info_logger_mock.assert_called_once()
        self.assertEquals(user_id, self.user.id)

    @patch("logging.Logger.info")
    def test_log_anonymous_user_request(self, info_logger_mock):
        request = self.factory.get("/")
        request.user = self.anon_user

        middleware = ZupitLoggingMiddleware(
            get_response=mock.MagicMock(return_value=MockResponse(status_code=200))
        )
        middleware(request)

        _, kwargs = info_logger_mock.call_args
        msg = kwargs.get("msg")
        user_id = msg.get("user_id")

        info_logger_mock.assert_called_once()
        self.assertEquals(user_id, "")

    @patch("logging.Logger.info")
    @patch("logging.Logger.debug")
    def test_log_successfull_request(self, info_logger_mock, debug_logger_mock):
        request = self.factory.get("/")
        request.user = self.user

        middleware = ZupitLoggingMiddleware(
            get_response=mock.MagicMock(return_value=MockResponse(status_code=200))
        )
        middleware(request)

        info_logger_mock.assert_called_once()
        debug_logger_mock.assert_called_once()

    @patch("logging.Logger.info")
    @patch("logging.Logger.warning")
    def test_log_client_error_request(self, info_logger_mock, warning_logger_mock):
        request = self.factory.get("/")
        request.user = self.user

        middleware = ZupitLoggingMiddleware(
            get_response=mock.MagicMock(return_value=MockResponse(status_code=400))
        )
        middleware(request)

        info_logger_mock.assert_called_once()
        warning_logger_mock.assert_called_once()

    @patch("logging.Logger.info")
    @patch("logging.Logger.error")
    def test_log_server_error_request(self, info_logger_mock, error_logger_mock):
        request = self.factory.get("/")
        request.user = self.user

        middleware = ZupitLoggingMiddleware(
            get_response=mock.MagicMock(return_value=MockResponse(status_code=500))
        )
        middleware(request)

        info_logger_mock.assert_called_once()
        error_logger_mock.assert_called_once()
