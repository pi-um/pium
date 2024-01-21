from django.http import JsonResponse
from django.shortcuts import render, redirect
from . import models
from .models import AskInformation


# faq
def faqTemplate(request):
    faqList = models.Faq.objects.all().filter(useyn=True)
    return render(request, "faq/faq.html", {'faqPost': faqList})

# 1대1문의
def askInformation(request):
    askList = models.AskInformation.objects.all().filter(use_yn=True).order_by('-reg_date')
    for ask in askList:
        askLabel = get_status_display(ask.status)
        ask.dateFix = ask.reg_date.strftime('%m월 %d일')
        ask.askLabel = askLabel
    return render(request, "faq/community.html", {'askList': askList})

# 1 대 1 문의 본인인증
def get_askInformation(request):
    if request.method == "GET":
        askList = models.AskInformation.objects.all().filter(use_yn=True, email=request.GET.get("email")).order_by('-reg_date')

        for ask in askList:
            askLabel = get_status_display(ask.status)
            ask.dateFix = ask.reg_date.strftime('%m월 %d일')
            ask.askLabel = askLabel

        data = {
            'data': list(askList.values()),
            'status': 'success'
        }

        return JsonResponse(data)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def post_ask_form(request):
    if request.method == 'POST':
        askData = AskInformation()
        askData.status = request.POST['status']
        askData.name = request.POST['name']
        askData.email = request.POST['email']
        askData.title = request.POST['title']
        askData.content = request.POST['content']
        askData.save()
        return redirect('askInformationPage')

# 1대1 문의 문자열 유형 문자열 변환
def get_status_display(req):
    if req == "P" or req == "p":
        return "결제/예약"
    elif req == "A":
        return "상담"
    else:
        return "기타"

def askform(request):
    return render(request, "faq/askFrom.html")

