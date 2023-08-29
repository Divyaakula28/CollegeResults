from django.urls import path
from semisters import views


urlpatterns = [
    path('Home/', views.home,name='Home'),
    path('sample1/', views.sample1,name='sample1'),
    path('sample2/', views.sample2,name='sample2'),
    path('bnchpass/', views.bnchpass,name='bnchpass'),
    path('complete_det/', views.complete_det,name='complete_det'),
    path('subpass/', views.subpass,name='subpass'),
    path('Individual_info/', views.Individual_info,name='Individual_info'),
]
