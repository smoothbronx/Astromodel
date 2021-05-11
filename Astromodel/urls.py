from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('common.urls', 'common'), namespace='common')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
]
