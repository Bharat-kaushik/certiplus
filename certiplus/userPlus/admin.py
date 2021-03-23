from django.contrib.auth.admin import UserAdmin
from userPlus.forms import *
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.conf.urls import url
from django.contrib import admin
from userPlus import models
from django.contrib import messages
from django.contrib.admin import ModelAdmin
from userPlus import signals
from userPlus.models import Country,Otp
from userPlus.models import Logo





sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


class BaseUserAdmin(UserAdmin):
    form = UserChagneForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    change_user_password_template = None
    list_display = ( 'username','name',  'is_active', 'is_staff', 'timezone',
                    'is_Verified', 'last_login')

    """
    Set fieldsets to control the layout of admin “add” and “change” pages.
    """
    fieldsets = (
        (None, {
            'fields': ('password', 'name', 'email',)
        }),
        ('Security', {
            'fields': (
            'is_active', 'is_superuser', 'is_staff', 'timezone', 'last_login_ip', 'groups', 'user_permissions',),
        }),
        ('Important dates', {
            'fields': ('last_login', 'created_on', 'updated_on',),
        }),
    )

    """
    The add_fieldsets class variable is used to define the fields that will be displayed on the create user page.
    """
    add_fieldsets = (
        (None, {
            'fields': ('username', 'name', 'mobile', ),
        }),
        ('Preferences', {
            'fields': ('timezone', 'is_active'),
        }),
        ('Security', {
            'fields': ( 'is_superuser', 'is_staff', 'groups', 'user_permissions',),
        }),
    )
    search_fields = ('email', 'name',)
    ordering = ('email',)
    readonly_fields = ('last_login', 'created_on', 'updated_on',)
    actions = ('reset_passwords',)
    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ('is_active', 'is_Verified')

    def queryset(self, request):
        queryset = super(BaseUserAdmin, self).queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.exclude(is_superuser=True)
        return queryset

    def get_urls(self):
        return [url(r'^(/d+)/change/password/$',
                    self.admin_site.admin_view(self.user_change_password))
                ] + super(BaseUserAdmin, self).get_urls()

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(BaseUserAdmin, self).get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            readonly_fields = list(readonly_fields)
            readonly_fields.append('is_superuser')
            readonly_fields = set(readonly_fields)
        return readonly_fields

    """ 
    figure out where to redirect after the 'save' button has been pressed
    when adding a new object.
    """

    # def response_post_save_add(self, request, obj):
    #     response = super(BaseUserAdmin, self).response_post_save_add(request, obj)
    #     # change the password to a random password
    #     pw = obj.set_random_password()
    #     print('User {}\'s new random password: {}'.format(obj.email, pw))
    #     self.message_user(request, 'User {}\'s new random password: {}'.format(obj.email, pw), messages.SUCCESS)
    #     return response


class BaseCompanyAdmin(ModelAdmin):
    form = ComapanyDetails
    search_fields = ('Company_Name',)
    list_display = ('Company_Name', 'Legal_Name', 'Tax_ID', 'PAN_CARD', 'Address_Line_1', 'Address_Line_2', 'Locality', 'City', 'State', 'Country', 'Postal_Code',)
    readonly_fields = ('created_on', 'updated_on',)

    fieldsets = (
        (None, {
            'fields': ('Company_Name', 'Legal_Name', 'PAN_CARD', 'Tax_ID',)
        }),
        ('Address', {
            'fields': ('Address_Line_1', 'Address_Line_2', 'Locality', 'City', 'State', 'Country', 'Postal_Code'),
        }),
        ('Security', {
            'fields': (
                'created_on', 'updated_on'),
        }),
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        if 'Company_Name' in form.changed_data:
            signals.company_name_change.send(
                sender=self.__class__, request=request, user=request.user, company=obj,
                old_name=form.initial.get('Company_Name'),
                new_name=obj.Company_Name)
        super(BaseCompanyAdmin, self).save_model(request, obj, form, change)


# Register your models here.
admin.site.register(models.Company, BaseCompanyAdmin)
admin.site.register(models.User, BaseUserAdmin)
admin.site.register(Country)
admin.site.register(Otp)


class LogoAdmin(ModelAdmin):
    def has_add_permission(self, request):
        if len(Logo.objects.all()) >= 1:
            return False
        else:
            return True

admin.site.register(Logo, LogoAdmin)