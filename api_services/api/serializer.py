from rest_framework import serializers
from api_services.models import Company, Employee, Device, Transaction


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    checkout_date = serializers.DateTimeField(format="%B %d, %Y", read_only=True)
    return_date = serializers.DateTimeField(format="%B %d, %Y", required=False, allow_null=True)

    class Meta:
        model = Transaction
        fields = "__all__"
