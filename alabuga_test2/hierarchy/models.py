from django.db import models

#grades
lord = "олигарх"
soldier = "солдат"
slave = "пролетарий"

# Create your models here.

class lords(models.Model):
    vassal_of = None
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    status = lord    
    name = models.CharField(max_length=30, default="")
    surname = models.CharField(max_length=30, default="")
    salary = models.DecimalField(
        "месячный доход",
        max_digits=6,
        decimal_places=2,
        default=0.0
    )

    def __str__(self):
        return f"""гражданин: {self.status} {self.name} {self.surname},
                возраст {self.age} лет,
                ЗП: {self.salary}, подчиняется {self.vassal_of}"""

    class Meta:
        verbose_name = lord
        verbose_name_plural = lord + "и"

class soldiers(models.Model):
    vassal_of = models.ForeignKey(
        lords,
        on_delete = models.SET_NULL,
        null=True,
        blank=True
    )
    status = soldier
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=30, default="")
    surname = models.CharField(max_length=30, default="")
    salary = models.DecimalField(
        "месячный доход",
        max_digits=6,
        decimal_places=2,
        default=0.0
    )

    def __str__(self):
        return f"""гражданин: {self.status} {self.name} {self.surname},
                возраст {self.age} лет,
                ЗП: {self.salary}, подчиняется {self.vassal_of}"""

    class Meta:
        verbose_name = soldier
        verbose_name_plural = soldier + "ы"
    
class slaves_of_lords(models.Model):
    vassal_of = models.ForeignKey(
        lords,
        on_delete = models.SET_NULL,
        null=True,
        blank=True
    )
    status = slave
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=30, default="")
    surname = models.CharField(max_length=30, default="")
    salary = models.DecimalField(
        "месячный доход",
        max_digits=6,
        decimal_places=2,
        default=0.0
    )

    def __str__(self):
            return f"""гражданин: {self.status} {self.name} {self.surname},
                возраст {self.age} лет,
                ЗП: {self.salary}, подчиняется {self.vassal_of}"""

    class Meta:
        verbose_name = slave
        verbose_name_plural = slave[:-2] + "и (для " + lord + "ов)"

class slaves_of_soldiers(models.Model):
    vassal_of = models.ForeignKey(
        soldiers,
        on_delete = models.SET_NULL,
        null=True,
        blank=True
    )
    status = slave
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    name = models.CharField(max_length=30, default="")
    surname = models.CharField(max_length=30, default="")
    salary = models.DecimalField(
        "месячный доход",
        max_digits=6,
        decimal_places=2,
        default=0.0
    )

    def __str__(self):
            return f"""гражданин: {self.status} {self.name} {self.surname},
                возраст {self.age} лет,
                ЗП: {self.salary}, подчиняется {self.vassal_of}"""

    class Meta:
        verbose_name = slave
        verbose_name_plural = slave[:-2] + "и (для " + soldier + ")"