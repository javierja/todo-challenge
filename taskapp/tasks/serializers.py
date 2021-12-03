from os import write
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from tasks.models import User, Task




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields='__all__'

#validacion de creacion y encriptacion del password al guardar
    def create(self, validated_data):
        user=User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated_user=super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


#defino los campos que voy a mostar en el get
    
    def to_representation(self, instance):

        return {

            'username':instance.username,
            'name': instance.name,
            'last_name': instance.last_name,
            'email':instance.email,
            'password':instance.password,
        
        }



class TasksSerilizer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
   
    class Meta:
        model= Task
        fields= ['titulo','descripcion','completada','user']

    def save(self, **kwargs):
        """Include default for read_only `user` field"""
        kwargs["user"] = self.context['request'].user
        return super().save(**kwargs)

    def to_representation(self, instance):

        return {

            'titulo':instance.titulo,
            'descripcion': instance.descripcion,
            'completada': instance.completada,
            'created_at':instance.created_at
        
        }

class TasksSerilizerUpdt(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(required=False,read_only=True)
    class Meta:
        model= Task
        fields='__all__'


    
        
