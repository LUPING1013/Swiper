from django.db import models

# Create your models here.
class User(models.Model):

    GENDERS=(('male','男性'),('female','女性'))
    LOCATIONS = (
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('成都', '成都'),
        ('西安', '西安'),
        ("武汉", "武汉"),
        ("沈阳", "沈阳")
)

    phonenum = models.CharField(max_length=32,unique=True)
    nickname = models.CharField(max_length=32,db_index=True)
    gender=models.CharField(max_length=16,choices=GENDERS)
    birthday=models.DateField(auto_now=True)
    avatar=models.CharField(max_length=256)
    location=models.CharField(max_length=32,choices=LOCATIONS)

    class Meta:
        db_table='user'

    def to_dict(self):
        return {
            'id': self.id,
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'gender': self.gender,
            'birthday': str(self.birthday),
            'avatar': self.avatar,
            'location': self.location,
        }


