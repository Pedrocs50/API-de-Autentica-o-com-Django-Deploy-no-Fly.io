import time
import logging

logger = logging.getLogger(__name__)

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start

        method = request.method
        path = request.get_full_path()
        status = response.status_code
        user = request.user if request.user.is_authenticated else "Anonymous"

        logger.info(f"{method} {path} - {status} - {user} - {duration:.2f}s")

        return response
