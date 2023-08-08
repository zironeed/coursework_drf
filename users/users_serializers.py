from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email',)


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'tg_name',)

    def save(self, **kwargs):
        user = User(
            email=self.validated_data['email'],
            tg_name=self.validated_data['tg_name'],
            fist_name=self.validated_data['email'],
            last_name=self.validated_data['email'],
            is_superuser=False,
            is_stuff=False,
            is_active=True
        )

        if self.validated_data['password1'] != self.validated_data['password2']:
            raise serializers.ValidationError('Passwords do not match')

        user.set_password(self.validated_data['password1'])
        user.save()

        return user
