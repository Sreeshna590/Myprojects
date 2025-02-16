"""
URL configuration for restaurent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.MenuListView.as_view(), name='menu_list'),
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name='menu_detail'),
    path('menu_item/add/', views.MenuItemCreateView.as_view(), name='add_menu_item'),
    path('menu_item/<int:pk>/update_price/', views.MenuItemUpdateView.as_view(), name='update_price'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),

]
