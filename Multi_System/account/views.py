from django.shortcuts import render, redirect
from django.http import JsonResponse
from validate_email import validate_email
from django.contrib import messages
from account.models import CustomUser
import json
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from evoting.models import CandidateCategory

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        choice = request.POST.get('choice')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        context = {
            'fieldValues': request.POST
        }

        #print(choice)
        if not CustomUser.objects.filter(username = username).exists():
            if not CustomUser.objects.filter(email = email).exists():
                if len(password) < 7:
                    messages.warning(request, 'Password too short')
                    return redirect('account:register')
                if password != password2:
                    messages.error(request, "Password does not match")
                    return redirect("account:register")
                if choice == "Candidate":
                    user = CustomUser.objects.create_user(username = username, email = email, user_type = "2")
                    user.set_password(password)
                    user.save()
                    print(user)
                    #CandidateName.objects.create(user = user)
                    
                    messages.success(request, "Registration Successfully")
                    return redirect("account:login")
                elif choice == "Voter":
                    user = CustomUser.objects.create_user(username = username, email = email, user_type = "3")
                    user.set_password(password)
                    user.save()
                    #CandidateName.objects.create(user = user)
                    
                    
                    messages.success(request, "Registration Successfully")
                    return redirect("account:login")
                else:
                    messages.error(request, "Select a Registration choice")
                    return edirect("account:register")
                
                return render(request, 'register.html', context)  
    return render(request, 'register.html')   

def validateEmail(request):
    data = json.loads(request.body)
    email = data['email']
    if not validate_email(email):
        return JsonResponse({"email_error": "Invalid Email"})
    if CustomUser.objects.filter(email = email).exists():
        return JsonResponse({"email_exist": "Email already use"})

    return JsonResponse({"email": True})

def validateUsername(request):
    data = json.loads(request.body)
    username = data['username']
    if CustomUser.objects.filter(username = username).exists():
        return JsonResponse({"username_exist": "Username Already Exist"})
    if not str(username).isalnum():
        return JsonResponse({"username_error": "Username must contain only Alpanumeric character"})
    

    return JsonResponse({"username": True})



    #return render(request, 'register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, email=email, password=password)
        if user:
            #REDIRECT TO ADMIN OR HOD DASHBOARD PAGE
            if user.is_active and user.user_type == "1":
                login(request, user)
                messages.success(request, "Login Successfully")
                return redirect("evoting:admimDashboard")
            elif user.is_active and user.user_type == "2":
                if user.account_updated == False:
                    login(request, user)
                    messages.success(request, "Login Successfully")
                    return redirect("account:cUpdate-page")
                else:
                    login(request, user)
                    messages.success(request, "Login Successfully")
                    return redirect("evoting:cHome-page")
            elif user.is_active and user.user_type == "3":
                if user.account_updated == False:
                    login(request, user)
                    messages.success(request, "Login Successfully")
                    return redirect("account:vUpdate-page")
                else:
                    login(request, user)
                    messages.success(request, "Login Successfully")
                    return redirect("evoting:vHome-page")
            
        else:
            messages.info(request, "Invalid Details")
            return redirect("account:login")

    return render(request, 'login.html')

@login_required
def logoutBtn(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successfully")
        return redirect("account:login")

# CANDIDATE UPDATE ACCOUNT
@login_required
def cUpdate_page(request):
    if request.user.is_authenticated:
        userId = request.user.id
        userData = CustomUser.objects.get(pk = userId)
        can_cat = CandidateCategory.objects.all()
        ca = CandidateCategory.objects.get(user = userData)
        #if not ca.exists():
            #print("user does not exist")
            #return redirect("account:cUpdate-page")
        print(ca.name)
        context ={
            'userData': userData,
            'can_cat': can_cat,
            'ca': ca
        }
        
        if request.method == 'POST' or request.method == "FILES":
            username = request.POST.get("username")
            email = request.POST.get("email")
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            phoneNo = request.POST.get("phoneNo")
            photo = request.FILES.get("photo")
            if photo == None:
                print("no image")
            cat_choice = request.POST.get("cat_choice")
            if cat_choice == "Select":
                print("Nothing selected")

            
            #print(catCatId)

            userData.username = username
            userData.email = email
            userData.first_name = firstname
            userData.last_name = lastname
            userData.phone_no = int(phoneNo)
            userData.image = photo
            userData.account_updated = True
            userData.save()

            catCatId = CandidateCategory.objects.get(pk = cat_choice)
            if catCatId == None:
                print("jsjsj")
            catCatId.user.add(userData)
            catCatId.save()
            messages.success(request, 'Details updated successfully')
            return redirect("account:cUpdate-page")

        return render(request, 'evoting/candidate/update_acc.html', context)
        

    return render(request, 'evoting/candidate/update_acc.html')

# VOTERS UPDATE ACCOUNT
def vUpdate_page(request):
    if request.user.is_authenticated:
        userId = request.user.id
        userData = CustomUser.objects.get(pk = userId)

        print(userData.username)
        context ={
            'userData': userData
        }
        
        if request.method == 'POST' or request.method == "FILES":
            username = request.POST.get("username")
            email = request.POST.get("email")
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            phoneNo = request.POST.get("phoneNo")
            photo = request.FILES.get("photo")
            if photo == None:
                print("no image")

            userData.username = username
            userData.email = email
            userData.first_name = firstname
            userData.last_name = lastname
            userData.phone_no = int(phoneNo)
            userData.image = photo
            userData.account_updated = True
            userData.save()

            messages.success(request, 'Details updated successfully')
            return redirect("account:vUpdate-page")

        return render(request, 'evoting/voter/update_acc.html', context)
    return render(request, 'evoting/voter/update_acc.html')
