from django.urls import path
from . import views  


urlpatterns = [

    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('userlist/',views.userlist,name='userlist'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('feedback/',views.feedbackpage,name='feedback'),
    path('feedbacklist/',views.feedbacklist,name='feedbacklist'),
    path('deleteuser/<int:id>/',views.deleteuser,name='deleteuser'),
    path('deletefeedback/<int:id>/',views.deletefeedback,name='deletefeedback'),
    path('trainer_registration/',views.trainer_registration,name='trainer_registration'),
    path('trainerlogin/',views.trainerlogin,name='trainerlogin'),
    path('trainerhome/',views.trainerhome,name='trainerhome'),
    path('trainerlist/',views.trainerlist,name='trainerlist'),
    path('trainerprofile/',views.trainerprofile,name='trainerprofile'),
    path('deletetrainer/<int:id>/',views.deletetrainer,name='deletetrainer'),
    path('approveuser/<int:id>/',views.approveuser, name='approveuser'),
    path('rejectuser/<int:id>/',views.rejectuser,name='rejectuser'),
    path('addevent/',views.addevent,name='addevent'),
    path('eventlist/',views.eventlist,name='eventlist'),
    path('editevent/<int:id>/',views.editevent, name='editevent'),
    # path('ownerpage/',views.ownerpage, name='ownerpage'),
    path('owner_register/',views.owner_register, name='owner_register'),
    path('owner_login/',views.owner_login, name='owner_login'),
    path('ownerhome/',views.ownerhome, name='ownerhome'), 
    path('ownerlist/',views.ownerlist, name='ownerlist'),  
    path('approveshop/<int:id>/',views.approveshop, name='approveshop'),
    path('rejectshop/<int:id>/',views.rejectshop,name='rejectshop'),
    path('deleteshop/<int:id>/',views.deleteshop,name='deleteshop'),
    path('deleteevent/<int:id>/',views.deleteevent,name='deleteevent'),
    path('shop_ownerprofile/',views.shop_ownerprofile,name='shop_ownerprofile'),
    path('ownereditprofile/',views.ownereditprofile,name='ownereditprofile'),
    path('usertrainerlist/',views.usertrainerlist,name='usertrainer'),
    path('about/',views.about,name='about'),
    path('usereventlist/',views.usereventlist,name='usereventlist'),
    path('addcostumes/',views.addcostume,name='addcostume'),
    path('listcostumes/',views.listcostumes,name='listcostumes'),
    path('listcostume_shop/',views.listcostumes_shop,name='listcostumes_shop'),
    path('deletecostume/<int:id>/',views.deletecostume,name='deletecostume'),
    path('editcostume/<int:id>/',views.editcostume,name='editcostume'),
    path('admincostumesview/',views.admincostumesview,name='admincostumesview'),
    path('admindeletecostume/<int:id>/',views.admindeletecostume,name='admindeletecostume'),
    path('institution/', views.institution_register, name='institution'),
    path('institutionlogin/', views.institutionlogin, name='institutionlogin'),
    path('admininstitutionlist/', views.admininstitutionlist, name='admininstitutionlist'),
    path('approveinstitution/<int:id>/', views.approveinstitution, name='approveinstitution'),
    path('rejectinstitution/<int:id>/', views.rejectinstitution, name='rejectinstitution'),
    path('deleteinstitution/<int:id>/', views.deleteinstitution, name='deleteinstitution'),
    path('institutionhome/', views.institutionhome, name='institutionhome'),
    path('listTrainer/', views.listTrainer, name='listTrainer'),
    path('profile_institution/',views.profile_institution,name='profile_institution'),

    
    
    path('dancepackages/', views.dancepackages, name='dancepackages'),
    path('listdancepackage/<int:trainer_id>/', views.listdancepackage, name='listdancepackage'),
    path('trainerpackagelist/',views.trainer_package,name='trainerpackagelist'),
    path('deletepackage/<int:id>/', views.deletepackage,name='deletepackage'),
    path('edit_package/<int:id>/', views.edit_package,name='edit_package'),
    path('adminpackagelist/', views.adminpackagelist,name='adminpackagelist'),
    # path("listcostumes/<int:id>/", views.addtocart, name='addtocart'),
    path('cartlist/', views.cartlist,name='cartlist'),
path("cart/add/<int:id>/", views.addtocart, name='addtocart'),
    path('removecart/<int:id>/', views.removecart,name='removecart'),


    path('buynow/<int:productid>/', views.buynow, name='buynow'),
    path('singleordersucess/',views.singlebuy,name='singleordersucess'),
    path('out_of_stock/',views.out_of_stock,name='out_of_stock'),
    path('payment/<int:id>/', views.payment_view, name='single_payment'),  
    path('payment_success/', views.payment_success, name='payment_success'),  # For cart
    path('payment_success/<int:id>/', views.payment_success, name='payment_success_single'),
    path('buynow/', views.buynow_view, name='buynow'),
    path('payment/', views.payment_view, name='group_payment'),  # For cart checkout

   
    path('user_orders_list/', views.user_order_list, name='user_orders_list'),
    path('shopowner_order/', views.shopowner_order, name='shopowner_order'),
    path('dispatch/<int:userid>/', views.dispatch, name='dispatch'),
    path('outfordelivery/<int:userid>/', views.outfordelivery, name='outfordelivery'),
    path('deliver/<int:userid>/', views.deliver, name='deliver'),
    path('cancel-delivery/<int:userid>/', views.cancel_delivery, name='cancel_delivery'),
    path('subscriptions/<int:id>/', views.subscriptions, name='subscriptions'),
    path('subs_payment_view/<int:id>/', views.subs_payment_view, name='subs_payment_view'),
    path('subs_payment_success/<int:id>/', views.subs_payment_success, name='subs_payment_success'),
    path('buypackage/<int:id>/', views.buypackage, name='buypackage'),
    path('pack_payment_view/<int:id>/', views.pack_payment_view, name='pack_payment_view'),
    path('pack_payment_success/<int:id>/', views.pack_payment_success, name='pack_payment_success'),
    path('subscriptionlist/', views.subscriptionlist, name='subscriptionlist'),
    path('profile_institution/',views.profile_institution,name='profile_institution'),
    path('edit_profile_institution/',views.edit_profile_institution,name='edit_profile_institution'),
    path('registered_students_list/', views.registered_students_list, name='registered_students_list'),
    path('studentslist/', views.studentslist, name='studentslist'),
    path('chat_list/', views.chat_list, name='chat_list'),
    path('chat_detail/<str:user_email>/', views.chat_detail, name='chat_detail'),

    path('like_video/<int:video_id>/', views.like_video, name='like_video'),
    path('comment_video/<int:video_id>/', views.comment_video, name='comment_video'),
    path('my_uploads/', views.my_uploads, name='my_uploads'),
    path('upload/', views.upload, name='upload'),
    path('videos/', views.video_view, name='videoview'),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),

    path('medialistadmin/', views.medialistadmin, name='medialistadmin'), 
    path('medialistuser/', views.medialistuser, name='medialistuser'), 
    
    path('approve/<int:id>/',views.approve,name='approve'),
    path('rejected<int:id>/',views.rejected,name='rejected'),
    path('trainerfeedback/', views.trainerfeedback, name='trainerfeedback'),
    path('add_trainer/',views.add_trainer,name='add_trainer'),
    path('edit_trainer/<int:trainer_id>',views.edit_trainer,name='edit_trainer'),
    path('delete_trainer/<int:trainer_id>',views.delete_trainer,name='delete_trainer'),
    path('add_class/<int:course_id>',views.add_class,name='add_class'),
    path('list_class/<int:course_id>/', views.list_class, name='list_class'),
    path('edit_class/<int:id>/', views.edit_class, name='edit_class'),
    path('delete_class/<int:id>/', views.delete_class, name='delete_class'),
    path('institution_events/',views.institution_events,name='institution_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<int:id>/', views.edit_event, name='edit_event'),
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
    path('add_course/',views.add_course,name='add_course'),
    path('list_courses/',views.list_courses,name='list_courses'),
    path('edit_course/<int:id>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),
    path('user_list_institution/',views.user_list_institution,name='user_list_institution'),
    path('institution_courses/<int:id>/', views.institution_courses, name='institution_courses'),

    path('course_buynow/<int:courseid>/', views.course_buynow, name='course_single_buynow'),
    path('course_single_order_sucess/',views.course_single_order_sucess,name='course_single_order_sucess'),
    path('course_out_of_stock/',views.course_out_of_stock,name='course_out_of_stock'),
    path('course_payment/<int:id>/', views.course_payment_view, name='course_single_payment'),
    path('course_payment_success/<int:id>/', views.course_payment_success_view, name='course_payment_success_single'),

    path('course_classes/<int:id>/',views.course_classes,name='course_classes'),


    path('add_reels/', views.add_reels, name='add_reels'),
    path('reels_view/', views.reels_view, name='reels_view'),
    path('like_reels/<int:video_id>/', views.like_reels, name='like_reels'),
    path('comment_reels/<int:video_id>/', views.comment_reels, name='comment_reels'),
    path('like_media/<int:video_id>/', views.like_media, name='like_media'),
    path('comment_media/<int:video_id>/', views.comment_media, name='comment_media'),
    path('institute_my_reels/', views.institute_my_reels, name='institute_my_reels'),
    path('delete_reels/<int:id>/',views.delete_reels,name='delete_reels'),

    path('view_costumes/',views.view_costumes,name='view_costumes'),
    path('delete_costume/<int:id>/',views.delete_costume,name='delete_costume'),
    path('edit_costume/<int:id>/',views.edit_costume,name='edit_costume'),

    path('view_orders/',views.owner_view_orders,name='owner_view_orders'),

    path('venue_list/', views.venue_list, name='venue_list'),
    path('add_venue/', views.add_venue, name='add_venue'),
    path('edit_venue/<int:venue_id>/', views.edit_venue, name='edit_venue'),
    path('delete_venue/<int:venue_id>/', views.delete_venue, name='delete_venue'),

    path('eventdetails/<int:event_id>/',views.eventdetails,name='eventdetails'),
    path('register_event/<int:id>/', views.register_event, name='register_event'),
    path('seat_selection/<int:booking_id>/', views.user_seat_selection, name='user_seat_selection'),
    path('create_razorpay_order/<int:booking_id>/', views.create_razorpay_order, name='create_razorpay_order'),
    path('my_bookings/', views.user_my_bookings, name='user_my_bookings'),

    path('view_event_booking/',views.view_event_booking,name='view_event_booking'),

    path('edit_trainerprofile/<int:id>/', views.edit_trainerprofile, name='edit_trainerprofile'),

    path('my_video/<str:trainer_name>/', views.my_video, name='my_video'),

    path('adminsubscriptionlist/',views.adminsubscriptionlist,name='adminsubscriptionlist'),


    # path('add_schedule/', views.add_schedule, name='add_schedule'),
    # path('view_schedule/', views.view_schedule, name='view_schedule'),

    path('costume/<int:id>/', views.costume_detail, name='costume_detail'),


    path('add_user_reels/', views.add_user_reels, name='add_user_reels'),
    path('like_userreels/<int:video_id>/', views.like_userreels, name='like_userreels'),
    path('comment_userreels/<int:video_id>/', views.comment_userreels, name='comment_userreels'),
    path('user_my_reels/', views.user_my_reels, name='user_my_reels'),
    path('user_delete_reels/<int:id>/',views.user_delete_reels,name='user_delete_reels'),

    path('viewpackagelist/', views.viewpackagelist, name='viewpackagelist'),
    path('select-login/', views.select_login, name='select_login'),


    path('trainer/<int:course_id>/', views.view_trainer, name='view_trainer'),
    path('trainer/<int:trainer_id>/feedback/', views.trainer_feedback_list, name='trainer_feedback_list'),
    path('trainer/<int:trainer_id>/feedback/add/', views.add_trainer_feedback, name='add_trainer_feedback'),
    path('feedback_trainer/<int:trainer_id>',views.trainer_feedback,name='trainer_feedback'),


]    
