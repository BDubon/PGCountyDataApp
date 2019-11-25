from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),  # admin site
    ]