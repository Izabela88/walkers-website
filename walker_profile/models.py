from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator


class WalkerUser(AbstractUser):

    address_details = models.OneToOneField(
        "AddressDetails", null=True, on_delete=models.CASCADE
    )
    petsitter_details = models.OneToOneField(
        "PetsitterDetails", null=True, on_delete=models.CASCADE
    )
    is_petsitter = models.BooleanField(null=True)
    username = models.CharField(max_length=150, null=True, unique=False)
    phone_number = PhoneNumberField(null=True, blank=False, unique=True)

    def validate_image(fieldfile_obj):
        # https://stackoverflow.com/questions/6195478/max-image-size-on-file-upload
        filesize = fieldfile_obj.file.size
        megabyte_limit = 0.4
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError(
                "Image is too big. Max file size is %sMB" % str(megabyte_limit)
            )

    avatar = models.ImageField(
        upload_to="avatar_images/",
        null=True,
        blank=True,
        validators=[validate_image],
    )

    def reviews_rating(self) -> tuple[float, int]:
        """Return user avarage reviews rating

        Returns:
            tuple[float, int]: Avarage rating and number of reviews
        """
        reviews = self.user_reviews.filter(
            is_admin_approved=True, is_visible=True
        )
        ratings = [i.stars for i in reviews]
        try:
            avg_rating = round(sum(ratings) / len(reviews))
        except ZeroDivisionError:
            avg_rating = 0
        return avg_rating, len(reviews)

    @classmethod
    def search_petsitter(cls, search_params):
        """Search petsitters

        Args:
            search_params (dict): Form search data

        Returns:
            list: List of Walker Users
        """
        dog_type_mapping = {
            "small": Q(service_details__is_small_dog=True),
            "medium": Q(service_details__is_medium_dog=True),
            "big": Q(service_details__is_big_dog=True),
        }

        size_filter = dog_type_mapping[search_params["dog_size"]]
        filter_ = Q(
            is_petsitter=True,
            service_details__service_type__type=search_params["care_type"],
            service_details__is_active=True,
        )
        return cls.objects.filter(filter_ & size_filter).all()

    def get_service_details(self):
        """Get all petsitter active services"""
        active_services = []
        for i in self.service_details.filter(is_active=True).all():
            service = {"type": i.service_type.type, "dog_sizes": {}}
            if i.is_small_dog and (i.s_price_hour or i.s_price_day):
                service["dog_sizes"]["small"] = {
                    "price_hour": i.s_price_hour,
                    "price_day": i.s_price_day,
                }
            if i.is_medium_dog and (i.m_price_hour or i.m_price_day):
                service["dog_sizes"]["medium"] = {
                    "price_hour": i.m_price_hour,
                    "price_day": i.m_price_day,
                }
            if i.is_big_dog and (i.b_price_hour or i.b_price_day):
                service["dog_sizes"]["big"] = {
                    "price_hour": i.b_price_hour,
                    "price_day": i.b_price_day,
                }
            if service["dog_sizes"]:
                active_services.append(service)
        return active_services

    def __str__(self):
        return str(self.username)


class AddressDetails(models.Model):
    address = models.CharField(
        verbose_name="Address", max_length=100, null=True
    )
    address_1 = models.CharField(
        verbose_name="Address 1", max_length=100, null=True
    )
    address_2 = models.CharField(
        verbose_name="Address 2", max_length=100, null=True
    )
    town = models.CharField(
        verbose_name="Town/City", max_length=100, null=True
    )
    postcode = models.CharField(
        verbose_name="Post Code", max_length=8, null=True
    )
    county = models.CharField(verbose_name="County", max_length=100, null=True)
    country = models.CharField(
        verbose_name="Country", max_length=100, null=True
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class PetsitterDetails(models.Model):
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class ServiceTypes(models.Model):
    type = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class ServiceDetails(models.Model):
    user = models.ForeignKey(
        WalkerUser,
        on_delete=models.CASCADE,
        null=False,
        related_name="service_details",
    )
    service_type = models.ForeignKey(
        ServiceTypes, on_delete=models.CASCADE, null=False
    )
    is_active = models.BooleanField(null=True)
    is_small_dog = models.BooleanField(null=True)
    s_price_hour = models.PositiveIntegerField(
        null=True, default=0, validators=[MaxValueValidator(10)]
    )
    s_price_day = models.PositiveIntegerField(
        null=True, default=0, validators=[MaxValueValidator(10)]
    )
    is_medium_dog = models.BooleanField(null=True)
    m_price_hour = models.PositiveIntegerField(
        null=True, default=0, validators=[MaxValueValidator(10)]
    )
    m_price_day = models.PositiveIntegerField(
        null=True, default=0, validators=[MaxValueValidator(10)]
    )
    is_big_dog = models.BooleanField(null=True)
    b_price_hour = models.PositiveIntegerField(
        null=True, default=0, validators=[MaxValueValidator(10)]
    )
    b_price_day = models.PositiveIntegerField(
        null=True, default=0, validators=[MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
