from . import models
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')


def registration(request):
    if request.method=='POST':
        username=request.POST.get('username') 
        email=request.POST.get('email') 
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')                                                                            
        gender=request.POST.get('gender')
        district=request.POST.get('district') 
        
        if password==confirm_password:
            if models.Registration.objects.filter(email=email).exists():
            
               return HttpResponse("<script>alert('Email Already Exist!');window.location.href='/registration/';</script>")
                # return redirect('registration')
            else:  
                user=models.Registration(
                username=username,
                email=email,
                password=password,
                confirm_password=confirm_password,
                gender=gender,
                DISTRICT=district
                )
                user.save()
                # return HttpResponse("<script>alert('Registration Sucessfull!');window.location.href='/login/';</script>")
                return redirect('login')
        else:
            return HttpResponse("<script>alert('Password Mismatch!');window.location.href='/registration/';</script>")
            # return redirect('registration')
    else:
        return render(request,'registration.html')     


from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = models.Registration.objects.get(email=email)
            if user.password == password:
                request.session['email'] = email
                # return HttpResponse("<script>alert('Login Sucessfull!');window.location.href='/home/';</script>")
                return redirect('home')
            else:
                return HttpResponse("<script>alert('Invalid Email/Password!');window.location.href='/login/';</script>")
                # return redirect('login')
        except models.Registration.DoesNotExist:
            return HttpResponse("<script>alert('User Not Found!Please Register First!');window.location.href='/login/';</script>")
            # return redirect('login')
    return render(request, 'login.HTML')

def logout(request):
    request.session.flush()
    # return HttpResponse("<script>alert('User Logout Successfully!');window.location.href='/select-login/';</script>") 
    return redirect('select_login')

def profile(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            user=models.Registration.objects.get(email=email)
            return render(request,'profile.html',{'user':user})
        except models.Registration.DoesNotExist:
            # return HttpResponse("<script>alert('User Not Found!');window.location.href='/login/';</script>")
            return redirect('login')
    return HttpResponse("<script>alert('User Not Found!');window.location.href='/login/';</script>") 
    # return redirect('login')

def editprofile(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            client = models.Registration.objects.get(email=email)
            if request.method=='POST':
                client.username=request.POST.get('username')
                client.bio=request.POST.get('bio')
                client.links=request.POST.get('links')
                client.image=request.FILES.get('image')
                client.save()
                # return HttpResponse("<script>alert('Profile Updated!');window.location.href='/profile/';</script>")
                return redirect('profile')
            return render(request,'usereditprofile.html',{'client':client})
        except models.Registration.DoesNotExist:
                return HttpResponse("<script>alert('User Not Found!');window.location.href='/login/';</script>")
            # return redirect('login')
    return HttpResponse("<script>alert('User Not Found!');window.location.href='/login/';</script>")
    # return redirect('login')
            
def adminhome(request):
    if not 'username' in request.session:
        return HttpResponse("<script>alert('Admin Not Found!');window.location.href='/adminlogin/';</script>")
        # return redirect('adminlogin')
    user=models.Registration.objects.all()
    trainer=models.Trainer.objects.all()
    shops=models.shop.objects.all()
    return render(request,'admindashboard.html',{'user':user,'trainers':trainer,'shops':shops}) 

def adminlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['username']=username
        request.session['password']=password
        if username=='admin' and password=='admin':
            request.session['role'] = 'admin' 
            # return HttpResponse("<script>alert('Login Successfull!');window.location.href='/adminhome/';</script>")
            return redirect('adminhome')
        return HttpResponse("<script>alert('Password Incorrect/Mismatched!');window.location.href='/adminlogin/';</script>")
        # return redirect('adminlogin')
    return render(request,'adminlogin.html')

def userlist(request):
    user=models.Registration.objects.all()
    return render(request,'userlist.html',{'user':user}) 

def deleteuser(request,id):
    user=models.Registration.objects.get(id=id)
    user.delete()
    # return HttpResponse("<script>alert('User Deleted Successfully!');window.location.href='/userlist/';</script>")
    return redirect('userlist')

def feedbackpage(request):
    if request.method=='POST':
         name=request.POST.get('name')
         email=request.POST.get('email')
         message=request.POST.get('message')
         rating=request.POST.get('rating')

         feedback=models.Feedback(name=name,email=email,message=message,rating=rating)
         feedback.save()
        #  return HttpResponse("<script>alert('Feedback Added Successfully!');window.location.href='/home/';</script>")
         return redirect('home')
    return render(request,'feedback.html')

def feedbacklist(request):
    feedback=models.Feedback.objects.all()
    return render(request,'feedbacklist2.html',{'feedback':feedback})

def deletefeedback(request,id):
    feedback=models.Feedback.objects.get(id=id)
    feedback.delete()
    # return HttpResponse("<script>alert('Feedback Removed Successfully!');window.location.href='/feedbacklist/';</script>")
    return redirect('feedbacklist')

# from django.shortcuts import render, redirect
# from django.db.models import Sum
# from django.http import HttpResponse
# from . import models

# def trainerhome(request):
#     if 'email' not in request.session:
#         return HttpResponse("<script>alert('Email Not Found! Please Login!');window.location.href='/trainerlogin/';</script>")
        

#     email = request.session['email']
#     trainer = models.Trainer.objects.get(email=email)

#     # Total Packages Created
#     total_packages = models.DancePackage.objects.filter(trainer=trainer).count()

#     # Active Students (Subscriptions)
#     active_students = models.Subscription.objects.filter(
#         trainer=trainer,
#         payment_status='Completed'
#     ).count()

#     # Total Earnings from Package Purchases
#     earnings = models.Buypackage.objects.filter(
#         package__trainer=trainer,
#         payment_status='Completed'
#     ).aggregate(total=Sum('fees'))['total'] or 0

#     # Latest 5 Package Purchases
#     recent_orders = models.Buypackage.objects.filter(
#         package__trainer=trainer
#     ).order_by('-ordered_at')[:5]

#     context = {
#         'trainer': trainer,
#         'total_packages': total_packages,
#         'active_students': active_students,
#         'earnings': earnings,
#         'recent_orders': recent_orders,
#     }

#     return render(request, 'trainerdashboard.html', context)


from django.shortcuts import render, HttpResponse
from django.db.models import Sum
from . import models

def trainerhome(request):
    if 'email' not in request.session:
        return HttpResponse("<script>alert('Email Not Found! Please Login!');window.location.href='/trainerlogin/';</script>")

    email = request.session['email']
    trainer = models.Trainer.objects.get(email=email)

    # Total Packages Created
    total_packages = models.DancePackage.objects.filter(trainer=trainer).count()

    # Active Students (Subscriptions)
    active_students = models.Subscription.objects.filter(
        trainer=trainer,
        payment_status='Paid'
    ).count()

    # Total Earnings from Paid Packages using trainer CharField
    earnings = models.Subscription.objects.filter(
        trainer=trainer,   # look at the related package’s trainer
        payment_status='Paid'
    ).aggregate(total=Sum('price'))['total'] or 0

    # Get all package IDs created by this trainer
    trainer_packages = models.DancePackage.objects.filter(trainer=trainer).values_list('id', flat=True)

    # Latest 5 orders for these packages
    recent_orders = models.Buypackage.objects.filter(
        package_id__in=trainer_packages,  # only packages created by this trainer
        payment_status='Paid'
    ).select_related('user', 'package').order_by('-ordered_at')[:5]

    context = {
        'trainer': trainer,
        'total_packages': total_packages,
        'active_students': active_students,
        'earnings': earnings,
        'recent_orders': recent_orders,
    }

    return render(request, 'trainerdashboard.html', context)

def trainer_registration(request):
    if request.method=='POST':
        name=request.POST.get('name') 
        email=request.POST.get('email') 
        password=request.POST.get('password')
        phone=request.POST.get('phone')                                                                            
        gender=request.POST.get('gender')
        experience=request.POST.get('experience')
        idproof=request.FILES.get('idproof') 
        image=request.FILES.get('image') 

        if models.Trainer.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('Email Already Registered!');window.location.href='/trainer_registration/';</script>")
        else:  
                user=models.Trainer(
                name=name,
                email=email,
                password=password,
                phone=phone,
                gender=gender,
                experience=experience,
                idproof=idproof,
                image=image
                )
                user.save()
                # return HttpResponse("<script>alert('Registration Successfull!');window.location.href='/trainerlogin/';</script>")
                return redirect('trainerlogin')
    else:
        return render(request,'trainer_registration.html')   

def trainerlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = models.Trainer.objects.get(email=email)
            if user.password == password:
                if user.isapproved:
                    request.session['email'] = email
                    request.session['trainer_name'] = user.name
                    request.session['trainer_id'] = user.id
                    # return HttpResponse("<script>alert('Login Successfull!');window.location.href='/trainerhome/';</script>")
                    return redirect('trainerhome')
                else:
                    return HttpResponse("<script>alert('Login successful but your account is pending approval!');window.location.href='/trainerlogin/';</script>")
            else:
                return HttpResponse("<script>alert('Invalid Pasword!');window.location.href='/trainerlogin/';</script>")
        except models.Trainer.DoesNotExist:
            return HttpResponse("<script>alert('Invalid Email! Please Register First!');window.location.href='/trainerlogin/';</script>")

    return render(request, 'trainerlogin.HTML')

def trainerlist(request):
    trainer=models.Trainer.objects.all()
    return render(request,'trainerlist.html',{'trainer':trainer})  
     

def trainerprofile(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            trainer=models.Trainer.objects.get(email=email)
            return render(request,'trainerprofile.html',{'trainer':trainer})
        except models.Trainer.DoesNotExist:
            return HttpResponse("<script>alert('Trainer Not Found!');window.location.href='/trainerprofile/';</script>")
    return HttpResponse("<script>alert('Email Not Found!');window.location.href='/trainerprofile/';</script>")  

def deletetrainer(request,id):
    trainer=models.Trainer.objects.get(id=id)
    trainer.delete()
    # return HttpResponse("<script>alert('Trainer Deleted Successfully!');window.location.href='/trsinerlist/';</script>")
    return redirect('trsinerlist')

def approveuser(request,id):
    trainer=models.Trainer.objects.get(id=id)
    trainer.isapproved=True
    trainer.isrejected=False
    trainer.save()
    return redirect('trainerlist')

def rejectuser(request,id):
    trainer=models.Trainer.objects.get(id=id)
    trainer.isapproved=False
    trainer.isrejected=True
    trainer.save()
    return redirect('trainerlist')


from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# ---------------- Admin: Add Event ----------------
def addevent(request):

    if request.method == 'POST':
        name = request.POST.get('event_name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        poster = request.FILES.get('poster')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        date = request.POST.get('date')
        trainer_position = request.POST.get('trainer_position')
        age_category = request.POST.get('age_category')
        priceperperson = request.POST.get('priceperperson')

        institution_id = request.POST.get('institution')
        trainer_id = request.POST.get('trainer')
        venue_id = request.POST.get('venue')

        try:
            institution = models.DanceInstitution.objects.get(id=institution_id)
        except ObjectDoesNotExist:
            messages.error(request, "Invalid institution selected.")
            return HttpResponse("<script>alert('Invalid Institution Selected!');window.location.href='/addevent/';</script>")

        trainer = None
        if trainer_id:
            try:
                trainer = models.Institution_AddTrainer.objects.get(id=trainer_id)
            except ObjectDoesNotExist:
                trainer = None

        venue = None
        if venue_id:
            try:
                venue = models.Venue.objects.get(
                    id=venue_id,
                    institution=institution
                )
            except models.Venue.DoesNotExist:
                messages.error(request, "Invalid venue selected.")
                return HttpResponse("<script>alert('Invalid Venue Selected!');window.location.href='/addevent/';</script>")


        event = models.InstitutionEvent.objects.create(
            institution=institution,
            trainer=trainer,
            name=name,
            description=description,
            trainer_position=trainer_position,
            location=location,
            poster=poster,
            start_time=start_time,
            end_time=end_time,
            date=date,
            age_category=age_category,
            priceperperson=priceperperson,
            venue=venue,
            booked_venue={}
        )

        messages.success(request, "Event added successfully.")
        # return HttpResponse("<script>alert('Event Added Successfully!');window.location.href='/eventlist/';</script>")
        return redirect('eventlist')

    institutions = models.DanceInstitution.objects.all()
    trainers = models.Institution_AddTrainer.objects.all()
    venues = models.Venue.objects.all()  

    return render(request, 'addevent.html', {
        'institutions': institutions,
        'trainers': trainers,
        'venues': venues
    })

# ---------------- Admin: List Events ----------------
def eventlist(request):
    email = request.session.get('username')
    role = request.session.get('role')  

    if not email:
        return redirect('adminlogin')  

    is_admin = (role == 'admin')  

    events = models.InstitutionEvent.objects.all().order_by('-date', '-start_time')

    return render(request, 'eventlist.html', {
        'events': events,
        'is_admin': is_admin
    })


# ---------------- Admin: Edit Event ----------------
def editevent(request, id):
    email = request.session.get('email')
    role = request.session.get('role')

    if not email:
        return HttpResponse("<script>alert('Email Not Found!');window.location.href='/institutionlogin/';</script>")

    if role != 'admin':
        messages.error(request, "You are not authorized to edit events.")
        return HttpResponse("<script>alert('You are not authorized to edit events!');window.location.href='/eventlist/';</script>")

    try:
        event = models.InstitutionEvent.objects.get(id=id)
    except models.InstitutionEvent.DoesNotExist:
        messages.error(request, "Event not found.")
        return HttpResponse("<script>alert('Event not found!');window.location.href='/eventlist/';</script>")

    trainers = models.Institution_AddTrainer.objects.filter(
        institution=event.institution, is_active=True
    )

    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        event.trainer_position = request.POST.get('trainer_position')
        event.date = request.POST.get('date')
        event.start_time = request.POST.get('start_time')
        event.end_time = request.POST.get('end_time') or None
        event.location = request.POST.get('location')
        event.status = request.POST.get('status') or 'UP'
        event.age_category = request.POST.get('age_category')
        event.priceperperson = request.POST.get('priceperperson') or 0

        trainer_id = request.POST.get('trainer')
        if trainer_id:
            try:
                event.trainer = trainers.get(id=trainer_id)
            except models.Institution_AddTrainer.DoesNotExist:
                event.trainer = None
        else:
            event.trainer = None

        if request.FILES.get('poster'):
            event.poster = request.FILES.get('poster')

        event.save()
        messages.success(request, "Event updated successfully!")
        # return HttpResponse("<script>alert('event updated successfully!');window.location.href='/eventlist/';</script>")
        return redirect('eventlist')

    return render(request, 'editevent.html', {
        'event': event,
        'trainers': trainers
    })


# ---------------- Admin: Delete Event ----------------
def deleteevent(request, id):
    email = request.session.get('email')
    role = request.session.get('role')

    if not email:
        return HttpResponse("<script>alert('Email Not Found!');window.location.href='/institutionlogin/';</script>")

    if role != 'admin':
        messages.error(request, "You are not authorized to delete events.")
        return HttpResponse("<script>alert('You are not authorized to Delete events!');window.location.href='/eventlist/';</script>")

    try:
        event = models.InstitutionEvent.objects.get(id=id)
        event.delete()
        messages.success(request, "Event deleted successfully!")
    except models.InstitutionEvent.DoesNotExist:
        messages.error(request, "Event not found.")

    # return HttpResponse("<script>alert('event deleted successfully!');window.location.href='/eventlist/';</script>")
    return redirect('eventlist')


def owner_register(request):
    if request.method=='POST':
        name=request.POST.get('name') 
        email=request.POST.get('email') 
        password=request.POST.get('password')
        phone=request.POST.get('phone')                                                                            
        licenseno=request.POST.get('licenseno')
        image=request.FILES.get('image') 
        shopname=request.POST.get('shopname')
        
        if models.shop.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('Email already exsist!');window.location.href='/owner_register/';</script>")

        else:  
                user=models.shop(
                name=name,
                email=email,
                password=password,
                phone=phone,
                licenseno=licenseno,
                shopname=shopname,
                image=image,
                )
                user.save()
                # return HttpResponse("<script>alert('Registration Successfull!');window.location.href='/owner_login/';</script>")
                return redirect('owner_login')
    else:
        return render(request,'owner_register.html')
    
def owner_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password=request.POST.get('password')

        try:
            user = models.shop.objects.get(email=email)
            if user.password == password:
                if user.isapproved:
                
                    request.session['email'] = email
                    # return HttpResponse("<script>alert('Login Successfull!');window.location.href='/ownerhome/';</script>")
                    return redirect('ownerhome')
                else:
                    return HttpResponse("<script> alert('login successfull but your account is pending approval'); window.location.href='/owner_login/'; </script>")
            else:
                return HttpResponse("<script> alert('Invalid Password '); window.location.href='/owner_login/'; </script>")
        except models.shop.DoesNotExist:
            return HttpResponse("<script> alert('Invalid Email '); window.location.href='/owner_login/'; </script>")

    return render(request, 'owner_login.html')

def ownerhome(request):
    return render(request,'ownerdashboard.html')

def ownerlist(request):
    shops=models.shop.objects.all()
    return render(request,'ownerlist.html',{'shops':shops})

def approveshop(request,id):
    trainer=models.shop.objects.get(id=id)
    trainer.isapproved=True
    trainer.isrejected=False
    trainer.save()
    return redirect('ownerlist')

def rejectshop(request,id):
    trainer=models.shop.objects.get(id=id)
    trainer.isapproved=False
    trainer.isrejected=True
    trainer.save()
    return redirect('ownerlist')

def deleteshop(request,id):
    shops=models.shop.objects.get(id=id)
    shops.delete()
    # return HttpResponse("<script> alert('Shop Deleted Successfully'); window.location.href='/ownerlist/'; </script>")
    return redirect('ownerlist')


def shop_ownerprofile(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            owner=models.shop.objects.get(email=email)
            return render(request,'shop_ownerprofile.html',{'owner':owner})
        except models.shop.DoesNotExist:
            return HttpResponse("<script> alert('Owner not found'); window.location.href='/owner_login/'; </script>")
    return HttpResponse("<script> alert('email not found'); window.location.href='/owner_login/'; </script>") 

def ownereditprofile(request):
    if 'email' in request.session:
        email=request.session['email']
        try:
            owner = models.shop.objects.get(email=email)
            if request.method=='POST':
                owner.name=request.POST.get('name')
                owner.email=request.POST.get('email')
                owner.phone=request.POST.get('phone')
                owner.shopname=request.POST.get('shopname')
                owner.licenceno=request.POST.get('licenceno')
                owner.image=request.POST.get('image')
                owner.save()
                # return HttpResponse("<script> alert('Profile Updated Successfully!'); window.location.href='/shop_ownerprofile/'; </script>")
                return redirect('shop_ownerprofile')
            return render(request,'ownereditprofile.html',{'owner':owner})
        except models.Registration.DoesNotExist:
                return HttpResponse("<script> alert('Owner Not Found!'); window.location.href='/owner_login/'; </script>")
    return HttpResponse("<script> alert('Email Not Found!'); window.location.href='/owner_login/'; </script>")
 

def usertrainerlist(request):
    trainer=models.Trainer.objects.all()
    return render(request,'usertrainerlist.html',{'trainer':trainer})


def about(request):
    return render(request, 'about.html')

from .models import InstitutionEvent, Booking, Registration

def usereventlist(request):
    events = InstitutionEvent.objects.all()
    email = request.session.get('email') 

    user_obj = None
    if email:
        user_obj = Registration.objects.filter(email=email).first()

    for event in events:
        if user_obj:
            event.is_booked = Booking.objects.filter(
                user=user_obj,
                event=event,
                status='confirmed'
            ).exists()
        else:
            event.is_booked = False

    return render(request, 'usereventlist.html', {
        'events': events,
        'session_email': email
    })



# def addcostume(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         color = request.POST.get("color")
#         size = request.POST.get("size")
#         rate = request.POST.get("rate")
#         desc = request.POST.get("desc")
#         quantity = request.POST.get("quantity")
#         image = request.FILES.get("image")
#         email=request.session.get('email')
#         shop=models.shop.objects.get(email=email)

#         models.Costume.objects.create(
#             name=name,
#             color=color,
#             size=size,
#             rate=rate,
#             description=desc,
#             quantity=quantity,
#             image=image,
#             shop=shop
#         )
#         # return HttpResponse("<script> alert('Costumes Added Successfully!'); window.location.href='/view_costumes/'; </script>")
#         return redirect('view_costumes')
#     return render(request, "addcostumes.html")

def institution_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        owner_name = request.POST.get('owner_name')
        description = request.POST.get('description')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        district = request.POST.get('district')
        certificate = request.FILES.get('certificate')
        logo = request.FILES.get('logo')

        if password != confirm_password:
            return HttpResponse("<script> alert('Password Mismatch!'); window.location.href='/institution/'; </script>")

        if models.DanceInstitution.objects.filter(email=email).exists():
            return HttpResponse("<script> alert(Email Already Exsist!'); window.location.href='/institution/'; </script>")

        institution = models.DanceInstitution(
            name=name,
            owner_name=owner_name,
            description=description,
            email=email,
            phone=phone,
            password=password,
            district=district,
            certificate=certificate,
            logo=logo
        )
        institution.save()
        # return HttpResponse("<script> alert('Registration Successfull!'); window.location.href='/institutionlogin/'; </script>")
        return redirect('institutionlogin')
    return render(request, 'institution.html')


def institutionlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = models.DanceInstitution.objects.get(email=email)
            if user.password == password:
                if user.isapproved:
                    request.session['email'] = email
                    request.session['role'] = 'institution' 
                    # return HttpResponse("<script> alert('Login Successfull!'); window.location.href='/institutionhome/'; </script>")
                    return redirect('institutionhome')
                else:
                    return HttpResponse("<script> alert('Login successful but your account is pending approval!'); window.location.href='/institutionlogin/'; </script>")
            else:
                return HttpResponse("<script> alert('Invalid password!'); window.location.href='/institutionlogin/'; </script>")
        except models.DanceInstitution.DoesNotExist:
            return HttpResponse("<script> alert('Invalid Email!'); window.location.href='/institutionlogin/'; </script>")

    return render(request, 'institutionlogin.html')


def admininstitutionlist(request):
    institutions = models.DanceInstitution.objects.all()
    return render(request, 'admininstitutionlist.html', {'institutions': institutions})


def approveinstitution(request, id):
    institution = models.DanceInstitution.objects.get(id=id)
    institution.isapproved = True
    institution.isrejected = False
    institution.save()
    return redirect('admininstitutionlist')


def rejectinstitution(request, id):
    institution = models.DanceInstitution.objects.get(id=id)
    institution.isapproved = False
    institution.isrejected = True
    institution.save()
    return redirect('admininstitutionlist')


def deleteinstitution(request, id):
    institution = models.DanceInstitution.objects.get(id=id)
    institution.delete()
    # return HttpResponse("<script> alert('Deleted Successfully!'); window.location.href='/admininstitutionlist/'; </script>")
    return redirect('admininstitutionlist')

def institutionhome(request):
    email = request.session.get('email')

    if not email:
        return HttpResponse("<script> alert('email not found!'); window.location.href='/institutionlogin/'; </script>")

    try:
        institution = models.DanceInstitution.objects.get(email=email)
    except models.DanceInstitution.DoesNotExist:
        return HttpResponse("<script> alert('Email Not Found!'); window.location.href='/institutionlogin/'; </script>")

    return render(request, 'institutionhome.html', {'institution': institution})

def profile_institution(request):
    if 'email' in request.session:
        email = request.session['email']
        try:
            institution = models.DanceInstitution.objects.get(email=email)
            return render(request, 'profile_institution.html', {'institution': institution})
        except models.DanceInstitution.DoesNotExist:
            return HttpResponse("<script> alert('Institution Not Found!'); window.location.href='/institutionlogin/'; </script>")
    return HttpResponse("<script> alert('email not found!'); window.location.href='/institutionlogin/'; </script>")


def edit_profile_institution(request):
    if 'email' in request.session:
        email = request.session['email']
        try:
            institution = models.DanceInstitution.objects.get(email=email)

            if request.method == 'POST':
                # Update basic fields
                institution.name = request.POST.get('name')
                institution.owner_name = request.POST.get('owner_name')
                institution.email = request.POST.get('email')
                institution.phone = request.POST.get('phone')

                # Update files if uploaded
                if request.FILES.get('logo'):
                    institution.logo = request.FILES['logo']

                if request.FILES.get('certificate'):
                    institution.certificate = request.FILES['certificate']

                institution.save()
                # return HttpResponse("<script> alert('Profile Updated!'); window.location.href='/profile_institution/'; </script>")
                return redirect('profile_institution')
            return render(request, 'edit_profile_institution.html', {'institution': institution})

        except models.DanceInstitution.DoesNotExist:
            return HttpResponse("<script> alert('Institution Not Found!'); window.location.href='/institutionlogin/'; </script>")

    return HttpResponse("<script> alert('email not found!'); window.location.href='/institutionlogin/'; </script>")


def eventdetails(request, event_id):
    """
    View to display details of a specific event.
    """
    event = get_object_or_404(models.InstitutionEvent, id=event_id)

    context = {
        'event': event
    }
    return render(request, 'eventdetails.html', context)

from django.shortcuts import render, redirect
from . import models

def dancepackages(request):

    # get trainer info from session
    trainer_id = request.session.get("trainer_id")
    trainer_name = request.session.get("trainer_name")
    trainer_email = request.session.get("trainer_email")

    # session protection
    if not trainer_id:
        return HttpResponse("<script> alert('Please Login!'); window.location.href='/trainerlogin/'; </script>")
    if request.method == "POST":
        package_name = request.POST.get("packageName")
        description = request.POST.get("description")
        fees = request.POST.get("fees")
        duration = request.POST.get("duration")
        how = request.POST.get("how")
        type_value = request.POST.get("type")

        image_file = (
            request.FILES.get("imageFile") or
            request.FILES.get("browseImage")
        )

        models.DancePackage.objects.create(
            trainer_id=str(trainer_id),   # stored as CharField
            package_name=package_name,
            description=description,
            fees=fees,
            duration=duration,
            how=how,
            type=type_value,
            image=image_file,
        )

        # return HttpResponse("<script> alert('Package Added Successfully!'); window.location.href='/trainerhome/'; </script>")
        return redirect('trainerpackagelist')
    return render(request, "dancepackages.html", {
        "trainer_id": trainer_id,
        "trainer_name": trainer_name,
        "trainer_email": trainer_email,
    })


def listdancepackage(request, trainer_id):
    data = models.DancePackage.objects.filter(trainer_id=trainer_id)

    if not data.exists():
        return HttpResponse("<script>alert('No packages found!');window.history.back();</script>")

    return render(request, 'listdancepackage.html', {'data': data})

def trainer_package(request):
    trainer_id = request.session.get("trainer_id")
    if not trainer_id:
        return HttpResponse("<script> alert('Id not Found!'); window.location.href='/trainerlogin/'; </script>")
    data = models.DancePackage.objects.filter(trainer_id=trainer_id)
    return render(request, 'trainerpackagelist.html', {'data': data})

def deletepackage(request,id):
    user=models.DancePackage.objects.get(id=id)
    user.delete()
    # return HttpResponse("<script> alert('Package Deleted Successfully!'); window.location.href='/trainerpackagelist/'; </script>")
    return redirect('trainerpackagelist')

def edit_package(request,id):
    events=models.DancePackage.objects.get(id=id)
    if request.method=='POST':
        events.TRAINER_CHOICES=request.POST.get('choice')
        events.package_name=request.POST.get('package')
        events.description=request.POST.get('description')
        events.fees=request.POST.get('fees')
        events.duration=request.POST.get('duration')
        events.how=request.POST.get('how')
        if 'image' in request.FILES:
            events.image=request.FILES.get('image')
        events.save()
        # return HttpResponse("<script> alert('Package Updated!'); window.location.href='/trainerpackagelist/'; </script>")
        return redirect('trainerpackagelist')
    return render(request,'edit_package.html',{'package':events})

def adminpackagelist(request):
        data = models.DancePackage.objects.all()
        return render(request, 'adminpackagelist.html', {'data': data})

from django.db import transaction

def addcostume(request):
    if request.method == "POST":

        name = request.POST.get("name")
        rate = request.POST.get("rate")
        desc = request.POST.get("desc")
        image = request.FILES.get("image")

        sizes = request.POST.getlist('size')
        colors = request.POST.getlist('color')
        quantities = request.POST.getlist('quantity')

        if not sizes or not colors or not quantities:
            return render(request, "addcostumes.html", {
                "error": "Sizes, colors and quantities are required."
            })

        if len(sizes) != len(quantities):
            return render(request, "addcostumes.html", {
                "error": "Each size must have a quantity."
            })

        email = request.session.get('email')
        shop = models.shop.objects.get(email=email)

        with transaction.atomic():

            costume = models.Costume.objects.create(
                name=name,
                rate=rate,
                description=desc,
                image=image,
                shop=shop
            )

            # 🔥 Generate all size-color combinations
            for size, qty in zip(sizes, quantities):

                for color in colors:

                    models.CostumeVariant.objects.create(
                        costume=costume,
                        size=size.strip(),
                        color=color.strip(),
                        quantity=int(qty)
                    )

        return redirect('view_costumes')

    return render(request, "addcostumes.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch
from . import models


def view_costumes(request):

    # 1️⃣ Check login
    email = request.session.get('email')
    if not email:
        messages.error(request, "You must be logged in to view costumes.")
        return redirect('owner_login')

    # 2️⃣ Get shop safely
    try:
        shop = models.shop.objects.get(email=email)
    except models.shop.DoesNotExist:
        messages.error(request, "Shop not found.")
        return redirect('owner_login')

    # 3️⃣ Prefetch variants (important for performance)
    costumes = (
        models.Costume.objects
        .filter(shop=shop)
        .prefetch_related('variants')
        .order_by('-id')
    )

    context = {
        'costumes': costumes,
        'shop': shop
    }

    return render(request, 'view_costumes.html', context)


def delete_costume(request, id):
    if 'email' not in request.session:
        messages.error(request, "You must be logged in to delete a costume.")
        return redirect('owner_login')

    email = request.session['email']
    try:
        shop = models.shop.objects.get(email=email)
        costume = models.Costume.objects.get(id=id, shop=shop)
        costume.delete()
        messages.success(request, "Costume deleted successfully.")
    except ObjectDoesNotExist:
        messages.error(request, "Costume not found or you don't have permission to delete it.")

    return redirect('view_costumes')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from . import models


def edit_costume(request, id):

    email = request.session.get('email')
    if not email:
        messages.error(request, "You must be logged in.")
        return redirect('owner_login')

    try:
        shop = models.shop.objects.get(email=email)
        costume = models.Costume.objects.prefetch_related('variants').get(id=id, shop=shop)
    except models.Costume.DoesNotExist:
        messages.error(request, "Costume not found.")
        return redirect('view_costumes')

    sizes_list = ["S", "M", "L", "XL", "XXL","Free Size"]

    if request.method == "POST":

        sizes = request.POST.getlist('size')
        colors = request.POST.getlist('color')
        quantities = request.POST.getlist('quantity')

        cleaned_variants = [
            (s.strip(), c.strip(), q)
            for s, c, q in zip(sizes, colors, quantities)
            if s and c and q
        ]

        if not cleaned_variants:
            messages.error(request, "At least one valid variant required.")
            return redirect('edit_costume', id=id)

        with transaction.atomic():

            costume.name = request.POST.get("name")
            costume.rate = request.POST.get("rate")
            costume.description = request.POST.get("desc")

            image = request.FILES.get("image")
            if image:
                costume.image = image

            costume.save()

            costume.variants.all().delete()

            for size, color, qty in cleaned_variants:
                models.CostumeVariant.objects.create(
                    costume=costume,
                    size=size,
                    color=color,
                    quantity=int(qty)
                )

        messages.success(request, "Costume updated successfully.")
        return redirect('view_costumes')

    return render(request, 'edit_costume.html', {
        'costume': costume,
        'sizes_list': sizes_list
    })

from danceapp.models import Buynow, shop

def owner_view_orders(request):
    owner_email = request.session.get('email') 

    if not owner_email:
        orders = []
        message = "You are not logged in as a shop owner."
        return render(request, 'view_orders.html', {'orders': orders, 'message': message})

    try:
        owner_shop = shop.objects.filter(email=owner_email).first()
        if not owner_shop:
            orders = []
            message = "Shop not found."
            return render(request, 'view_orders.html', {'orders': orders, 'message': message})

        orders = Buynow.objects.filter(product__shop=owner_shop).order_by('-created_at')
        return render(request, 'view_orders.html', {'orders': orders, 'message': ''})

    except Exception as e:
        message = f"Error: {str(e)}"
        return render(request, 'view_orders.html', {'orders': orders, 'message': message})



def listcostumes(request):
    costumes = models.Costume.objects.all().order_by('-created_at')
    return render(request, 'listcostumes.html', {'costumes': costumes})

def listcostumes_shop(request):
    email=request.session.get('email')
    shop=models.shop.objects.get(email=email)
    costumes = models.Costume.objects.filter(shop=shop)
    return render(request, 'listcostume_shop.html', {'costumes': costumes})

def deletecostume(request,id):
    costume=models.Costume.objects.get(id=id)
    costume.delete()
    # return HttpResponse("<script> alert('deteted successfully!'); window.location.href='/listcostumes_shop/'; </script>")
    return redirect('listcostumes_shop')


def editcostume(request,id):
    costume=models.Costume.objects.get(id=id)
    if request.method=='POST':
        costume.name=request.POST.get('name')
        costume.color=request.POST.get('color')
        costume.size=request.POST.get('size')
        costume.description=request.POST.get('description')
        costume.rate=request.POST.get('rate')
        image=request.FILES.get('image')
        if image:
            costume.image=image
        costume.save() 
        # return HttpResponse("<script> alert('Costumes Edited Successfully!'); window.location.href='/listcostumes_shop/'; </script>")
        return redirect('listcostumes_shop')
    else:
        return render(request,'editcostume.html',{'costume':costume}) 

def admincostumesview(request):
    costumes = (
        models.Costume.objects
        .prefetch_related('variants')
        .order_by('-id')
    )
    return render(request, 'admincostumesview.html', {'costumes': costumes})


def admindeletecostume(request,id):
    costume=models.Costume.objects.get(id=id)
    costume.delete()
    # return HttpResponse("<script> alert('Deleted Successfully!'); window.location.href='/admincostumesview/'; </script>")
    return redirect('admincostumesview')

def addtocart(request, id):

    if 'email' not in request.session:
        return redirect('login')

    user = get_object_or_404(models.Registration, email=request.session['email'])
    costume = get_object_or_404(models.Costume, id=id)

    if request.method == "POST":

        # STEP 2 → Final confirmation (quantity present)
        if "quantity" in request.POST:

            variant_id = request.POST.get("variant_id")
            quantity = request.POST.get("quantity")

            variant = get_object_or_404(models.CostumeVariant, id=variant_id)

            try:
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError
            except:
                messages.error(request, "Invalid quantity.")
                return redirect("costume_detail", id=id)

            if quantity > variant.quantity:
                messages.error(request, "Requested quantity exceeds stock.")
                return redirect("costume_detail", id=id)

            totalprice = costume.rate * quantity

            cart_item, created = models.Addtocart.objects.get_or_create(
                user=user,
                costume=costume,
                variant=variant,
                defaults={
                    "quantity": quantity,
                    "totalprice": totalprice
                }
            )

            if not created:
                cart_item.quantity += quantity
                cart_item.totalprice = cart_item.quantity * costume.rate
                cart_item.save()

            messages.success(request, "Item added to cart.")
            return redirect("cartlist")

        # STEP 1 → Coming from detail page
        else:
            variant_id = request.POST.get("variant_id")

            if not variant_id:
                messages.error(request, "Please select size and color.")
                return redirect("costume_detail", id=id)

            variant = get_object_or_404(models.CostumeVariant, id=variant_id)

            return render(request, "addtocart.html", {
                "costume": costume,
                "variant": variant
            })

    return redirect("costume_detail", id=id)
def cartlist(request):
    if 'email' not in request.session:
        return redirect('login')

    email = request.session['email']
    user = models.Registration.objects.get(email=email)

    cart_items = models.Addtocart.objects.filter(user=user).select_related('costume', 'variant')

    grand_total = sum(item.totalprice for item in cart_items)

    return render(request, 'cartlist.html', {
        'cart_items': cart_items,
        'grand_total': grand_total
    })
    
def removecart(request,id):
    cartitem=models.Addtocart.objects.get(id=id)
    cartitem.delete()
    # return HttpResponse("<script> alert('Removed Successfully!'); window.location.href='/cartlist/'; </script>")
    return redirect('cartlist')


from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.db import transaction
from django.db.models import F
import razorpay
from danceapp import models
import shortuuid

# ------------------- BUY NOW -------------------

def buynow(request, productid):

    if 'email' not in request.session:
        return redirect('login')

    user = get_object_or_404(models.Registration, email=request.session['email'])
    product = get_object_or_404(models.Costume, id=productid)

    if request.method == "POST":

        variant_id = request.POST.get("variant_id")

        if not variant_id:
            return redirect('costume_detail', id=productid)

        variant = get_object_or_404(
            models.CostumeVariant,
            id=variant_id,
            costume=product
        )

        if variant.quantity <= 0:
            return render(request, 'out_of_stock.html', {'product': product})

        # Delete any old pending order for this user+variant
        models.Buynow.objects.filter(
            user=user,
            product=product,
            variant=variant,
            status='pending'
        ).delete()

        # 🔥 Quantity always 1
        buynow_item = models.Buynow.objects.create(
            user=user,
            product=product,
            variant=variant,
            name=f"{product.name} ({variant.size}-{variant.color})",
            quantity=1,
            total_price=product.rate,
            status='pending',
            order_number=shortuuid.ShortUUID().random(length=10)
        )

        return render(request, 'successbuynow.html', {
            'user': user,
            'items': [buynow_item],
            'total': buynow_item.total_price,
            'id': productid
        })

    return redirect('listcostumes')

# ------------------- RAZORPAY PAYMENT VIEW -------------------
def payment_view(request, id=None):
    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        amount_paise = int(amount * 100)  # convert to paise

        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        razorpay_order = client.order.create({
            'amount': amount_paise,
            'currency': 'INR',
            'payment_capture': 1
        })

        request.session['latest_amount'] = amount

        context = {
            'amount': amount,
            'api_key': settings.RAZOR_KEY_ID,
            'order_id': razorpay_order['id'],
            'id': id
        }

        return render(request, 'razorpay_checkout.html', context)

    return redirect('home')


# ------------------- PAYMENT SUCCESS -------------------
@transaction.atomic
def payment_success(request, id=None):

    if 'email' not in request.session:
        return redirect('login')

    user = get_object_or_404(models.Registration, email=request.session['email'])

    # ---------------- SINGLE BUY ----------------
    if id is not None:

        item = models.Buynow.objects.filter(
            user=user,
            product_id=id,
            status='pending'
        ).first()

        if not item:
            return render(request, 'payment_error.html', {
                'error': 'Order not found'
            })

        if not item.variant:
            return render(request, 'payment_error.html', {
                'error': 'Variant missing for this order'
            })

        variant = item.variant
        if not item.variant:
            item.delete()
            return render(request, 'payment_error.html', {
                'error': 'Invalid order. Please try again.'
            })

        if variant.quantity < item.quantity:
            return render(request, 'payment_error.html', {
                'error': 'Insufficient stock'
            })

        # Safe stock deduction
        variant.quantity = F('quantity') - item.quantity
        variant.save()
        variant.refresh_from_db()

        item.status = 'dispatched'
        item.save()

        # Remove matching cart item
        models.Addtocart.objects.filter(
            user=user,
            costume=item.product,
            variant=variant
        ).delete()

    # ---------------- CART PAYMENT ----------------
    else:

        cart_items = models.Addtocart.objects.filter(user=user)

        if not cart_items.exists():
            return render(request, 'payment_error.html', {
                'error': 'Cart is empty'
            })

        for cart in cart_items:

            variant = cart.variant

            if not variant:
                return render(request, 'payment_error.html', {
                    'error': f'Variant missing for {cart.costume.name}'
                })

            if variant.quantity < cart.quantity:
                return render(request, 'payment_error.html', {
                    'error': f'Insufficient stock for {variant.size}-{variant.color}'
                })

            # Safe stock deduction
            variant.quantity = F('quantity') - cart.quantity
            variant.save()
            variant.refresh_from_db()

            # Update matching pending order
            order = models.Buynow.objects.filter(
                user=user,
                product=cart.costume,
                variant=variant,
                status='pending'
            ).first()

            if order:
                order.status = 'dispatched'
                order.save()

        cart_items.delete()

    return render(request, 'payment_success.html', {'user': user})

# ------------------- CART TO BUYNOW -------------------
def buynow_view(request):

    if 'email' not in request.session:
        return redirect('login')

    user = get_object_or_404(models.Registration, email=request.session['email'])
    cart_items = models.Addtocart.objects.filter(user=user)

    if not cart_items.exists():
        return redirect('cartlist')

    buynow_items = []

    for item in cart_items:

        existing = models.Buynow.objects.filter(
            user=user,
            product=item.costume,
            variant=item.variant,
            status='pending'
        ).first()

        if existing:
            existing.quantity = item.quantity
            existing.total_price = item.costume.rate * item.quantity
            existing.save()
            buynow_items.append(existing)
        else:
            new_item = models.Buynow.objects.create(
                user=user,
                product=item.costume,
                variant=item.variant,
                name=f"{item.costume.name} ({item.variant.size}-{item.variant.color})",
                quantity=item.quantity,
                total_price=item.costume.rate * item.quantity,
                status='pending',
                order_number=shortuuid.ShortUUID().random(length=10)
            )
            buynow_items.append(new_item)

    total = sum(i.total_price for i in buynow_items)

    return render(request, 'order_sucess.html', {
        'user': user,
        'items': buynow_items,
        'total': total
    })

# ------------------- USER ORDER LIST -------------------
from django.shortcuts import render, redirect, get_object_or_404
from danceapp import models

def user_order_list(request):
    if 'email' not in request.session:
        return redirect('login')

    user = get_object_or_404(
        models.Registration,
        email=request.session['email']
    )

    # Show only completed/confirmed orders
    orders = (
        models.Buynow.objects
        .filter(user=user)
        .exclude(status='pending')
        .select_related('product', 'variant')
        .order_by('-created_at')
    )

    return render(request, 'user_orders_list.html', {
        'orders': orders
    })

    
def singlebuy(request):
    return render(request,'successbuynow.html')


def out_of_stock(request):
    return render(request,'home.html')

def costume_detail(request, id):
    costume = get_object_or_404(
        models.Costume.objects.prefetch_related('variants'),
        id=id
    )

    return render(request, "costume_detail.html", {
        "costume": costume,
        "shop": costume.shop
    })



def shopowner_order(request):
    orders = models.Buynow.objects.all().order_by('-created_at')
    return render(request, 'admindeliverystatus.html', {'data': orders})



def dispatch(request, userid):
    order = models.Buynow.objects.get(id=userid)
    order.status = 'dispatched'
    order.save()
    return redirect('shopowner_order')

def outfordelivery(request, userid):
    order = models.Buynow.objects.get(id=userid)
    order.status = 'outfordelivery'
    order.save()
    return redirect('shopowner_order')

def deliver(request, userid):
    order = models.Buynow.objects.get(id=userid)
    order.status = 'delivered'
    order.save()
    return redirect('shopowner_order')

def cancel_delivery(request, userid):
    order = models.Buynow.objects.get(id=userid)
    order.status = 'cancelled'
    order.save()
    return redirect('shopowner_order')











def subscriptions(request, id):
    if 'email' not in request.session:
        return redirect('login')

    user = models.Registration.objects.get(email=request.session['email'])
    trainer = models.Trainer.objects.get(id=id)

    if request.method == 'POST':
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')

        start = datetime.strptime(startdate, "%Y-%m-%d").date()
        end = datetime.strptime(enddate, "%Y-%m-%d").date()

        if end <= start:
            messages.error(request, "Invalid date range")
            return redirect(request.path)

        days = (end - start).days
        price = days * 100

        subscription = models.Subscription.objects.create(
            trainer=trainer,
            user=user,
            startdate=start,
            enddate=end,
            price=price,
        )

        return redirect('subs_payment_view', subscription.id)

    return render(request, 'subscriptions.html', {'trainer': trainer})




def subs_payment_view(request, id):
    if 'email' not in request.session:
        return redirect('login')

    subscription = models.Subscription.objects.get(id=id)

    amount = subscription.price
    amount_paise = int(amount * 100)

    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

    razorpay_order = client.order.create({
        'amount': amount_paise,
        'currency': 'INR',
        'payment_capture': 1
    })

    context = {
        'amount': amount,
        'api_key': settings.RAZOR_KEY_ID,
        'order_id': razorpay_order['id'],
        'subscription_id': subscription.id,
        'user': subscription.user
    }

    return render(request, 'sub_razorpay_checkout.html', context)



def subs_payment_success(request, id):
    if 'email' not in request.session:
        return redirect('login')

    subscription = models.Subscription.objects.get(id=id)
    subscription.payment_status = 'Paid'
    subscription.save()

    return render(request, 'payment_success.html', {
        'user': subscription.user
    })



def buypackage(request, id):
    if 'email' not in request.session:
        return redirect('login')

    user = models.Registration.objects.get(email=request.session['email'])
    package = models.DancePackage.objects.get(id=id)

    pack = models.Buypackage.objects.create(
        package=package,
        trainer=package.trainer_id,
        user=user,
        fees=package.fees,
        duration=package.duration,
        type=package.type,
        package_name=package.package_name
    )
    pack.save()

    return redirect('pack_payment_view', pack.id)

    


def pack_payment_view(request, id):
    if 'email' not in request.session:
        return redirect('login')

    package = models.Buypackage.objects.get(id=id)

    amount = package.fees
    amount_paise = int(amount * 100)

    client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

    razorpay_order = client.order.create({
        'amount': amount_paise,
        'currency': 'INR',
        'payment_capture': 1
    })

    context = {
        'amount': amount,
        'api_key': settings.RAZOR_KEY_ID,
        'order_id': razorpay_order['id'],
        'package_id': package.id,
        'user': package.user
    }

    return render(request, 'pack_razorpay_checkout.html', context)



def pack_payment_success(request, id):
    if 'email' not in request.session:
        return redirect('login')

    package = models.Buypackage.objects.get(id=id)
    package.payment_status = 'Paid'
    package.save()

    return render(request, 'payment_success.html', {
        'user': package.user
    })


def subscriptionlist(request):
    trainer_id = request.session.get('trainer_id') 
    subscription = models.Subscription.objects.filter(trainer_id=trainer_id)
    return render(request,'subscriptionlist.html',{'events':subscription})


def registered_students_list(request):
    register = models.course_buynow.objects.select_related(
        'user',        
        'course',      
        'course__institution' 
    ).all()

    return render(request, 'registered_students_list.html', {'register': register})



def adminsubscriptionlist(request):
    subscription = models.Subscription.objects.all()
    return render(request,'adminsubscriptionlist.html',{'events':subscription})


from django.db.models import Q

# =========================
# CHAT LIST VIEW
# =========================
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import ChatMessage

def chat_list(request):
    sender_email = request.session.get('email')

    if not sender_email:
        return redirect('trainerlogin')

    # Identify logged-in user
    if models.Trainer.objects.filter(email=sender_email).exists():
        users = models.Registration.objects.all()
    elif models.Registration.objects.filter(email=sender_email).exists():
        users = models.Trainer.objects.all()
    else:
        return redirect('trainerlogin')

    chat_users = []

    for user in users:
        last_message = ChatMessage.objects.filter(
            Q(sender=sender_email, receiver=user.email) |
            Q(sender=user.email, receiver=sender_email)
        ).order_by('-timestamp').first()

        unread_count = ChatMessage.objects.filter(
            sender=user.email,
            receiver=sender_email,
            is_read=False
        ).count()

        chat_users.append({
            'user': user,
            'last_message': last_message,
            'unread_count': unread_count
        })

    return render(request, 'chat_list.html', {
        'chat_users': chat_users
    })



# =========================
# CHAT DETAIL VIEW
# =========================
from django.db.models import Q

def chat_detail(request, user_email):
    sender_email = request.session.get('email')

    if not sender_email:
        return redirect('tainerlogin')

    # Identify sender
    sender = (
        models.Registration.objects.filter(email=sender_email).first()
        or models.Trainer.objects.filter(email=sender_email).first()
    )

    receiver = (
        models.Trainer.objects.filter(email=user_email).first()
        or models.Registration.objects.filter(email=user_email).first()
    )

    if not sender or not receiver:
        return redirect('chat_list')

    messages = ChatMessage.objects.filter(
        Q(sender=sender.email, receiver=receiver.email) |
        Q(sender=receiver.email, receiver=sender.email)
    ).order_by('timestamp')

    # ✅ Mark unread messages as read
    ChatMessage.objects.filter(
        sender=receiver.email,
        receiver=sender.email,
        is_read=False
    ).update(is_read=True)

    # Media type detection
    for msg in messages:
        if msg.media:
            name = msg.media.name.lower()
            if name.endswith(('.jpg', '.jpeg', '.png')):
                msg.media_type = 'image'
            elif name.endswith(('.mp4', '.avi', '.mov')):
                msg.media_type = 'video'
            else:
                msg.media_type = 'file'

    if request.method == 'POST':
        content = request.POST.get('content', '')
        media = request.FILES.get('media')

        if content.strip() or media:
            ChatMessage.objects.create(
                sender=sender.email,
                receiver=receiver.email,
                content=content,
                media=media
            )

        return redirect('chat_detail', user_email=receiver.email)

    return render(request, 'chat_detail.html', {
        'sender': sender,
        'receiver': receiver,
        'messages': messages
    })



from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from .models import Media, VideoLike, VideoComment, Trainer
from django.views.decorators.csrf import csrf_exempt

def upload(request):
    if 'email' not in request.session:
        return HttpResponse("<script>alert('You must login');window.location.href='/login/';</script>")
    
    user_email = request.session['email']
    try:
        user = Trainer.objects.get(email=user_email)
    except Trainer.DoesNotExist:
        return HttpResponse("<script>alert('User not found');window.location.href='/trainerlogin/';</script>")

    if request.method == 'POST':
        name = request.POST.get('name')
        mediatypes = request.POST.get('mediatype')
        categories = request.POST.get('category')
        # language = request.POST.get('language')
        description = request.POST.get('description')
        media_file = request.FILES.get('media')

        Media.objects.create(
            user_name=user.name,
            user_email=user.email,
            name=name,
            mediatypes=mediatypes,
            categories=categories,
            # language=language,
            description=description,
            mediapath=media_file,
            created_at=timezone.now()
        )
        # return HttpResponse("<script> alert('Uploaded Successfully!'); window.location.href='/my_uploads/'; </script>")
        return redirect('my_uploads')

    return render(request, 'upload.html')

def my_uploads(request):
    if 'email' not in request.session:
        return HttpResponse("<script>alert('You must login');window.location.href='/login/';</script>")

    user_email = request.session['email']
    uploaded_media = Media.objects.filter(user_email=user_email).order_by('-created_at')
    return render(request, 'my_uploads.html', {'media_list': uploaded_media})

@csrf_exempt
def like_video(request, video_id):
    if 'email' not in request.session:
        return JsonResponse({"status": "login_required"})
    user_email = request.session['email']
    video = get_object_or_404(Media, id=video_id)
    like = VideoLike.objects.filter(video=video, user_email=user_email)
    if like.exists():
        like.delete()
        return JsonResponse({"status": "unliked"})
    else:
        VideoLike.objects.create(video=video, user_email=user_email)
        return JsonResponse({"status": "liked"})

def comment_video(request, video_id):
    if request.method == "POST":
        if 'email' not in request.session:
            return redirect('login')
        video = get_object_or_404(Media, id=video_id)
        comment_text = request.POST.get('comment')
        if comment_text.strip():
            VideoComment.objects.create(
                video=video,
                user_email=request.session['email'],
                username=request.session.get('name', 'User'),
                comment=comment_text
            )
        return redirect('video_view')
    return redirect('video_view')


import os
from django.shortcuts import render, redirect
from .models import Media

def video_view(request):

    trainer_email = request.session.get("email")

    if not trainer_email:
        return redirect("trainerlogin")  # change if needed

    category_filter = request.GET.get('category', '')
    language_filter = request.GET.get('language', '')

    # 🔥 Filter using user_email
    videos = Media.objects.filter(user_email=trainer_email)

    if category_filter:
        videos = videos.filter(categories=category_filter)

    if language_filter:
        videos = videos.filter(language=language_filter)

    # Detect media type
    for v in videos:
        ext = os.path.splitext(v.mediapath.name)[1].lower()

        if ext in ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv']:
            v.media_type = "video"
        elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
            v.media_type = "image"
        elif ext in ['.mp3', '.wav', '.aac', '.ogg', '.m4a']:
            v.media_type = "audio"
        else:
            v.media_type = "other"

    return render(request, 'video_view.html', {
        'videos': videos,
        'category_filter': category_filter,
        'language_filter': language_filter,
    })

def delete_video(request, video_id):
    if 'email' not in request.session:
        return redirect('login')
    video = get_object_or_404(Media, id=video_id)
    if video.user_email != request.session['email']:
        return HttpResponse("<script>alert('Not allowed');window.location.href='/my_uploads/';</script>")
    video.delete()
    return redirect('my_uploads')


def medialistuser(request):
    listuser=models.Media.objects.all().order_by('-created_at')
    return render(request, 'medialistuser.html', {'item':listuser})  

def medialistadmin(request):
    listadmin=models.Media.objects.all().order_by('-created_at')
    return render(request, 'medialistadmin.html', {'listadmin':listadmin})
      
def approve(request,id):
    medialist=models.Media.objects.get(id=id)
    medialist.isapproved = True
    medialist.isrejected = False
    medialist.save()
    return redirect('medialistadmin')

def rejected(request,id):
    medialist=models.Media.objects.get(id=id)
    medialist.isapproved = False
    medialist.isrejected = True
    medialist.save()
    return redirect('medialistadmin')


def trainerfeedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        ratings=request.POST.get('ratings')
        fdbck=models.Trainerfeedback(name=name,email=email,message=message,ratings=ratings)
        fdbck.save()
        return redirect('home')
    user=models.Registration.objects.get(email=request.session.get('email'))
    return render(request,'trainerfeedback.html',{'user':user})





def listTrainer(request):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        institution = models.DanceInstitution.objects.get(email=email)
    except models.DanceInstitution.DoesNotExist:
        return redirect('institutionlogin')

    trainer=models.Institution_AddTrainer.objects.filter(institution=institution)
    return render(request,'listTrainer.html',{'trainer':trainer}) 

def add_trainer(request):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        institution = models.DanceInstitution.objects.get(email=email)
    except models.DanceInstitution.DoesNotExist:
        return redirect('institutionlogin')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        trainer_email = request.POST.get('email')
        dance_styles = request.POST.get('dance_styles')
        years_of_experience = request.POST.get('years_of_experience')
        teaching_experience = request.POST.get('teaching_experience')
        trainer_type = request.POST.get('trainer_type')
        is_active = True if request.POST.get('is_active') else False

        photo = request.FILES.get('photo')
        portfolio = request.FILES.get('portfolio') 
       
        models.Institution_AddTrainer.objects.create(
            institution=institution,
            full_name=full_name,
            gender=gender,
            phone_number=phone_number,
            email=trainer_email,
            photo=photo,
            dance_styles=dance_styles,
            years_of_experience=years_of_experience,
            teaching_experience=teaching_experience,
            trainer_type=trainer_type,
            portfolio=portfolio,
            is_active=is_active,
        )

        return HttpResponse(
            "<script>"
            "alert('Trainer Added Successfully!');"
            "window.location.href='/listTrainer/';"
            "</script>"
        )

    return render(request, 'add_trainer.html')


def edit_trainer(request, trainer_id):
    try:
        trainer = models.Institution_AddTrainer.objects.get(id=trainer_id)
    except models.Institution_AddTrainer.DoesNotExist:
        return HttpResponse(
            "<script>"
            "alert('Trainer not found!');"
            "window.location.href='/listTrainer/';"
            "</script>"
        )

    if request.method == 'POST':
        trainer.full_name = request.POST.get('full_name')
        trainer.gender = request.POST.get('gender')
        trainer.phone_number = request.POST.get('phone_number')
        trainer.email = request.POST.get('email')
        trainer.dance_styles = request.POST.get('dance_styles')
        trainer.years_of_experience = request.POST.get('years_of_experience')
        trainer.teaching_experience = request.POST.get('teaching_experience')
        trainer.trainer_type = request.POST.get('trainer_type')
        trainer.is_active = True if request.POST.get('is_active') else False

        if 'photo' in request.FILES:
            trainer.photo = request.FILES['photo']
        if 'portfolio' in request.FILES:
            trainer.portfolio = request.FILES['portfolio']
        
        trainer.save()

        return HttpResponse(
            f"<script>"
            f"alert('Trainer \"{trainer.full_name}\" updated successfully!');"
            "window.location.href='/listTrainer/';"
            "</script>"
        )

    return render(request, 'edit_trainer.html', {'trainer': trainer})


def delete_trainer(request, trainer_id):
    try:
        trainer = models.Institution_AddTrainer.objects.get(id=trainer_id)
        trainer_name = trainer.full_name
        trainer.delete()
        return HttpResponse(
            f"<script>"
            f"alert('Trainer \"{trainer_name}\" deleted successfully!');"
            "window.location.href='/listTrainer/';"
            "</script>"
        )
    except models.Institution_AddTrainer.DoesNotExist:
        return HttpResponse(
            "<script>"
            "alert('Trainer not found!');"
            "window.location.href='/listTrainer/';"
            "</script>"
        )


def add_class(request, course_id):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    institution = models.DanceInstitution.objects.filter(email=email).first()
    if not institution:
        return redirect('institutionlogin')

    course = models.DanceCourse.objects.filter(
        id=course_id,
        institution=institution
    ).first()

    if not course:
        messages.error(request, "Course not found.")
        return redirect('list_courses')

    trainers = models.Institution_AddTrainer.objects.filter(
        institution=institution,
        is_active=True
    )

    if request.method == 'POST':
        trainer_id = request.POST.get('trainer')
        trainer = trainers.filter(id=trainer_id).first()

        models.DanceClass.objects.create(
            institution=institution,
            course=course,         
            trainer=trainer,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            dance_style=request.POST.get('dance_style') or None,
            uploaded_video=request.FILES.get('uploaded_video')
        )

        messages.success(request, "Dance Class Added Successfully!")
        return redirect('list_class', course_id=course.id)

    return render(request, 'add_class.html', {
        'course': course,
        'trainers': trainers
    })


def list_class(request, course_id):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    institution = models.DanceInstitution.objects.filter(
        email=email
    ).first()

    if not institution:
        return redirect('institutionlogin')

    course = models.DanceCourse.objects.filter(
        id=course_id,
        institution=institution,
        status__in=['UP', 'CO']
    ).first()

    if not course:
        return redirect('list_courses')  

    classes = models.DanceClass.objects.filter(
        course=course
    ).order_by('-created_at')

    return render(request, 'list_class.html', {
        'course': course,
        'classes': classes
    })

def edit_class(request, id):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    institution = models.DanceInstitution.objects.filter(email=email).first()
    if not institution:
        return redirect('institutionlogin')

    dance_class = models.DanceClass.objects.filter(
        id=id,
        institution=institution
    ).first()

    if not dance_class:
        messages.error(request, "Dance Class not found.")
        return redirect('list_courses')

    trainers = models.Institution_AddTrainer.objects.filter(
        institution=institution,
        is_active=True
    )

    if request.method == 'POST':
        dance_class.name = request.POST.get('name')
        dance_class.description = request.POST.get('description')
        dance_class.dance_style = request.POST.get('dance_style') or None

        trainer_id = request.POST.get('trainer')
        dance_class.trainer = trainers.filter(id=trainer_id).first()

        if request.FILES.get('uploaded_video'):
            dance_class.uploaded_video = request.FILES['uploaded_video']

        dance_class.save()
        messages.success(request, "Dance Class Updated Successfully!")

        return redirect('list_class', course_id=dance_class.course.id)

    return render(request, 'edit_class.html', {
        'dance_class': dance_class,
        'trainers': trainers
    })


def delete_class(request, id):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    institution = models.DanceInstitution.objects.filter(email=email).first()
    if not institution:
        return redirect('institutionlogin')

    dance_class = models.DanceClass.objects.filter(id=id, institution=institution).first()
    if not dance_class:
        messages.error(request, "Dance Class not found.")
        return redirect('list_courses')

    course_id = dance_class.course.id  

    dance_class.delete()
    messages.success(request, "Dance Class Deleted Successfully!")
    return redirect('list_class', course_id=course_id)


# ---------------- Institution: Add Event ----------------
def add_event(request):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        institution = models.DanceInstitution.objects.get(email=email)
    except models.DanceInstitution.DoesNotExist:
        return redirect('institutionlogin')

    trainers = models.Institution_AddTrainer.objects.filter(
        institution=institution, is_active=True
    )
    venues = models.Venue.objects.filter(institution=institution)

    if request.method == 'POST':
        trainer = None
        trainer_id = request.POST.get('trainer')
        if trainer_id:
            trainer = trainers.filter(id=trainer_id).first()

        venue = None
        venue_id = request.POST.get('venue')
        if venue_id:
            venue = venues.filter(id=venue_id).first()

        event = models.InstitutionEvent.objects.create(
            institution=institution,
            trainer=trainer,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            trainer_position=request.POST.get('trainer_position'),
            date=request.POST.get('date'),
            start_time=request.POST.get('start_time'),
            end_time=request.POST.get('end_time') or None,
            location=request.POST.get('location'),
            poster=request.FILES.get('poster'),
            status=request.POST.get('status') or 'UP',
            age_category=request.POST.get('age_category'),
            priceperperson=request.POST.get('priceperperson'),
            venue=venue
        )

        messages.success(request, "Event added successfully!")
        return redirect('institution_events')

    return render(request, 'add_event.html', {
        'trainers': trainers,
        'venues': venues
    })


# ---------------- Institution: List Events ----------------
def institution_events(request):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        institution = models.DanceInstitution.objects.get(email=email)
    except models.DanceInstitution.DoesNotExist:
        return redirect('institutionlogin')

    events = models.InstitutionEvent.objects.filter(
        institution=institution
    ).order_by('-date', '-start_time')

    return render(request, 'institution_events.html', {
        'events': events
    })


# ---------------- Institution: Edit Event ----------------
def edit_event(request, id):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        event = models.InstitutionEvent.objects.get(
            id=id,
            institution__email=email
        )
    except models.InstitutionEvent.DoesNotExist:
        messages.error(request, "Event not found or not authorized.")
        return redirect('institution_events')

    trainers = models.Institution_AddTrainer.objects.filter(
        institution=event.institution, is_active=True
    )
    venues = models.Venue.objects.filter(institution=event.institution)

    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        event.trainer_position = request.POST.get('trainer_position')
        event.date = request.POST.get('date')
        event.location = request.POST.get('location')
        event.status = request.POST.get('status') or 'UP'
        event.age_category = request.POST.get('age_category')
        event.priceperperson = request.POST.get('priceperperson')

        # ✅ FIX: handle empty time fields
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        event.start_time = start_time if start_time else None
        event.end_time = end_time if end_time else None

        # Trainer
        trainer_id = request.POST.get('trainer')
        event.trainer = trainers.filter(id=trainer_id).first() if trainer_id else None

        # Venue
        venue_id = request.POST.get('venue')
        event.venue = venues.filter(id=venue_id).first() if venue_id else None

        # Poster
        if request.FILES.get('poster'):
            event.poster = request.FILES.get('poster')

        event.save()
        messages.success(request, "Event updated successfully!")
        return redirect('institution_events')

    return render(request, 'edit_event.html', {
        'event': event,
        'trainers': trainers,
        'venues': venues,
        'status_choices': models.InstitutionEvent.STATUS_CHOICES
    })


# ---------------- Institution: Delete Event ----------------
def delete_event(request, id):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        institution = models.DanceInstitution.objects.get(email=email)
    except models.DanceInstitution.DoesNotExist:
        return redirect('institutionlogin')

    try:
        event = models.InstitutionEvent.objects.get(
            id=id,
            institution=institution
        )
    except models.InstitutionEvent.DoesNotExist:
        messages.error(request, "Event not found or not authorized.")
        return redirect('institution_events')

    event.delete()
    messages.success(request, "Event deleted successfully.")
    return redirect('institution_events')




def add_course(request):
    trainers = models.Institution_AddTrainer.objects.filter(is_active=True)
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        institution = models.DanceInstitution.objects.get(email=email)
    except models.DanceInstitution.DoesNotExist:
        return redirect('institutionlogin')

    if request.method == "POST":
        course_name = request.POST.get('course_name')
        description = request.POST.get('description')
        course_type = request.POST.get('course_type')
        duration_in_weeks = request.POST.get('duration_in_weeks')
        schedule = request.POST.get('schedule')
        number_of_classes = request.POST.get('number_of_classes')
        tutor_id = request.POST.get('tutor')
        fees_per_head = request.POST.get('fees_per_head')
        extra_details = request.POST.get('extra_details')
        poster = request.FILES.get('poster')

        tutor = None
        if tutor_id:
            tutor = models.Institution_AddTrainer.objects.filter(id=tutor_id, is_active=True).first()

        course = models.DanceCourse.objects.create(
            course_name=course_name,
            description=description,
            course_type=course_type,
            duration_in_weeks=duration_in_weeks,
            schedule=schedule,
            number_of_classes=number_of_classes,
            tutor=tutor,
            fees_per_head=fees_per_head,
            extra_details=extra_details,
            poster=poster,
            institution=institution  
        )
        messages.success(request, f"Course '{course.course_name}' added successfully!")
        return redirect('list_courses')

    return render(request, 'add_course.html', {'trainers': trainers})


def list_courses(request):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        institution = models.DanceInstitution.objects.get(email=email)
    except models.DanceInstitution.DoesNotExist:
        return redirect('institutionlogin')

    courses  = models.DanceCourse.objects.filter(
        institution=institution
    ).order_by('-created_at')

    return render(request, 'list_courses.html', {
        'courses': courses 
    })


def delete_course(request, id):
    try:
        course = models.DanceCourse.objects.get(id=id)
    except models.DanceCourse.DoesNotExist:
        messages.error(request, "Course not found.")
        return redirect('list_courses')

    course.delete()
    messages.success(request, "Course deleted successfully.")
    return redirect('list_courses')


def edit_course(request, id):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')

    try:
        institution = models.DanceInstitution.objects.get(email=email)
        course = models.DanceCourse.objects.get(id=id, institution=institution)
    except (models.DanceInstitution.DoesNotExist, models.DanceCourse.DoesNotExist):
        return redirect('list_courses')

    trainers = models.Institution_AddTrainer.objects.filter(institution=institution)

    if request.method == 'POST':
        course.course_name = request.POST.get('course_name')
        course.description = request.POST.get('description')
        course.course_type = request.POST.get('course_type')
        course.duration_in_weeks = request.POST.get('duration')
        course.schedule = request.POST.get('schedule')
        course.number_of_classes = request.POST.get('num_classes')
        course.fees_per_head = request.POST.get('fees_per_head')
        course.extra_details = request.POST.get('other_details')

        trainer_id = request.POST.get('tutor')
        course.tutor = trainers.filter(id=trainer_id).first() if trainer_id else None

        if request.FILES.get('image'):
            course.poster = request.FILES.get('image')

        course.save()
        # return HttpResponse("<script> alert('Course Updated Sucessfully!'); window.location.href='/list_courses/'; </script>")
        return redirect('list_courses')
    return render(request, 'edit_course.html', {
        'course': course,
        'trainers': trainers
    })

def user_list_institution(request):
    institution=models.DanceInstitution.objects.all()
    return render(request,'user_list_institution.html',{'institution':institution})


def institution_courses(request, id):
    try:
        institution = models.DanceInstitution.objects.get(id=id)
    except models.DanceInstitution.DoesNotExist:
        messages.error(request, "Institution not found.")
        return redirect('user_list_institution')

    courses = models.DanceCourse.objects.filter(institution=institution)

    booked_course_ids = []
    if 'email' in request.session:
        try:
            user = models.Registration.objects.get(email=request.session['email'])
            booked_course_ids = models.course_buynow.objects.filter(
                user=user,
                course__in=courses,
                payment_status='Success'
            ).values_list('course_id', flat=True)
        except models.Registration.DoesNotExist:
            booked_course_ids = []

    return render(request, 'institution_courses.html', {
        'institution': institution,
        'courses': courses,
        'booked_course_ids': booked_course_ids
    })



def course_buynow(request, courseid):
    if 'email' not in request.session:
        return redirect('login')

    try:
        course = models.DanceCourse.objects.get(id=courseid)  # get course first
    except models.DanceCourse.DoesNotExist:
        # If course doesn't exist, redirect to institution list
        return redirect('user_list_institution')

    try:
        user = models.Registration.objects.get(email=request.session['email'])

        # Check if course is out of stock
        if course.number_of_classes <= 0:
            return render(request, 'course_out_of_stock.html', {'course': course})

        # Check if this course is already in buynow table for this user
        existing_entry = models.course_buynow.objects.filter(
            user=user, course=course, payment_status='Pending'
        ).first()

        if existing_entry:
            # Update quantity
            existing_entry.quantity = 1
            existing_entry.total_price = course.fees_per_head
            existing_entry.save()
            buynow_item = existing_entry
        else:
            # Create new entry in buynow
            buynow_item = models.course_buynow.objects.create(
                user=user,
                course=course,
                quantity=1,
                total_price=course.fees_per_head
            )

        total = buynow_item.total_price

        return render(request, 'course_single_order_sucess.html', {
            'user': user,
            'items': [buynow_item],
            'total': total,
            'id': courseid,
        })

    except models.Registration.DoesNotExist:
        return redirect('login')
    except Exception as e:
        print("Error in course_single_buynow:", e)
        # Redirect to institution's courses
        return redirect('institution_courses', id=course.institution.id)

    
def course_single_order_sucess(request):
    return render(request,'course_single_order_sucess.html')

def course_out_of_stock(request):
    return render(request,'course_out_of_stock.html')

def course_payment_error(request):
     return render(request,'course_payment_error.html')

import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

def course_payment_view(request, id=None):
    if request.method == 'POST':
        price = request.POST.get('price')

        try:
            amount = float(price)
        except:
            amount = 0

        if amount < 1:
            return render(request, 'course_payment_error.html', {
                'error': 'Invalid payment amount'
            })

        amount_paise = int(amount * 100)

        client = razorpay.Client(
            auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
        )

        razorpay_order = client.order.create({
            'amount': amount_paise,
            'currency': 'INR',
            'payment_capture': 1
        })

        user = models.Registration.objects.get(email=request.session['email'])

        context = {
            'amount': amount,
            'api_key': settings.RAZOR_KEY_ID,
            'order_id': razorpay_order['id'],
            'id': id,
            'user': user
        }

        return render(request, 'course_razorpay_checkout.html', context)

    return redirect('user_list_institution')


from django.shortcuts import render, redirect
from . import models
from django.conf import settings
from django.core.mail import send_mail

def course_payment_success_view(request, id=None):
    # User must be logged in
    if 'email' not in request.session:
        return redirect('login')

    try:
        user = models.Registration.objects.get(email=request.session['email'])

        # Single room buy now only
        if id is None:
            return render(request, 'course_payment_error.html', {
                'user': user,
                'error': "Invalid payment request."
            })

        # Get room
        try:
            course = models.DanceCourse.objects.get(id=id)
            item = models.course_buynow.objects.get(
                user=user,
                course=course,
                payment_status='Pending'
            )
        except models.DanceCourse.DoesNotExist:
            return render(request, 'course_payment_error.html', {
                'user': user,
                'error': "kit not found."
            })
        except models.course_buynow.DoesNotExist:
            return render(request, 'course_payment_error.html', {
                'user': user,
                'error': "Order already completed or not found."
            })

        # Stock check
        if course.number_of_classes < item.quantity:
            return render(request, 'swabkit_payment_error.html', {
                'user': user,
                'error': f"Insufficient stock for {course.course_name}"
            })

        # Reduce stock
        course.number_of_classes -= item.quantity
        course.save()

        # Mark payment success
        item.payment_status = 'Success'
        item.save()

        # Send out-of-stock mail if needed
        if course.number_of_classes <= 0:
            send_mail(
                subject='🔔 kit Out of Stock Alert',
                message=(
                    f'Dear Admin,\n\n'
                    f'The following room is now out of stock:\n\n'
                    f'🏨 Room Type: {course.course_name}\n'
                    f'🏨 Hotel: {course.course_name}\n\n'
                    f'Please update availability.\n\n'
                    f'Thank you.'
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['grapesgenixpython2025@example.com'],
                fail_silently=False,
            )

        return render(request, 'course_payment_success.html', {'user': user})

    except models.Registration.DoesNotExist:
     
        return redirect('login')

    except Exception as e:
        return render(request, 'course_payment_error.html', {
            'user': None,
            'error': f"Payment processing error: {str(e)}"
        })

def course_classes(request, id):
    course_list = models.DanceCourse.objects.filter(id=id)
    if not course_list.exists():
        messages.error(request, "Course not found.")
        return redirect('user_list_institution')

    course = course_list.first()
    classes = models.DanceClass.objects.filter(course=course)

    return render(request, 'course_classes.html', {
        'course': course,
        'classes': classes
    })

def studentslist(request):
    students=models.course_buynow.objects.all()
    return render(request,'studentslist.html',{'students':students})


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib import messages
from . import models


def add_reels(request):
    if 'email' not in request.session:
        return HttpResponse("<script>alert('Login required');window.location='/institutionlogin/';</script>")

    try:
        user = models.DanceInstitution.objects.get(email=request.session['email'])
    except models.DanceInstitution.DoesNotExist:
        return HttpResponse("<script>alert('User not found');window.location='/institutionlogin/';</script>")

    if request.method == "POST":
        models.Reels.objects.create(
            user_name=user.owner_name,
            user_email=user.email,
            name=request.POST.get('name'),
            mediatypes=request.POST.get('mediatype'),
            categories=request.POST.get('category'),
            # language=request.POST.get('language'),
            description=request.POST.get('description'),
            mediapath=request.FILES.get('media'),
            created_at=timezone.now()
        )
        # return HttpResponse("<script> alert('Reels Added Successfully!'); window.location.href='/institute_my_reels/'; </script>")
        return redirect('institute_my_reels')
    return render(request, 'add_reels.html')


def institute_my_reels(request):
    if 'email' not in request.session:
        return redirect('institutionlogin')

    media_list = models.Reels.objects.filter(
        user_email=request.session['email']
    ).order_by('-created_at')

    return render(request, 'institute_my_reels.html', {'media_list': media_list})

def reels_view(request):
    reels_videos = models.Reels.objects.prefetch_related(
        'reelslike_set', 'reelscomment_set'
    ).all().order_by('-created_at')

    media_videos = models.Media.objects.prefetch_related(
        'videolike_set', 'videocomment_set'
    ).order_by('-created_at')

    user_reels_videos = models.UserReels.objects.prefetch_related(
        'userreelslike_set', 'userreelscomment_set'
    ).order_by('-created_at')

    videos = sorted(
        list(reels_videos) + list(media_videos) + list(user_reels_videos),
        key=lambda x: x.created_at,
        reverse=True
    )

    return render(request, 'reels_view.html', {'videos': videos})




def like_reels(request, video_id):
    email = request.session.get('email')
    if not email:
        return JsonResponse({'status': 'login_required'})

    reel = get_object_or_404(models.Reels, id=video_id)

    like_obj, created = models.ReelsLike.objects.get_or_create(
        video=reel,
        user_email=email
    )

    if not created:
        like_obj.delete()

    new_count = models.ReelsLike.objects.filter(video=reel).count()
    return JsonResponse({'status': 'ok', 'new_like_count': new_count})


def like_media(request, video_id):
    email = request.session.get('email')
    if not email:
        return JsonResponse({'status': 'login_required'})

    media = get_object_or_404(models.Media, id=video_id)

    like_obj, created = models.VideoLike.objects.get_or_create(
        video=media,
        user_email=email
    )

    if not created:
        like_obj.delete()

    new_count = models.VideoLike.objects.filter(video=media).count()
    return JsonResponse({'status': 'ok', 'new_like_count': new_count})


def like_userreels(request, video_id):
    email = request.session.get('email')
    if not email:
        return JsonResponse({'status': 'login_required'})

    userreel = get_object_or_404(models.UserReels, id=video_id)

    like_obj, created = models.UserReelsLike.objects.get_or_create(
        video=userreel,
        user_email=email
    )

    if not created:
        like_obj.delete()

    new_count = models.UserReelsLike.objects.filter(video=userreel).count()
    return JsonResponse({'status': 'ok', 'new_like_count': new_count})


def comment_reels(request, video_id):
    email = request.session.get('email')
    if not email:
        return JsonResponse({'status': 'login_required'})

    comment_text = request.POST.get('comment', '').strip()
    if not comment_text:
        return JsonResponse({'status': 'error', 'message': 'Comment cannot be empty'})

    reel = get_object_or_404(models.Reels, id=video_id)

    comment = models.ReelsComment.objects.create(
        video=reel,
        user_email=email,
        username=email.split('@')[0],  # or store username in session
        comment=comment_text
    )

    return JsonResponse({
        'status': 'ok',
        'comment': comment.comment,
        'username': comment.username
    })


def comment_media(request, video_id):
    email = request.session.get('email')
    if not email:
        return JsonResponse({'status': 'login_required'})

    comment_text = request.POST.get('comment', '').strip()
    if not comment_text:
        return JsonResponse({'status': 'error', 'message': 'Comment cannot be empty'})

    media = get_object_or_404(models.Media, id=video_id)

    comment = models.VideoComment.objects.create(
        video=media,
        user_email=email,
        username=email.split('@')[0],  # or session username
        comment=comment_text
    )

    return JsonResponse({
        'status': 'ok',
        'comment': comment.comment,
        'username': comment.username
    })

def comment_userreels(request, video_id):
    email = request.session.get('email')
    if not email:
        return JsonResponse({'status': 'login_required'})

    comment_text = request.POST.get('comment', '').strip()
    if not comment_text:
        return JsonResponse({'status': 'error', 'message': 'Comment cannot be empty'})

    userreel = get_object_or_404(models.UserReels, id=video_id)

    comment = models.UserReelsComment.objects.create(
        video=userreel,
        user_email=email,
        username=email.split('@')[0],  # or store username in session
        comment=comment_text
    )

    return JsonResponse({
        'status': 'ok',
        'comment': comment.comment,
        'username': comment.username
    })

def delete_reels(request, id):
    if 'email' not in request.session:
        messages.error(request, "You must be logged in to delete media.")
        return redirect('institutionlogin')
    try:
        media = models.Reels.objects.get(id=id, user_email=request.session['email'])
        media.delete()
        messages.success(request, "Media deleted successfully.")
    except models.Reels.DoesNotExist:
        messages.error(request, "Media not found or you do not have permission to delete it.")

    return redirect('institute_my_reels')


 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Venue, InstitutionEvent, DanceInstitution
from datetime import date
import json

# Agency Venue List View
def venue_list(request):
    if 'email' not in request.session:
        return redirect('institutionlogin')
    institution = get_object_or_404(DanceInstitution, email=request.session['email'])
    venues = Venue.objects.filter(institution=institution)
    return render(request, 'venue_list.html', {'venues': venues})

# Add Venue View
def add_venue(request):
    if 'email' not in request.session:
        return redirect('institutionlogin')
    institution = get_object_or_404(DanceInstitution, email=request.session['email'])
    if request.method == 'POST':
        name = request.POST.get('name')
        total_seats = int(request.POST.get('total_seats') or 0)
        seat_layout_raw = request.POST.get('seat_layout')  # Comma-separated, e.g., "AB1,GK2"
        seat_layout = [s.strip() for s in seat_layout_raw.split(',')] if seat_layout_raw else []
        
        if len(seat_layout) != total_seats:
            return HttpResponse("<script>alert('Seat count mismatch!'); history.back();</script>")
        
        venue = Venue(institution=institution, name=name, total_seats=total_seats, seat_layout=seat_layout)
        venue.save()
        # return HttpResponse("<script> alert('Venue Added Successfully!'); window.location.href='/venue_list/'; </script>")
        return redirect('venue_list')
    return render(request, 'add_venue.html')

# Edit Venue View (similar to add, with pre-fill)
def edit_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if venue.institution.email != request.session.get('email'):
        return redirect('institutionhome')
    if request.method == 'POST':
        venue.name = request.POST.get('name')
        total_seats = int(request.POST.get('total_seats') or 0)
        seat_layout_raw = request.POST.get('seat_layout')
        venue.seat_layout = [s.strip() for s in seat_layout_raw.split(',')] if seat_layout_raw else []
        venue.total_seats = total_seats
        venue.save()
        # return HttpResponse("<script> alert('Venue Updated Successfully!'); window.location.href='/venue_list/'; </script>")
        return redirect('venue_list')
    return render(request, 'edit_venue.html', {'venue': venue})

def delete_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    if venue.institution.email != request.session.get('email'):
        return redirect('institutionhome')
    venue.delete()
    # return HttpResponse("<script> alert('Venue Deleted Successfully!'); window.location.href='/venue_list/'; </script>")
    return redirect('venue_list')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
import razorpay
import traceback

# --------------------------
# Register for Event
# --------------------------
def register_event(request, id):
    if 'email' not in request.session:
        messages.error(request, "Please login first")
        return redirect('login')

    user = get_object_or_404(models.Registration, email=request.session['email'])
    event = get_object_or_404(models.InstitutionEvent, id=id)

    booking, created = models.Booking.objects.get_or_create(
        event=event,
        user=user,
        defaults={'status': 'pending'}
    )

    if request.method == 'POST':
        messages.success(request, "Booking is pending! You can now select seats.")
        return redirect('register_event', id=event.id)

    return render(request, 'register_event.html', {
        'event': event,
        'user': user,
        'booking': booking,
        'age_category': event.age_category
    })

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

# --------------------------
# Seat Selection Page
# --------------------------
def user_seat_selection(request, booking_id):
    if 'email' not in request.session:
        return redirect('login')

    booking = get_object_or_404(
        models.Booking,
        id=booking_id,
        user__email=request.session['email']
    )

    event = booking.event
    venue = event.venue

    if request.method == 'POST':
        try:
            raw_seats = request.POST.get('selected_seats')
            selected_seats = json.loads(raw_seats) if raw_seats else []

            num_seats = len(selected_seats)
            price_per_person = event.totalprice or event.priceperperson or 0
            total_amount = num_seats * price_per_person

            booking.seats = selected_seats
            booking.numberofpeople = num_seats
            booking.totalamount = total_amount

            razorpay_payment_id = request.POST.get('razorpay_payment_id')
            if razorpay_payment_id:
                booking.status = 'confirmed'

                # Lock seats
                for seat in selected_seats:
                    event.booked_venue[seat] = True

                event.save()
                booking.save()

                # Send Confirmation Email
                try:
                    subject = f"Booking Confirmed – {event.name}"

                    html_content = f"""
                    <html>
                    <body style="font-family:Arial,sans-serif;background:#f4f4f4;padding:20px;">
                        <div style="max-width:600px;margin:auto;background:white;padding:20px;border-radius:10px;">
                            <h2 style="color:#3f7fff;">🎟 Event Booking Confirmed</h2>
                            <p>Dear {booking.user.username},</p>
                            <p>Your booking for <strong>{event.name}</strong> has been successfully confirmed.</p>

                            <hr>

                            <p><strong>Event:</strong> {event.name}</p>
                            <p><strong>Date:</strong> {event.date}</p>
                            <p><strong>Location:</strong> {event.location}</p>
                            <p><strong>Seats:</strong> {", ".join(selected_seats)}</p>
                            <p><strong>Total Paid:</strong> ₹{total_amount}</p>
                            <p><strong>Payment ID:</strong> {razorpay_payment_id}</p>

                            <hr>

                            <p>Please carry this confirmation email on the event day.</p>
                            <p style="margin-top:30px;">Thank you for booking with us!</p>

                            <p style="font-size:12px;color:gray;">
                                This is an automated email. Please do not reply.
                            </p>
                        </div>
                    </body>
                    </html>
                    """

                    email = EmailMultiAlternatives(
                        subject,
                        "",
                        settings.DEFAULT_FROM_EMAIL,
                        [booking.user.email],
                    )
                    email.attach_alternative(html_content, "text/html")
                    email.send()

                except Exception as e:
                    print("Email sending failed:", str(e))

            booking.save()
            return JsonResponse({'status': 'success'})

        except Exception as e:
            traceback.print_exc()
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return render(request, 'user_seat_selection.html', {
        'booking': booking,
        'venue': venue
    })


# --------------------------
# Razorpay Order Creation
# --------------------------
@csrf_exempt
def create_razorpay_order(request, booking_id):
    try:
        booking = get_object_or_404(models.Booking, id=booking_id)

        if not request.body:
            return JsonResponse({'error': 'Empty request body'}, status=400)

        data = json.loads(request.body)
        amount = int(data.get('amount', 0)) * 100  # convert to paise

        if amount <= 0:
            return JsonResponse({'error': 'Invalid amount'}, status=400)

        # Replace with your actual Razorpay key and secret
        client = razorpay.Client(
            auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
        )

        order = client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": 1
        })

        return JsonResponse(order)

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)


# --------------------------
# My Bookings Page
# --------------------------
def user_my_bookings(request):
    if 'email' not in request.session:
        return redirect('login')

    user = get_object_or_404(models.Registration, email=request.session['email'])

    bookings = models.Booking.objects.filter(
        user=user,
        status='confirmed'
    ).select_related('event', 'event__venue').order_by('-bookingdate')

    return render(request, 'user_my_bookings.html', {
        'bookings': bookings
    })

from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Booking, DanceInstitution, InstitutionEvent

def view_event_booking(request):
    email = request.session.get('email')
    if not email:
        return redirect('institutionlogin')
    institution = DanceInstitution.objects.filter(email=email).first()
    if not institution:
        return redirect('institutionlogin') 
    events = InstitutionEvent.objects.filter(institution=institution)
    bookings = Booking.objects.filter(event__in=events).select_related('user', 'event', 'event__venue').order_by('-bookingdate')

    context = {'bookings': bookings}
    return render(request, 'view_event_booking.html', context)






def edit_trainerprofile(request, id):
    try:
        trainer = models.Trainer.objects.get(id=id)
    except models.Trainer.DoesNotExist:
        return redirect('trainerprofile')

    if request.method == "POST":
        trainer.name = request.POST.get('name')
        trainer.phone = request.POST.get('phone')
        trainer.experience = request.POST.get('experience')
        trainer.gender = request.POST.get('gender')

        if 'image' in request.FILES:
            trainer.image = request.FILES['image']

        trainer.save()
        # return HttpResponse("<script> alert('Profile Updated !'); window.location.href='/trainerprofile/'; </script>")
        return redirect('trainerprofile')
    return render(request, 'edit_trainerprofile.html', {'trainer': trainer})



from django.shortcuts import get_object_or_404, render
from danceapp.models import Trainer, Media
import os

def my_video(request, trainer_name):

    trainer = get_object_or_404(Trainer, name=trainer_name)

    # 🔥 Show ALL media uploaded by this trainer
    medias = Media.objects.filter(user_email=trainer.email)

    # Detect media type using file extension (optional but useful)
    for m in medias:
        ext = os.path.splitext(m.mediapath.name)[1].lower()

        if ext in ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv']:
            m.media_type = "video"
        elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
            m.media_type = "image"
        elif ext in ['.mp3', '.wav', '.aac', '.ogg', '.m4a']:
            m.media_type = "audio"
        else:
            m.media_type = "other"

    return render(request, 'my_video.html', {
        'medias': medias,
        'trainer': trainer
    })


# from django.shortcuts import render, redirect
# from .models import Trainer, TrainerSchedule

# def add_schedule(request):
#     trainers = Trainer.objects.filter(isapproved=True)

#     if request.method == 'POST':
#         trainer_id = request.POST.get('trainer')
#         day = request.POST.get('day')
#         dance_style = request.POST.get('dance_style')
#         batch_name = request.POST.get('batch_name')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
#         duration = request.POST.get('duration')
#         max_students = request.POST.get('max_students')

#         trainer = Trainer.objects.get(id=trainer_id)

#         TrainerSchedule.objects.create(
#             trainer=trainer,
#             day=day,
#             dance_style=dance_style,
#             batch_name=batch_name,
#             start_time=start_time,
#             end_time=end_time,
#             duration=duration,
#             max_students=max_students
#         )

#         return redirect('view_schedule') 

#     return render(request, 'add_schedule.html', {'trainers': trainers})


# def view_schedule(request):
#     trainer_id = request.session.get('trainer_id')

#     if not trainer_id:
#         return redirect('trainerlogin') 

#     trainer = Trainer.objects.get(id=trainer_id)
#     schedules = TrainerSchedule.objects.filter(trainer=trainer)

#     return render(request, 'view_schedule.html', {
#         'schedules': schedules,
#         'trainer': trainer
#     })







from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.contrib import messages
from . import models


def add_user_reels(request):
    if 'email' not in request.session:
        return HttpResponse("<script>alert('Login required');window.location='/login/';</script>")

    try:
        user = models.Registration.objects.get(email=request.session['email'])
    except models.Registration.DoesNotExist:
        return HttpResponse("<script>alert('User not found');window.location='/login/';</script>")

    if request.method == "POST":
        models.UserReels.objects.create(
            user_name=user.username,
            user_email=user.email,
            name=request.POST.get('name'),
            mediatypes=request.POST.get('mediatype'),
            categories=request.POST.get('category'),
            # language=request.POST.get('language'),
            description=request.POST.get('description'),
            mediapath=request.FILES.get('media'),
            created_at=timezone.now()
        )
        # return HttpResponse("<script> alert('Reels Added Successfully!'); window.location.href='/user_my_reels/'; </script>")
        return redirect('user_my_reels')
    return render(request, 'add_user_reels.html')


def user_my_reels(request):
    if 'email' not in request.session:
        return redirect('login')

    media_list = models.UserReels.objects.filter(
        user_email=request.session['email']
    ).order_by('-created_at')

    return render(request, 'user_my_reels.html', {'media_list': media_list})


def user_delete_reels(request, id):
    if 'email' not in request.session:
        messages.error(request, "You must be logged in to delete media.")
        return redirect('login')
    try:
        media = models.UserReels.objects.get(id=id, user_email=request.session['email'])
        media.delete()
        messages.success(request, "Media deleted successfully.")
    except models.UserReels.DoesNotExist:
        messages.error(request, "Media not found or you do not have permission to delete it.")

    return redirect('user_my_reels')

from django.shortcuts import render, redirect
from .models import Buypackage

def viewpackagelist(request):

    if 'trainer_id' not in request.session:
        return redirect('trainer_login')  

    trainer_id = request.session['trainer_id']

    buypackages = Buypackage.objects.filter(trainer=str(trainer_id))

    return render(request, 'viewpackagelist.html', {
        'buypackages': buypackages
    })

def select_login(request):
    return render(request, 'select_login.html')



from django.shortcuts import render, get_object_or_404
from .models import DanceCourse

def view_trainer(request, course_id):
    course = get_object_or_404(DanceCourse, id=course_id)
    trainer = course.tutor

    return render(request, 'trainer_detail.html', {
        'course': course,
        'trainer': trainer
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Institution_AddTrainer, Trainerfeedback

def trainer_feedback_list(request, trainer_id):
    trainer = get_object_or_404(Institution_AddTrainer, id=trainer_id)
    feedbacks = Trainerfeedback.objects.filter(email=trainer.email).order_by('-created_at')

    return render(request, 'trainer_feedback_list.html', {
        'trainer': trainer,
        'feedbacks': feedbacks
    })


def add_trainer_feedback(request, trainer_id):
    trainer = get_object_or_404(Institution_AddTrainer, id=trainer_id)

    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        ratings = request.POST.get('ratings')

        Trainerfeedback.objects.create(
            name=name,
            email=trainer.email,   # AUTO FROM TRAINER
            message=message,
            ratings=ratings
        )

        return redirect('trainer_feedback_list', trainer_id=trainer.id)

    return render(request, 'add_trainer_feedback.html', {
        'trainer': trainer
    })




def trainer_feedback(request, trainer_id):
    trainer = get_object_or_404(Institution_AddTrainer, id=trainer_id)
    feedbacks = Trainerfeedback.objects.filter(
        email=trainer.email
    ).order_by('-created_at')

    return render(request, 'trainer_feedback.html', {
        'trainer': trainer,
        'feedbacks': feedbacks
    })