from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse


from datetime import datetime 
from .models import personalInfo
from .forms import SignupForm
# Create your views here.

auth_success = 0
user = ""

def home(request):
    global auth_success 
    return render(request, "home.html",{'auth_success': auth_success, 'user' : user})


def login(request):
    global auth_success 
    global user
    flag=1
    if auth_success == 1:
        return redirect('home')
    if request.method == 'POST':
        
        data = personalInfo.objects.all()
        element = request.POST.get('u_id') 
        password1 = request.POST.get('pass')
        if(element == LinearSearch(data, element, password1)):
            auth_success = 1
            user = element
            return redirect('home')
        else:
            flag = 0
    context = {'flag' : flag}
    return render(request, "login.html", context)
   

def signup(request):
    
    if request.method == 'POST':
        reg = personalInfo()
        date_str = request.POST.get('Date of Birth')
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
        reg.first_name = request.POST.get('First Name')
        reg.middle_name = request.POST.get('Middle Name')
        reg.last_name = request.POST.get('Last Name')
        reg.email = request.POST.get('Email')
        reg.date_of_birth = d
        reg.gender = request.POST.get('gender')

        reg.country = request.POST.get('country')
        reg.state = request.POST.get('state')
        reg.city = request.POST.get('city')
        reg.address_line1 = request.POST.get('addressline1')
        reg.address_line2 = request.POST.get('addressline2')
        reg.pincode = request.POST.get('pin code')
        reg.primary_contact = request.POST.get('country codePC') + request.POST.get('primaryContact') 
        reg.secondary_contact = request.POST.get('country codeSC') + request.POST.get('secondaryContact') 

        reg.primary_speciality = request.POST.get('Primary Speciality') 
        reg.secondary_speciality = request.POST.get('Secondary Speciality')
        reg.Expirience_in_Years = request.POST.get('Experience in Years')
        reg.NPI_or_GMC_or_IMC_number = request.POST.get('NPI/GMC/IMC number')
        reg.profile_image = request.POST.get('ProfilePhoto')

        reg.medical_school = request.POST.get('Medical School')
        reg.Residency_or_Specialist_Training_or_PG = request.POST.get('Residency/Specialist Training/ PG')
        reg.Fellowship = request.POST.get('Fellowship')
        reg.board_certification = request.POST.get('Board Certificatiom')
        reg.states_to_practice = request.POST.get('States to Practice')
        reg.Revalidation_or_Continuing_Medical_Education_Year = request.POST.get('Revalidation/ Continuing medical education Year')
        reg.Honors_or_Awards_or_Recognition = request.POST.get('Honors/Awards/ Recognition')
        reg.publication = request.POST.get('Publications')
        reg.Hospital_Privileges_to_practice = request.POST.get('Hospital Privileges to practice')
        reg.Description = request.POST.get('Description about yourself')
        reg.Comments = request.POST.get('Additional Comments')
        reg.Resume_or_CV = request.POST.get('Resume/CV')
        reg.save()
        return redirect('home')
    
    
    return render(request,'signup.html')


def logout(request):
    global auth_success
    global user
    if request.method == 'POST':
        auth_success = 0
        user = ""
        return redirect('home')
    return render(request, 'logout.html')

def LinearSearch(lys, element, pwd):
    for i in range (len(lys)):
        if lys[i].u_id == element and lys[i].password == pwd:
            return element
    return -1