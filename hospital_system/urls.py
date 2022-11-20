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

    path('register_card/', views.client_register_card, name='reg_card'),
    path('register_card/add/', views.add, name='reg_card'),

    path('choose_medical_test/', views.client_choose_med_test, name='choose_med_test'),

    path('cures/', views.client_find_cure, name='find_cures'),
    path('cures/<str:cure_title>', views.client_find_cure, name='find_cures_title'),

    path('client/', views.client_homepage, name='clt'),
    # path('log_in/check/', views.check, name='check'),
    # path('client/<int:id>', views.client_homepage, name='clt_id'),
    path('client/doctor_card_order/', views.add, name='clt_dc_order'),
    path('client/medical_test_order/', views.add, name='clt_mt_order'),
    path('client/card_registration/', views.client_register_card, name='clt_card_reg'),
    path('client/card_registration/add', views.client_register_card_add, name='clt_card_reg_add'),
    path('client/choose_region', views.add, name='clt_region'),
    path('client/cures_search', views.client_find_cure, name='clt_c_search'),
    path('client/hospital_search', views.add, name='clt_h_search'),

    path('staff/', views.staff_homepage, name='stf'),
    path('staff/list/', views.staff_client_list, name='stf_lst'),
    path('staff/registration_requests/', views.staff_card_registration_list, name='stf_rr'),

    path('hospital_admin/', views.admin_hp, name='adm'),

    path('hospital_admin/cure_records', views.admin_cures_list, name='adm_cr'),
    path('hospital_admin/cure_records/change/<int:id>', views.admin_edit_cure, name='adm_cr_cng'),
    path('hospital_admin/cure_records/change/change_record/<int:id>', views.admin_edit_cure_record, name='adm_cr_cng'),
    path('hospital_admin/cure_records/delete/<int:id>', views.admin_delete_cure_record, name='adm_cr_dlt'),
    path('hospital_admin/cure_records/add', views.admin_add_cure, name='adm_cr_add'),
    path('hospital_admin/cure_records/add_record', views.admin_add_cure_record, name='adm_cr_add_rec'),

    path('hospital_admin/hospital_records', views.admin_hospitals_list, name='adm_hr'),
    path('hospital_admin/hospital_records/change/<int:id>', views.admin_edit_hospital, name='adm_hr_cng'),
    path('hospital_admin/hospital_records/change/change_record/<int:id>', views.admin_edit_hospital_record, name='adm_hr_cng'),
    path('hospital_admin/hospital_records/delete/<int:id>', views.admin_delete_hospital_record, name='adm_hr_dlt'),
    path('hospital_admin/hospital_records/add', views.admin_add_hospital, name='adm_hr_add'),
    path('hospital_admin/hospital_records/add_record', views.admin_add_hospital_record, name='adm_hr_add_rec'),

    path('hospital_admin/staff_records', views.admin_staff_list, name='adm_sr'),
    path('hospital_admin/staff_registration', views.admin_register_staff, name='adm_sreg'),
    path('hospital_admin/staff_records/change/<int:id>', views.admin_edit_staff, name='adm_sr_cng'),
    path('hospital_admin/staff_records/change/change_record/<int:id>', views.admin_edit_staff_record, name='adm_sr_cng'),
    path('hospital_admin/staff_records/delete/<int:id>', views.admin_delete_staff_record, name='adm_sr_dlt'),
    path('hospital_admin/staff_records/add', views.admin_add_staff, name='adm_sr_add'),
    path('hospital_admin/staff_records/add_record', views.admin_add_staff_record, name='adm_sr_add_rec'),

    path('hello/', views.add, name='hello')
]
