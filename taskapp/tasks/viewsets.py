from rest_framework import response, viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from tasks.models import User, Task
from tasks.serializers import UserSerializer, TasksSerilizer, TasksSerilizerUpdt
from rest_framework.permissions import IsAuthenticated


### Creo el viewset para las peticiones de los usuarios (listar, detalle, actualizar, crear, y borrar)
class UsersViewSet(viewsets.ViewSet):
#utilizo el permiso del JWT para acceder solo si esta autenticado
    # permission_classes = (IsAuthenticated,)


    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):

        user=User.objects.get(pk=pk)
        serializer=UserSerializer(user,data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response({'message':'Usuario actualizado correctamente'},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):

        user=User.objects.get(pk=pk)
        user.delete()
        return Response({'message':'Usuario eliminado Correctamente!'}, status=status.HTTP_200_OK)


### Creo el viewset para las peticiones de las tareas (listar, detalle, actualizar, crear, y borrar)
class TasksViewSet(viewsets.ViewSet):
#utilizo el permiso del JWT para acceder solo si esta autenticado
    permission_classes = (IsAuthenticated,)


    def list(self, request):
        queryset = Task.objects.all()
        serializer = TasksSerilizer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task= get_object_or_404(queryset, pk=pk)
        serializer = TasksSerilizer(task)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request,*args, **kwargs):
        serializer=TasksSerilizer(data=request.data,context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Tarea creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):

        task=Task.objects.get(pk=pk)
        serializer=TasksSerilizerUpdt(task,data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response({'message':'Tarea actualizada correctamenta'},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):

        task=Task.objects.get(pk=pk)
        task.delete()
        return Response({'message':'Tarea eliminada Correctamenta!'}, status=status.HTTP_200_OK)