from django.core.files.base import ContentFile
from .models import Query
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render

from django.utils.decorators import method_decorator

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .utils.decorators import validate
from .utils.functions import createQuery
from common.utils.handlers import JSONHandler, KuramotoHandler

from json import dumps, loads


class IndexView(View):
    def get(self, request):
        return HttpResponse('Welcome to api home page')


@method_decorator(require_POST, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class TradeView(View):
    @validate
    def post(self, request, **kwargs):
        request = loads(request.body)
        response = KuramotoHandler(request).setHandler(JSONHandler).build()
        
        createQuery("http", request, response)
        return JsonResponse(response, json_dumps_params={'indent': 4})


@method_decorator(csrf_exempt, name='dispatch')
class ApiTestView(View):
    template_name = 'api/test.html'

    @validate
    def get(self, request, **kwargs):
        return render(request, self.template_name, context={'token': kwargs['token']})




