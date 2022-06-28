from django.contrib.auth.models import User
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

User = get_user_model()
from .models import NewPerson, ContactsUser


class ContactsUserSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    iduserCreator = serializers.SlugRelatedField(slug_field="id", queryset=User.objects.all())

    class Meta:
        model = ContactsUser
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'photo', 'notes', 'iduserCreator', 'tags')
        # extra_kwargs = {"iduserCreator": {"read_only": True}}


class NewPersonHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewPerson
        fields = ('id', 'first_name', 'last_name', 'email', 'work_experience')
        lookup_field = 'first_name'
        extra_kwargs = {
            'url': {'lookup_field': 'first_name'}
        }


class RegisterSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        read_only_fields = ['username']
        fields = [
            # "username",
            "email",
            "password",
            # "password2",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, validated_data):
        # username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        # password2 = validated_data["password2"]
        if not password:
            raise serializers.ValidationError({"password": "Введите пароль"})
        user = User(email=email)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, trim_whitespace=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {"password": {"write_only": True}, "email": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance

# class WoomenModel:
#
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# class WoomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#
#
# def encode():
#     model = WoomenModel('Gooroo', 'Hooroo')
#     model_st = WoomenSerializer(model)
#     print(model_st.data, type(model_st.data)) #{'title': 'Gooroo', 'content': 'Hooroo'}
#     render = JSONRenderer().render(model_st.data)
#     print(render) #b'{"title":"Gooroo","content":"Hooroo"}'
#
# def decode():
#     streem = io.BytesIO(b'{"title":"Gooroo","content":"Hooroo"}')
#     data = JSONParser().parse(streem)
#     print(data) # {'title': 'Gooroo', 'content': 'Hooroo'}
#     serializer = WoomenSerializer(data=data)
#     print(serializer) #WoomenSerializer(data={'title': 'Gooroo', 'content': 'Hooroo'}):
#                         # title = CharField(max_length=255)
#                         # content = CharField()
#     serializer.is_valid()
#     print(serializer.validated_data) # OrderedDict([('title', 'Gooroo'), ('content', 'Hooroo')])
