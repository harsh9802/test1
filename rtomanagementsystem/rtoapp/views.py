from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from .models import llr_table,registration_table,complaint_table,Dl_table
from . import models
from django.db.models import When
#from django.views.generic.base import RedirectView 
# Create your views here.
# class tutorial(RedirectView): url = ‘https://data-flair.training/blogs/category/django/’
def home(request):
    return render(request,'home.html')
def llr(request): 
    return render(request,'llr.html')

def llr_validate(request):
    aadhar_num=request.POST.get('aadhaar')
    nm=request.POST.get('name')
    psd=request.POST.get('password')
    mail=request.POST.get('email')
    d_ob=request.POST.get('dob')
    cty=request.POST.get('city')
    addr=request.POST.get('address')
    gndr=request.POST.get('gender')
    vt=request.POST.get('vtype')
    user=llr_table(AadharNumber=aadhar_num,Name=nm,password=psd,email_id=mail,dateofbirth=d_ob,City=cty,Address=addr,Gender=gndr,VehicleType=vt)
    user.save()
    context={"City":cty,"name":nm,"pass":psd}
    return render(request,'llr_validate.html',context)
    #return self.request.GET.get('llr_validate.html',reverse('home.html'))
    
def vehicle_registration(request):
    return render(request,'vehicle_registration.html')

def vehicle_status(request):
    #message.info("vehicle registration successful"),
    id=request.POST.get('r_id')
    a_num=request.POST.get('aadhaar')
    nm=request.POST.get('name')
    c_ov=request.POST.get('company')
    psd=request.POST.get('pass')
    mdl=request.POST.get('model')
    cty=request.POST.get('city')
    ri=request.POST.get('reg_date')
    re=request.POST.get('exp_date')
    email=request.POST.get('email')
    gen=request.POST.get('gender')
    f_type=request.POST.get('fuel_type')
    cav=request.POST.get('cat_v')
    veh=registration_table(aadharNumber=a_num,name=nm,cov=c_ov,password=psd,model=mdl,city=cty,reg_issue_date=ri,reg_expiry_date=re,mail_id=email,Gender=gen,fuel_type=f_type,vehicle_category=cav)
    veh.save()
    context={"City":cty,"id":id}
    return render(request,'vehicle_status.html',context)
def dl_view(request):
    return render(request,'DL.html')
def dl_status(request):
    # id=request.POST.get('ID')
    # var=llr_table.objects.filter('llr_id')
    # if id==var:
    #     return redirect('dl_verification.html')
    # else:
    #     return render(request,'dl_status.html')
    ps=request.POST.get('pass')
    if llr_table.objects.filter(password=ps).exists():
        return render(request,'dl_status.html')
    else:
        return render(request,'DL.html')
def dl_verification(request):
    anum=request.POST.get('aadhaar')
    name=request.POST.get('name')
    mail=request.POST.get('email')
    cty=request.POST.get('city')
    cov=request.POST.get('type')
    dl=Dl_table(AadharNumber=anum,Name=name,cov=cov,email_id=mail,City=cty)
    dl.save()
    context={"Cty":cty,"Nm":name,"aadhaar":anum}
    return render(request,'dl_verification.html',context)

def Complaint_view(request):
    return render(request,'Complaint.html')

def complaint_status(request):
    anum=request.POST.get('aadhaar')
    desc=request.POST.get('complaint_desc')
    cty=request.POST.get('city')
    comp=complaint_table(AadharNumber=anum,cdesc=desc,City=cty)
    comp.save()
    return render(request,'complaint_status.html')
