from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("book_detail/<int:pk>", views.BookDetailView.as_view(), name="book_detail"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("book_form/", views.BookFormView.as_view(), name="book_form")
]
