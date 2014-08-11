from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
	url(r'^vhost/$',                            views.VHostList.as_view(),     name='web_vhost_list'),
	url(r'^vhost/add$',                         views.VHostCreate.as_view(),   name='web_vhost_add'),
	url(r'^vhost/(?P<pk>\d+)/update$',          views.VHostUpdate.as_view(),   name='web_vhost_update'),
	url(r'^vhost/(?P<pk>\d+)/delete$',          views.VHostDelete.as_view(),   name='web_vhost_delete'),

	url(r'^vhost/(?P<pk>\d+)/catchall$',        views.vhostCatchallSet,        name='web_vhost_catchall_set'),
	url(r'^vhost/catchall/(?P<pk>\d+)/delete$', views.vhostCatchallDelete,     name='web_vhost_catchall_delete'),

	url(r'^sslcert/$',                          views.SSLCertList.as_view(),   name='web_sslcert_list'),
	url(r'^sslcert/add$',                       views.sslcertCreate,           name='web_sslcert_add'),
	url(r'^sslcert/(?P<pk>\d+)/delete$',        views.SSLCertDelete.as_view(), name='web_sslcert_delete'),
)