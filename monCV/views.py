from django.shortcuts import render

# Create your views here.


def contactsView(request):
    return render(request, 'monCV/contacts_page.html', locals())
