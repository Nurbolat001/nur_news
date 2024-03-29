from django.urls import path
from . import views
from .views import login_view, register_view, logout_view


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/all', views.all_news_page, name='all_news_page'),
    path('news/card/<int:pk>/', views.news_card, name='news_card_page'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register')

]


