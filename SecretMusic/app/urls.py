from django.urls import path
from .views import Book  # Templates, Index,message

urlpatterns = [
    # path('', message),
    # path('index', Index.as_view()),
    # path('<str:book_name>', Book.as_view(), name='index'),
    path('<str:book1>', Book.as_view(),name='index1'),
    # path('a', Templates.as_view())
]
