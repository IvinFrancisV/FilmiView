from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views, user_login, user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.BASE, name='base'),
    path('', views.HOME_PAGE, name='Home_page'),
    path('User_home', views.USER_HOME, name='User_home'),

    path('register', user_login.REGISTER, name='register'),
    path('Admin_register', user_login.ADMIN_REGISTRATION, name='Admin_register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Logout', user_login.LOGOUT, name='Logout'),
    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('Administrator_home', views.ADMINISTRATOR_HOME, name='Administrator_home'),
    path('accounts/profile', user_login.PROFILE, name='profile'),
    path('Administrator_profile', views.ADMINISTRATOR_PROFILE, name='Administrator_profile'),
    path('Admin_profile_update', views.ADMIN_PROFILE_UPDATE, name='Admin_profile_update'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),
    path('Add_viewer', views.ADD_VIEWER, name='Add_viewer'),
    path('View_viewer', views.VIEW_VIEWERS, name='View_viewer'),
    path('Delete_viewer/<str:admin>', views.DELETE_VIEWER, name='Delete_viewer'),
    path('Add_trailers', views.ADD_TRAILERS, name='Add_trailers'),
    path('View_all_trailers', views.VIEW_ALL_TRAILERS, name='View_all_trailers'),
    path('Delete_trailer/<str:id>', views.DELETE_TRAILER, name='Delete_trailer'),
    path('View_single_trailer/<str:id>', views.VIEW_SINGLE_TRAILER, name='View_single_trailer'),
    path('Add_movies', views.ADD_MOVIES, name='Add_movies'),
    path('View_all_movies_admin', views.VIEW_ALL_MOVIES_ADMIN, name='View_all_movies_admin'),
    path('Delete_movies/<str:id>', views.DELETE_MOVIES, name='Delete_movies'),
    path('View_single_movie/<str:id>', views.VIEW_SINGLE_MOVIE, name='View_single_movie'),
    path('View_movie_cast_admin/<int:id>', views.VIEW_MOVIE_CAST_ADMIN, name='View_movie_cast_admin'),
    path('Add_contact', views.ADD_CONTACT, name='Add_contact'),
    path('View_contact_admin', views.VIEW_CONTACT_ADMIN, name='View_contact_admin'),
    path('Delete_contact/<str:id>', views.DELETE_CONTACT, name='Delete_contact'),
    path('Add_about', views.ADD_ABOUT, name='Add_about'),
    path('View_about_admin', views.VIEW_ABOUT_ADMIN, name='View_about_admin'),
    path('Delete_about/<str:id>', views.DELETE_ABOUT, name='Delete_about'),
    path('Add_notifications', views.ADD_NOTIFICATIONS, name='Add_notifications'),
    path('View_notifications_admin', views.VIEW_NOTIFICATIONS_ADMIN, name='View_notifications_admin'),
    path('Delete_notifications_admin/<int:id>', views.DELETE_NOTIFICATIONS_ADMIN, name='Delete_notifications_admin'),
    path('Add_subscription_details', views.ADD_SUBSCRIPTION, name='Add_subscription_details'),
    path('View_subscription_plans_admin', views.VIEW_SUBSCRIPTION_PLANS_ADMIN, name='View_subscription_plans_admin'),
    path('View_subscription_plans_user_two', user_views.VIEW_SUBSCRIPTION_PLANS_USER_TWO, name='View_subscription_plans_user_two'),
    path('Delete_subscription_plan/<int:id>', views.DELETE_SUBSCRIPTION_PLAN, name='Delete_subscription_plan'),
    path('View_user_complaints', views.VIEW_USER_COMPLAINTS, name='View_user_complaints'),


    path('View_all_trailers_user', user_views.VIEW_ALL_TRAILERS_USER, name='View_all_trailers_user'),
    path('View_single_trailer_user/<str:id>', user_views.VIEW_SINGLE_TRAILER_USER, name='View_single_trailer_user'),
    path('View_about_user', user_views.VIEW_ABOUT_USER, name='View_about_user'),
    path('View_contact_user', user_views.VIEW_CONTACT_USER, name='View_contact_user'),
    path('View_all_movies_user', user_views.VIEW_ALL_MOVIES_USER, name='View_all_movies_user'),
    path('View_single_movie_user/<str:id>', user_views.VIEW_SINGLE_MOVIE_USER, name='View_single_movie_user'),
    path('Like/<int:id>', user_views.LIKE, name='Like'),
    path('View_notifications_user', user_views.VIEW_NOTIFICATIONS_USER, name='View_notifications_user'),
    path('View_subscription_plans_user', user_views.VIEW_SUBSCRIPTION_PLANS_USER, name='View_subscription_plans_user'),
    path('Checkout_one/<str:id>', user_views.CHECKOUT_ONE, name='Checkout_one'),
    path('Checkout_session/<int:id>', user_views.CHECKOUT_SESSION, name='Checkout_session'),
    path('Payment_success', user_views.PAYMENT_SUCCESS, name='Payment_success'),
    path('Payment_cancel', user_views.PAYMENT_CANCEL, name='Payment_cancel'),
    path('Send_complaints_user', user_views.SEND_COMPLAINTS_USER, name='Send_complaints_user'),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
