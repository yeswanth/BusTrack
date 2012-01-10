from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import password_reset, password_reset_done
from django.contrib.auth.views import  password_change, password_change_done
from django.views.generic.simple import direct_to_template
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'bustrack.views.home', name='home'),
    # url(r'^bustrack/', include('bustrack.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
    #url(r'^accounts/', include('registration.simple.urls')),
)

urlpatterns += patterns('',
  (r'^accounts/profile/$', direct_to_template, {'template': 'registration/profile.html'}),
  (r'^accounts/password_reset/$', password_reset, {'template_name': 'registration/password_reset.html'}),
  (r'^accounts/password_reset_done/$', password_reset_done, {'template_name': 'registration/password_reset_done.html'}),
  (r'^accounts/password_change/$', password_change, {'template_name': 'registration/password_change.html'}),
  (r'^accounts/password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
)


