from django.db import models

# Create your models here.

class BaseModel(models.Model):
    class Meta:
        abstract = True
        db_table = "user_info"

class BaseInfo(BaseModel):
    token = models.CharField(max_length=255)
    password = models.CharField(max_length=127)

class User(BaseModel):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    is_admin = models.BooleanField(default=False)
    info = models.ForeignKey(BaseInfo, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name + self.last_name