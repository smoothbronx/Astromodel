from django.urls import path
from api.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('kuramoto/data/trade/', TradeView.as_view(), name='trade'),
    path('test/<str:token>', ApiTestView.as_view(), name='test'),
]