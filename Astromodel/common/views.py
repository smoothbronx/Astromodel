from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = ''
    model = ''

    def get(self, request):
        return HttpResponse('Hello from start page')
