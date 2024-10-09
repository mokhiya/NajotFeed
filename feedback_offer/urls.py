from django.urls import path
from . import views

app_name = 'feedback_offer'
urlpatterns = [
    path('problems/', views.problems_page_view, name='problems'),
    path('comments/', views.comments_page_view, name='comments'),
    path('offers/', views.offers_page_view, name='offers'),
    path('', views.home_page_view, name='index'),
]