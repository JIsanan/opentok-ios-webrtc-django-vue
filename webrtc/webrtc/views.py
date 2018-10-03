from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from opentok import OpenTok, MediaModes, Roles
import uuid

api_key = '46131672'
api_secret = 'd2f75f9d0f27a7d52a4ebb0fe7b93ab34aa4511c'
opentok = OpenTok(api_key, api_secret)


class OpenTok(ViewSet):

    def create(self, request):
        session = opentok.create_session(media_mode=MediaModes.routed)
        token = opentok.generate_token(session.session_id,
                                       role=Roles.publisher)
        response = {
            'message': 'successfully started session',
            'session_id': session.session_id,
            'apikey': api_key,
            'token': token,
        }
        return Response(response)

    @action(methods=['post'], detail=False)
    def start_archive(self, request):
        archive = opentok.start_archive(request.data['session_id'], name='Videos')
        response = {
            'message': 'successfully started arhciving',
            'archive_id': archive.id}
        return Response(response)

    @action(methods=['post'], detail=False)
    def stop_archive(self, request):
        opentok.stop_archive(request.data['archive_id'])
        return Response({'message': 'successfully stopped archiving'})

    @action(methods=['post'], detail=False)
    def get_archive(self, request):
        archive = opentok.get_archive(request.data['uuid'])
        return Response({'url': archive.url})
