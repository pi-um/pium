from datetime import timezone

from django.db import models

from accounts.models import ReservationUser


# Create your models here.

class Reservation(models.Model):
    class Status(models.TextChoices):
        RESERVED = "RESERVED", "예약 완료"
        WAITTING = "WAITTING", "예약 대기"
        CANCELLED = "CANCELLED", "예약 취소"

    class BookCourse(models.TextChoices):
        SIMPLE = "SIMPLE", "간단 진단"
        BASIC = "BASIC", "기본 진단"
        BODY = "BODY", "골격 진단"
        PRO = "PRO", "프로 진단"

    id = models.AutoField(primary_key=True)
    status = models.CharField(choices=Status.choices, default=Status.WAITTING, max_length=50)
    course = models.CharField(choices=BookCourse.choices, default=BookCourse.SIMPLE, max_length=50)
    user = models.CharField(max_length=200)
    reservation_many = models.IntegerField(default=1)
    reservation_date = models.DateField(null=False)
    reservation_hour = models.BigIntegerField(null=False)
    reservation_min = models.BigIntegerField(null=False)


    reg_date = models.DateTimeField(auto_now=True)

    def userName(self):
        return self.user.name
    def userEmail(self):
        return self.user.email
    def userPhone(self):
        return self.user.phone

    def show_date_time(self):
        return f"{self.reservation_date} {self.reservation_hour}:{self.reservation_min} "

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = verbose_name_plural = "예약 관리"


class ReservationConstraint(models.Model):
    class Status(models.TextChoices):
        OPEN = "OPEN", "영업 시간"
        CLOSED = "CLOSED", "영업 종료"

    id = models.AutoField(primary_key=True)
    type = models.CharField(choices=Status.choices, default=Status.OPEN, max_length=50)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    class Meta:
        verbose_name = verbose_name_plural = "예약 제약"
