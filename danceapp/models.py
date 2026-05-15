from django.db import models
from django.utils import timezone
import shortuuid
from django.core.validators import FileExtensionValidator
from django.db.models import Sum
from django.utils.timezone import now


# Create your models here.
class Registration(models.Model):

    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    confirm_password=models.CharField(max_length=20,null=True,blank=True)
    GENDER_CHOICES=(
        ('M','male'),
        ('F','female'),
        ('O','other'),
    )

    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    DISTRICT_CHOICES=(
        ('Trivandrum','Trivandrum'),
        ('Kollam','Kollam'),
        ('Pathanamthitta','Pathanamthitta'),
        ('Alappuzha','Alappuzha'),
        ('Kottayam','Kottayam'),
        ('Idukki','Idukki'),
        ('Ernakulam','Ernakulam'),
        ('Thrissur','Thrissur'),
        ('Palakkad','Palakkad'),
        ('Malappuram','Malappuram'),
        ('Kozhikode','Kozhikode'),
        ('Wayanad','Wayanad'),
        ('Kannur','Kannur'),
        ('Kasargod','Kasaragod'),
    )
    DISTRICT=models.CharField(max_length=20,choices=DISTRICT_CHOICES,null=True,blank=True)

    bio=models.TextField(null=True,blank=True)
    links=models.TextField(null=True,blank=True)
    image=models.FileField(upload_to='images/',null=True,blank=True)

class Feedback(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Trainer(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True,unique=True)
    phone=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    experience=models.IntegerField(null=True,blank=True)
    idproof=models.FileField(upload_to='images/',null=True,blank=True)
    GENDER_CHOICES=[
        ('M','male'),
        ('F','female'),
        ('O','other'),
    ]
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True,blank=True)
    image=models.FileField(upload_to='images/',null=True,blank=True)
    isapproved=models.BooleanField(default=False)
    isrejected=models.BooleanField(default=False)




# class TrainerSchedule(models.Model):
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    
#     DAY_CHOICES = [
#         ('Mon', 'Monday'),
#         ('Tue', 'Tuesday'),
#         ('Wed', 'Wednesday'),
#         ('Thu', 'Thursday'),
#         ('Fri', 'Friday'),
#         ('Sat', 'Saturday'),
#         ('Sun', 'Sunday'),
#     ]

#     day = models.CharField(max_length=3, choices=DAY_CHOICES)
#     dance_style = models.CharField(max_length=100)
#     batch_name = models.CharField(max_length=100)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     duration = models.IntegerField(help_text="Duration in minutes")
#     max_students = models.IntegerField()

#     def __str__(self):
#         return f"{self.trainer.name} - {self.day} ({self.start_time} to {self.end_time})"







from django.db import models

class DanceInstitution(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)  
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    
    certificate = models.FileField(upload_to='institution_docs/', null=True, blank=True)
    logo = models.FileField(upload_to='institution_logos/', null=True, blank=True)
    DISTRICT_CHOICES=[
            ('Trivandrum','Trivandrum'),
            ('Kollam','Kollam'),
            ('Pathanamthitta','Pathanamthitta'),
            ('Alappuzha','Alappuzha'),
            ('Kottayam','Kottayam'),
            ('Idukki','Idukki'),
            ('Ernakulam','Ernakulam'),
            ('Thrissur','Thrissur'),
            ('Palakkad','Palakkad'),
            ('Malappuram','Malappuram'),
            ('Kozhikode','Kozhikode'),
            ('Wayanad','Wayanad'),
            ('Kannur','Kannur'),
            ('Kasargod','Kasaragod'),
        ]
    district = models.CharField(max_length=20,choices=DISTRICT_CHOICES,null=True,blank=True)

    isapproved = models.BooleanField(default=False)
    isrejected = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

from django.db import models
from django.utils import timezone

class Media(models.Model): 
    user_name = models.CharField(max_length=50, null=True, blank=True)
    user_email = models.EmailField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    MEDIA_TYPES = (
        ('video','video'), 
        ('image','image'), 
        ('audio','audio'), 
    )
    mediatypes = models.CharField(max_length=100, choices=MEDIA_TYPES, null=True, blank=True)

    CATEGORIES = [
        ('entertainment','entertainment'), 
        ('news','news'), 
        ('petsandanimals','petsandanimals'), 
        ('education','education'), 
        ('music','music'), 
        ('gaming','gaming'), 
        ('sports','sports'), 
        ('advertisement','advertisement'), 
        ('travel','travel'),
    ]
    categories = models.CharField(max_length=100, choices=CATEGORIES, null=True, blank=True)

    # LANGUAGES = [ 
    #     ('english','english'), 
    #     ('malayalam','malayalam'), 
    #     ('hindi','hindi'), 
    # ]
    # language = models.CharField(max_length=100, choices=LANGUAGES, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    mediapath = models.FileField(upload_to='uploads/', null=True)
    isapproved = models.BooleanField(default=False)
    isrejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user_name} ({self.user_email})"

 
class VideoLike(models.Model): 
    video = models.ForeignKey(Media, on_delete=models.CASCADE) 
    user_email = models.CharField(max_length=200) 
    liked_at = models.DateTimeField(default=timezone.now) 
 
class VideoComment(models.Model): 
    video = models.ForeignKey(Media, on_delete=models.CASCADE) 
    user_email = models.CharField(max_length=200) 
    username = models.CharField(max_length=200) 
    comment = models.TextField() 
    commented_at = models.DateTimeField(default=timezone.now)    


    



from django.db import models

class DancePackage(models.Model):
    TRAINER_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('workshop', 'Workshop'),
    ]
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # item_id = models.CharField(max_length=100, unique=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    how = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=TRAINER_CHOICES)
    
    image = models.ImageField(upload_to='packages/', blank=True, null=True)

    def __str__(self):
        return self.package_name


class shop(models.Model):
     name=models.CharField(max_length=100,null=True,blank=True)
     email=models.EmailField(max_length=100,null=True,blank=True,unique=True)
     image=models.FileField(upload_to='owner_images/',null=True,blank=True)
     phone=models.IntegerField(null=True,blank=True)
     password=models.CharField(max_length=20,null=True,blank=True)
     isapproved=models.BooleanField(default=False)
     isrejected=models.BooleanField(default=False)
     licenseno=models.CharField(max_length=10,null=True,blank=True)
     shopname=models.CharField(max_length=100,null=True,blank=True)

class CostumeVariant(models.Model):
    costume = models.ForeignKey('Costume', on_delete=models.CASCADE, related_name="variants")
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.costume.name} - {self.size} - {self.color}"

class Costume(models.Model):
    shop=models.ForeignKey(shop,on_delete=models.CASCADE,related_name="costume",null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
   
    rate = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    image = models.FileField(upload_to='costumes/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
   
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    @property
    def total_stock(self):
        return sum(v.quantity for v in self.variants.all())



class Addtocart(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE)
    variant = models.ForeignKey('CostumeVariant', on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()
    totalprice = models.IntegerField()
    
from django.utils import timezone

class Buynow(models.Model):
    user = models.ForeignKey('Registration', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('Costume', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(default=1)  # default=0 might cause issues, better 1
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Delivery Status using Boolean Fields (as you wanted, like approve/reject)
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('dispatched', 'Dispatched'),
    ('outfordelivery', 'Out for Delivery'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'

    )
    # Auto-generated unique order number
    

    order_number = models.CharField(max_length=20, blank=True)
    
    variant = models.ForeignKey(
        'CostumeVariant',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # better than default=timezone.now

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = shortuuid.ShortUUID().random(length=10)
        super().save(*args, **kwargs)



class Subscription(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    startdate = models.DateField(null=True, blank=True)
    enddate = models.DateField(null=True, blank=True)
    price = models.IntegerField(default=100)   
    ordered_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='Pending')

class Buypackage(models.Model):
    package = models.ForeignKey(DancePackage, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    trainer = models.CharField(max_length=20,null=True, blank=True)
    fees = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=20,null=True, blank=True)
    package_name = models.CharField(max_length=20,null=True, blank=True)
    type = models.CharField(max_length=20,null=True, blank=True)   
    ordered_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='Pending')

class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    media = models.FileField(upload_to='chat_media/', null=True, blank=True)
    timestamp = models.DateTimeField(default=now)
    is_read = models.BooleanField(default=False)


class Trainerfeedback(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=254,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    ratings=models.IntegerField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

class Institution_AddTrainer(models.Model):
    institution = models.ForeignKey(
        DanceInstitution,
        on_delete=models.CASCADE
    )

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    TRAINER_TYPE_CHOICES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('GT', 'Guest'),
    ]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    photo = models.ImageField(
        upload_to='trainers/photos/',
        blank=True,
        null=True
    )

    dance_styles = models.CharField(
        max_length=200,
        help_text="Example: Bharatanatyam, Hip-Hop, Contemporary"
    )

    years_of_experience = models.PositiveIntegerField()
    teaching_experience = models.PositiveIntegerField(
        help_text="In years"
    )

    trainer_type = models.CharField(
        max_length=2,
        choices=TRAINER_TYPE_CHOICES
    )

    portfolio = models.FileField(
        upload_to='trainers/portfolios/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    # documents
                    'pdf', 'doc', 'docx', 'ppt', 'pptx',
                    # videos
                    'mp4', 'webm', 'ogg', 'mov', 'm4v',
                    'avi', 'wmv', 'mkv',
                    # images
                    'jpg', 'jpeg', 'png', 'gif',
                    'webp', 'bmp', 'svg', 'tif', 'tiff'
                ]
            )
        ]
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class DanceClass(models.Model):
    DANCE_STYLES = [
        ('bharatanatyam', 'Bharatanatyam'),
        ('hiphop', 'Hip Hop'),
        ('kathak', 'Kathak'),
        ('salsa', 'Salsa'),
        ('contemporary', 'Contemporary'),
    ]

    institution = models.ForeignKey(
        'DanceInstitution', 
        on_delete=models.CASCADE, 
        related_name='classes'
    )
    trainer = models.ForeignKey(
        'Institution_AddTrainer', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='classes'
    )
    course = models.ForeignKey(
        'DanceCourse', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='classes'
    )
    name = models.CharField(max_length=100) 
    description = models.TextField(blank=True, null=True)  

    dance_style = models.CharField(
        max_length=50,
        choices=DANCE_STYLES,
        null=True,
        blank=True
    )
    
    uploaded_video = models.FileField(
        upload_to='dance_videos/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.institution.name})"


class Venue(models.Model):
    institution = models.ForeignKey(DanceInstitution, on_delete=models.CASCADE, related_name='venue')
    name = models.CharField(max_length=100, help_text="e.g., 'Venue name'")
    total_seats = models.PositiveIntegerField(default=0)
    seat_layout = models.JSONField(default=list, help_text="List of custom seat names, e.g., ['AB1', 'GK2']")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.institution.name})"


class InstitutionEvent(models.Model):
    STATUS_CHOICES = [
        ('UP', 'Upcoming'),
        ('CO', 'Completed'),
        ('CA', 'Cancelled'),
    ]

    institution = models.ForeignKey('DanceInstitution',on_delete=models.CASCADE,related_name='events')
    trainer = models.ForeignKey('Institution_AddTrainer',on_delete=models.SET_NULL,null=True,blank=True, related_name='events' )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    trainer_position = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    poster = models.ImageField( upload_to='event_posters/',
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif','webp'])
        ]
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='UP')
    AGE_CATEGORY=[
        ('kids','Kids'),
        ('teens','Teens'),
        ('adults','Adults'),
    ]
    age_category=models.CharField(max_length=10,choices=AGE_CATEGORY,null=True,blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True,related_name='events')
    booked_venue = models.JSONField(default=dict, help_text="Dict of booked venue, e.g., {'AB1': {'booked': True, 'gender': 'M'}}")
    priceperperson = models.IntegerField(null=True, blank=True)
    totalprice = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

     # -------- SEAT CALCULATION --------
    @property
    def total_seats(self):
        return self.venue.total_seats if self.venue else 0

    @property
    def booked_seats(self):
        return (
            Booking.objects
            .filter(event=self, status='confirmed')
            .aggregate(total=Sum('numberofpeople'))['total']
            or 0
        )

    @property
    def available_seats(self):
        return max(self.total_seats - self.booked_seats, 0)

    def __str__(self):
        return f"{self.name} ({self.institution.name}) on {self.date}"


class DanceCourse(models.Model):
    COURSE_TYPES = [
        ('CL', 'Classical'),
        ('HP', 'Hip Hop'),
        ('KS', 'Kathak'),
        ('BS', 'Bharatanatyam'),
        ('MO', 'Mohiniyattam'),
        ('OT', 'Other'),
    ]
    course_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    course_type = models.CharField(max_length=20, choices=COURSE_TYPES, default='OT')
    duration_in_weeks = models.PositiveIntegerField()
    schedule = models.CharField(max_length=200, help_text="E.g. Mon, Wed, Fri - 5:00 PM to 6:00 PM")
    number_of_classes = models.PositiveIntegerField(help_text="Total number of classes")
    tutor = models.ForeignKey('Institution_AddTrainer',on_delete=models.SET_NULL,null=True,blank=True, related_name='courses')
    institution = models.ForeignKey('DanceInstitution',on_delete=models.CASCADE,related_name='courses')
    fees_per_head = models.DecimalField(max_digits=10,decimal_places=2)
    extra_details = models.TextField(blank=True, null=True)
    poster = models.ImageField(
        upload_to='course_posters/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif','webp'])]
    )
    status = models.CharField(
        max_length=20,
        choices=[('UP', 'Upcoming'), ('CO', 'Ongoing'), ('COC', 'Completed')],
        default='UP'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course_name} ({self.get_course_type_display()})"


class course_buynow(models.Model):
    user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    course = models.ForeignKey(DanceCourse, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='Pending')


 
class Reels(models.Model):
    user_name = models.CharField(max_length=50, null=True, blank=True)
    user_email = models.EmailField(max_length=50, null=True, blank=True)
    name = models.TextField(max_length=50, null=True, blank=True)

    MEDIA_TYPES = [
        ('video','video'),
        ('image','image'),
        ('audio','audio'),
    ]
    mediatypes = models.CharField(max_length=100, choices=MEDIA_TYPES)

    CATEGORIES = [
        ('entertainment','entertainment'),
        ('news','news'),
        ('petsandanimals','petsandanimals'),
        ('education','education'),
        ('music','music'),
        ('gaming','gaming'),
        ('sports','sports'),
        ('advertisement','advertisement'),
        ('travel','travel'),
    ]
    categories = models.CharField(max_length=100, choices=CATEGORIES)

    # LANGUAGE = [
    #     ('english','english'),
    #     ('malayalam','malayalam'),
    #     ('hindi','hindi'),
    # ]
    # language = models.CharField(max_length=100, choices=LANGUAGE)

    description = models.TextField(max_length=200)
    mediapath = models.FileField(upload_to='uploads/')
    # status = models.CharField(max_length=20, default='Uploaded')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ReelsLike(models.Model):
    video = models.ForeignKey(Reels, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=200)
    liked_at = models.DateTimeField(default=timezone.now)


class ReelsComment(models.Model):
    video = models.ForeignKey(Reels, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    comment = models.TextField()
    commented_at = models.DateTimeField(default=timezone.now)



class Booking(models.Model):
    event = models.ForeignKey(InstitutionEvent, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    seats = models.JSONField(default=dict)  # Changed to dict for seat:gender mapping e.g. {"A1": "M", "B2": "F"}
    bookingdate = models.DateTimeField(auto_now_add=True)
    numberofpeople = models.PositiveIntegerField(default=0)  # Use PositiveIntegerField for people count
    totalamount = models.PositiveIntegerField(default=0)     # PositiveIntegerField for money

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"Booking {self.id} - {self.event.name if self.event else 'No Package'} by {self.user.email if self.user else 'Guest'}"

    class Meta:
        ordering = ['-bookingdate']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'


class UserReels(models.Model):
    user_name = models.CharField(max_length=50, null=True, blank=True)
    user_email = models.EmailField(max_length=50, null=True, blank=True)
    name = models.TextField(max_length=50, null=True, blank=True)

    MEDIA_TYPES = [
        ('video','video'),
        ('image','image'),
        ('audio','audio'),
    ]
    mediatypes = models.CharField(max_length=100, choices=MEDIA_TYPES)

    CATEGORIES = [
        ('entertainment','entertainment'),
        ('news','news'),
        ('petsandanimals','petsandanimals'),
        ('education','education'),
        ('music','music'),
        ('gaming','gaming'),
        ('sports','sports'),
        ('advertisement','advertisement'),
        ('travel','travel'),
    ]
    categories = models.CharField(max_length=100, choices=CATEGORIES)

    # LANGUAGE = [
    #     ('english','english'),
    #     ('malayalam','malayalam'),
    #     ('hindi','hindi'),
    # ]
    # language = models.CharField(max_length=100, choices=LANGUAGE)

    description = models.TextField(max_length=200)
    mediapath = models.FileField(upload_to='uploads/')
    # status = models.CharField(max_length=20, default='Uploaded')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class UserReelsLike(models.Model):
    video = models.ForeignKey(UserReels, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=200)
    liked_at = models.DateTimeField(default=timezone.now)


class UserReelsComment(models.Model):
    video = models.ForeignKey(UserReels, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    comment = models.TextField()
    commented_at = models.DateTimeField(default=timezone.now)