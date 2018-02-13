from django.conf.urls import url
from bb_enxoval import views
from django.conf.urls import include

urlpatterns = [
    url(r'^$', views.form, name='index'),
    url(r'^form/$', views.form, name='form'),
    url(r'^chaining/', include('smart_selects.urls')),
]
