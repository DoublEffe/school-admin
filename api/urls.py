from django.urls import path

from . import views

urlpatterns = [
    path("csrf", views.csrf_cookie, name="csrf_cookie"),
    path("login", views.auth_login, name="login"),
    path("logout", views.auth_logout, name="logout"),
    path("gclasses", views.get_classes, name="get_classes"),
    path("sclasses", views.set_classes, name="set_classes"),
    path("gusers", views.get_users, name="get_users"),
    path("susers", views.set_users, name="set_users"),
    path("newclass", views.new_class, name="new_class"),
    path("upload", views.upload, name="file"),
    path("gbooks", views.get_books, name="get_books"),
    path("download", views.download, name="download"),
    path("delete", views.delete, name="delete"),
]