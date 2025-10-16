from django.db import models

# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Any other fields you would like to include in car make model

    def __str__(self):
        # Return the name as the string representation
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    # Many-To-One relationship to Car Make model
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    # Type (CharField with a choices argument)
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    COUPE = "Coupe"
    HATCHBACK = "Hatchback"
    CAR_TYPES = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "Wagon"),
        (COUPE, "Coupe"),
        (HATCHBACK, "Hatchback"),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default=SEDAN)

    # Year (IntegerField with min/max value validators)
    year = models.IntegerField(
        default=2023, validators=[
            MaxValueValidator(2023), MinValueValidator(2015)
            ]
    )
    # Any other fields you would like to include in car model

    def __str__(self):
        # Return the car make name and the model name
        return f"{self.car_make.name} {self.name}"
