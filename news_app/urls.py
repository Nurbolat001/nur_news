from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/all', views.all_news_page, name='all_news_page'),
    path('news/card/<int:pk>/', views.news_card, name='news_card_page'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path("user/register/", views.register_view, name="register"),
    path("delete/<int:pk>/", views.delete_news, name="delete"),
    path('add/', views.add_news, name='add_news'),
    path('update/<int:pk>/', views.update_news, name='update_news'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





