from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated and request.path_info != reverse('login'):
            # Redirect unauthenticated users to the login page
            return redirect(reverse('login'))

        response = self.get_response(request)
        return response
