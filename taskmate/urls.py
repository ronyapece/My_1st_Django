from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('todolist_app.urll')),
    path('sharad/', include('sharad_app.url')),
    path('account/', include('user_app.url')),
]
