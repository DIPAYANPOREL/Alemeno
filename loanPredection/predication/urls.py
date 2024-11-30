from django.urls import path
from . import views

urlpatterns = [
    path('upload_loan_data/', views.upload_loan_data, name='upload_loan_data'),
    path('upload_customer_data/', views.upload_customer_data, name='upload_customer_data'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('loan_eligibility/', views.loan_eligibility, name='loan_eligibility'),  
    path('create_new_loan/', views.create_new_loan, name='create_new_loan'),  
    path('view_loan/loanid/<int:loan_id>/', views.view_loan_against_loan_id, name='view_loan_loan_id'),  
    path('view_loan/customerid/<int:customer_id>/', views.view_loan_against_customer_id, name='view_loan_against_customer_id'),  
]

