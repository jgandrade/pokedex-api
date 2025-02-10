from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseController(APIView):
    def json_response(self, data, code=status.HTTP_200_OK):
        return Response(data, status=code)

    def not_found(self, message="Not found"):
        return Response({"message": message}, status=status.HTTP_404_NOT_FOUND)

    def unauthorized(self, message="Unauthorized"):
        return Response({"message": message}, status=status.HTTP_401_UNAUTHORIZED)
