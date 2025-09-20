from django.urls import include, path
from . import views


urlpatterns = [
]

url_for_htmx = [
    path('CreateSubFile', views.CreateFile, name='CreateSubFile'),
]

urlpatterns += url_for_htmx 