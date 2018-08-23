from django.conf.urls import url
# from django.urls import include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(
        template_name='monCV/home_page.html'),
        name='home_page'),

    url(r'services/$', TemplateView.as_view(
        template_name='monCV/services_page.html'),
        name='services_page'),

    url(r'contacts/$', views.contactsView, name='contacts_page'),

    url(r'portofolio/$', TemplateView.as_view(
        template_name='monCV/portofolio_page.html'),
        name='portofolio_page'),

    url(r'blog/$', TemplateView.as_view(
        template_name='monCV/blog_page.html'),
        name='blog_page'),

    url(r'store/$', TemplateView.as_view(
        template_name='monCV/store_page.html'),
        name='store_page'),

    url(r'recherche/$', TemplateView.as_view(template_name='monCV/home_page'),
        name='recherche'),
]
