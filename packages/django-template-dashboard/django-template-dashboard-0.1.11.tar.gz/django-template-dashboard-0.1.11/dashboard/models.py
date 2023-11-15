from django.db import models
from django.utils.translation import gettext_lazy as _


class DashboardBase(models.Model):
    """
    Base class for all dashboard.
    """
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)
    update_time = models.DateTimeField(_('Update Time'), auto_now=True)
    is_active = models.BooleanField(_('Is Active'), default=True)

    class Meta:
        ordering = ['-id']
        abstract = True
