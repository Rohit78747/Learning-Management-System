from django.shortcuts import redirect, render


def Base(request):
    return render(request, 'base.html')


def HOME(request):
    return render(request, 'main/home.html')


def single_course(request):
    return render(request, 'main/single_course.html')


def contact(request):
    return render(request, 'main/contact_us.html')


def about(request):
    return render(request, 'main/about_us.html')
