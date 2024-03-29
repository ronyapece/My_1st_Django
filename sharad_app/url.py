from django.urls import path
from sharad_app import views

urlpatterns = [
    path('', views.show_detail, name='detail'),
    path('contact', views.contact, name= 'contact'),
    path('about', views.about, name= 'about'),
    path('todo', views.show_query, name='todo'),
    path('delete/<task_id>', views.delete_entry, name='delete'),
    path('edit/<task_id>', views.edit_entry, name='edit'),
    path('done/<task_id>', views.done_field, name='done'),   
]
