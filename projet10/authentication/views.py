from authentication.serializers import UserSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


class SignUpAPIView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)







