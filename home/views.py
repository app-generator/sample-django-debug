from logging import CRITICAL

from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from django.shortcuts import render

from loggers import apps_home_logger

import pdb


def index(request):
    # Page from the theme
    return render(request, "pages/index.html")


def test_logs(request):
    users = User.objects.all()

    pdb.set_trace()

    try:
        a = 1 / 0
        return render(request, "pages/index.html")
    except ZeroDivisionError as e:
        apps_home_logger.log(CRITICAL, msg=str(e))

        return render(request, "pages/examples/500.html")
