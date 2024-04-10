from django.urls import path
from .views import *

# urlpatterns = [
#     path('deals/', DealListCreate.as_view(), name='deal-list-create'),
#     path('deals/<int:pk>', DealRetrieveUpdateDestroy.as_view(), name='deal-detail'),
#     # path('delete/<int:pk>', DealDetail.as_view(), name='deal-detail'),
#     # path('post/',GenerateRandomDeals.as_view())
# ]

urlpatterns = [
    path('deals/', DealList.as_view(), name='deal-list'),
    path('deals/<int:pk>', DealDetail.as_view(), name='deal-detail'),
]
