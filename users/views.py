from rest_framework import generics, viewsets, filters
from users.models import Pay, CustomUser
from users.serilazers import (
    PaySerializer,
    CustomUserSerializer,
    MyTokenObtainPairSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .services import convert_rub_to_dollars, create_stripe_price, create_stripe_session


class UserCreateAPIView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PayViewSet(viewsets.ModelViewSet):
    queryset = Pay.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = (
        "paid_course",
        "paid_lesson",
        "payment_method",
    )
    ordering_fields = ("date_pay",)


class PayCreateAPIView(generics.CreateAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        amount_in_dollars = convert_rub_to_dollars(payment.amount)
        price = create_stripe_price(amount_in_dollars)
        session_id, payment_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_link
        payment.save()


class PayListAPIView(generics.ListAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()


class PayRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()


class PayUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PaySerializer
    queryset = Pay.objects.all()


class PayDestroyAPIView(generics.DestroyAPIView):
    queryset = Pay.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
