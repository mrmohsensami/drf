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