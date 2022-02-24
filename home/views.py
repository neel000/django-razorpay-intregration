from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import razorpay

razor_id = 'your_id'
razor_secrect_key = 'your_key'


def homeIndex(request):
    client = razorpay.Client(auth=(razor_id, razor_secrect_key))
    payment = client.order.create({'amount':(50*100), 'currency':'INR', 'payment_capture':'1'})
    show = {'payment':payment, 'api_id': razor_id }
    print(show)
    return render(request, 'home/homeIndex.html', show)


@csrf_exempt
def success_payment(request):
    data = "failed"
    if request.method == "POST":
        a =  (request.POST)
        order_id = ""
        for key , val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                data = "success"

                print(order_id)
                # updt = Transaction.objects.filter(tr_id=order_id)[0:1]
                # for i in updt:
                #     updt2 = MemberForm.objects.filter(email=i.email)
                #     for m in updt2:
                #         m.bal = m.bal + i.amt
                #         m.save()
                #     i.status = 'success'
                #     i.save()
    return HttpResponse(data)