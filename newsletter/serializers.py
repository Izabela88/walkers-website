from rest_framework import serializers


class SubscriptionDataSerializer(serializers.Serializer):
    """Nested fields from mailchimp"""

    id = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)


class SubscriptionSerializer(serializers.Serializer):
    """Serializer for the subscription object. Mailchimp body fields"""

    data = SubscriptionDataSerializer(many=False, required=True)
    type = serializers.CharField(required=True)
    fired_at = serializers.DateTimeField(required=True)
