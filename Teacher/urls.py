from django.conf.urls import url,include
from .import views

urlpatterns = [
    url(r'^study_material', views.study_material, name='study_material'),
    url(r'^study_material_input', views.study_material_input, name='study_material_input'),

]