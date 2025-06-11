"""fracas_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required

from django.contrib import admin
from django.urls import path, include
from fracas.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from fracas_admin.views import *
from forms.views import *

admin.autodiscover()
admin.site.login = login_required(admin.site.login, login_url='/admin/login/')

urlpatterns = [
    # url(r'^accounts/login/$',auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
    # path('admin/login/', UserLoginView.as_view(), name="login"),
    # path('admin/logout/', UserLogoutView.as_view(), name='logout'),
    # path('admin/', admin.site.urls),
    # path('', index, name="HomePage"),
    #path('', IndexView.as_view(), name='index'),
    # path('register/', RegistrationView.as_view(), name='register'),
    #path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    # path('password_update/', PasswordUpdateView.as_view(), name='password_update'),

    # path('failuredatacollection/', failure_data_view,),
    # path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('reports/', include('reports.urls')),
    path('forms/', include('forms.urls')),
    path('django-sb-admin/', include('django_sb_admin.urls')),
    path('fracas_admin/', include('fracas_admin.urls')),
    
    path('',Index.as_view(),name='index'),
    path('userlogin/',UserLogin.as_view(),name='userlogin'),
    path('login/<int:id>/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('changepassword/',ChangePassword.as_view(),name='changepassword'),
    path('dashboard/',Dashboard.as_view(),name='dashboard'),
    path('PBSMaster/',PBSMasterView.as_view(),name='pbsmaster'),
    path('PBSMaster/add/',PBSMasterAdd.as_view(),name='add_pbsmaster'),
    path('PBSMaster/import/',PBSMasterImport.as_view(),name='import_pbsmaster'),
    # path('PBSMaster/import/',PBSMasterImport.as_view(),name='import_pbsmaster'), #Merrin
    path('PBSMaster/addimport/',PBSMasterAddImport.as_view(),name='addimport_pbsmaster'),
    path('PBSMaster/add/<int:id>/',PBSMasterAdd.as_view(),name='add_pbsmaster'),
    path('PBSMaster/add/delete/',DeletePBSMaster.as_view(),name='delete_pbsmaster'),
    path('PBSMaster/add/deleteAll/',DeleteAllPBSMaster.as_view(),name='deleteAll_pbsmaster'),
    
    path('history/',History.as_view(),name='history'),
    path('history/<int:id>/',HistoryP.as_view(),name='historyp'),
    path('history/personal/',PersonalHistory.as_view(),name='personalhistory'),
    
    path('forms/review_board/details/',AdminReviewBoardDetailsView.as_view(),name='review_board_details'),
    path('manageProject/',ProjectManage.as_view(),name='manageProject'),
    path('manageProject/add/<int:id>/',ManageEdit.as_view(),name='manage_project'),
    path('manageProject/add/',ManageEdit.as_view(),name='manage_project'),
    path('manageProject/delete/',DeleteManageEdit.as_view(),name='delete_manage_project'),

    path('manageSystem/',SystemManage.as_view(),name='manageProject'),
    path('Systemmanage/add/<int:id>/',ManageSystemEdit.as_view(),name='manage_System'),
    path('Systemmanage/add/',ManageSystemEdit.as_view(),name='manage_System'),
    path('Systemmanage/delete/',DeleteManageSystemEdit.as_view(),name='delete_manage_System'),
    
    path('config/',Config.as_view(),name='config'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
