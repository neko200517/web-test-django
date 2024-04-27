from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from .serializers import (
    UserSerializer,
    SegmentSerializer,
    BrandSerializer,
    VehicleSerializer,
)
from .models import Segment, Brand, Vehicle


# ユーザー作成
# generics.CreateAPIView・・・登録（POST）
class CreateUserView(generics.CreateAPIView):
    # UserSerializerを割り当て
    serializer_class = UserSerializer
    # # 認証なしでもアクセス可能にする
    permission_classes = (permissions.AllowAny,)


# ログインしているユーザーのユーザー情報を返す
# generics.RetrieveUpdateAPIView・・・取得（GET, PUT, PATCH）
class ProfileUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    # ログインユーザーを返す
    def get_object(self):
        return self.request.user

    # PUTで呼び出し場合
    def update(self, request, *args, **kwargs):
        # エラーを返す（テスト用）
        respose = {"mesage": "PUT method is not allowed"}
        return Response(respose, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # PATCHで呼び出した場合
    def partial_update(self, request, *args, **kwargs):
        # エラーを返す（テスト用）
        respose = {"mesage": "PATCH method is not allowed"}
        return Response(respose, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# SegmentのCRUD操作を行う
class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer


# BrandのCRUD操作を行う
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# VehicleのCRUD操作を行う
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    # Vehicleを新規作成する
    def perform_create(self, serializer):
        # user属性に現在ログイン中のユーザーを割り当て
        serializer.save(user=self.request.user)
