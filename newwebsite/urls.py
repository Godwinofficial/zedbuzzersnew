from django import urls
from django.urls import path
from newwebsite.views import (
  home_list_view,
  post_detail_view,
  category_list_view,
  search_list_view,
  about_us_list_view,
  privacy_policy_list_view,
  terms_and_conditions_list_view,
)


urlpatterns = [
  path('', home_list_view, name='home'),
  path('post/<slug:slug>/', post_detail_view, name='post-details'), 
  path('category/<slug:slug>/', category_list_view, name='category'),
  path('about_us/', about_us_list_view, name='about'),
  path('privacy_policy/', privacy_policy_list_view, name='privacy_policy'),
  path('terms_and_conditions/', terms_and_conditions_list_view, name='Ts&Cs'),
  path('search/', search_list_view, name='search'),
  
]