from django.shortcuts import render, redirect
from django.utils import translation
# Create your views here.


def contactsView(request):
    return render(request, 'monCV/contacts_page.html', locals())


def i18n(request):
    lang = request.POST.get('language')
    translation.activate(lang)
    template = request.POST.get('next')
    return redirect(template)
