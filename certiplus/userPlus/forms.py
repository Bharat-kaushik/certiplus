from django import forms
from django.utils.translation import ugettext
from userPlus.models import User, Company
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from django.apps import apps
from django.conf import settings


sensitive_post_parameter_m = method_decorator(sensitive_post_parameters())


class UserCreationForm(forms.ModelForm):
    """"
    A Form that creates a user, with no privilages, from the given username and password.
    """
    error_message = {
        'duplicate_username': ugettext("A User with this username already exists")
    }

    class Meta:
        model = User
        fields = ('email', 'name', 'mobile', 'password')
        exclude = ('is_active', 'created_on', 'updated_on', 'is_emailVerified', 'is_staff', 'is_superuser',
                   'last_login_ip', 'last_login', 'groups', 'user_permissions' , 'sex', 'height', 'age', 'weight', 'blood_group')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_random_password()
        if commit:
            user.save()
        return user


class UserChagneForm(forms.ModelForm):

    """A form for updating users. Includes all the fields on
    the user, but replace the password field with admin's password hash display field."""

    password = ReadOnlyPasswordHashField(
        label=_('Password'),
        help_text=_('Raw passwords are not stored, so there is no way to see'
                    'this user\'s password, but you can change the password '
                    'using <a href ="password"/>this form</a>')
        )

    class Meta:
        model = apps.get_model(settings.AUTH_USER_MODEL)
        fields = "__all__"

    def clean_password(self):
        return self.initial.get('password')


class ComapanyDetails(forms.ModelForm):
    class Meta:
        db_table = 'Comapany_data'
        model = Company
        fields = ('Company_Name', 'Legal_Name', 'PAN_CARD', 'Tax_ID', 'Address_Line_1', 'Address_Line_2', 'Locality', 'City', 'State', 'Country', 'Postal_Code')
        exclude = ('created_on', 'updated_on')