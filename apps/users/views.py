"""ViewSets quản lý danh mục vai trò và thông tin tài khoản người dùng/nhân viên."""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.models import NguoiDung, VaiTro
from apps.users.serializers import NguoiDungSerializer, RegisterSerializer, VaiTroSerializer


class VaiTroViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet chỉ đọc để truy vấn danh mục vai trò hệ thống."""

    queryset = VaiTro.objects.all()
    serializer_class = VaiTroSerializer
    permission_classes = [AllowAny]


class NguoiDungViewSet(viewsets.ModelViewSet):
    """ViewSet quản lý CRUD danh sách tài khoản người dùng và đăng ký nhân viên mới."""

    queryset = NguoiDung.objects.all().select_related("vai_tro").order_by("-ma_nguoi_dung")
    serializer_class = NguoiDungSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """Trả về serializer phù hợp tùy thuộc vào thao tác tạo mới hay xem danh sách."""
        if self.action in ["create", "register"]:
            return RegisterSerializer
        return NguoiDungSerializer

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request):
        """API hỗ trợ đăng ký tài khoản nhân viên mới."""
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "Đăng ký tài khoản thành công!",
                    "user": NguoiDungSerializer(user).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

