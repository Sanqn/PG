from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, generics, permissions
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import NewPersonHeroSerializer, RegisterSerializer, UserSerializer, ContactsUserSerializer
from .models import NewPerson, ContactsUser


class ContactsUsersView(viewsets.ModelViewSet):
    serializer_class = ContactsUserSerializer
    queryset = ContactsUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]


def main(request):
    return HttpResponse("It's work")


class NewPersonViewsets(viewsets.ModelViewSet):
    queryset = NewPerson.objects.all().order_by('first_name')
    serializer_class = NewPersonHeroSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'first_name'


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # user = serializer.save()
        return Response({
            # "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Пользователь успешно создан",
            'data': serializer.data
        })


class UsersView(APIView):
    def get(self, request):
        w = User.objects.all()
        serializer = UserSerializer(w, many=True)
        return Response({'user': serializer.data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # new_user = User.objects.create(
        #     username=request.data['username'],
        #     password=request.data['password']
        # )
        # return Response({'message': 'User created',
        #                  'user': UserSerializer(new_user).data})
        return Response({'message': 'User created',
                         'user': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'insert key'})
        try:
            instance = User.objects.get(pk=pk)
        except:
            return Response({'error': 'not created'})

        serializer = UserSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'user uodate': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(pk=pk).delete()
        return Response({'data': str(user)})


class FindUser(APIView):
    def get(self, request):
        users = NewPerson.objects.all()
        return Response({'user': NewPersonHeroSerializer(users, many=True).data})


class FindUserOne(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response({'data': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        user = User.objects.get(pk=pk).delete()
        return Response({'data': str(user)})


class UserApiViewList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateList(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserOne(APIView):

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Bad request'})
        inst = User.objects.get(pk=pk)
        serializer = UserSerializer(data=request.data, instance=inst)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AllUsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # queryset = User.objects.all()[:3]

    def get_queryset(self, **kwargs):
        pk = self.kwargs.get('pk')
        if not pk:
            return User.objects.all()[:3]
        return User.objects.filter(pk=pk)
