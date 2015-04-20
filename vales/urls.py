from django.conf.urls import patterns, include, url
from django.contrib import admin
from contactos import views as contacto_views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', contacto_views.home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', contacto_views.login_view, name='login'),
    url(r'^signup/$', contacto_views.register, name='signup'),
    url(r'^logout/$', contacto_views.logout, name='logout'),
    url(r'^contactos/$', contacto_views.get_contactos, name='get_contactos'),

)
