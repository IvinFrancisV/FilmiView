from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from Film_viewing_app.models import CustomUser, viewer, Trailer, Film, Contact, About, Notifications, SubscriptionPlan, Complaints
from django.contrib.auth.decorators import login_required




def BASE(request):
    return render(request, "base.html")


def HOME_PAGE(request):
    film = Film.objects.all()
    subscription_plan = SubscriptionPlan.objects.all()
    context = {
        'subscription_plan':subscription_plan,
        'film':film,
    }
    return render(request, "Home_page.html", context)

@login_required
def USER_HOME(request):
    film = Film.objects.all()
    subscription_plan = SubscriptionPlan.objects.all()
    context = {
        'subscription_plan': subscription_plan,
        'film': film,
    }
    return render(request, "User_Home.html", context)



@login_required
def ADMINISTRATOR_HOME(request):
    Viewer = CustomUser.objects.all()
    Viewers_count = Viewer.count()
    film = Film.objects.all()
    film_count = film.count()
    trailer = Trailer.objects.all()
    trailer_count = trailer.count()
    context = {
        'Viewer':Viewer,
        'Viewers_count':Viewers_count,
        'film':film,
        'film_count':film_count,
        'trailer':trailer,
        'trailer_count':trailer_count,
    }
    return render(request, "Administrator_home.html", context)


def ADMINISTRATOR_PROFILE(request):
    return render(request, "Administrator_profile.html")


def ADMIN_PROFILE_UPDATE(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_id = request.user.id

        user = User.objects.get(id = user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request, "Profile Updated Successfully")
        return redirect('Administrator_profile')

@login_required
def ADD_VIEWER(request):
    if request.method == "POST":
        viewer_firstname = request.POST.get('viewer_firstname')
        viewer_lastname = request.POST.get('viewer_lastname')
        viewer_mobile = request.POST.get('viewer_mobile')
        viewer_email = request.POST.get('viewer_email')
        viewer_username = request.POST.get('viewer_username')
        viewer_password = request.POST.get('viewer_password')

        if CustomUser.objects.filter(email=viewer_email).exists():
            messages.warning(request, "An Account is Already Registered with this E-Mail")
            return redirect('Add_viewer')

        elif CustomUser.objects.filter(username=viewer_username):
            messages.warning(request, "This Username is already taken. Please try another.")
            return redirect('Add_viewer')

        else:
            user = CustomUser(
                first_name=viewer_firstname,
                last_name=viewer_lastname,
                username=viewer_username,
                email=viewer_email,
            )
            user.set_password(viewer_password)
            user.save()

            Viewer = viewer(
                admin=user,
                mobile=viewer_mobile,
            )

            Viewer.save()
            messages.success(request, "Successfully Added User")
            return redirect('Add_viewer')

    return render(request, "Add_viewer.html")

@login_required
def VIEW_VIEWERS(request):
    search_query = ''
    if request.GET.get('user_search'):
        search_query = request.GET.get('user_search')
    Viewer = viewer.objects.all()
    User = CustomUser.objects.filter(username__icontains=search_query)

    context = {
        'Viewer':Viewer,
        'search_query':search_query,
    }
    return render(request, "View_viewer.html", context)

@login_required
def DELETE_VIEWER(request, admin):
    Viewer = CustomUser.objects.get(id = admin)
    Viewer.delete()
    messages.success(request, "User Deleted Successfully")
    return redirect('View_viewer')

@login_required
def ADD_TRAILERS(request):
    if request.method == "POST":
        Trailer_moviename = request.POST.get('Trailer_moviename')
        Trailer_releasedate = request.POST.get('Trailer_releasedate')
        Movie_releasedate = request.POST.get('Movie_releasedate')
        Trailer_duration = request.POST.get('Trailer_duration')
        Trailer_language = request.POST.get('Trailer_language')
        Trailer_thumbnail = request.FILES.get('Trailer_thumbnail')
        trailer = request.FILES.get('trailer')

        trailers = Trailer(
            Movie_name = Trailer_moviename,
            Release_date = Trailer_releasedate,
            Movie_to_release = Movie_releasedate,
            duration = Trailer_duration,
            Language = Trailer_language,
            Thumbnail = Trailer_thumbnail,
            trailer = trailer

        )
        trailers.save()
        messages.success(request, "Trailer Added Succesfully")
    return render(request, "Add_trailers.html")


@login_required
def VIEW_ALL_TRAILERS(request):
    search_query = ''
    if request.GET.get('trailer_search'):
        search_query = request.GET.get('trailer_search')
    trail = Trailer.objects.filter(Movie_name__icontains=search_query)

    context = {
        'trail':trail,
        'search_query':search_query
    }

    return render(request, "View_all_trailers.html", context)

@login_required
def DELETE_TRAILER(request, id):
    trail = Trailer.objects.get(id=id)
    trail.delete()
    messages.success(request, "Trailer Deleted Successfully")
    return redirect('View_all_trailers')

@login_required
def VIEW_SINGLE_TRAILER(request, id):
    trail = Trailer.objects.filter(id=id)

    context = {
        'trail':trail,
    }
    return render(request,"View_single_trailer.html", context)

@login_required
def ADD_MOVIES(request):
    if request.method == "POST":
        Movie_Name = request.POST.get('Movie_Name')
        Director_name = request.POST.get('Director_name')
        Movie_ReleaseDate = request.POST.get('Movie_ReleaseDate')
        language = request.POST.get('language')
        genre = request.POST.get('genre')
        duration = request.POST.get('duration')
        Movie_thumbnail = request.FILES.get('Movie_thumbnail')
        Movie_file = request.FILES.get('Movie_file')
        description = request.POST.get('description')
        Cast_name_one = request.POST.get('Cast_name_one')
        Cast_image_one = request.FILES.get('Cast_image_one')
        Cast_name_two = request.POST.get('Cast_name_two')
        Cast_image_two = request.FILES.get('Cast_image_two')
        Cast_name_three = request.POST.get('Cast_name_three')
        Cast_image_three = request.FILES.get('Cast_image_three')
        Cast_name_four = request.POST.get('Cast_name_four')
        Cast_image_four = request.FILES.get('Cast_image_four')
        Cast_name_five = request.POST.get('Cast_name_five')
        Cast_image_five = request.FILES.get('Cast_image_five')
        Cast_name_six = request.POST.get('Cast_name_six')
        Cast_image_six = request.FILES.get('Cast_image_six')
        Cast_name_seven = request.POST.get('Cast_name_seven')
        Cast_image_seven = request.FILES.get('Cast_image_seven')
        Cast_name_eight = request.POST.get('Cast_name_eight')
        Cast_image_eight = request.FILES.get('Cast_image_eight')
        Cast_name_nine = request.POST.get('Cast_name_nine')
        Cast_image_nine = request.FILES.get('Cast_image_nine')
        Cast_name_ten = request.POST.get('Cast_name_ten')
        Cast_image_ten = request.FILES.get('Cast_image_ten')


        film = Film(
            film_name = Movie_Name,
            release_date = Movie_ReleaseDate,
            length = duration,
            director_name = Director_name,
            industry = language,
            genre = genre,
            thumbnail=Movie_thumbnail,
            film=Movie_file,
            description=description,
            cast_one_name=Cast_name_one,
            cast_one_image=Cast_image_one,
            cast_two_name=Cast_name_two,
            cast_two_image=Cast_image_two,
            cast_three_name=Cast_name_three,
            cast_three_image=Cast_image_three,
            cast_four_name=Cast_name_four,
            cast_four_image=Cast_image_four,
            cast_five_name=Cast_name_five,
            cast_five_image=Cast_image_five,
            cast_six_name=Cast_name_six,
            cast_six_image=Cast_image_six,
            cast_seven_name=Cast_name_seven,
            cast_seven_image=Cast_image_seven,
            cast_eight_name=Cast_name_eight,
            cast_eight_image=Cast_image_eight,
            cast_nine_name=Cast_name_nine,
            cast_nine_image=Cast_image_nine,
            cast_ten_name=Cast_name_ten,
            cast_ten_image=Cast_image_ten,
        )
        film.save()
        return redirect('View_all_movies_admin')
    return render(request, "Admin_add_movie.html")

@login_required
def VIEW_ALL_MOVIES_ADMIN(request):
    search_query = ''
    if request.GET.get('movie_search'):
        search_query = request.GET.get('movie_search')
    film = Film.objects.filter(film_name__icontains=search_query)

    context = {
        'film':film,
        'search_query':search_query,
    }
    return render(request, "View_all_movies_admin.html", context)

@login_required
def DELETE_MOVIES(request, id):
    film = Film.objects.get(id=id)
    film.delete()
    messages.success(request, "Movie Deleted Successfully")
    return redirect('View_all_movies_admin')

@login_required
def VIEW_SINGLE_MOVIE(request, id):
    film = Film.objects.filter(id=id)
    context = {
        'film':film,
    }
    return render(request, "View_single_movie.html", context)

@login_required
def VIEW_MOVIE_CAST_ADMIN(request, id):
    film = Film.objects.filter(id=id)
    context = {
        'film':film,
    }
    return render(request, "View_movie_cast_admin.html", context)

@login_required
def ADD_CONTACT(request):
    if request.method == "POST":
        email = request.POST.get('email')
        alt_email = request.POST.get('alt_email')
        mobile = request.POST.get('mobile')
        alt_mobile = request.POST.get('alt_mobile')
        address = request.POST.get('address')

        contact = Contact(
            contact_email = email,
            alt_email = alt_email,
            contact_mobile = mobile,
            alt_mobile = alt_mobile,
            address = address,
        )
        contact.save()
        messages.success(request, "Contact Information Added Successfully")
        return redirect('View_contact_admin')
    return render(request, "Add_contact.html")

@login_required
def VIEW_CONTACT_ADMIN(request):
    contact = Contact.objects.all()
    context = {
        'contact':contact,
    }
    return render(request, "View_contact_admin.html", context)

@login_required
def DELETE_CONTACT(request,id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request, "Contact Deleted Successfully")
    return redirect('View_contact_admin')

@login_required
def ADD_ABOUT(request):
    if request.method == "POST":
        about = request.POST.get('about')

        about = About(
            About = about
        )
        about.save()
        return redirect('View_about_admin')
    return render(request, "Add_about.html")

@login_required
def VIEW_ABOUT_ADMIN(request):
    about = About.objects.all()
    context = {
        'about':about,
    }
    return render(request,"View_about_admin.html",context)

@login_required
def DELETE_ABOUT(request,id):
    about = About.objects.get(id=id)
    about.delete()
    messages.success(request,"About Information deleted Successfully")
    return redirect('View_about_admin')

@login_required
def ADD_NOTIFICATIONS(request):
    if request.method == "POST":
        notification = request.POST.get('notification')

        notification = Notifications(
            Notification_msg = notification
        )
        notification.save()
        messages.success(request, "Successful")
        return redirect('Add_notifications')
    return render(request, "Add_notifications.html")


@login_required
def VIEW_NOTIFICATIONS_ADMIN(request):
    search_query = ''
    if request.GET.get('notification_search'):
        search_query = request.GET.get('notification_search')
    notifications = Notifications.objects.filter(Notification_msg__icontains=search_query)

    context = {
        'notifications':notifications,
        'search_query':search_query,
    }
    return render(request, "View_notifications_admin.html",context)

@login_required
def DELETE_NOTIFICATIONS_ADMIN(request,id):
    notifications = Notifications.objects.filter(id=id)
    notifications.delete()
    messages.success(request, "Notification Deleted Successfully")
    return redirect('View_notifications_admin')

@login_required
def ADD_SUBSCRIPTION(request):
    if request.method == "POST":
        plan_name = request.POST.get('plan_name')
        plan_amount = request.POST.get('plan_amount')
        plan_validity = request.POST.get('plan_validity')

        subscription_plan = SubscriptionPlan(
            plan_name=plan_name,
            plan_amount=plan_amount,
            plan_validity=plan_validity,
        )
        subscription_plan.save()
        messages.success(request, "Subscription Plan Added Successfully")
        return redirect('Add_subscription_details')
    return render(request, "Add_subscription_details.html")

@login_required
def VIEW_SUBSCRIPTION_PLANS_ADMIN(request):
    subscription_plan = SubscriptionPlan.objects.all()
    context = {
        'subscription_plan':subscription_plan,
    }
    return render(request, "View_subscription_plans_admin.html", context)

@login_required
def DELETE_SUBSCRIPTION_PLAN(request, id):
    subscription_plan = SubscriptionPlan.objects.filter(id=id)
    subscription_plan.delete()
    messages.success(request, "Subscription Plan Deleted Successfuly ")
    return redirect('View_subscription_plans_admin')

@login_required
def VIEW_USER_COMPLAINTS(request):
    complaint = Complaints.objects.all()
    context = {
        'complaint':complaint,
    }
    return render(request, "View_user_complaints.html", context)






