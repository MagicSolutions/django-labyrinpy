from django.db import models


class Message(models.Model):
    MESSAGE_TYPES = (('text', 'Plain text'), ('binary', 'Binary'), ('wap_url', 'WAP Push SI Message'))
    _CLASS = (('normal', 'Normal Message'), ('flash', 'Flash Message'))
    BOOLEAN = (('yes', 'yes'), ('no', 'no'))

    destination = models.CharField(max_length=16)
    message_type = models.CharField(max_length=7, choices=MESSAGE_TYPES)

    source_name = models.CharField(max_length=16, blank=True)
    source = models.CharField(max_length=2, blank=True)
    service = models.CharField(max_length=10, blank=True)
    header = models.CharField(max_length=15, blank=True)
    wap_text = models.URLField(blank=True)
    _class = models.CharField(max_length=6, choices=_CLASS, blank=True)
    concatenate = models.CharField(max_length=3, choices=BOOLEAN, blank=True)
    unicode = models.CharField(max_length=3, choices=BOOLEAN, blank=True)
    validity = models.CharField(max_length=16, blank=True)
    delivery = models.CharField(max_length=16, blank=True)
    report = models.URLField(blank=True)

    def __unicode__(self):
        return 'Sent to {}'.format(self.destination)


class Report(models.Model):
    STATUS = (('OK', 'OK'), ('ERROR', 'ERROR'), ('WAITING', 'WAITING'))

    message = models.ForeignKey(Message, related_name='reports')
    source = models.CharField(max_length=6)
    dest = models.CharField(max_length=16)
    status = models.CharField(max_length=7, choices=STATUS)
    code = models.CharField(max_length=2)
    description = models.CharField(max_length=40)  # message
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return 'Report from {}'.format(self.timestamp)
