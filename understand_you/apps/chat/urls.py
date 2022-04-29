from django.urls import path

from apps.chat import views

urlpatterns = [
    path('contacts/', views.ContactsViews.as_view()),
]