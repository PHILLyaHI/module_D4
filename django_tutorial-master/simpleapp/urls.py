from django.urls import path
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:pk>', ArticleDetail.as_view()),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]