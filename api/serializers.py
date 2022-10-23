from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class AnalyticSerializer(serializers.ModelSerializer):
    total_store = serializers.IntegerField()
    total_prod = serializers.IntegerField()
    total_dist = serializers.IntegerField()

    class Meta:
        model = Company
        fields = ("total_store", "total_dist", "total_prod")
