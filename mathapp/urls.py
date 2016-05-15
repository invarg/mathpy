from django.conf.urls import url

from mathapp.view import home_view, account_view

urlpatterns = [
    url(r'^$', home_view.index, name='index'),
    url(r'^home/$', home_view.index),
    url(r'^home/(?P<view>[a-z]+)/', home_view.index),
    url(r'^numbers/$', home_view.numbers),
    url(r'^numbers/(?P<view>[a-z]+)/', home_view.numbers),
    url(r'^client/', home_view.client),
    url(r'^client/(?P<view>[a-z]+)/', home_view.client),
    url(r'^contact/$', home_view.contact),
    url(r'^contact/(?P<view>[a-z]+)/', home_view.contact),
    url(r'^practice/$', home_view.practice),
    url(r'^practice/(?P<view>[a-z]+)/', home_view.practice),
    url(r'^account/$', account_view.account),
    url(r'^account/(?P<view>[a-z]+)/', account_view.account),
    url(r'^user_check/', account_view.user_check),
]

