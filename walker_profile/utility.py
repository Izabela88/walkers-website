"""Utility functions"""
from django.contrib import messages
from walker_profile.forms import (
    UpdateWalkerProfileForm,
    WalkerAddressForm,
    WalkerUserAvatarForm,
    PetsitterDescriptionForm,
    ServiceDetailsForm,
)
from .models import ServiceDetails
import requests
from django.http import HttpResponseRedirect
from haversine import haversine, Unit


def _handle_profile_form(request, context, *args):
    profile_form = UpdateWalkerProfileForm(
        instance=request.user, data=request.POST or None
    )
    request.session['tab'] = "personal_information"
    if profile_form.is_valid() and profile_form.has_changed():
        profile_form.save()
        messages.success(request, 'Your profile is updated successfully')
    else:
        print(profile_form.errors)
        request.session["profile_form_errors"] = profile_form.errors
        context['profile_form'] = UpdateWalkerProfileForm(
            instance=request.user
        )
    return context


def _handle_address_form(request, context, *arg):
    address_form = WalkerAddressForm(
        instance=request.user.address_details, data=request.POST or None
    )
    request.session['tab'] = "address_details"
    if address_form.is_valid() and address_form.has_changed():
        try:
            long, lat = get_postcode_coordinates(
                address_form.cleaned_data["postcode"]
            )
        except GeoCodeError:
            messages.error(request, "Invalid postcode!")
            return HttpResponseRedirect("/profile/user_profile")

        address_form.instance.longitude = long
        address_form.instance.latitude = lat
        address_form.save()
        if request.user.address_details_id != address_form.instance.id:
            request.user.address_details_id = address_form.instance.id
            request.user.save()
        messages.success(request, 'Your address is updated successfully')
    else:
        print(address_form.errors)
        request.session["address_form_errors"] = address_form.errors
        context['address_form'] = WalkerAddressForm(
            instance=request.user.address_details
        )
    return context


def _handle_avatar_form(request, context, *arg):
    avatar_form = WalkerUserAvatarForm(
        request.POST or None, request.FILES, instance=request.user
    )
    request.session['tab'] = "upload_photo"
    if avatar_form.is_valid() and avatar_form.has_changed():
        avatar_form.save()
        messages.success(request, 'Your avatar is updated successfully')
    else:
        print(avatar_form.errors)
        request.session["avatar_form_errors"] = avatar_form.errors
        context['avatar_form'] = WalkerUserAvatarForm(instance=request.user)
    return context


def _handle_description_form(request, context, *arg):
    description = PetsitterDescriptionForm(
        instance=request.user.petsitter_details, data=request.POST or None
    )
    request.session['tab'] = "petsitter_profile"

    if description.is_valid() and description.has_changed():
        description.save()
        if request.user.petsitter_details_id != description.instance.id:
            request.user.petsitter_details_id = description.instance.id
            request.user.save()
        messages.success(request, 'Your description is updated successfully')
    else:
        request.session["description_errors"] = description.errors
        context['description_form'] = PetsitterDescriptionForm(
            instance=request.user.petsitter_details
        )
    return context


def _handle_service_details_forms(request, context, service_type_id):
    if service_type_id:
        service_detail = ServiceDetails.objects.filter(
            service_type_id=service_type_id, user_id=request.user.id
        ).first()
        service_details_form = ServiceDetailsForm(
            instance=service_detail, data=request.POST or None
        )
        request.session['tab'] = "petsitter_profile"
        if (
            service_details_form.is_valid()
            and service_details_form.has_changed()  # noqa: W503
        ):
            service_details_form.instance.service_type_id = service_type_id
            service_details_form.instance.user_id = request.user.id
            service_details_form.save()
            messages.success(request, 'Your data is updated successfully')
        else:
            request.session[
                "service_details_errors"
            ] = service_details_form.errors
            context['service_details_forms'] = ServiceDetailsForm(
                instance=service_detail
            )
    return context


class GeoCodeError(Exception):
    pass


def get_postcode_coordinates(postcode):
    r = requests.get(f'https://api.postcodes.io/postcodes/{postcode}')
    if r.ok:
        geocode_data = r.json()
        try:
            return (
                geocode_data['result']['longitude'],
                geocode_data['result']['latitude'],
            )
        except KeyError:
            raise GeoCodeError
    raise GeoCodeError


def get_users_within_radius(long, lat, users_list, radius_miles):
    users_within_radius = []
    for i in users_list:
        distance_miles = haversine(
            (lat, long),
            (i.address_details.latitude, i.address_details.longitude),
            unit=Unit.MILES,
        )
        if distance_miles <= float(radius_miles):
            users_within_radius.append(i)
    return users_within_radius
