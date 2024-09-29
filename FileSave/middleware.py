from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.shortcuts import redirect

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin/'):
            if request.COOKIES.get('access_token') and request.COOKIES.get('refresh_token'):
                    auth = JWTAuthentication()
                    try:
                        access_token = auth.get_validated_token(request.COOKIES.get('access_token'))
                        user = auth.get_user(access_token)
                        if user.is_authenticated:
                            request.user = user
                            if request.path in ['/register/', '/login/']:
                                return redirect('app')
                    except (InvalidToken, TokenError):
                        try:
                            refresh_token = RefreshToken(request.COOKIES.get('refresh_token'))
                            access_token = refresh_token.access_token

                            request.user = auth.get_user(access_token)

                            response = self.get_response(request)
                            response.set_cookie('access_token', access_token, httponly=True)
                            return response
                        except TokenError:
                            response = redirect('login')
                            response.delete_cookie('access_token')
                            response.delete_cookie('refresh_token')
                            return response
            else:
                if request.path not in ['/register/', '/login/']:
                    return redirect('register')
        response = self.get_response(request)
        return response