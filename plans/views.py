from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from .models import Plan

# django views listview
from django.views.generic import ListView
from django.conf import settings


from rest_framework import viewsets
from rest_framework import permissions

from .models import Plan
from .serializers import PlanSerializer



# scrape
from .scraper import *

# adding plans to database
def add_plans(plans=None):
    if plans is None:
        plans = scrape_plans()
    # only delete if there are plans
    if plans:
        # remove old plans
        Plan.objects.all().delete()
        print("deleted old plans")
        # add new plans
        for plan in plans:
            Plan.objects.get_or_create(
                price=plan["price"],
                extra_data=plan["priceInfo"],
                benifits=plan["benifits"],
            )
        print("Plans added to database")


if settings.ONE_TIME:
    plans = scrape_plans()
    print(plans)
    add_plans(plans)

class PlanList(ListView):
    model = Plan
    template_name = 'plans/list.html'
    context_object_name = 'plans'


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]