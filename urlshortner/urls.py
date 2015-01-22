from django.conf.urls import patterns, include, url
from tiny.views import LinkCreate, LinkShow, RedirectUrlView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'urlshortner.views.home', name='home'),
    # url(r'^urlshortner/', include('urlshortner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LinkCreate.as_view(), name='home'),
    url(r'^link/(?P<token>\w+)$', LinkShow.as_view(), name='link_show'),
    url(r'^r/(?P<short_url>\w+)$', RedirectUrlView.as_view(), name='redirect-url'),
)
