from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import User


class Content(models.Model):
    title = models.CharField(
        verbose_name=_("Title"), max_length=500,
        null=True, blank=True)
    definition = models.TextField(
        verbose_name=_('Definition'),
        null=True, blank=True)


class ScoreResponse(models.Model):
	user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )
	content = models.ForeignKey(
		Content,
		on_delete=models.CASCADE,
		related_name='content'
	)
	content_score = models.PositiveSmallIntegerField(
		verbose_name=_('Assessed level score'),
		null=True,
		default=0
	)
