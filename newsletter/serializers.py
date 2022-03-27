from rest_framework import serializers


class SUbscriptionDataSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)


class SubscriptionSerializer(serializers.Serializer):
    """Serializer for the subscription object"""

    type = serializers.CharField(required=True)
    fired_at = serializers.DateTimeField(required=True)
    data = SUbscriptionDataSerializer(required=True)
