from django.conf.urls import url,include
from .import views

urlpatterns = [
    url(r'^result',views.result,name='result'),
    url(r'^discussion_form',views.discussion_form,name='discussion_form'),
    url(r'^search_discussion_form',views.search_discussion_form,name='search_discussion_form'),
    url(r'^post_discussion_form',views.post_discussion_form,name='post_discussion_form'),


]