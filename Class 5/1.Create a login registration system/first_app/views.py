from django.shortcuts import render,redirect
from .forms import Registerform,ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
#PasswordResetForm needs old password for new password
#SetPassWordForm doesn't need old password
#django.contrib.auth.forms has all the authentication related
#AuthenticationForm has user name and pass
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
#update_session_auth_hash to hash the pass

# Create your views here.

def home(request):
    return render(request,"home.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=='POST':
        form=Registerform(request.POST)
        if form.is_valid():
            messages.success(request,"Account Created Successfully")
            #form.save()
             # Log the user in
            user=form.save()
            login(request, user)
            # name=form.cleaned_data['username']
            # return render(request,'profile.html',{'name':name})
            return redirect('profile')
    else:
        form=Registerform()
    return render(request,'signup.html',{'form':form})
        
def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST) 
        if form.is_valid():
            name=form.cleaned_data['username'] 
            user_pass=form.cleaned_data['password']
            user=authenticate(username=name,password=user_pass)
            if user is not None:
                print("User Exist")
                login(request,user)
                return redirect('profile')
            else:
                print("User not Exist")
                form=AuthenticationForm()
                messages.success(request,"no account exist")
                return render(request,"login.html",{'form':form})
    else:
        print("Wrong method")
        form=AuthenticationForm()
        # messages.success(request,'No account exist')
        #return render(request,'login.html',{'form':form})
    return render(request,'login.html',{'form':form})        

def user_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user':request.user})
    else:
        return redirect('login')
    
def pass_change(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user,data=request.POST) #need user and data also
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        
        return render(request,'pass_change.html',{'form':form})
    
    return redirect('signup')

def change_user_data(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=ChangeUserData(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,"Your data changed successfully")
                print(form.cleaned_data)
                return redirect('profile')
        else:
            form=ChangeUserData(instance=request.user)
        return render(request,'change_data.html',{'form':form,'name':"Change User Data"})
    
    else:
        return redirect('signup')
        
                
                
            