from django.http import JsonResponse
from django.shortcuts import render, redirect

from accounts.models import RecommendMarkup, ReservationUser, PersonalColor
from reservation.models import Reservation



# Create your views here.

def login_view(request):
    return render(request, 'accounts/login.html')

def loginConfirm(request):
    if request.method == 'GET':
        request.GET.get("email")
        user = ReservationUser.objects.all().filter(email=request.GET.get("email"))

        if user.count() > 0:
            return JsonResponse({'status': 'success', 'message': 'successData'})
        else:
            return JsonResponse({'status': 'emailNone', 'message': 'Invalid request method.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def myPage(request):
    if request.method == 'GET':
        email = request.GET.get('email')

    user = ReservationUser.objects.all().filter(email=email)
    reservation = Reservation.objects.filter(user=email)
    res_data = list(reservation.values())

    if len(res_data) == 0:
        res_data = [
            {
                'status': 'custom',
                'user': 'custom',
                'course': 'custom'
             }
        ]
    
    print(res_data)
    user_data = list(user.values())

    if user.count() <= 0:
        return redirect("login")

    personalColor = {
        "SPRINGBLIGHT": "봄 브라이트",
        "SPRINGLIGHT": "봄 라이트",
        "SUMMERBLIGHT": "여름 브라이트",
        "SUMMERLIGHT": "여름 라이트",
        "SUMMERMUTE": "여름 뮤트",
        "FALLMUTE": "가을 뮤트",
        "FALLDEEP": "가을 딥",
        "WINTERBLIGHT": "겨울 브라이트",
        "WINTERDEEP": "겨울 딥",
    }

    for e in user:
        if e.consultResult:
            type = list(RecommendMarkup.objects.all().filter(type=str(e.consultResult)).values())
        if e.consultResult02:
            type02 = list(RecommendMarkup.objects.all().filter(type=str(e.consultResult02)).values())

    try:
        if e.consultResult02:
            data = {
                "userName": user_data[0].get("name"),
                "res_data": res_data[0],
                "typeTitle": personalColor.get(type[0].get("type")),
                "type02Title": personalColor.get(type02[0].get("type")),
                "type": type,
                "type02": type02
            }
        else:
            data = {
                "userName": user_data[0].get("name"),
                "res_data": res_data[0],
                "typeTitle": personalColor.get(type[0].get("type")),
                "type": type
            }
    except:
        data = {
            "userName": user_data[0].get("name"),
            "res_data": res_data[0]
        }

    return render(request, 'accounts/mypage.html', {"data": data})
