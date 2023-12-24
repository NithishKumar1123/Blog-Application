from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('new_blog/', views.new_blog, name = "new blog"),
    path('profile/', views.view_profile, name = "profile"),
    path('edit_blog/<int:blog_id>', views.edit_blog, name = "edit blog"),
    path('delete_blog/<int:blog_id>', views.delete_blog, name = "delete blog")
]