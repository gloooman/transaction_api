from django.contrib import admin
from django.urls import path, include

from transactions import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers))
]
