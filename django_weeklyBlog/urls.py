
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views #model based view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),   #creates backend logic but not template for frontend
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
