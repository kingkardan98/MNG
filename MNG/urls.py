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
from django.urls import path, include

from pages.views import *
from members.views import *
from userAuth.views import *

# View parent script is commented near its path,
# so when shit hits the fan I know where to go looking.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),                                                            # pages.views
    path('contacts/', contacts_view, name='contacts'),                                           # pages.views
    path('about/', about_view, name='about_view'),                                               # pages.views
    path('refused/', refused, name='refused'),                                                   # pages.views

    path('create_member/', member_create_view, name='member_create_view'),                       # member.views
    path('<str:logged_user>/member_list/', member_list_view, name="member_list_view"),           # member.views
    path('user/<str:name>/', member_detail_view, name='member_detail_view'),                     # member.views
    path('user/<str:name>/history/', member_history_list_view, name='member_history_list_view'), # member.views
    path('user/<str:name>/delete/', delete_member_view, name='delete_member_view'),              # member.views
    path('user/<str:name>/update/', update_member_view, name='update_member_view'),              # member.views
    path('creation_success/', create_success_view, name='create_success_view'),                  # member.views
    path('update_success/', update_success_view, name='update_success_view'),                    # member.views
    path('delete_success/', delete_success_view, name='delete_success_view'),                    # member.views

    path('login/', include('django.contrib.auth.urls')),                                         # userAuth.views
    path('login/', login_user, name='login_user'),                                               # userAuth.views
    path('logout/', logout_user, name='logout_user'),                                            # userAuth.views
    path('create_user/', create_user_view, name = 'create_user_view'),                           # userAuth.views
    path('delete/', delete_user, name='delete_user')                                             # userAuth.views

]
