from django.db import models

# Create your models here.
class department(models.Model):
    id = models.AutoField(primary_key=True)
    dName = models.CharField(max_length=35, help_text="ປ້ອນຊື່ຂອງສາຂາຮຽນ")
    email = models.CharField(max_length=50, help_text="ປ້ອນອີເມວຂອງສາຂາຮຽນ")

    def __str__(self):
        return self.dName

class student(models.Model):
    id = models.AutoField(primary_key=True)
    fName = models.CharField(max_length=35, help_text="ປ້ອນຊື່ຂອງທ່ານ")
    lName = models.CharField(max_length=50, help_text="ປ້ອນນາມສະກຸນຂອງທ່ານ")
    email = models.CharField(max_length=50, help_text="ປ້ອນອີເມວຂອງທ່ານ")
    address = models.TextField(help_text="ປ້ອນທີ່ຢູ່ຂອງທ່ານ")
    DOB = models.DateField(blank=True, null=True)
    Register = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + ". " + self.fName + " " + self.lName
