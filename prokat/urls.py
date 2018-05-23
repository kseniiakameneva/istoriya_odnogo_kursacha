from django.conf.urls import url
from prokat.views import base_view, type_l

urlpatterns = [
    # url(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
    # url(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    url(r'^category/(?P<pk>\d+)/$', type_l, name='category'),

    url(r'^$', base_view, name='base'),
]
 