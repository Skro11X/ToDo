from django.db import models


class Task(models.Model):
    _status_choices = (
        ("TD","to do"),
        ("IP", "in progress"),
        ("DN","done"),
    )

    status = models.BooleanField(default=False, choices=_status_choices, verbose_name="Status")
    label = models.CharField(max_length=100 , verbose_name="Label")
    description = models.TextField(verbose_name="Description")
