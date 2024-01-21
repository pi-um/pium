from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.db.models import SET_NULL

from base import settings


# Create your models here.
# 커스텀 유저모델을 위해 기존 유저모델 상속 자세한내용을 원하면 AbstractUser 컨트롤 클릭
class User(AbstractUser):
    pass


class PersonalColor(models.TextChoices):
    SPRINGBLIGHT = "SPRINGBLIGHT", "봄 브라이트"
    SPRINGLIGHT = "SPRINGLIGHT", "봄 라이트"
    SUMMERBLIGHT = "SUMMERBLIGHT", "여름 브라이트"
    SUMMERLIGHT = "SUMMERLIGHT", "여름 라이트"
    SUMMERMUTE = "SUMMERMUTE", "여름 뮤트"
    FALLMUTE = "FALLMUTE", "가을 뮤트"
    FALLDEEP = "FALLDEEP", "가을 딥"
    WINTERBLIGHT = "WINTERBLIGHT", "겨울 브라이트"
    WINTERDEEP = "WINTERDEEP", "겨울 딥"

    def __str__(self):
        # Customize the representation for each choice
        custom_repr = {
            self.SPRINGBLIGHT: "봄 브라이트",
            self.SPRINGLIGHT:  "봄 라이트",
            self.SUMMERBLIGHT: "여름 브라이트",
            self.SUMMERLIGHT: "여름 라이트",
            self.SUMMERMUTE: "여름 뮤트",
            self.FALLMUTE: "가을 뮤트",
            self.FALLDEEP: "가을 딥",
            self.WINTERBLIGHT: "겨울 브라이트",
            self.WINTERDEEP: "겨울 딥",
        }

        return custom_repr.get(self, super().__str__())

class RecommendMarkup(models.Model):
    class TOOL(models.TextChoices):
        BASE = "BASE", "베이스"
        SHADOW = "SHADOW", "쉐도우"
        BLUSHER = "BLUSHER", "블러셔"
        LIP = "LIP", "립"

    type = models.CharField(choices=PersonalColor.choices, default=PersonalColor.SPRINGBLIGHT, max_length=50)
    content = models.TextField()
    tool = models.CharField(choices=TOOL.choices, null=True, blank=True, max_length=20)

    link = models.URLField(blank=True)
    class Meta:
        verbose_name = verbose_name_plural = "화장품추천"


class ReservationUser(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    consultResult = models.CharField(choices=PersonalColor.choices,null=True, blank=True, max_length=50)
    consultResult02 = models.CharField(choices=PersonalColor.choices, null=True, blank=True, max_length=50)
    memo = models.TextField(blank=True, null=True)
    reg_date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = verbose_name_plural = "회원관리"
