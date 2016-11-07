from django.conf.urls import url
from django.views.generic import TemplateView

# import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='styleguide.html')),
    # url(r'^$', views.index, name='doc-index'),
]
