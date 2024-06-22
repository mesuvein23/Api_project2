from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/contact/', views.ContactDataListCreate.as_view(),name='api'),
    path('api/contact/<int:pk>', views.ContactDataRetrieveUpdateDestroy.as_view(),name='retrieveapi'),
    path('api/categorycreate/', views.CategoryListCreate.as_view(),name='categorycreate'),

]
