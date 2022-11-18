from django.shortcuts import render
from django.http import HttpResponse

from hospital.models import MedicalTestEntity, CureEntity


def home(request, *args, **kwargs):
    return render(request, 'home.html', {})


def register_staff(request, *args, **kwargs):
    return render(request, "register_staff.html", {})


def add_stuff(request, *args, **kwargs):
    d = request.POST.items()
    for i, val in d:
        print(i, val)
    return HttpResponse("Hello")


def register(request, *args, **kwargs):
    return render(request, 'register.html', {})


def add(request, *args, **kwargs):
    d = request.POST.items()
    for i, val in d:
        print(i, val)
    return HttpResponse("Hello")


def sign_in(request, *args, **kwargs):
    return render(request, 'sign_in.html', {})


def register_card(request, *args, **kwargs):
    return render(request, 'register_card.html', {})


def choose_med_test(request, *args, **kwargs):
    med_tests = MedicalTestEntity.objects.all().values()
    return render(request, 'medical_test.html', {"med_tests": med_tests})


def choose_cure(request, *args, **kwargs):
    title = request.GET.get('cures_search')
    try:
        cures = CureEntity.objects.filter(title=title)
    except Exception:
        content = {}
    else:
        content = {"cures": cures}
    return render(request, 'cure.html', content)
