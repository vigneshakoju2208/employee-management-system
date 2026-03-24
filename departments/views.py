from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .models import Department
from .serializers import DepartmentSerializer
from users.permissions import IsAdmin, IsManager
from rest_framework.permissions import IsAuthenticated

class DepartmentPagination(PageNumberPagination):
    page_size = 5

class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.prefetch_related('employees')
    serializer_class = DepartmentSerializer
    pagination_class = DepartmentPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAdmin]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsManager]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
