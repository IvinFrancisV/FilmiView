from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, 'Administrator'),
        (2, "Viewer")
    )
    user_type = models.CharField(choices=USER, max_length=100)
    is_admin = models.BooleanField(null=True)



class Administrator(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    user_type = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class viewer(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name



class Trailer(models.Model):
    Thumbnail = models.ImageField(upload_to="Media/Trailer_Thumbnails", blank=True)
    Movie_name = models.CharField(max_length=2000)
    Release_date = models.CharField(max_length=200)
    Movie_to_release = models.CharField(max_length=200)
    Language = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    trailer = models.FileField(upload_to="Media/Trailer")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Movie_name


class Film(models.Model):
    film_name = models.CharField(max_length=500)
    release_date = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to="Media/Movie_Thumbnails")
    film = models.FileField(upload_to="Media/Movies")
    length = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=500)
    cast_one_name = models.CharField(max_length=100)
    cast_one_image = models.ImageField(upload_to="Media/Cast")
    cast_two_name = models.CharField(max_length=100)
    cast_two_image = models.ImageField(upload_to="Media/Cast")
    cast_three_name = models.CharField(max_length=100)
    cast_three_image = models.ImageField(upload_to="Media/Cast")
    cast_four_name = models.CharField(max_length=100)
    cast_four_image = models.ImageField(upload_to="Media/Cast")
    cast_five_name = models.CharField(max_length=100)
    cast_five_image = models.ImageField(upload_to="Media/Cast")
    cast_six_name = models.CharField(max_length=100)
    cast_six_image = models.ImageField(upload_to="Media/Cast")
    cast_seven_name = models.CharField(max_length=100)
    cast_seven_image = models.ImageField(upload_to="Media/Cast")
    cast_eight_name = models.CharField(max_length=100)
    cast_eight_image = models.ImageField(upload_to="Media/Cast")
    cast_nine_name = models.CharField(max_length=100)
    cast_nine_image = models.ImageField(upload_to="Media/Cast")
    cast_ten_name = models.CharField(max_length=100)
    cast_ten_image = models.ImageField(upload_to="Media/Cast")
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.film_name


class About(models.Model):
    About = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    contact_email = models.EmailField()
    alt_email = models.EmailField()
    contact_mobile = models.CharField(max_length=100)
    alt_mobile = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Complaints(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    complaint = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Likes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_likes")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="movie_likes")


class Notifications(models.Model):
    Notification_msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SubscriptionPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    plan_amount = models.IntegerField()
    plan_validity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plan_name


class Subscription(models.Model):
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)


class Userprofile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    is_pro = models.BooleanField(default=False)
    subscription_expiry_date = models.DateTimeField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100)

    def __str__(self):
        return self.user













