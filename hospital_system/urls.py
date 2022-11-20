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

import os

from pages import views
from pages.views import (ControllerHome, UIHome,
                         ControllerStaffRegistration, UIStaffRegistration,
                         ControllerRegistration, UIRegistration,
                         ControllerLogIn, UILogIn,
                         ControllerClientCardRegistration, UIClientCardRegistration,
                         ControllerOrderMedicalTest, UIOrderMedicalTest,
                         ControllerSearchCure, UISearchCure,
                         ControllerOrderMedicalCard, UIOrderDoctorCard,
                         ControllerStaffCardRegistration, UIStaffCardRegistration,
                         ControllerStaffClients, UIStaffClients,
                         ControllerAdminStaffRegistration, UIAdminStaffRegistration,
                         ControllerAdminCuresList, UIAdminCuresList,
                         ControllerAdminEditCure, UIAdminEditCure,
                         ControllerAdminAddCure, UIAdminCreateCure,
                         ControllerHospitalsList, UIAdminHospitalsList,
                         ControllerEditHospital, UIEditHospital,
                         ControllerAddHospital, UIAddHospital,
                         ControllerStaffList, UIStaffList,
                         ControllerEditStaff, UIEditStaff,
                         ControllerAddStaff, UIAddStuff)

ui_home = UIHome()
controller_home = ControllerHome(ui_home)

ui_reg_staff = UIStaffRegistration()
controller_reg_staff = ControllerStaffRegistration(ui_reg_staff)

ui_reg = UIRegistration()
controller_reg = ControllerRegistration(ui_reg)

ui_log_in_clt = UILogIn('log_in_clt.html')
ui_log_in_stf = UILogIn('log_in_stf.html')
ui_log_in_adm = UILogIn('log_in_adm.html')
controller_log_in_clt = ControllerLogIn(ui_log_in_clt)
controller_log_in_stf = ControllerLogIn(ui_log_in_stf)
controller_log_in_adm = ControllerLogIn(ui_log_in_adm)

ui_clt_reg_card = UIClientCardRegistration()
controller_clt_reg_card = ControllerClientCardRegistration(ui_clt_reg_card, "card")

ui_med_test = UIOrderMedicalTest()
controller_med_test = ControllerOrderMedicalTest(ui_med_test)

ui_search_cure = UISearchCure()
controller_search_cure = ControllerSearchCure(ui_search_cure)

ui_order_dc = UIOrderDoctorCard()
controller_order_dc = ControllerOrderMedicalCard(ui_order_dc)

ui_staff_reg_card = UIStaffCardRegistration()
controller_staff_reg_card = ControllerStaffCardRegistration(ui_staff_reg_card)

ui_staff_clients = UIStaffClients()
controller_staff_clients = ControllerStaffClients(ui_staff_clients)

ui_admin_staff_reg = UIAdminStaffRegistration()
controller_admin_staff_reg = ControllerAdminStaffRegistration(ui_admin_staff_reg)

ui_admin_cures = UIAdminCuresList()
cntr_admin_cures = ControllerAdminCuresList(ui_admin_cures, "cure")

ui_admin_edit_cure = UIAdminEditCure()
cntr_admin_edit_cure = ControllerAdminEditCure(ui_admin_edit_cure)

ui_admin_create_cure = UIAdminCreateCure()
cntr_admin_create_cure = ControllerAdminAddCure(ui_admin_create_cure)

ui_admin_hospitals = UIAdminHospitalsList()
cntr_admin_hospitals = ControllerHospitalsList(ui_admin_hospitals, "h1")

ui_admin_edit_hos = UIEditHospital()
cntr_admin_edit_hos = ControllerEditHospital(ui_admin_edit_hos)

ui_add_hos = UIAddHospital()
cntr_add_hos = ControllerAddHospital(ui_add_hos)

ui_staff_list = UIStaffList()
cntr_staff_list = ControllerStaffList(ui_staff_list, "staff")

ui_staff_edit = UIEditStaff()
cntr_edit_staff = ControllerEditStaff(ui_staff_edit)

ui_add_staff = UIAddStuff()
cntr_add_staff = ControllerAddStaff(ui_add_staff)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', controller_home.home, name='home'),

    path('register_staff/', controller_reg_staff.register_staff_page, name='reg_staff'),
    path('register_staff/add_stuff/', controller_reg_staff.add_stuff, name='add_stuff'),

    path('register/', controller_reg.register_page, name='reg'),
    path('register/add/', controller_reg.add, name='add'),

    path('log_in_client/', controller_log_in_clt.log_in_page, name='log_in_clt'),
    path('log_in_staff/', controller_log_in_stf.log_in_page, name='log_in_stf'),
    path('log_in_admin/', controller_log_in_adm.log_in_page, name='log_in_adm'),

    path('register_card/', controller_clt_reg_card.client_register_card_page, name='reg_card'),
    path('register_card/add/', controller_home.home, name='reg_card'),

    # path('choose_medical_test/', controller_med_test.client_choose_med_test, name='choose_med_test'),

    # path('cures/', controller_search_cure.client_find_cure, name='find_cures'),
    # path('cures/<str:cure_title>', controller_search_cure.client_find_cure, name='find_cures_title'),

    path('client/', controller_log_in_clt.client_homepage, name='clt'),
    path('client/doctor_card_order/', controller_log_in_clt.client_homepage, name='clt_dc_order'),
    path('client/medical_test_order/', controller_med_test.client_med_tests_page, name='clt_mt_order'),
    path('client/card_registration/', controller_clt_reg_card.client_register_card_page, name='clt_card_reg'),
    path('client/card_registration/add', controller_clt_reg_card.create_client_home, name='clt_card_reg_add'),
    path('client/choose_region', controller_home.home, name='clt_region'),
    path('client/cures_search', controller_search_cure.client_find_cure_page, name='clt_c_search'),
    path('client/hospital_search', controller_log_in_clt.client_homepage, name='clt_h_search'),

    path('staff/', controller_log_in_stf.staff_homepage, name='stf'),
    path('staff/list/', controller_staff_clients.staff_client_list, name='stf_lst'),
    path('staff/registration_requests/', controller_staff_reg_card.staff_card_registration_list, name='stf_rr'),
    path('staff/order_doctor_card/', controller_order_dc.client_filter_dc_page, name='stf_dc_filter'),
    path('staff/order_doctor_card/doctor_card_list/', controller_order_dc.client_dc_list_page, name='stf_dc_list'),

    path('hospital_admin/', controller_log_in_adm.admin_hp, name='adm'),

    path('hospital_admin/cure_records', cntr_admin_cures.admin_cures_list_page, name='adm_cr'),
    path('hospital_admin/cure_records/change/<int:id>', cntr_admin_edit_cure.admin_edit_cure_page, name='adm_cr_cng'),
    path('hospital_admin/cure_records/change/change_record/<int:id>', cntr_admin_edit_cure.admin_edit_cure_record, name='adm_cr_cng'),
    path('hospital_admin/cure_records/delete/<int:id>', cntr_admin_cures.delete_cure_page, name='adm_cr_dlt'),
    path('hospital_admin/cure_records/add', cntr_admin_create_cure.admin_add_cure_page, name='adm_cr_add'),
    path('hospital_admin/cure_records/add_record', cntr_admin_create_cure.admin_add_cure_record, name='adm_cr_add_rec'),

    path('hospital_admin/hospital_records', cntr_admin_hospitals.admin_hospitals_list_page, name='adm_hr'),
    path('hospital_admin/hospital_records/change/<int:id>', cntr_admin_edit_hos.admin_edit_hospital_page, name='adm_hr_cng'),
    path('hospital_admin/hospital_records/change/change_record/<int:id>', cntr_admin_edit_hos.admin_edit_hospital_record, name='adm_hr_cng'),
    path('hospital_admin/hospital_records/delete/<int:id>', cntr_admin_hospitals.delete_hospital_page, name='adm_hr_dlt'),
    path('hospital_admin/hospital_records/add', cntr_add_hos.admin_add_hospital_page, name='adm_hr_add'),
    path('hospital_admin/hospital_records/add_record', cntr_add_hos.admin_add_hospital_record, name='adm_hr_add_rec'),

    path('hospital_admin/staff_records', cntr_staff_list.admin_staff_list_page, name='adm_sr'),
    path('hospital_admin/staff_registration', controller_admin_staff_reg.admin_register_staff_page, name='adm_sreg'),
    path('hospital_admin/staff_records/change/<int:id>', cntr_edit_staff.admin_edit_staff_page, name='adm_sr_cng'),
    path('hospital_admin/staff_records/change/change_record/<int:id>', cntr_edit_staff.admin_edit_staff_record, name='adm_sr_cng'),
    path('hospital_admin/staff_records/delete/<int:id>', cntr_staff_list.delete_stuff_page, name='adm_sr_dlt'),
    path('hospital_admin/staff_records/add', cntr_add_staff.admin_add_staff_page, name='adm_sr_add'),
    path('hospital_admin/staff_records/add_record', cntr_add_staff.admin_add_staff_record, name='adm_sr_add_rec'),

    path('hello/', controller_home.home, name='hello')
]



