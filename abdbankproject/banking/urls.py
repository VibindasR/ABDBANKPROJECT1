from django.urls import path

from banking import views

app_name = 'banking'

urlpatterns=[
    path('',views.index,name='index'),
    path('base/',views.base,name='base'),
    # path('contact/',views.contact,name='contact'),

]