from django.contrib import admin

from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from manager.models import ExpenseItem, ExpenseCategory, ExpenseAccount


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ExpenseItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpenseItem
        fields = (
            'title',
            'type',
            'account',
            'date',
            'amount',
            'description',
        )


class ExpenseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = (
            'name',
            'slug',
        )


class ExpenseAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExpenseAccount
        fields = (
            'name',
            'slug',
            'balance',
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ExpenseItemViewSet(viewsets.ModelViewSet):
    queryset = ExpenseItem.objects.all()
    serializer_class = ExpenseItemSerializer


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class ExpenseAccountViewSet(viewsets.ModelViewSet):
    queryset = ExpenseAccount.objects.all()
    serializer_class = ExpenseAccountSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'expenses', ExpenseItemViewSet)
router.register(r'category', ExpenseCategoryViewSet)
router.register(r'account', ExpenseAccountViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'router/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include('manager.urls')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('manager.urls')),
#     url(r'^api-auth/', include('rest_framework.urls'))
# ]
