from logging import CRITICAL

from django.http import HttpResponseServerError
from django.shortcuts import render

from loggers import apps_home_logger


# Create your views here.


def index(request):
    # Page from the theme
    return render(request, "pages/index.html")


def test_logs(request):

    try:
        a = 1 / 0
        return render(request, "pages/index.html")
    except ZeroDivisionError as e:
        apps_home_logger.log(CRITICAL, msg=e)

        return HttpResponseServerError(
            "<h1>Server Error (500)</h1>", content_type="text/html"
        )
