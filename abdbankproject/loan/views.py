from django.contrib import messages
from django.shortcuts import render, redirect

from banking.models import Branch
from loan.forms import LoanCreationForm


# Create your views here.
def loan(request):
    form = LoanCreationForm()
    if request.method=='POST':
        form = LoanCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Application accepted")
            return redirect('loan:loan_application_accepted')
    return render(request,"loan.html",{'form':form})

def loan_application_accepted(request):
    return render(request,'loan_application_accepted.html')

def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)