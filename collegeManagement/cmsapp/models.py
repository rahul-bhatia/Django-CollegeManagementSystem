from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
	deptid=models.IntegerField(primary_key=True)
	deptname=models.CharField(max_length=20)

	def __str__(self):
		return self.deptname


class StudentModel(models.Model):
	rno=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=20)
	dept=models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)


	def __str__(self):
		return self.name
