from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('projects/', include('softdesk.urls')),
]

