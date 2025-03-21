
from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
from .import views
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book
urlpatterns = [
        path("books/",list_books, name ="list_books"),
        path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
        path('register/', views.register, name='register'),
        path('login/', LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
        path('admin-dashboard/', admin_view, name='admin-dashboard'),
        path('librarian-dashboard/', librarian_view, name='librarian-dashboard'),
        path('member-dashboard/', member_view, name='member-dashboard'),
        path('books/add/', add_book, name='add-book'),
        path('books/edit/<int:book_id>/', edit_book, name='edit-book'),
        path('books/delete/<int:book_id>/', delete_book, name='delete-book'),
        ]
