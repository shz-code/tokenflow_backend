from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now  

# Create your models here.
class Event(models.Model):
    name = models.CharField(_("Event"),max_length=50,null=True,blank=True)
    event_date = models.DateTimeField(_("Event Date"),null=True,blank=True)
    token_dist_start = models.DateTimeField(_("Token Distribution Start"),null=True,blank=True)
    token_dist_end = models.DateTimeField(_("Token Distribution End"),null=True,blank=True)
    token_usage = models.IntegerField(_("Token Usage Limit"),default=0)
    distribution_place = models.CharField(_("Distribution"),max_length=100,null=True,blank=True)
    desc = models.TextField(_("Description"),null=True,blank=True)
    created = models.DateTimeField(_("Created"),default=now)

    def __str__(self):
        return self.name
    
    @property
    def get_tokens(self):
        tokens = self.token_set.all()
        return tokens  
    
    @property
    def get_tokens_non_printed_count(self):
        tokens = self.token_set.filter(is_printed=False).count()
        return tokens  
    
    @property
    def get_printed_tokens(self):
        tokens = self.token_set.filter(is_printed=True)
        return tokens  
    
    @property
    def get_activated_tokens(self):
        tokens = self.token_set.filter(is_activated=True)
        return tokens  
    

class EventStudentList(models.Model):
    student_id = models.CharField(_("Student Id"),max_length=8,null=True, blank=True)
    name = models.CharField(_("Name"),max_length=50,null=True,blank=True)
    event = models.ForeignKey(Event,verbose_name=_("Event"),on_delete=models.CASCADE,null=True,blank=True)
    claimed = models.BooleanField(_("Token Claimed"),default=False,null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Student List"
    
    def __str__(self):
        return f'{self.student_id} for - {self.event}'
