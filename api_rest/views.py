from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def get_movies(request):

    if request.method == 'GET':

        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_by_id(request, id):

    try:
        movie_id = Movie.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = MovieSerializer(movie_id)
        return Response(serializer.data)
    
    if request.method == 'PUT':

        serializer = MovieSerializer(movie_id, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
          
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'POST', 'PUT'])
def movie_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['movie_id']:
                id = request.GET['movie_id']

                try:
                    movie_id = Movie.objects.get(pk=id)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = MovieSerializer(movie_id)
                return Response(serializer.data)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        new_movie = request.data

        serializer = MovieSerializer(data=new_movie)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':

        id = request.data['movie_id']

        try:
            updated_movie = Movie.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(updated_movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_movie(request, id):
    try:
        movie_to_delete = Movie.objects.get(pk=id)
        movie_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
