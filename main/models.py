from django.db import models


class Personnel(models.Model):
    code = models.CharField(max_length=120)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    birthDate = models.DateField()
    gender = models.CharField(max_length=200)
    address = models.TextField()

    # def __str__(self):
    #     return [self.firstName]
    # return[self.firstName, self.lastName, self.birthDate, self.gender, self.address]


class Contact(models.Model):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=120)
    status = models.CharField(max_length=120, default="active")

    def __str__(self):
        return self.email
        # return[self.phone, self.email, self.status]
