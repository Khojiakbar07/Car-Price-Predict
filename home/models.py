from django.db import models

class CarPricePrediction(models.Model):
    symboling = models.IntegerField()
    wheelbase = models.FloatField()
    carlength = models.FloatField()
    carwidth = models.FloatField()
    carheight = models.FloatField()
    curbweight = models.FloatField()
    horsepower = models.FloatField()
    peakrpm = models.IntegerField()
    citympg = models.FloatField()
    highwaympg = models.FloatField()
    
    FUELTYPE_CHOICES = [
        ('gas', 'Gas'),
        ('diesel', 'Diesel')
    ]
    fueltype = models.CharField(max_length=6, choices=FUELTYPE_CHOICES)
    
    CARBODY_CHOICES = [
        ('convertible', 'Convertible'),
        ('hardtop', 'Hardtop'),
        ('hatchback', 'Hatchback'),
        ('sedan', 'Sedan'),
        ('wagon', 'Wagon')
    ]
    carbody = models.CharField(max_length=11, choices=CARBODY_CHOICES)
    
    ENGINETYPE_CHOICES = [
        ('dohc', 'DOHC'),
        ('dohcv', 'DOHCV'),
        ('l', 'L'),
        ('ohc', 'OHC'),
        ('ohcf', 'OHCF'),
        ('ohcv', 'OHCV'),
        ('rotor', 'Rotor')
    ]
    enginetype = models.CharField(max_length=5, choices=ENGINETYPE_CHOICES)
    
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
    CarCompanyName = models.CharField(max_length=15, choices=CARCOMPANY_CHOICES)
    
    predicted_price = models.FloatField()

    def str(self):
        return f"{self.CarCompanyName} - {self.predicted_price}"