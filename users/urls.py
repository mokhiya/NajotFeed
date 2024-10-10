from django.urls import path
from . import views
from .views import verify_email

app_name = 'users'


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('verify-email/<uidb64>/<token>', verify_email, name='verify_email'),
]
