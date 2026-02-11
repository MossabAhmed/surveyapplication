"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib.sites.models import Site
from django.http import HttpResponse

def create_site_emergency(request):
    # إنشاء الموقع رقم 1 يدوياً
    site, created = Site.objects.get_or_create(
        id=1, 
        defaults={'domain': 'askio-survey.onrender.com', 'name': 'Askio'}
    )
    if not created:
        site.domain = 'askio-survey.onrender.com'
        site.save()
    return HttpResponse(f"Site created/updated with ID: {site.id}")

urlpatterns = [
    path('emergency-site-fix/', create_site_emergency),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('survey.urls')),
] + debug_toolbar_urls()
