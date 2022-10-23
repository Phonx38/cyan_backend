from rest_framework.response import Response
from django.shortcuts import render
from .models import Company
from rest_framework import viewsets, generics
from .serializers import AnalyticSerializer, CompanySerializer
from django.db.models import Count
from django.db.models import Q
from rest_framework.decorators import api_view

# Create your views here.


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


@api_view(["GET"])
def analytics(request):

    store = Company.objects.filter(company_type="STORE")
    dist = Company.objects.filter(company_type="DISTRIBUTOR")
    prod = Company.objects.filter(company_type="PRODUCTION")

    grocery = Company.objects.filter(category="GROCERIES")
    electronic = Company.objects.filter(category="ELECTRONICS")
    stationery = Company.objects.filter(category="STATIONERY")
    furniture = Company.objects.filter(category="FURNITURE")
    construction = Company.objects.filter(category="CONSTRUCTION")

    total_dist = sum(i.budget for i in dist)
    total_store = sum(i.budget for i in store)
    total_prod = sum(i.budget for i in prod)
    total_company_type_budget = total_dist + total_store + total_prod
    dist_percentage = (total_dist * 100) / (total_company_type_budget)
    store_percentage = (total_store * 100) / (total_company_type_budget)
    prod_percentage = (total_prod * 100) / (total_company_type_budget)

    total_grocery = sum(i.budget for i in grocery)
    total_electronic = sum(i.budget for i in electronic)
    total_stationery = sum(i.budget for i in stationery)
    total_furniture = sum(i.budget for i in furniture)
    total_construction = sum(i.budget for i in construction)
    total_category_budget = (
        total_grocery
        + total_electronic
        + total_stationery
        + total_furniture
        + total_construction
    )
    grocery_percentage = (total_grocery * 100) / (total_category_budget)
    electronic_percentage = (total_electronic * 100) / (total_category_budget)
    stationery_percentage = (total_stationery * 100) / (total_category_budget)
    furniture_percentage = (total_furniture * 100) / (total_category_budget)
    construction_percentage = (total_construction * 100) / (total_category_budget)

    return Response(
        [
            {
                "label": "stores",
                "val": store_percentage,
            },
            {
                "label": "distributors",
                "val": dist_percentage,
            },
            {
                "label": "productions",
                "val": prod_percentage,
            },
            {
                "label": "groceries",
                "val": grocery_percentage,
            },
            {
                "label": "electronics",
                "val": electronic_percentage,
            },
            {
                "label": "stationeries",
                "val": stationery_percentage,
            },
            {
                "label": "furnitures",
                "val": furniture_percentage,
            },
            {
                "label": "constructions",
                "val": construction_percentage,
            },
        ],
    )
