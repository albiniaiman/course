from django.conf.urls import url
from . import views

app_name = "cart"
urlpatterns = [
    url(r'^remove/(?P<book_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<book_id>\d+)/$', views.CartAdd, name='CartAdd'),
    url(r'^$', views.CartDetail, name='CartDetail'),
]
