from django.urls import path, include
from django.contrib import admin
from .views import index, data, ChartData

urlpatterns = [
    path('', index, name='index'),
    path('data/', data, name='data'),
    path('api/chart/data/', ChartData.as_view()),
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),  # admin site
    ]