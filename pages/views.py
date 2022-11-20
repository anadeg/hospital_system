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


class ControllerRegisterStaff:
    def __init__(self, ui):
        self.ui = ui
    def register_staff(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def create_main_page(self):
        pass
    def add_stuff(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('home'))

class UIRegisterStaff:
    def __init__(self):
        self.page = 'register_staff.html'


class ControllerRegistration:
    def __init__(self, ui):
        self.ui = ui
    def register(self, request, *args, **kwargs):
        return render(request, self.ui.page, {})
    def add(self, request, *args, **kwargs):
        return render(request, 'home.html', {})

class UIRegistration:
    def __init__(self):
        self.page = 'register.html'


class ControllerLogIn:
    def __init__(self, ui):
        self.ui = ui



class UILogInClient:
    def __init__(self):
        self.page = 'log_in_clt.html'

class UILogInStaff:
    def __init__(self):
        self.page = 'log_in_stf.html'

class UILogInAdmin:
    def __init__(self):
        self.page = 'log_in_admin.html'


def log_in_clt(request, *args, **kwargs):
    return render(request, 'log_in_clt.html', {})


def log_in_stf(request, *args, **kwargs):
    return render(request, 'log_in_stf.html', {})


def log_in_adm(request, *args, **kwargs):
    return render(request, 'log_in_admin.html', {})


def client_register_card(request, *args, **kwargs):
    path = os.path.join('client', 'client_register_card.html')
    return render(request, path, {})


def client_register_card_add(request, *args, **kwargs):
    return HttpResponseRedirect(reverse('clt'))


def client_choose_med_test(request, *args, **kwargs):
    med_tests = MedicalTestEntity.objects.all().values()
    path = os.path.join('client', 'medical_test.html')
    return render(request, path, {"med_tests": med_tests})


def client_find_cure(request, *args, **kwargs):
    title = request.GET.get('cures_search')
    path = os.path.join('client', 'cure_search.html')
    try:
        cures = CureEntity.objects.filter(title=title)
    except Exception:
        content = {}
    else:
        content = {"cures": cures}
    return render(request, path, content)


def client_filter_dc(request, *args, **kwargs):
    path = os.path.join('client', 'doctor_order_card.html')
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
    return render(request, path, content)


def client_dc_list(request, *args, **kwargs):
    path = os.path.join('client', 'order_dc_list.html')

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
    return render(request, path, {"doctor_cards": dc_list, "name": name})


def client_homepage(request, *args, **kwargs):
    path = os.path.join('client', 'client_home.html')
    return render(request, path, {})


def staff_homepage(request, *args, **kwargs):
    path = os.path.join('staff', 'staff_home.html')
    return render(request, path, {})


def admin_hp(request, *args, **kwargs):
    path = os.path.join('admin', 'admin_hm.html')
    return render(request, path, {})


def staff_card_registration_list(request, *args, **kwargs):
    path = os.path.join('staff', 'doctor_register_card.html')
    return render(request, path, {})


def staff_client_list(request, *args, **kwargs):
    path = os.path.join('staff', 'doctor_clients.html')
    return render(request, path, {})


def admin_register_staff(request, *args, **kwargs):
    path = os.path.join('admin', 'admin_register_staff.html')
    return render(request, path, {})


def admin_cures_list(request, *args, **kwargs):
    cures = CureEntity.objects.all().values()
    path = os.path.join('admin', 'cures_list.html')
    return render(request, path, {"cures": cures})


def admin_edit_cure(request, id, *args, **kwargs):
    path = os.path.join('admin', 'cure_change.html')
    cure = CureEntity.objects.get(id=id)
    return render(request, path, {"cure": cure})


def admin_edit_cure_record(request, id, *args, **kwargs):
    cure = CureEntity.objects.get(id=id)
    title = request.POST['title']
    description = request.POST['description']
    address = request.POST['address']
    cure.title, cure.description, cure.address = title, description, address
    cure.save()
    # return cures_list(request, *args, **kwargs)
    return HttpResponseRedirect(reverse('adm_cr'))


def admin_delete_cure_record(request, id, *args, **kwargs):
    cure = CureEntity.objects.get(id=id)
    cure.delete()
    # return cures_list(request, *args, **kwargs)
    return HttpResponseRedirect(reverse('adm_cr'))


def admin_add_cure(request, *args, **kwargs):
    path = os.path.join('admin', 'cure_add.html')
    return render(request, path, {})


def admin_add_cure_record(request, *args, **kwargs):
    title = request.POST.get('title')
    description = request.POST.get('description')
    address = request.POST.get('address')
    cure = CureEntity(title=title, description=description, address=address)
    cure.save()
    return HttpResponseRedirect(reverse('adm_cr'))


def admin_hospitals_list(request, *args, **kwargs):
    path = os.path.join('admin', 'hospitals_list.html')
    hospitals = HospitalEntity.objects.all().values()
    return render(request, path, {"hospitals": hospitals})


def admin_edit_hospital(request, id, *args, **kwargs):
    path = os.path.join('admin', 'hospital_change.html')
    hospital = HospitalEntity.objects.get(id=id)
    return render(request, path, {"hospital": hospital})


def admin_edit_hospital_record(request, id, *args, **kwargs):
    hospital = HospitalEntity.objects.get(id=id)
    title = request.POST.get('title')
    info = request.POST.get('info')
    sections = request.POST.get('sections')
    address = request.POST.get('address')
    hospital.title, hospital.info, hospital.sections, hospital.address = title, info, sections, address
    hospital.save()
    return HttpResponseRedirect(reverse('adm_hr'))


def admin_delete_hospital_record(request, id, *args, **kwargs):
    hospital = HospitalEntity.objects.get(id=id)
    hospital.delete()
    return HttpResponseRedirect(reverse('adm_hr'))


def admin_add_hospital(request, *args, **kwargs):
    path = os.path.join('admin', 'hospital_add.html')
    return render(request, path, {})


def admin_add_hospital_record(request, *args, **kwargs):
    title = request.POST['title']
    info = request.POST['info']
    sections = request.POST['sections']
    address = request.POST['address']
    hospital = HospitalEntity(title=title, info=info, sections=sections, address=address)
    hospital.save()
    return HttpResponseRedirect(reverse('adm_hr'))


def admin_staff_list(request, *args, **kwargs):
    path = os.path.join('admin', 'staff_list.html')
    staff = StaffEntity.objects.all().values()
    return render(request, path, {"staff": staff})


def admin_edit_staff(request, id, *args, **kwargs):
    path = os.path.join('admin', 'staff_change.html')
    staff = StaffEntity.objects.get(id=id)
    return render(request, path, {"staff": staff})


def admin_edit_staff_record(request, id, *args, **kwargs):
    staff = StaffEntity.objects.get(id=id)
    staff.name = request.POST.get('name')
    staff.speciality = request.POST.get('speciality')
    staff.hospital_title = request.POST.get('hospital_title')
    staff.cabinet_no = request.POST.get('cabinet_no')
    staff.time = request.POST.get('time')

    staff.save()
    return HttpResponseRedirect(reverse('adm_sr'))


def admin_delete_staff_record(request, id, *args, **kwargs):
    hospital = StaffEntity.objects.get(id=id)
    hospital.delete()
    return HttpResponseRedirect(reverse('adm_sr'))


def admin_add_staff(request, *args, **kwargs):
    path = os.path.join('admin', 'staff_add.html')
    return render(request, path, {})


def admin_add_staff_record(request, *args, **kwargs):
    name = request.POST.get('name')
    speciality = request.POST.get('speciality')
    hospital_title = request.POST.get('hospital_title')
    cabinet_no = request.POST.get('cabinet_no')
    time = request.POST.get('time')
    staff = StaffEntity(name=name, speciality=speciality,
                           hospital_title=hospital_title, cabinet_no=cabinet_no, time=time)
    staff.save()
    return HttpResponseRedirect(reverse('adm_sr'))

