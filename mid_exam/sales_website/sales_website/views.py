# from django.shortcuts import render
# from car.models import Car
# from brand.models import Brand
# from django.shortcuts import get_object_or_404

# # def home(request, brand_slug=None):
# #     cars = Car.objects.all()
# #     brand=Brand.objects.all()
# #     if brand_slug is not None:
# #         brand = get_object_or_404(Brand, slug=brand_slug)
# #         cars = cars.filter(brand=brand)
    
# #     return render(request, 'home.html', {'cars': cars})


 
# def home(request, brand_slug = None):
#     brandData = Brand.objects.all()
#     carData = Car.objects.all()
 
#     if brand_slug is not None:
#         brand = Brand.objects.get(slug = brand_slug)
#         carData = Car.objects.filter(brand = brand)
#     brands = Brand.objects.all()
 
#     return render(request, 'home.html', {'brandData': brandData, 'cars': carData, 'brand': brands})




# from django.shortcuts import render, redirect
# from car.models import Car
# from brand.models import Brand
 
# def home(request, brand_slug = None):
#     brandData = Brand.objects.all()
#     carData = Car.objects.all()
 
#     if brand_slug is not None:
#         brand = Brand.objects.get(slug = brand_slug)
#         carData = Car.objects.filter(brand = brand)
#     brands = Brand.objects.all()
 
#     return render(request, 'home.html', {'brandData': brandData, 'cars': carData, 'brand': brands})



# from django.shortcuts import render, redirect
# from django.core.exceptions import ObjectDoesNotExist
# from car.models import Car
# from brand.models import Brand

# def home(request, brand_slug=None):
#     brandData = Brand.objects.all()
#     carData = Car.objects.all()
    
#     try:
#         if brand_slug is not None:
#             brand = Brand.objects.get(slug=brand_slug)
#             carData = Car.objects.filter(brand=brand)
#     except ObjectDoesNotExist:
#         # Handle the case where the brand doesn't exist
#         return render(request, 'brand_does_not_exist.html')

#     brands = Brand.objects.all()

#     return render(request, 'home.html', {'brandData': brandData, 'cars': carData, 'brands': brands})


from django.shortcuts import render, redirect
from car.models import Car
from brand.models import Brand
 
def home(request, brand_slug=None):
    brandData = Brand.objects.all()
    carData = Car.objects.all()  # Define carData here
    
    if brand_slug is not None:
        brand = Brand.objects.get(slug=brand_slug)
        carData = Car.objects.filter(brand=brand)
    
    return render(request, 'home.html', {'brandData': brandData, 'cars': carData})
