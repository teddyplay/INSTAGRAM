from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from users.serailizers import RegisUserSerializer
from users.serailizers import ProfileSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate
from users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication







class SignUp(generics.GenericAPIView):
    serializer_class = RegisUserSerializer



    def post(self, request):

        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {"Сообщение":"Пользователь успешно зарегестрирован!",
                        "data":serializer.data
                        }

            return Response(data=response)

        return Response(data=serializer.errors)



class SignIn(APIView):



    def post(self, request:Request):
        email = request.data.get("email",
                                 )
        password = request.data.get("password",
                                    )

        user = authenticate(email=email,
                           password=password,
                            )

        if user is not None:
            refresh = RefreshToken.for_user(user)

            response = {"Сообщение": "Вы успешно вошли в систему!",
                        "Tokens": {"Access":str(refresh.access_token),
                                   "Refresh":str(refresh)},
                        "User": user.username,
                        }
            return Response(data=response)
        else:
            return Response(data={"Сообщение":"Такого пользоваетеля нет в системе , "
                                              "пожалуйста зарегестрируйтесь!"})



    def get(self, request:Request):
        context = {"User": str(request.user),
                   "Auth": str(request.auth),
                   }

        return Response(data=context)




class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]





class EditProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]















