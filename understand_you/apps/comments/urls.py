from django.urls import path

from apps.comments import views

urlpatterns = [
    path('write_comment/', views.WriteCommentViews.as_view()),
]