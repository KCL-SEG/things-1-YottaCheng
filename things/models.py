from django.core.validators import MaxLengthValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, validators=[MaxLengthValidator(120)])  # 限制最大长度为120
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(100)])  # 添加验证规则

    def __str__(self):
        return self.name
