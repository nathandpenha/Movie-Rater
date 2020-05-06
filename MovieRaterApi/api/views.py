from django.shortcuts import render
from .models import Movie, Rating
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import  action
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import MovieSerializer, RatingSerializer, UserSerializer
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = UserSerializer



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)

    @action(detail=True,methods=['POST'])
    def rate_movie(self, request, pk=None):
        print("hello")
        print(request.data)
        if 'stars' in request.data:
            #print(request.POST.items())
            stars = request.data['stars']
            user = request.user
            #user = User.objects.get(id=1)
            print('user',user.username)

            movie = Movie.objects.get(id=pk)
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                seralizer = RatingSerializer(rating, many= False)

                response = {'message': 'updated','result':seralizer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                Rating.objects.get(user=user.id, movie=movie.id,stars=stars)
                seralizer = RatingSerializer(rating, many= False)

                response = {'message': 'created','result':seralizer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'its not working'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
