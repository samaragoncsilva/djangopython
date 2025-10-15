from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'telefone', 'first_name', 'last_name']
        
    def create(self, validated_data):
        if 'password' in validated_data:
                # Criptografa a senha antes de salvar no banco
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
                    # Criptografa a nova senha antes de salvar no banco
            instance.password = make_password(validated_data.pop('password'))
        return super().update(instance, validated_data)