from django.contrib.auth.models import AbstractUser
from django.db import models
from lms.models import Course, Lesson


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    country = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Pay(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date_pay = models.DateTimeField(auto_now_add=True)
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, null=True, blank=True
    )
    payment_method = models.CharField(
        max_length=150, verbose_name="Способ оплаты", null=True
    )
    payment_amount = models.PositiveIntegerField(
        verbose_name="Цена", help_text="Укажите цену"
    )
    session_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Id сессии",
        help_text="Укажите Id сессию",
    )
    link = models.URLField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату",
    )

    def __str__(self):
        return f"{self.payment_amount}"

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплата"
