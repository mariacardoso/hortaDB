import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Species(models.Model):
    common_name = models.CharField(max_length=100)
    species     = models.CharField(max_length=100)
    genus       = models.CharField(max_length=100)
    family      = models.CharField(max_length=100)
    order       = models.CharField(max_length=100)

    # pub_date    = models.DateTimeField('date added')

    def __str__(self):
        return self.common_name

    #def was_created_recently(self):
    #    now = timezone.now()
    #    return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #was_created_recently.admin_order_field = 'pub_date'
    #was_created_recently.boolean = True
    #was_created_recently.short_description = 'Published recently?'

    class Meta:
        verbose_name_plural = "species"


class Cultivar(models.Model):
    LIFE_CYCLE_CHOICES = (
        ('AN', 'annual'),
        ('BI', 'biennial'),
        ('PR', 'perennial'),
        ('UN', 'unknown'),
    )
    species    = models.ForeignKey(Species, on_delete=models.CASCADE)
    variety    = models.CharField(max_length=100)
    life_cycle = models.CharField(
                        choices    = LIFE_CYCLE_CHOICES,
                        max_length = 20,
                        default    = 'UN',
                        blank      = False,
    )
    # votes   = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.species, self.variety)

    def get_name(self):
        """
        Returns the common name of the cultivar.
        """
        return self.species.common_name
    get_name.short_description = ('common name')
    get_name.admin_order_field = ('species__common_name')

    def get_species(self):
        """
        Returns the species of the cultivar.
        """
        return self.species.species
    get_species.short_description = ('plant species')
    get_species.admin_order_field = ('species__species')
    

class Seed(models.Model):
    plant_seed   = models.ForeignKey(Cultivar, on_delete=models.CASCADE)
    brand        = models.CharField('brand/origin', max_length=50)
    date_sowo_ini = models.IntegerField(
                        'month sowing outside starts',
                        blank=True, null= True,
                        validators=[MinValueValidator(1), MaxValueValidator(12)])
    date_sowo_end = models.IntegerField(
                        'month sowing outside ends',
                        blank=True, null= True,
                        validators=[MinValueValidator(1), MaxValueValidator(12)])
    date_sowi_ini = models.IntegerField(
                        'month sowing inside starts',
                        blank=True, null= True,
                        validators=[MinValueValidator(1), MaxValueValidator(12)])
    date_sowi_end = models.IntegerField(
                        'month sowing inside ends',
                        blank=True, null= True,
                        validators=[MinValueValidator(1), MaxValueValidator(12)])                                    
    date_tran_ini = models.IntegerField(
                        'month transplanting starts',
                        blank=True, null= True,
                        validators=[MinValueValidator(1), MaxValueValidator(12)])
    date_tran_end = models.IntegerField(
                        'month transplanting ends',
                        blank=True, null= True,
                        validators=[MinValueValidator(1), MaxValueValidator(12)])
    date_harv_ini = models.IntegerField(
                        'month harvesting starts',
                        blank=True, null= True,
                        validators=[MinValueValidator(1), MaxValueValidator(12)])
    date_harv_end = models.IntegerField(
                        'month harvesting ends',
                        blank=True, null= True,
                        validators=[MinValueValidator(1), MaxValueValidator(12)])
    # TO ADD
    # days_harvest    = models.IntegerField('time until harvest')
    # days_to_maturity

    def __str__(self):
        return '%s %s' % (self.plant_seed, self.brand)


class Seed_Packet(models.Model):
    seed_packet   = models.ForeignKey(Seed, on_delete=models.CASCADE)
    date_packing  = models.DateField('packing date of seed bag', blank=True, null=True)
    date_validity = models.DateField('expiry date of seed bag', blank=True, null=True)
    weight        = models.IntegerField('weight of seed bag [g]', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.seed_packet)

    class Meta:
        verbose_name = "seed packet"
        verbose_name_plural = "seed packets"
