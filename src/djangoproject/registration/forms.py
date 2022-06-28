from django import forms
from django_registration.forms import RegistrationForm
from localflavor.us.forms import USStateField,USZipCodeField, USStateSelect
from phone_field.forms import PhoneFormField, PhoneWidget
from django.core.validators import RegexValidator
from .models import User, ReferrerProfile
import re
from django.db import transaction

class ReferrerRegistrationForm(RegistrationForm):
    # def __init__(self):
    #     self.initial['state'] = 'Michigan'
    first_name = forms.CharField(max_length=50, label=u'First Name', required=False)
    last_name = forms.CharField(max_length=50, label=u'Last Name', required=False)
    street_address = forms.CharField(max_length=50)
    city = forms.CharField(max_length=30)
    state = USStateField(widget=USStateSelect)
    zipcode = USZipCodeField()
    # phone = forms.Charfield(widget=PhoneWidget(attrs={'placeholder': '10-digit Phone number'}),
    #                                label="Phone number", required=True,)
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder':'10-digit Phone'}),
                            label="Phone number", required=True,)
    extension = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ext'}),
                                   label="Extension", required=False,)
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        # Check for ddd-ddd-dddd or dddddddddd formats for Phone
        m = re.match('\d{3}-?\d{3}-?\d{4}', phone)
        if not m:
            raise forms.ValidationError("Invalid phone number; please enter 10-digit phone")
        return phone

    def save(self, *args, **kwargs):
        with transaction.atomic():
            new_user = super().save(*args, **kwargs)

            # put them on the User model instead of the profile and save the user
            new_user.is_referrer=True
            new_user.save()

            # get the profile fields information
            first_name = self.cleaned_data['first_name']
            last_name = self.cleaned_data['last_name']
            street_address = self.cleaned_data['street_address']
            city = self.cleaned_data['city']
            state = self.cleaned_data['state']
            zipcode = self.cleaned_data['zipcode']
            field_dict = {"first_name":first_name, "last_name":last_name,
                "street_address":street_address, "city": city, "state":state, "zipcode":zipcode}
            # create a new profile for this user with his information
            profile = ReferrerProfile(**field_dict)
            profile.user = self.instance
            profile.save()

        # return the User model
        return new_user