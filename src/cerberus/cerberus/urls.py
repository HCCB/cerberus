from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'cerberus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),

    url(r'^docs/', include('docs.urls', namespace='docs')),

    url(r'^admin/', include(admin.site.urls)),
]
