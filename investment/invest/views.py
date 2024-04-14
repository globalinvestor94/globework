from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import SignUpForm, UserCreationForm, LoginForm, EmailForm,BeginnerForm,ProfessionalForm,PromoForm, RepForm, FinaleForm
from .models import learnMore, Testimony, About,InvestBeginner,InvestProfessional,InvestPromo, InvestRep,InvestFinale
from django.views.generic import ListView,DetailView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.models import User


# Create your views here.
def GlobalView(request):
    items = Testimony.objects.order_by('-date')
    if request.method == 'GET':
        form = EmailForm()
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            message = form.cleaned_data.get("message")
            from_email = settings.EMAIL_HOST_USER
            email = form.cleaned_data.get("email")
            to_email = [settings.EMAIL_HOST_USER]
            full_message= f"""Recieved message from {email}
            _______________________
            {message}"""
             

            try:
                send_mail(
                    subject=name,
                    message=full_message, 
                    from_email=from_email,
                    recipient_list=['comeseeme@gmail.com'], fail_silently=False)
                
                messages.info(request, "This means alot to us, we'll get back to you shortly")
                return redirect("invest:home")
            except  BadHeaderError:
                messages.info(request, "Your Mail Wasn't Sent!!!, Please Try Again")
                return redirect("invest:home") 

    return render(request,'folder/home.html', {'items':items, "form":form})
       

@login_required(login_url='/login')
def beginnerPlan(request):
    begin = InvestBeginner.objects.all()
    if request.method == "POST":
        form = BeginnerForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('invest:beginner')
    else:
        form = BeginnerForm()
        
    context = {"form":form, "begin":begin}
    
    return render(request,"folder/beginner.html", context)


@login_required(login_url='/login')
def professionalPlan(request):
    pro = InvestProfessional.objects.all()
    if request.method == "POST":
        form = ProfessionalForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('invest:professional')
    else:
        form = ProfessionalForm()
        
    context = {"form":form, "pro":pro}
    
    return render(request,"folder/professional.html", context)


@login_required(login_url='/login')
def promoPlan(request):
    promo = InvestPromo.objects.all()
    if request.method == "POST":
        form = PromoForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('invest:promo')
    else:
        form = PromoForm()
        
    context = {"form":form, "promo":promo}
    
    return render(request,"folder/promo.html", context)



@login_required(login_url='/login')
def representativePlan(request):
    rep = InvestRep.objects.all()
    if request.method == "POST":
        form = RepForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('invest:representative')
    else:
        form = RepForm()
        
    context = {"form":form, "rep":rep}
    
    return render(request,"folder/representative.html", context)


@login_required(login_url='/login')
def finalePlan(request):
    finale = InvestFinale.objects.all()
    if request.method == "POST":
        form = FinaleForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('invest:finale')
    else:
        form = FinaleForm()
        
    context = {"form":form, "finale":finale}
    
    return render(request,"folder/finale.html", context)


def AboutView(request):
    about = get_object_or_404(About)
    return render(request,"folder/about.html", {"about":about})

def detailView(request):
    detail = get_object_or_404(learnMore)
    return render(request,"folder/detail.html", {"detail":detail})


def Signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.succes(request, user + 'Your account was created succesfully')
            return redirect('invest:home')
        
    context = {"form":form}
    return render(request, "folder/registration.html", context)

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # user = User.objects.get(email=form.cleaned_data['username'])
        # remember_me = request.POST['remember_me']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            form=login (request, user)
            messages.success(request, f"Welcome {username} !!!")
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            else:
                return redirect('invest:home')

                # if not remember_me:
                #   request.session.set_expiry(0)           
        else:
            messages.success(request, "Wrong username or password.. please try again")
    form = LoginForm()                  
    return render(request, "folder/login.html", {'form':form})



def logoutUser(request):
    logout(request)
    messages.success(request, "You just logged out, see you soon!!!")
    return redirect('invest:home')
