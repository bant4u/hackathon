from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
    
    url(r'', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rainfall/$','ews.views.rainfall_watch', name='clientform'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^googlemap/', 'ews.views.google_map'),
)
