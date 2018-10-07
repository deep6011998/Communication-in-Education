from django.conf.urls import url,include
from .import views

urlpatterns = [
    url(r'^index',views.index,name='index'),
    url(r'^show_student_register',views.show_student_register,name='show_student_register'),
    url(r'^show_parent_register',views.show_parent_register,name='show_parent_register'),
    url(r'^show_teacher_register',views.show_teacher_register,name='show_teacher_register'),
    url(r'^show_student_login',views.show_student_login,name='show_student_login'),
    url(r'^show_parent_login',views.show_parent_login,name='show_parent_login'),
    url(r'^show_teacher_login',views.show_teacher_login,name='show_teacher_login'),
    url(r'^student_register',views.student_register,name='student_register'),
    url(r'^parent_register',views.parent_register,name='parent_register'),
    url(r'^teacher_register',views.teacher_register,name='teacher_register'),
    url(r'^student_login', views.student_login, name='student_login'),
    url(r'^parent_login', views.parent_login, name='parent_login'),
    url(r'^teacher_login', views.teacher_login, name='teacher_login')


]