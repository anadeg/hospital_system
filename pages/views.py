from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from hospital.models import (MedicalTestEntity,
                             CureEntity,
                             HospitalEntity,
                             StaffEntity,
                             DoctorCardEntity)

import os


class ControllerHome:
    def __init__(self, ui):
        self.ui = ui
    def home(self, request, *args, **kwargs):
        return render(request, self.ui.homepage, {})
    def create_register_page(self):
        pass
    def create_log_in_page(self):
        pass
    def create_register_staff_page(self):
        pass

class UIHome:
    def __init__(self):
        self.homepage = 'home.html'


class ControllerStaffRegistration:
    def __init__(self, ui):
        self.ui = ui
    def register_staff_page(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def create_main_page(self):
        pass
    def add_stuff(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('home'))
    def send_request(self):
        pass

class UIStaffRegistration:
    def __init__(self):
        self.page = 'register_staff.html'


class ControllerRegistration:
    def __init__(self, ui):
        self.ui = ui
    def register_page(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def add(self, request, *args, **kwargs):
        return render(request, 'home.html', {})

class UIRegistration:
    def __init__(self):
        self.page = 'register.html'


class ControllerLogIn:
    def __init__(self, ui):
        self.ui = ui
    def log_in_page(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def client_homepage(self, request, *args, **kwargs):
        path = os.path.join('client', 'client_home.html')
        return render(request, path, {})
    def staff_homepage(self, request, *args, **kwargs):
        path = os.path.join('staff', 'staff_home.html')
        return render(request, path, {})
    def admin_hp(self, request, *args, **kwargs):
        path = os.path.join('admin', 'admin_hm.html')
        return render(request, path, {})
class UILogIn:
    def __init__(self, page):
        self.page = page


class ControllerClientCardRegistration:
    def __init__(self, ui, med_card):
        self.ui = ui
        self.med_card = med_card
    def client_register_card_page(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def create_client_home(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('clt'))
    def __accept(self):
        pass
class UIClientCardRegistration:
    def __init__(self):
        self.page = os.path.join('client', 'client_register_card.html')


class ControllerOrderMedicalTest:
    def __init__(self, ui):
        self.ui = ui
    def client_med_tests_page(self, request, *args, **kwargs):
        med_tests = MedicalTestEntity.objects.all().values()
        return render(request, self.ui.page, {"med_tests": med_tests})
    def create_client_home(self):
        pass
    def __choose_medical_test(self):
        pass
class UIOrderMedicalTest:
    def __init__(self):
        self.page = os.path.join('client', 'medical_test.html')


class ControllerSearchCure:
    def __init__(self, ui):
        self.ui = ui

    def client_find_cure_page(self, request, *args, **kwargs):
        title = request.GET.get('cures_search')
        try:
            cures = CureEntity.objects.filter(title=title)
        except Exception:
            content = {}
        else:
            content = {"cures": cures}
        return render(request, self.ui.page, content)
    def create_client_page(self):
        pass
    def __search(self):
        pass

class UISearchCure:
    def __init__(self):
        self.page = os.path.join('client', 'cure_search.html')


class ControllerOrderMedicalCard:
    def __init__(self, ui):
        self.ui = ui
    def client_filter_dc_page(self, request, *args, **kwargs):
        dc = DoctorCardEntity.objects.all()
        hospitals = set(dc.get('hospital_title'))
        specialities = set(dc.get('doctor_speciality'))
        date = set(dc.get('date'))
        time = set(dc.get('time'))
        staff_list = StaffEntity.objects.all()
        staff = set(staff_list.get('name'))
        content = {
            "hospitals": hospitals,
            "specialities": specialities,
            "staff": staff,
            "date": date,
            "time": time
        }
        return render(request, self.ui.page, content)
    def select_hospital_page(self):
        pass
    def select_speciality_page(self):
        pass
    def select_name_page(self):
        pass
    def select_date_page(self):
        pass
    def select_time_page(self):
        pass
    def submit_dc_page(self):
        pass
    def client_dc_list_page(self, request, *args, **kwargs):
        hospital = request.POST.get('hospitals')
        speciality = request.POST.get('specialities')
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        dc_list = DoctorCardEntity.objects.filter(
            hospital_title=hospital,
            speciality=speciality,
            date=date,
            time=time
        )
        return render(request, self.ui.page, {"doctor_cards": dc_list, "name": name})
    def __select_hospital(self):
        pass
    def __select_speciality(self):
        pass
    def __select_name(self):
        pass
    def __select_date(self):
        pass
    def __submit_dc(self):
        pass


class UIOrderDoctorCard:
    def __init__(self):
        self.page = os.path.join('client', 'doctor_order_card.html')

class ControllerStaffCardRegistration:
    def __init__(self, ui):
        self.ui = ui
    def staff_card_registration_list(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def create_staff_page(self):
        pass
    def __update_page(self):
        pass
    def __accept(self):
        pass
    def __reject(self):
        pass

class UIStaffCardRegistration:
    def __init__(self):
        self.page = os.path.join('staff', 'doctor_register_card.html')


class ControllerStaffClients:
    def __init__(self, ui):
        self.ui = ui

    def staff_client_list(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})

class UIStaffClients:
    def __init__(self):
        self.page = os.path.join('staff', 'doctor_clients.html')


class ControllerAdminStaffRegistration:
    def __init__(self, ui):
        self.ui = ui
    def admin_register_staff_page(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def __update(self):
        pass
    def __accept(self):
        pass
    def __reject(self):
        pass
    def __generate_password(self):
        pass

class UIAdminStaffRegistration:
    def __init__(self):
        self.page = os.path.join('admin', 'admin_register_staff.html')


class ControllerAdminCuresList:
    def __init__(self, ui, cure):
        self.ui = ui
        self.cure = cure
    def admin_cures_list_page(self, request, *args, **kwargs):
        cures = CureEntity.objects.all().values()
        return render(request, self.ui.page, {"cures": cures})
    def add_cure_page(self):
        pass
    def edit_cure_page(self):
        pass
    def delete_cure_page(self, request, id, *args, **kwargs):
        cure = CureEntity.objects.get(id=id)
        cure.delete()
        return HttpResponseRedirect(reverse('adm_cr'))
    def create_admin_page(self):
        pass
    def __add(self):
        pass
    def __edit(self):
        pass
    def __delete(self):
        pass

class UIAdminCuresList:
    def __init__(self):
        self.page = os.path.join('admin', 'cures_list.html')


class UIAdminEditCure:
    def __init__(self):
        self.page = os.path.join('admin', 'cure_change.html')

class ControllerAdminEditCure:
    def __init__(self, ui):
        self.ui = ui
    def admin_edit_cure_page(self, request, id, *args, **kwargs):
        cure = CureEntity.objects.get(id=id)
        return render(request, self.ui.page , {"cure": cure})
    def admin_edit_cure_record(self, request, id, *args, **kwargs):
        cure = CureEntity.objects.get(id=id)
        title = request.POST['title']
        description = request.POST['description']
        address = request.POST['address']
        cure.title, cure.description, cure.address = title, description, address
        cure.save()
        return HttpResponseRedirect(reverse('adm_cr'))


class UIAdminCreateCure:
    def __init__(self):
        self.page = os.path.join('admin', 'cure_add.html')

class ControllerAdminAddCure:
    def __init__(self, ui):
        self.ui = ui
    def admin_add_cure_page(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def admin_add_cure_record(self, request, *args, **kwargs):
        title = request.POST.get('title')
        description = request.POST.get('description')
        address = request.POST.get('address')
        cure = CureEntity(title=title, description=description, address=address)
        cure.save()
        return HttpResponseRedirect(reverse('adm_cr'))


class UIAdminHospitalsList:
    def __init__(self):
        self.page = os.path.join('admin', 'hospitals_list.html')

class ControllerHospitalsList:
    def __init__(self, ui, hospital):
        self.ui = ui
        self.hospital = hospital
    def admin_hospitals_list_page(self, request, *args, **kwargs):
        hospitals = HospitalEntity.objects.all().values()
        return render(request, self.ui.page, {"hospitals": hospitals})
    def create_admin_page(self):
        pass
    def edit_hospital_page(self):
        pass
    def delete_hospital_page(self, request, id, *args, **kwargs):
        hospital = HospitalEntity.objects.get(id=id)
        hospital.delete()
        return HttpResponseRedirect(reverse('adm_hr'))
    def __add(self):
        pass
    def __edit(self):
        pass
    def __delete(self):
        pass


class UIEditHospital:
    def __init__(self):
        self.page = os.path.join('admin', 'hospital_change.html')

class ControllerEditHospital:
    def __init__(self, ui):
        self.ui = ui
    def admin_edit_hospital_page(self, request, id, *args, **kwargs):
        hospital = HospitalEntity.objects.get(id=id)
        return render(request, self.ui.page, {"hospital": hospital})
    def admin_edit_hospital_record(self, request, id, *args, **kwargs):
        hospital = HospitalEntity.objects.get(id=id)
        title = request.POST.get('title')
        info = request.POST.get('info')
        sections = request.POST.get('sections')
        address = request.POST.get('address')
        hospital.title, hospital.info, hospital.sections, hospital.address = title, info, sections, address
        hospital.save()
        return HttpResponseRedirect(reverse('adm_hr'))


class UIAddHospital:
    def __init__(self):
        self.page = os.path.join('admin', 'hospital_add.html')

class ControllerAddHospital:
    def __init__(self, ui):
        self.ui = ui

    def admin_add_hospital_page(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})

    def admin_add_hospital_record(self, request, *args, **kwargs):
        title = request.POST['title']
        info = request.POST['info']
        sections = request.POST['sections']
        address = request.POST['address']
        hospital = HospitalEntity(title=title, info=info, sections=sections, address=address)
        hospital.save()
        return HttpResponseRedirect(reverse('adm_hr'))


class UIStaffList:
    def __init__(self):
        self.page = os.path.join('admin', 'staff_list.html')

class ControllerStaffList:
    def __init__(self, ui, staff):
        self.ui = ui
        self.staff = staff
    def admin_staff_list_page(self, request, *args, **kwargs):
        staff = StaffEntity.objects.all().values()
        return render(request, self.ui.page, {"staff": staff})
    def create_admin_page(self):
        pass
    def add_stuff_page(self):
        pass
    def edit_staff_page(self):
        pass
    def delete_stuff_page(self):
        staff = StaffEntity.objects.get(id=id)
        staff.delete()
        return HttpResponseRedirect(reverse('adm_sr'))
    def __add(self):
        pass
    def __edit(self):
        pass
    def __delete(self):
        pass


class UIEditStaff:
    def __init__(self):
        self.page = os.path.join('admin', 'staff_change.html')

class ControllerEditStaff:
    def __init__(self, ui):
        self.ui = ui
    def admin_edit_staff_page(self, request, id, *args, **kwargs):
        staff = StaffEntity.objects.get(id=id)
        return render(request, self.ui.page, {"staff": staff})
    def admin_edit_staff_record(self, request, id, *args, **kwargs):
            staff = StaffEntity.objects.get(id=id)
            staff.name = request.POST.get('name')
            staff.speciality = request.POST.get('speciality')
            staff.hospital_title = request.POST.get('hospital_title')
            staff.cabinet_no = request.POST.get('cabinet_no')
            staff.time = request.POST.get('time')

            staff.save()
            return HttpResponseRedirect(reverse('adm_sr'))


class UIAddStuff:
    def __init__(self):
        self.page = os.path.join('admin', 'staff_add.html')

class ControllerAddStaff:
    def __init__(self, ui):
        self.ui = ui
    def admin_add_staff_page(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def admin_add_staff_record(self, request, *args, **kwargs):
        name = request.POST.get('name')
        speciality = request.POST.get('speciality')
        hospital_title = request.POST.get('hospital_title')
        cabinet_no = request.POST.get('cabinet_no')
        time = request.POST.get('time')
        staff = StaffEntity(name=name, speciality=speciality,
                            hospital_title=hospital_title, cabinet_no=cabinet_no, time=time)
        staff.save()
        return HttpResponseRedirect(reverse('adm_sr'))



