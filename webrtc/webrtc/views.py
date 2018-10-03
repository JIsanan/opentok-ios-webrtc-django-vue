from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from opentok import OpenTok, MediaModes, Roles

api_key = 1111
api_secret = 1111
opentok = OpenTok(api_key, api_secret)


class OpenTok(ViewSet):

    def list(self, request):
        return Response("wow galing")
