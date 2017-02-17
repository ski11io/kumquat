from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

WHEN = (
		('0,5,10,15,20,25,30,35,40,45,50,55 * * * *', _('every 5 minutes')),
		('0,30 * * * *',                              _('every 30 minutes')),
		('0 * * * *',                                 _('hourly')),
		('0 0 * * *',                                 _('daily')),
		('0 0 * * 0',                                 _('weekly')),
		('0 0 1 * *',                                 _('monthly')),
)

class Cronjob(models.Model):
	when = models.CharField(verbose_name=_("When"), max_length=255, choices=WHEN)
	command = models.CharField(verbose_name=_("Command"), max_length=1024, help_text=_("Posix shell command which will be executed"))

	def __str__(self):
		return self.when + " " + self.command
