from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerializer
from .models import Post
from rest_framework import status
from rest_framework.permissions import IsAdminUser

@api_view(['GET', 'POST'])
def test(request):
    if request.method == 'POST':
        name = request.data['name']
        return Response({'name': f'my name is {name}'})
    else:
        return Response({'name': 'my name is mohsen'})

@api_view()
def all(request):
    posts = Post.objects.all()
    ser_data = PostSerializer(posts, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)

@api_view()
@permission_classes([IsAdminUser])
def detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return Response({'error': 'this user doese not exist'}, status=status.HTTP_404_NOT_FOUND)
    ser_data = PostSerializer(post)
    return Response(ser_data.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    info = PostSerializer(data=request.data)
    if info.is_valid():
        # Post(title=info.validated_data['title'], body=info.validated_data['body']).save()
        info.save()
        return Response({'message': 'OK'}, status=status.HTTP_201_CREATED)
    else:
        return Response(info.errors, status=status.HTTP_400_BAD_REQUEST)