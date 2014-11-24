from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^signup', 'signups.views.newUser', name='newUser'),
    url(r'^user_created_success', 'signups.views.user_created_success_view'),
    
    url(r'^ticket_list', 'signups.views.ticket_list', name='ticket_list'),
    url(r'^settings', 'signups.views.settings', name='settings'),
    url(r'^invalid', 'signups.views.invalid', name='invalid'),
    url(r'^logout', 'signups.views.logout', name='logout'),
    #url(r'^register','signups.views.newUser', name='newUser'),
    
    #auth urls
    #url(r'^login', 'signups.views.login', name='login'),
    url(r'^auth_view', 'signups.views.auth_view', name='auth_view'),
    #url(r'^logout', 'signups.views.logout', name='logout'),
    #url(r'^loggedin', 'signups.views.loggedin', name='loggedin'),
    #url(r'^invalid_login', 'signups.views.invalid_login', name='invalid_login'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', include('image_space_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),

)
