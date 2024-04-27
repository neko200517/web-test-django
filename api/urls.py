from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework.routers import DefaultRouter

# Router:ビューとURLを紐づけ
router = DefaultRouter()
router.register("segments", views.SegmentViewSet)
router.register("brands", views.BrandViewSet)
router.register("vehicles", views.VehicleViewSet)

app_name = "api"

# エンドポイントの登録
urlpatterns = [
    # genericsのviewはas_viewでビューにキャスト
    path("create/", views.CreateUserView.as_view(), name="create"),
    path("profile/", views.ProfileUserView.as_view(), name="profile"),
    # トークン取得用エンドポイント
    path("auth/", obtain_auth_token, name="auth"),
    # ルートにアクセスがあった場合、登録したRouterを参照する
    path("", include(router.urls)),
]
