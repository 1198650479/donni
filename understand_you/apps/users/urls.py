from django.urls import path

from apps.users import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('user_info/', views.UserInfoViews.as_view()),
    path('change_user_info/', views.ChangeUserInfoViews.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('user_collection/', views.UserCollectionViews.as_view()),
    path('cancel_collection/', views.CancelCollectionViews.as_view()),
    path('user_like/', views.UserLikeViews.as_view()),
    path('cancel_like/', views.CancelLikeViews.as_view()),
    path('user_follow/', views.UserFollowViews.as_view()),
    path('cancel_follow/', views.CancelFollowViews.as_view())
]