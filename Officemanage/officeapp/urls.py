from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all_member',views.all_member,name='all_member'),
    path('add_member',views.add_member,name='add_member'),
    path('remove_member',views.remove_member,name='remove_member'),
    path('remove_member/<int:mem_id>',views.remove_member,name='remove_member'),
    path('filter_member',views.filter_member,name='filter_member'),
  

]
