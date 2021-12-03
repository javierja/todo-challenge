from rest_framework.views import APIView
from tasks.models import User, Task
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from tasks.serializers import UserSerializer, TasksSerilizer, TasksSerilizerUpdt
from rest_framework.permissions import IsAuthenticated



#Creo la ApiView para el Login

class UserLogin(APIView):

    def post(self,request):

        email=request.data['email']
        password=request.data['password']
        user=User.objects.filter(email=email).first()
        user_id=User.objects.filter(email=email).values_list('id',flat=True).first()
        if user is None:

            raise AuthenticationFailed('Usuario o Contraseña invalidos')

        if not user.check_password(password):

            raise AuthenticationFailed('Usuario o Contraseña invalidos')

    
       #Capturo el token para el usuario
        usertoken=str(AccessToken.for_user(user))

        print (usertoken)
        return Response({
            'message': 'Logueado Correctamente',
            'jwt': usertoken,
            'user_id':user_id
        },status=status.HTTP_200_OK)

#Creo Api para busqueda
class SearchView(APIView):
    permission_classes = (IsAuthenticated,)
    

    def post(self,request):
     
        if request.data['fecha'] != '':
            fecha=request.data['fecha']
       
            queryset = Task.objects.select_related('user').filter(created_at=fecha)
            
            tasks=[]
            for task in queryset:
                tasks.append({'titulo': task.titulo, 'descripcion': task.descripcion, 'fecha': task.created_at, 'user': task.user.username})
            return Response(data=tasks,status=status.HTTP_200_OK)

        elif request.data['descripcion'] != '':
            descripcion=request.data['descripcion']
            queryset1 = Task.objects.filter(descripcion__contains=descripcion)

            tasks1=[]
            for task1 in queryset1:
                tasks1.append({'titulo': task1.titulo, 'descripcion': task1.descripcion, 'fecha': task1.created_at})
            return Response(data=tasks1,status=status.HTTP_200_OK)

        elif request.data['user'] != '':
            user=request.data['user']
            queryset1 = Task.objects.select_related('user').filter(user__username=user)

            tasks1=[]
            for task1 in queryset1:
                tasks1.append({'titulo': task1.titulo, 'descripcion': task1.descripcion, 'fecha': task1.created_at,'user':task1.user.username})
            return Response(data=tasks1,status=status.HTTP_200_OK)

         
#Creo Api para listar tareas completadas
class CompletedView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        completados = Task.objects.filter(completada=True).values('titulo','descripcion','created_at').order_by('-created_at')
        print(completados)

        return Response(data=completados,status=status.HTTP_200_OK)