from django.urls import path

from apps.users import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('user_info/', views.UserInfoViews.as_view())
]