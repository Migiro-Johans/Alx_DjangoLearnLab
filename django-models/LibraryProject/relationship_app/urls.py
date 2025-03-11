
from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
urlpatterns = [
        path("books/",list_books, name ="list_books"),
        path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
        path('register/', register, name='register'),
        path('login/', LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
        ]
