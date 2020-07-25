from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^issuers_count$', views.issuers_count, name='v2_api_issuers_count'),
    url(r'^badgeclasses_count$', views.badgeclasses_count, name='v2_api_badgeclasses_count'),

]
