from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now  
from events.models import Event

# Create your models here.
class Token(models.Model):
    event = models.ForeignKey(Event,verbose_name=_("Event"),on_delete=models.CASCADE,null=True,blank=True)
    token_serial = models.CharField(_("Serial"),max_length=20,null=True,blank=True)
    is_printed = models.BooleanField(_("Printed"),default=False)
    is_activated = models.BooleanField(_("Activated"),default=False)
    entry_flag = models.BooleanField(_("Entry Status"),default=False,null=True,blank=True)
    food_flag = models.BooleanField(_("Food Status"),default=False,null=True,blank=True)
    student_id = models.CharField(_("Student Id"),max_length=8,null=True,blank=True)
    created = models.DateTimeField(_("Created"),default=now)

    class Meta:
        verbose_name_plural = "Tokens"
    
    def __str__(self):
        return f'{self.event} - {self.id} - {self.token_serial}'