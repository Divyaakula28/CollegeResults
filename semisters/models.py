from django.db import models

class Fourthtwo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    htno = models.TextField(db_column='Htno', blank=True, null=True)  # Field name made lowercase.
    subcode = models.TextField(db_column='Subcode', blank=True, null=True)  # Field name made lowercase.
    subname = models.TextField(db_column='Subname', blank=True, null=True)  # Field name made lowercase.
    grade = models.TextField(db_column='Grade', blank=True, null=True)  # Field name made lowercase.
    credits = models.IntegerField(db_column='Credits', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fourthtwo'