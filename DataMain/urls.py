from django.urls import path, include
from .views import index, data, ChartData

urlpatterns = [
    path('', index, name='index'),
    path('data/', data, name='data'),
    path('api/chart/data/', ChartData.as_view())
    ]