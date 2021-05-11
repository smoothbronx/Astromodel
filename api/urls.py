from django.urls import path
from api.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('kuramoto/data/trade/<str:token>', TradeView.as_view(), name='trade'),
    path('test/<str:token>', TradeView.as_view(), name='test')
]