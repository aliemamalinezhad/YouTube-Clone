from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('<int:video_id>', views.get_video, name='video'),
    path('admin_panel', views.admin_panel, name='admin_panel')

]