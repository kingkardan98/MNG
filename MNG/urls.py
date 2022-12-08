"""MNG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from pages.views import *
from user.views import *

# View parent script is commented near its path,
# so when shit hits the fan I know where to go looking.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),                                            # pages.views
    path('contacts/', contacts_view, name='contacts'),                           # pages.views
    path('about/', about_view, name='about_view'),                               # pages.views
    path('create_user', user_create_view, name='user_create_view'),              # user.views
    path('user/<int:id>', user_detail_view, name='user_detail_view'),            # user.views
    path('user/<int:id>/delete', delete_user_view, name="delete_user_view"),     # user.views
    path('success/', create_success_view, name="create_success_view"),           # user.views
    path('deleted/', delete_success_view, name="delete_success_view"),           # user.views
]
