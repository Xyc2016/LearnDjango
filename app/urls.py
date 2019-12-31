from django.urls import path, include
from . import views

app_name = 'app'
urlpatterns = [
    path('index', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    path('home', views.home, name='home'),
    path('learn_template', views.learn_template, name='learn_template'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('upload_file_success', views.upload_file_success, name='upload_file_success'),
    path('some_words/', include([
        path('history/', views.history),
        path('edit/', views.edit),
        path('discuss/', views.discuss),
        path('permissions/', views.permissions),
    ])),
    path('learn_redirect', views.learn_redirect, name='learn_redirect'),
    path('test_error', views.test_error, name='test_error'),
    path('post_comment', views.post_comment, name='post_comment'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
