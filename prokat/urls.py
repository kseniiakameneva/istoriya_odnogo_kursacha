from django.conf.urls import url
from prokat.views import base_view

urlpatterns = [
    url(r'^$', base_view, name='base'),
]
