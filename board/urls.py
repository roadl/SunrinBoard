#blog\urls.py
from django.conf.urls import include, url
from . import views

#from django.contrib import admin

urlpatterns = [
    url(r'^$', views.free_board, name='free_board'),
    #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name = 'post_new'),
    url(r'^join/$', views.signup, name='join'),
]





