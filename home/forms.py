from django import forms

class CarPricePredictionForm(forms.Form):
    symboling = forms.IntegerField(label='Symboling', required=True)
    wheelbase = forms.FloatField(label='Wheelbase', required=True)
    carlength = forms.FloatField(label='Carlength', required=True)
    carwidth = forms.FloatField(label='Carwidth', required=True)
    carheight = forms.FloatField(label='Carheight', required=True)
    curbweight = forms.FloatField(label='Curbweight', required=True)
    horsepower = forms.FloatField(label='Horsepower', required=True)
    peakrpm = forms.IntegerField(label='Peakrpm', required=True)
    citympg = forms.FloatField(label='Citympg', required=True)
    highwaympg = forms.FloatField(label='Highwaympg', required=True)

    FUELTYPE_CHOICES = [
        ('gas', 'Gas'),
        ('diesel', 'Diesel')
    ]
    fueltype = forms.ChoiceField(choices=FUELTYPE_CHOICES, required=True, label='Fueltype')

    CARBODY_CHOICES = [
        ('convertible', 'Convertible'),
        ('hardtop', 'Hardtop'),
        ('hatchback', 'Hatchback'),
        ('sedan', 'Sedan'),
        ('wagon', 'Wagon')
    ]
    carbody = forms.ChoiceField(choices=CARBODY_CHOICES, required=True, label='Carbody')

    ENGINETYPE_CHOICES = [
        ('dohc', 'DOHC'),
        ('dohcv', 'DOHCV'),
        ('l', 'L'),
        ('ohc', 'OHC'),
        ('ohcf', 'OHCF'),
        ('ohcv', 'OHCV'),
        ('rotor', 'Rotor')
    ]
    enginetype = forms.ChoiceField(choices=ENGINETYPE_CHOICES, required=True, label='Enginetype')

    CARCOMPANY_CHOICES = [
        ('alfa-romeo', 'Alfa Romeo'),
        ('audi', 'Audi'),
        ('bmw', 'BMW'),
        ('buick', 'Buick'),
        ('chevrolet', 'Chevrolet'),
        ('dodge', 'Dodge'),
        ('honda', 'Honda'),
        ('isuzu', 'Isuzu'),
        ('jaguar', 'Jaguar'),
        ('mazda', 'Mazda'),
        ('mercury', 'Mercury'),
        ('mitsubishi', 'Mitsubishi'),
        ('nissan', 'Nissan'),
        ('peugeot', 'Peugeot'),
        ('plymouth', 'Plymouth'),
        ('porsche', 'Porsche'),
        ('renault', 'Renault'),
        ('saab', 'Saab'),
        ('subaru', 'Subaru'),
        ('toyota', 'Toyota'),
        ('volkswagen', 'Volkswagen'),
        ('volvo', 'Volvo')
    ]
    CarCompanyName = forms.ChoiceField(choices=CARCOMPANY_CHOICES, required=True, label='Car Company Name')