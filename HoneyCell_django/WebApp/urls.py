__author__ = 'jianheluo'

from django.conf.urls import include, url
from . import views


urlpatterns = [

    # empty url
    url(r'^$', 'WebApp.views.index', name='index'),

    # new argument 'template_name'
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'WebApp/login.html'}, name='login'),

    # url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'WebApp.views.my_logout', name='logout'),

    # registration is normal route
    url(r'^registration/$', 'WebApp.views.registration', name='registration'),

    # after login, show the message page to the user
    url(r'^message/$', 'WebApp.views.message', name='message'),

    # go to upload page
    url(r'^upload/$', 'WebApp.views.upload', name='upload'),

    # go to preprocess page
    url(r'preprocess/$', 'WebApp.views.preprocess', name='preprocess'),

    # go to visualization page
    url(r'visualization/$', 'WebApp.views.visualization', name='visualization'),

    # go to honeycell page
    url(r'honeycell/$', 'WebApp.views.honeycell', name='honeycell'),

    # go to honeycomb page
    url(r'honeycomb/$', 'WebApp.views.honeycomb', name='honeycomb'),

    # go to analytics page
    url(r'analytics/$', 'WebApp.views.analytics', name='analytics'),

    url(r'^show_articles/$', 'WebApp.views.show_articles', name='show_articles'),

    url(r'^add_article/$', 'WebApp.views.add_article', name='add_article'),

    url(r'^article_detail/(?P<article_id>\d+)$', 'WebApp.views.article_detail', name='article_detail'),

    url(r'^like_article/(?P<article_id>\d+)$', 'WebApp.views.like_article', name='like_article'),

    url(r'^search_articles', 'WebApp.views.search_articles', name='search_articles'),

    url(r'^haystack_saerch/$', include('haystack.urls')),


]