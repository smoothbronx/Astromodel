from django.urls import path
from common.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]