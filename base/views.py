from datetime import datetime
from urllib import request

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('main.html')
    now = datetime.now()
    context = {
        'currnet_date': now
    }
    return HttpResponse(template.render(context, request) )