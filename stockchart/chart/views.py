from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import *


def home(request):
    form1 = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['symbol']
            url = "https://docker.api.srifintech.com/testassignment"
            data = {
                "ticker" : str(value)
            }
            res = requests.post(url=url,json=data).json()
            strike = res['strike']
            calloi = res['calloi']
            putoi = res['putoi']
            context = {
                'strike' : strike,
                'calloi': calloi,
                'putoi':putoi,
                'is_post':True,
                'form': form
            }
        return render(request,"chart/index.html", context)

    context = {
            "form": form1
        }
    return render(request, "chart/index.html", context)
