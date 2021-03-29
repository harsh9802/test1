from django.urls import path,re_path
from rtoapp.views import home,llr,llr_validate,vehicle_registration,vehicle_status,dl_view,dl_status,dl_verification,Complaint_view,complaint_status
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^home.html',home),

    url(r'^llr.html', llr),
    url(r'^llr_validate/$', llr_validate,name="llr_validate"),
    url(r'^llr_validate/llr.html', llr),
    url(r'^llr_validate/vehicle_registration.html',vehicle_registration),
    url(r'^llr_validate/DL.html',dl_view),
    url(r'^llr_validate/Complaint.html',Complaint_view),
    url(r'^llr_validate/home.html/',home),
    
    url(r'^vehicle_registration.html', vehicle_registration),
    url(r'^vehicle_status/$', vehicle_status,name="vehicle_status"),
    url(r'^vehicle_status/llr.html', llr),
    url(r'^vehicle_status/vehicle_registration.html', vehicle_registration),
    url(r'^vehicle_status/DL.html', dl_view),
    url(r'^vehicle_status/Complaint.html',Complaint_view),
    url(r'^vehicle_status/home.html/',home),
    
    url(r'^DL.html', dl_view),
    url(r'^dl_status.html/$', dl_status,name="dl_status"),
    url(r'^dl_verification.html/$', dl_verification,name="dl_verification"),
    url(r'^dl_verification.html/llr.html', llr),
    url(r'^dl_verification.html/vehicle_registration.html', vehicle_registration),
    url(r'^dl_verification.html/DL.html', dl_view),
    url(r'^dl_verification.html/Complaint.html', Complaint_view),
    url(r'^dl_verification.html/home.html/',home),
    
    url(r'^Complaint.html', Complaint_view),
    url(r'^complaint_status/$', complaint_status,name="complaint_status"),
    url(r'^complaint_status/llr.html', llr),
    url(r'^complaint_status/vehicle_registration.html', vehicle_registration),
    url(r'^complaint_status/DL.html', dl_view),
    url(r'^complaint_status/Complaint.html', Complaint_view),
    url(r'^complaint_status/home.html/',home),
]