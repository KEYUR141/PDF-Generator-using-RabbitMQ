

# Create your views here.
from django.shortcuts import render
from .publisher import publish_message

def form_data(request):
    if request.method == 'POST':
        data = {
            "name": request.POST.get("name"),
            "dept": request.POST.get("dept"),
            "university": request.POST.get("university"),
            "semester": request.POST.get("semester"),
            "year": request.POST.get("year"),
        }
        publish_message(data)
        return render(request, 'form.html', {"success": True})

    return render(request, 'form.html')