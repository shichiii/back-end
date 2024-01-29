from django.db import models
from CustomDate.models import CustomDate
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomAdvertisement(models.Model):
    owner_id = models.IntegerField(null=False, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    available_date_list = models.ManyToManyField(CustomDate)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
     
    #car_images = models.ManyToManyField(CustomCarImage)
    car_image1 = models.ImageField(upload_to='car_images/', blank=True)
    car_image2 = models.ImageField(upload_to='car_images/', blank=True)
    car_image3 = models.ImageField(upload_to='car_images/', blank=True)
    
    car_name = models.CharField(max_length=30, blank=True)
    CAR_COLOR = (
        ('black', 'black'),
        ('white', 'white'),
        ('gray', 'gray'), 
        ('brown', 'brown'),
        ('navy-blue', 'navy-blue'),
        ('others', 'others'),   
    )
    car_color = models.CharField(max_length=20, choices=CAR_COLOR, default='others')
    car_produced_date = models.DateField()
    car_seat_count = models.IntegerField(null=True, blank=True)
    car_door_count = models.IntegerField(null=True, blank=True)
    CAR_IS_COOLER = (
        ('yes', 'yes'),
        ('no', 'no')
    )
    car_Is_cooler = models.CharField(max_length=3, choices=CAR_IS_COOLER, default='yes')
    CAR_GEARBOX = (
        ('manual', 'manual'),
        ('automatic', 'automatic'),
    )
    car_gearbox = models.CharField(max_length=20, choices=CAR_GEARBOX, default='manual')
    car_fuel = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    CAR_CATEGORIES = (
        ('economy', 'economy'),
        ('luxury', 'luxury'),
        ('compact', 'compact'), 
        ('offroad', 'offroad'),
        ('hybrid', 'hybrid'),
        ('electric', 'electric'),
        ('truck', 'truck'),
        ('convertible', 'convertible'), 
        ('passenger-van', 'passenger-van'), 
        ('mini-van', 'mini-van'),
        ('others', 'others'),   
    )
    car_category = models.CharField(max_length=20, choices=CAR_CATEGORIES, default='others')
    
    location_STATES = (
        ('Tehran'                     , 'Tehran'),
        ('Khorasan-Razavi'            , 'Khorasan-Razavi'),
        ('Isfahan'                    , 'Isfahan'), 
        ('Fars'                       , 'Fars'),
        ('Khuzestan'                  , 'Khuzestan'),
        ('Azarbaijan, East'           , 'Azarbaijan, East'),
        ('Azarbaijan, West'           , 'Azarbaijan, West'),
        ('Mazandaran'                 , 'Mazandaran'), 
        ('Kerman'                     , 'Kerman'), 
        ('Alborz'                     , 'Alborz'),
        ('Gilan'                      , 'Gilan'),  
        ('Sistan-and-Baluchestan'     , 'Sistan-and-Baluchestan'),
        ('Kermanshah'                 , 'Kermanshah'),
        ('Hamedan'                    , 'Hamedan'), 
        ('Lorestan'                   , 'Lorestan'),
        ('Golestan'                   , 'Golestan'),
        ('Kurdistan'                  , 'Kurdistan'),
        ('Hormozgan'                  , 'Hormozgan'),
        ('Markazi'                    , 'Markazi'), 
        ('Ardabil'                    , 'Ardabil'), 
        ('Qazvin'                     , 'Qazvin'),
        ('Qom'                        , 'Qom'),  
        ('Bushehr'                    , 'Bushehr'),
        ('Yazd'                       , 'Yazd'),
        ('Zanjan'                     , 'Zanjan'), 
        ('Chahar-Mahaal-and-Bakhtiari', 'Chahar-Mahaal-and-Bakhtiari'),
        ('Khorasan-North'             , 'Khorasan-North'),
        ('Khorasan-South'             , 'Khorasan-South'),
        ('Kohgiluyeh-and-Boyer-Ahmad' , 'Kohgiluyeh-and-Boyer-Ahmad'),
        ('Semnan'                     , 'Semnan'), 
        ('Ilam'                       , 'Ilam'), 
    )
    location_state = models.CharField(max_length=30, choices= location_STATES, default='Tehran')
    location_geo_width = models.CharField(max_length=30, blank=True)
    location_geo_length = models.CharField(max_length=30, blank=True)
    
    
class Comment(models.Model):
    adv = models.ForeignKey(CustomAdvertisement, on_delete=models.CASCADE, related_name='comments')
    user_id = models.IntegerField(null=False, blank=False)
    created_date = models.DateField(auto_now_add=True)
    text = models.TextField()
    def __str__(self):
        return f"{self.adv.car_name} - {self.user_id.first_name} {self.user_id.last_name}: {self.text}"
    def is_owner(self, user):
        return self.user == user

class Rate(models.Model):
    adv = models.ForeignKey(CustomAdvertisement, on_delete=models.CASCADE, related_name='rates')
    user_id = models.IntegerField(null=False, blank=False)
    rate = models.DecimalField(
        max_digits=2, decimal_places=1, default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return f"rated {self.rate} to {self.adv.car_name}"