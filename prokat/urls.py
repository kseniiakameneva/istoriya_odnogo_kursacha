from django.conf.urls import url
from prokat.views import base_view, prod_list, rules_view, prod_detail,booking_view

urlpatterns = [
    # url(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
    # url(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    url(r'^$', base_view, name='base'),
    url(r'^category/(?P<pk>\d+)/$', prod_list, name='category'),

    url(r'^rules/', rules_view, name='rules'),
    url(r'^booking/', booking_view, name='booking'),
    url(r'^prod_detail/(?P<pk>\d+)/$', prod_detail, name='prod_detail'),

]
