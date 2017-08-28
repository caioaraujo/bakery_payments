from rest_framework import serializers

from branch.serializers import BranchSerializer
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    value = serializers.FloatField(help_text="Payment value (R$)", required=True)
    expiration_date = serializers.DateField(help_text="Date when payment will expires", required=True)
    branch = serializers.IntegerField(help_text="Unique identifier of branch", required=True)

    class Meta:
        model = Payment
        fields = ('value', 'expiration_date', 'branch')

class PaymentResponseSerializer(serializers.ModelSerializer):

    branch = BranchSerializer()

    class Meta:
        model = Payment
        fields = ('id', 'value', 'expiration_date', 'branch')