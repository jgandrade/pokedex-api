from functools import wraps
from django.http import JsonResponse
from modules.users.domain.services.jwtService import JWTService


def require_jwt(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization", None)

        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"message": "Unauthorized"}, status=401)

        token = auth_header.split(" ")[1]

        try:
            payload = JWTService.decode_token(token)
            request.jwt_payload = payload
        except ValueError as e:
            return JsonResponse({"message": str(e)}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper
