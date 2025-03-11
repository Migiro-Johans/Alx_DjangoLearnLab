
from django.urls import path
from .views import list_books, LibraryDetaiView, user_login, user_logout
rom django.contrib.auth.views import LoginView, LogoutView
from .views import register
urlpatterns = [
        path("books/",list_books, name ="list_books"),
        path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
        path('register/', register, name='register'),
        path('login/', user_login, name='login'),
        path('logout/', user_logout, name='logout'),
        ]
