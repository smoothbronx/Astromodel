from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from api.utils import validate
from json import loads


class IndexView(View):
    template_name = ''

    def get(self, request):
        return HttpResponse('Welcome to api home page')


class TradeView(View):
    template_name = ''

    @validate
    def get(self, request, **kwargs):
        return HttpResponse('Accepted')


@method_decorator(require_POST, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class ApiTestView(View):
    template_name = None

    @validate
    def post(self, request, **kwargs):
        return JsonResponse(loads(request.body))




