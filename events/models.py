from django.db.models import *
from django.contrib.auth.models import User

class Event(Model):
    title = CharField(max_length=120)
    description = TextField()
    date = DateField()
    time = TimeField()
    departure = CharField(max_length=255)
    is_active = BooleanField(default=True)


    def __str__(self):
        return self.title

    def registrations(self):
        return self.registration_set.all().count()
    
    def approved(self):
        return self.registration_set.filter(approved=True).count()
    
    def pending(self):
        return self.registration_set.filter(approved=False).count()
    

    class Meta:
        ordering = ['title', 'is_active']


class Registration(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    event = ForeignKey(Event, on_delete=CASCADE)
    medical_info = CharField(max_length=255, default='None')
    diatery_info = CharField(max_length=255, default='None')
    approved = BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()+ ' #' + self.event.title
    

    class Meta:
        ordering = ['event', 'approved']
