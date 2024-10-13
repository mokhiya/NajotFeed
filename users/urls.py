from django.urls import path
from . import views
from .views import verify_email
from .utils import profile_page_view

app_name = 'users'


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', profile_page_view, name='profile'),
    path('verify-email/<uidb64>/<token>', verify_email, name='verify_email'),
]
