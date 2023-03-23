from django.urls import path
from .views import Book, message,user_list, role_list, permission_list, role_permission_list, \
    assign_permission  # Templates, Index,message

urlpatterns = [
    path('', message),
    # path('index', Index.as_view()),
    # path('<str:book_name>', Book.as_view(), name='index'),
    path('<str:book1>', Book.as_view(), name='index1'),
    # path('a', Templates.as_view())
    path('users/', user_list, name='user_list'),
    path('roles/', role_list, name='role_list'),
    path('permissions/', permission_list, name='permission_list'),
    path('roles/<int:role_id>/', role_permission_list, name='role_permission_list'),
    path('assign_permission/', assign_permission, name='assign_permission'),

]
