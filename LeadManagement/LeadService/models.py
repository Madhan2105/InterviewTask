from django.db import models

# Create your models here.
class LeadModel(models.Model):
    current_stage_choices = (
        ("Pending","Pending"),
        ("Completed","Completed")
    )
    contact_person_name = models.CharField(max_length = 200)
    phone_numer         = models.IntegerField(max_length=10)
    address             = models.CharField(max_length = 2000)
    source              = models.CharField(max_length = 200)
    current_stage       = models.CharField(max_length = 20,choices=current_stage_choices,default="Pending")

    def __str__(self):
        return self.contact_person_name

class FollowUpModel(models.Model):
    medium_used_choices = (
        ("Call","Call"),
        ("Whatsapp","Whatsapp"),
        ("Email","Email")
    )    
    follow_up_date = models.DateField()
    response       = models.CharField(max_length = 2000)
    medium_used    = models.CharField(max_length = 20,choices=medium_used_choices)
    lead           = models.ForeignKey(LeadModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.medium_used