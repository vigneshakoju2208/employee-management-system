from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
from users.permissions import IsAdmin, IsManager
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            permission_classes = [IsAdmin]
        elif self.action in ['create', 'update', 'partial_update']:
            permission_classes = [IsManager]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception:
            return Response(
                {"error": "Unable to delete employee"},
                status=status.HTTP_400_BAD_REQUEST
            )
