from __future__ import unicode_literals
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddelware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated() and request.user.timezone:
            timezone.activate(request.user.timezone)
        else:
            timezone.deactivate(user)