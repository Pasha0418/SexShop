from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from authentication.service import activate_user


class ActivateUserApiView(GenericAPIView):
    def get(self, request, uid, token):
        response = activate_user(uid, token)
        if response:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(data={"error":"Invalid token for given user."}, status=status.HTTP_204_NO_CONTENT)











