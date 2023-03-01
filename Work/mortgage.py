# mortgage.py
#
# Exercise 1.7
#30 year fixed rate mortgage
#  $500000 Loan @ 5%
#  Monthly Payment $2684.11
principal=500000
interest=0.05
payment=2684.11
beginning_principal=principal
interest_payment=0.0
total_intrest_payment=0.0
extra_payment=1000.00
extra_payment_start=int(input('When will you begin extra payments? \n Example: 45 \n   Month:',))
extra_payment_end=int(input('When will you end extra payments? \n  Month:',))
total_extra_payment=extra_payment_end-extra_payment_start+1
month=0
actual_payment=0.00
total_paid=0.00

while principal>0 and month<10:
    if(month>=extra_payment_start and month<=extra_payment_end):
        actual_payment=payment+extra_payment
        print(-f'in range of extra payment:\n month{month}')
    else:
        actual_payment=payment
    month=month+1
    if(actual_payment>principal*(1+interest/12)):
       actual_payment=principal*(1+interest/12)
    beginning_principal=principal
    interest_payment=principal*(interest/12)
    principal=principal+interest_payment-actual_payment
    total_paid=total_paid+actual_payment
    total_intrest_payment=total_intrest_payment+interest_payment
    print(f'M:{month}, Beg. principal:{round(beginning_principal,2)},Interest Payment:{round(interest_payment,2)}, payment:{round(actual_payment,2)},Ending Bal:{round(principal,2)}')
          
print('Total Paid: $ ',round(total_paid,2),'\n','Months to Payoff: ',
      month,'\n',month//12,' Years and ',month%12,' Months' )
print(-f'Months of extra payment: {extra_payment}\n Month extra payment start{extra_payment_start}\n')