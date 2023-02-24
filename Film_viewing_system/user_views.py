from django.shortcuts import redirect, render
from django.contrib import messages
from Film_viewing_app.models import CustomUser, viewer, Trailer, Film, Contact, About, Likes, Notifications, Userprofile, SubscriptionPlan, Complaints
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
import stripe
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required


@login_required
def VIEW_ALL_TRAILERS_USER(request):
    search_query = ''
    if request.GET.get('trailer_search'):
        search_query = request.GET.get('trailer_search')
    trailer = Trailer.objects.filter(Movie_name__icontains=search_query)

    context = {
        'trailer':trailer,
        'search_query':search_query,
    }
    return render(request, "User/View_all_trailers_user.html",context)

@login_required
def VIEW_SINGLE_TRAILER_USER(request, id):
    trailer = Trailer.objects.filter(id=id)
    context = {
        'trailer':trailer
    }

    return render(request, "User/View_single_trailer_user.html", context)

@login_required
def VIEW_ABOUT_USER(request):
    about = About.objects.all()
    context = {
        'about':about
    }
    return render(request, "User/View_about_user.html", context)

@login_required
def VIEW_CONTACT_USER(request):
    contact = Contact.objects.all()
    context = {
        'contact':contact,
    }

    return render(request, "User/View_contact_user.html",context)

@login_required
def VIEW_ALL_MOVIES_USER(request):
    search_query = ''
    if request.GET.get('search'):
        search_query = request.GET.get('search')
    film = Film.objects.filter(Q(film_name__icontains=search_query) |
                               Q(industry__icontains=search_query) |
                               Q(director_name__icontains=search_query) |
                               Q(genre__icontains=search_query)
                               )
    context = {
        'film':film,
        'search_query':search_query,
    }
    return render(request, "User/View_all_movies_user.html",context)

@login_required
def VIEW_SINGLE_MOVIE_USER(request,id):
    film = Film.objects.filter(id=id)
    context = {
        'film':film,
    }
    return render(request, "User/View_single_movie_user.html", context)

@login_required
def LIKE(request, id):
    user = request.user
    film = Film.objects.get(id=id)
    current_likes = film.likes
    liked = Likes.objects.filter(user=user, film=film).count()
    if not liked:
        liked = Likes.objects.create(user=user, film=film)
        current_likes = current_likes + 1
    else:
        liked = Likes.objects.filter(user=user,film=film).delete()
        current_likes = current_likes - 1
    film.likes = current_likes
    film.save()
    return HttpResponseRedirect(reverse('View_single_movie_user', args=[id]))

@login_required()
def VIEW_NOTIFICATIONS_USER(request):
    notifications = Notifications.objects.all()
    context = {
        'notifications':notifications,
    }
    return render(request, "User/View_notifications_user.html", context)


def VIEW_SUBSCRIPTION_PLANS_USER(request):
    subscription_plan = SubscriptionPlan.objects.all()
    context = {
        'subscription_plan': subscription_plan,
    }
    return render(request, "User/View_subscription_plans_user.html", context)

@login_required
def VIEW_SUBSCRIPTION_PLANS_USER_TWO(request):
    subscription_plan = SubscriptionPlan.objects.all()
    context = {
        'subscription_plan': subscription_plan,
    }
    return render(request, "User/View_subscription_plans_user_two.html", context)


def CHECKOUT_ONE(request, id):
    checkout_one = SubscriptionPlan.objects.filter(id=id)
    context = {
        'checkout_one':checkout_one,
    }
    return render(request, "User/Checkout_one.html", context)


stripe.api_key = settings.STRIPE_SECRET_KEY


def CHECKOUT_SESSION(request, id):
    plan = SubscriptionPlan.objects.get(id=id)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency':'inr',
                    'product_data':{
                        'name':plan.plan_name,
                    },
                    'unit_amount':plan.plan_amount*100,
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://127.0.0.1:8000/Payment_success',
        cancel_url='http://127.0.0.1:8000/Payment_cancel',
    )

    user = CustomUser.objects.all()
    if checkout_session['amount_total'] == 30000:
        user_sub = Userprofile(
            user_id=request.user.id,
            subscription_type = "Basic",
            is_pro = True,
            subscription_expiry_date = datetime.now() + timedelta(30),
        )
        user_sub.save()


    elif checkout_session['amount_total'] == 60000:
        user_sub = Userprofile(
            user_id=request.user.id,
            subscription_type="Intermediate",
            is_pro=True,
            subscription_expiry_date=datetime.now() + timedelta(60),
        )
        user_sub.save()

    elif checkout_session['amount_total'] == 90000:
        user_sub = Userprofile(
            user_id=request.user.id,
            subscription_type="Advanced",
            is_pro=True,
            subscription_expiry_date=datetime.now() + timedelta(90),
        )
        user_sub.save()



    return redirect(checkout_session.url, code=303)


def PAYMENT_SUCCESS(request):
    return render(request, "User/Payment_success.html")


def PAYMENT_CANCEL(request):
    return render(request, "User/Payment_cancel.html")

@login_required
def SEND_COMPLAINTS_USER(request):
    if request.method == "POST":
        user_name_ = request.POST.get('user_name_')
        user_email_ = request.POST.get('user_email_')
        user_message_ = request.POST.get('user_message_')

        complaint = Complaints(
            name=user_name_,
            email=user_email_,
            complaint=user_message_,
        )
        complaint.save()
        messages.success(request, "Message Sent Successfully")
    return redirect('View_contact_user')





