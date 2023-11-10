from django.db import models

# Create your models here.

class CustomAdvertisementLocation(models.Model):
    #city = models.CharField(max_length=30, blank=True)
    STATES = (
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
    state = models.CharField(max_length=30, choices=STATES, default='Tehran')
    geo_width = models.CharField(max_length=30, blank=True)
    geo_length = models.CharField(max_length=30, blank=True)