try:
    amount=float(input('The loan amount is :'))
    if not(float(amount)>=1000 and float(amount)<100000):
        raise Exception ('Invalid amount') 
    rate=float(input('The annual interest rate is:'))
    if not (float(rate)>=0.01 and float(rate)<=100):
        raise Exception ('Invalid rate') 
    payment=float(input('The monthly payment is:'))
    if (amount*(rate/12/100))>payment:
        raise Exception ('Invalid payment')
    ending=amount
    month=0
    starting=amount
    middle=0
    interest=0
    print('%-10s%-11s%-11s%-11s%-11s%-11s'%('','Starting','','Middle','','Ending'))
    print('%-10s%-11s%-11s%-11s%-11s%-11s'%('Month','Balance','Payment','Balance',
                                               'Interest','Balance'))
    print('{:->65}'.format(''))
    while not(ending==0):
        month=month+1
        starting=ending
        if ending<=payment:
            ending=0
            payment=ending
            middle=0
            interest=0
        else:
            middle=starting-payment
            interest=middle*(rate/12/100)
            ending=interest+middle
        print('%-10s%-11s%-11s%-11s%-11s%-11s'%(month,format(starting,'.2f'),format(payment,'.2f'),format(middle,'.2f'),format(interest,'.2f'),format(ending,'.2f')))
except Exception as exception:
    print(exception)
