from django.urls import path
from . import views
urlpatterns=[
    path('',views.IndexPage .as_view(),name='index'),
    path('contact/',views.contactPage.as_view(),name='contact'),

]
