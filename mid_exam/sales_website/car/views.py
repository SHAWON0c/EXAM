from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# @login_required
def buy_now(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    print("Initial quantity:", car.quantity)  # Debug statement
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        request.session['purchased_car'] = car.id
        print("Updated quantity:", car.quantity)  
        messages.success(request, f'You have successfully purchased {car.name}.')
        return redirect('profile')

    else:
        return render(request, 'out_of_stock.html')



# # @login_required
# def car_details(request, car_id):
#     car = get_object_or_404(Car, id=car_id)
#     return render(request, 'cardetails.html', {'car': car})




# # views.py

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Comment
# from .forms import CommentForm

# def car_details(request, car_id):
#     car = get_object_or_404(Car, id=car_id)
#     comments = car.comments.all()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.car = car
#             comment.save()
#             return redirect('car_details', car_id=car_id)
#     else:
#         form = CommentForm()
#     return render(request, 'cardetails.html', {'car': car, 'form': form})


# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm
from car.models import Car
from django.contrib.auth.decorators import login_required

# @login_required
def car_details(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    comments = car.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('cardetails', car_id=car_id)
    else:
        form = CommentForm()

    return render(request, 'cardetails.html', {'car': car, 'comments': comments, 'form': form})
