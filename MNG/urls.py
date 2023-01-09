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
    path('', choose_language_view, name='choose_language_view'),

    # All English URL patterns

    path('en/', home_view, name='home'),                                                                        # pages.views
    path('en/contacts/', contacts_view, name='contacts'),                                                       # pages.views
    path('en/about/', about_view, name='about_view'),                                                           # pages.views
    path('en/refused/', refused, name='refused'),                                                               # pages.views

    path('en/create_member/', member_create_view, name='member_create_view'),                                   # member.views
    path('en/<str:logged_user>/member_list/', member_list_view, name="member_list_view"),                       # member.views
    path('en/user/<str:name>/', member_detail_view, name='member_detail_view'),                                 # member.views
    path('en/user/<str:name>/history/', member_history_list_view, name='member_history_list_view'),             # member.views
    path('en/user/<str:name>/delete/', delete_member_view, name='delete_member_view'),                          # member.views
    path('en/user/<str:name>/update/', update_member_view, name='update_member_view'),                          # member.views
    path('en/creation_success/', create_success_view, name='create_success_view'),                              # member.views
    path('en/update_success/', update_success_view, name='update_success_view'),                                # member.views
    path('en/delete_success/', delete_success_view, name='delete_success_view'),                                # member.views

    path('en/login/', include('django.contrib.auth.urls')),                                                     # userAuth.views
    path('en/login/', login_user, name='login_user'),                                                           # userAuth.views
    path('en/logout/', logout_user, name='logout_user'),                                                        # userAuth.views
    path('en/create_user/', create_user_view, name = 'create_user_view'),                                       # userAuth.views
    path('en/delete/', delete_user, name='delete_user'),                                                        # userAuth.views
    path('en/user_deleted', user_delete_success_view, name='user_delete_success_view'),                         # userAuth.views

    # All Italian URL Patterns
    
    path('it', home_view_it, name='home_view_it'),                                                              # pages.views
    path('it/contacts/', contacts_view_it, name='contacts_it'),                                                 # pages.views
    path('it/about/', about_view_it, name='about_view_it'),                                                     # pages.views
    path('it/refused/', refused_it, name='refused_it'),                                                         # pages.views

    path('it/create_member/', member_create_view_it, name='member_create_view_it'),                             # member.views
    path('it/<str:logged_user>/member_list/', member_list_view_it, name="member_list_view_it"),                 # member.views
    path('it/user/<str:name>/', member_detail_view_it, name='member_detail_view_it'),                           # member.views
    path('it/user/<str:name>/history/', member_history_list_view_it, name='member_history_list_view_it'),       # member.views
    path('it/user/<str:name>/delete/', delete_member_view_it, name='delete_member_view_it'),                    # member.views
    path('it/user/<str:name>/update/', update_member_view_it, name='update_member_view_it'),                    # member.views
    path('it/creation_success/', create_success_view_it, name='create_success_view_it'),                        # member.views
    path('it/update_success/', update_success_view_it, name='update_success_view_it'),                          # member.views
    path('it/delete_success/', delete_success_view_it, name='delete_success_view_it'),                          # member.views

    path('it/login/', include('django.contrib.auth.urls')),                                                     # userAuth.views
    path('it/login/', login_user_it, name='login_user_it'),                                                           # userAuth.views
    path('it/logout/', logout_user_it, name='logout_user_it'),                                                  # userAuth.views
    path('it/create_user/', create_user_view_it, name = 'create_user_view_it'),                                 # userAuth.views
    path('it/delete/', delete_user_it, name='delete_user_it'),                                                  # userAuth.views
    path('it/user_deleted', user_delete_success_view_it, name='user_delete_success_view_it'),                   # userAuth.views

]
