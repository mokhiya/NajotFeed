from django.urls import path
from . import views

app_name = 'feedback_offer'
urlpatterns = [
    path('problems/', views.problems_page_view, name='problems'),
    path('submit/', views.submit_offer_view, name='offer'),
    path('comments/', views.comments_page_view, name='comments'),
    path('offers/', views.offers_page_view, name='offers'),
    path('comment/', views.comment_page_view, name='comment'),
    path('offer/<int:offer_id>/', views.offer_detail_view, name='offer_detail'),
    path('demand/<int:demand_id>/', views.demand_detail_view, name='demand_detail'),
    path('', views.home_page_view, name='index'),
]