from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from kitsune.sumo.urlresolvers import reverse


class LogoutDeactivatedUsersMiddleware(object):
    """Verifies that user.is_active == True.

    If a user has been deactivated, we log them out.
    """
    def process_request(self, request):

        user = request.user

        if user.is_authenticated() and not user.is_active:

            logout(request)
            return HttpResponseRedirect(reverse('home'))
