
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index,name = 'index'),
    path('post/<str:pk>',views.post,name='post'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('writingposts',views.writingposts,name='writingposts'),
    path('user_profile',views.user_profile,name = 'user_profile'),
    path('edit_profile',views.edit_profile,name = 'edit_profile'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)