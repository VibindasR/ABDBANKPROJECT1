from django.urls import path

from loan import views

app_name = 'loan'

urlpatterns=[

    path('apply_loan/',views.loan,name='loan'),
    path('loan_application_accepted/',views.loan_application_accepted,name='loan_application_accepted'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),  # AJAX

]