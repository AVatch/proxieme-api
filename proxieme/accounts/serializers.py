from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        extra_kwargs = {'password': {'write_only': True, 'allow_blank': True}}
        read_only_fields = ('last_login',)

    def create(self, validated_data):
        account = Account(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        account.set_password(validated_data['password'])
        
        account.save()
        return account

    def update(self, instance, validated_data):

        # update account email logic
        # -- TBD

        # update account fields
        instance.first_name = validated_data.get('first_name', 
            instance.first_name)
        instance.last_name = validated_data.get('last_name', 
            instance.last_name)

        # update account password
        if validated_data['password'] == '':
            pass
        else:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance
