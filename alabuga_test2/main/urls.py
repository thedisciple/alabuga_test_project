from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home_page"),
    path('hierarchy', views.hierarchy, name="hierarchy_page"),
    path('404', views.error_404, name="error_404_page"),
    path('auth', views.auth, name="log_in_page")
]
