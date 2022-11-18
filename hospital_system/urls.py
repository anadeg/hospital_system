"""hospital_system URL Configuration

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

from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('register_staff/', views.register_staff, name='reg_staff'),
    path('register_staff/add_stuff/', views.add_stuff, name='add_stuff'),

    path('register/', views.register, name='reg'),
    path('register/add/', views.add, name='add'),

    path('log_in_client/', views.log_in_clt, name='log_in_clt'),
    path('log_in_staff/', views.log_in_stf, name='log_in_stf'),
    path('log_in_admin/', views.log_in_adm, name='log_in_adm'),

    path('register_card/', views.register_card, name='reg_card'),
    path('register_card/add/', views.add, name='reg_card'),

    path('choose_medical_test/', views.choose_med_test, name='choose_med_test'),

    path('cures/', views.find_cure, name='find_cures'),
    path('cures/<str:cure_title>', views.find_cure, name='find_cures_title'),

    path('client/', views.client_homepage, name='clt'),
    # path('log_in/check/', views.check, name='check'),
    # path('client/<int:id>', views.client_homepage, name='clt_id'),
    path('client/doctor_card_order/', views.add, name='clt_dc_order'),
    path('client/medical_test_order/', views.add, name='clt_mt_order'),
    path('client/card_registration/', views.register_card, name='clt_card_reg'),
    path('client/choose_region', views.add, name='clt_region'),
    path('client/cures_search', views.find_cure, name='clt_c_search'),
    path('client/hospital_search', views.add, name='clt_h_search'),

    path('staff/', views.staff_homepage, name='stf'),
    path('staff/list/', views.client_list, name='stf_lst'),
    path('staff/registration_requests/', views.card_registration_list, name='stf_rr'),

    path('hospital_admin/', views.admin_hp, name='adm'),
    path('hospital_admin/hospital_records', views.add, name='adm_hr'),
    path('hospital_admin/cure_records', views.add, name='adm_cr'),
    path('hospital_admin/staff_records', views.add, name='adm_sr'),
    path('hospital_admin/staff_registration', views.adm_register_staff, name='adm_sreg'),

    path('hello/', views.add, name='hello')
]
