from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, EmprestimoViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'emprestimos', EmprestimoViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
