from django.db import models

# Create your models here.
class Archive(models.Model):
    id = models.BigAutoField(primary_key=True)
    subjects = models.CharField(max_length=255)
    questions = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archive'

class Classes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    id_student = models.BigIntegerField(blank=True, null=True)
    id_teacher = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classes'

class Exercise(models.Model):
    id = models.BigAutoField(primary_key=True)
    images = models.TextField(blank=True, null=True)
    questions = models.TextField(blank=True, null=True)
    subjects_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'exercise'

class Subjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    id_class = models.BigIntegerField()
    id_exercise = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjects'

class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class Books(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    file_url = models.TextField(blank=True, null=True)
    archive_id = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'books'