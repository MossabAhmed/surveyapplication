from django.urls import include, path
from . import views

app_name = "mysurvey" 

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.MySurvey, name='Dashboard'),

    # the views need to be Change 
    path('CreateSurvey', views.MySurvey, name='CreateSurvey'),
    path('responses', views.MySurvey, name='Responses'),

]

url_for_htmx = [
    
]

urlpatterns += url_for_htmx 