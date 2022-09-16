from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from .models import Post

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
    return Response(ser_data.data)

@api_view()
def detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return Response({'error': 'this user doese not exist'})
    ser_data = PostSerializer(post)
    return Response(ser_data.data)