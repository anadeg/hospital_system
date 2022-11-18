from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from hospital.models import MedicalTestEntity, CureEntity, UserEntity


def home(request, *args, **kwargs):
    return render(request, 'home.html', {})


def register_staff(request, *args, **kwargs):
    return render(request, "register_staff.html", {})


def add_stuff(request, *args, **kwargs):
    return HttpResponse("Hello")


def register(request, *args, **kwargs):
    return render(request, 'register.html', {})


def add(request, *args, **kwargs):
    d = request.POST.items()
    for i, val in d:
        print(i, val)
    return HttpResponse("Hello")


def log_in_clt(request, *args, **kwargs):
    return render(request, 'log_in_clt.html', {})


def log_in_stf(request, *args, **kwargs):
    return render(request, 'log_in_stf.html', {})


def log_in_adm(request, *args, **kwargs):
    return render(request, 'log_in_admin.html', {})


def register_card(request, *args, **kwargs):
    return render(request, 'client_register_card.html', {})


def choose_med_test(request, *args, **kwargs):
    med_tests = MedicalTestEntity.objects.all().values()
    return render(request, 'medical_test.html', {"med_tests": med_tests})


def find_cure(request, *args, **kwargs):
    title = request.GET.get('cures_search')
    try:
        cures = CureEntity.objects.filter(title=title)
    except Exception:
        content = {}
    else:
        content = {"cures": cures}
    return render(request, 'cure.html', content)


def client_homepage(request, *args, **kwargs):
    return render(request, 'client_home.html', {})


def staff_homepage(request, *args, **kwargs):
    return render(request, 'staff_home.html', {})


def card_registration_list(request, *args, **kwargs):
    return render(request, "doctor_register_card.html", {})


def client_list(request, *args, **kwargs):
    return render(request, 'doctor_clients.html', {})


def admin_hp(request, *args, **kwargs):
    return render(request, 'admin_hm.html', {})


def adm_register_staff(request, *args, **kwargs):
    return render(request, "admin_register_staff.html", {})

