from tokenize import String
import numpy as np # type: ignore
from django.shortcuts import render, redirect
from tensorflow.keras.models import load_model # type: ignore
from .forms import CarPricePredictionForm
from .models import CarPricePrediction
import pickle

from django.shortcuts import render
from .forms import CarPricePredictionForm
import pickle
import numpy as np

# Load the trained model   C:\Users\user\Desktop\carpricing\static\line_model.sav
with open('C:/Users/user/Desktop/carpricing/static/line_model.sav', 'rb') as model_file:
    model = pickle.load(model_file)

def car_predict(request):
    if request.method == 'POST':
        form = CarPricePredictionForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            input_data = [
                data['symboling'],
                data['wheelbase'],
                data['carlength'],
                data['carwidth'],
                data['carheight'],
                data['curbweight'],
                data['horsepower'], 
                data['peakrpm'],
                data['citympg'],
                data['highwaympg']
            ]

            # Handle categorical variables
            fueltype = data['fueltype']
            carbody = data['carbody']
            enginetype = data['enginetype']
            car_company = data['CarCompanyName']

            # Add one-hot encoding manually for the categorical features
            fueltype_gas = 1 if fueltype == 'gas' else 0
            fueltype_diesel = 1 if fueltype == 'diesel' else 0
            carbody_convertible = 1 if carbody == 'convertible' else 0
            carbody_hardtop = 1 if carbody == 'hardtop' else 0
            carbody_hatchback = 1 if carbody == 'hatchback' else 0
            carbody_sedan = 1 if carbody == 'sedan' else 0
            carbody_wagon = 1 if carbody == 'wagon' else 0
            enginetype_dohc = 1 if enginetype == 'dohc' else 0
            enginetype_dohcv = 1 if enginetype == 'dohcv' else 0
            enginetype_l = 1 if enginetype == 'l' else 0
            enginetype_ohc = 1 if enginetype == 'ohc' else 0
            enginetype_ohcf = 1 if enginetype == 'ohcf' else 0
            enginetype_ohcv = 1 if enginetype == 'ohcv' else 0
            enginetype_rotor = 1 if enginetype == 'rotor' else 0

            car_company_dict = {
                'alfa-romeo': 0, 'audi': 1, 'bmw': 2, 'buick': 3, 'chevrolet': 4,
                'dodge': 5, 'honda': 6, 'isuzu': 7, 'jaguar': 8, 'mazda': 9,
                'mercury': 10, 'mitsubishi': 11, 'nissan': 12, 'peugeot': 13,
                'plymouth': 14, 'porsche': 15, 'renault': 16, 'saab': 17,
                'subaru': 18, 'toyota': 19, 'volkswagen': 20, 'volvo': 21
            }
            car_company_vector = [0] * len(car_company_dict)
            car_company_vector[car_company_dict[car_company]] = 1

            input_data.extend([
                fueltype_diesel, fueltype_gas,
                carbody_convertible, carbody_hardtop, carbody_hatchback,
                carbody_sedan, carbody_wagon,
                enginetype_dohc, enginetype_dohcv, enginetype_l,
                enginetype_ohc, enginetype_ohcf, enginetype_ohcv,
                enginetype_rotor
            ])
            input_data.extend(car_company_vector)

            input_data = np.array(input_data).reshape(1, -1)

            predicted_price = model.predict(input_data)[0]
            

            return render(request, 'car-details.html', { 'predicted_price': predicted_price})
    else:
        form = CarPricePredictionForm()

    return render(request, 'car-details.html', {'form': form})








# def carpredict(request):
#     if request.method=="POST":
#         print (request.POST.get('Carname'))
#         print (request.POST.get('model'))
#         print (request.POST.get('model'))

#     return render(request, 'car-details.html')



def main(request):
    return render(request, 'electro-home.html')

def about(request):
    return render(request, 'about-modern.html')

def service(request):
    return render(request, 'services-modern.html')


def carlisting(request):
    return render(request, 'car-listing.html')

def contact(request):
    return render(request, 'contact-modern.html')

def login(request):
    return render(request, 'Login.html')
