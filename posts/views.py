from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer
from users.models import CustomUser
from users.serializers import StatusSerializer


class postsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class postStatusViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = StatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.status = serializer.data['status']
        request.user.save()

        return Response(status=status.HTTP_200_OK)