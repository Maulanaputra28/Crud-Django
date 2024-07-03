from django.urls import path
from .views import index, login, tambah_user, post_user, update_user, postupdate_user, delete_user ,admin

urlpatterns = [
    path('index', index, name='index'),
    path('login', login, name='login'),
    path('admin', admin, name='admin'),
    path('tambah_user', tambah_user, name='tambahuser'),
    path('post_user', post_user, name="postuser"),
    path('update_user/<str:id>', update_user, name="updateuser"),
    path('postupdate_user/<str:id>', postupdate_user, name="postupdateuser"),
    path('delete_user/<str:id>', delete_user, name="deleteuser")
]