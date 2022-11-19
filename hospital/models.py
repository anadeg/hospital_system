from django.db import models


# Create your models here.
class UserEntity(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)


class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    admin = models.IntegerField()


class UserDAO(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    db_access = models.CharField(max_length=20)


class StaffEntity(UserEntity):
    # id = models.IntegerField(primary_key=True)
    cabinet_no = models.CharField(max_length=4)
    time = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    hospital_title = models.CharField(max_length=100)       # should be FK
    speciality = models.CharField(max_length=50)


class StaffData(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    hospital_title = models.CharField(max_length=100)   # FK
    speciality = models.CharField(max_length=50)


class StaffDAO(models.Model):
    staff = models.ForeignKey(StaffData, on_delete=models.CASCADE)
    db_access = models.CharField(max_length=20)


class CureEntity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    address = models.CharField(max_length=100)


class CureData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    address = models.CharField(max_length=100)


class CureDAO(models.Model):
    cure = models.ForeignKey(CureData, on_delete=models.CASCADE)


class HospitalEntity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    sections = models.CharField(max_length=40)
    info = models.TextField()
    address = models.CharField(max_length=100)


class HospitalData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    sections = models.CharField(max_length=40)
    info = models.TextField()
    address = models.CharField(max_length=100)


class HospitalDAO(models.Model):
    hospital = models.ForeignKey(HospitalData, on_delete=models.CASCADE)


class MedicalTestEntity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    hospital_title = models.CharField(max_length=100)       # should be FK
    cabinet_no = models.CharField(max_length=4)
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=4)


class MedicalTestData(models.Model):
    id = models.AutoField(primary_key=True)
    hospital_title = models.CharField(max_length=100)  # should be FK
    cabinet_no = models.CharField(max_length=4)
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=4)


class MedicalTestDAO(models.Model):
    med_test = models.ForeignKey(MedicalTestData, on_delete=models.CASCADE)


class DoctorCardEntity(models.Model):
    id = models.AutoField(primary_key=True)
    hospital_title = models.CharField(max_length=100)       # should be FK
    doctor_speciality = models.CharField(max_length=50)     # should be FK
    cabinet_no = models.CharField(max_length=4)             # redundant. doctor has cabinet
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=4)


class DoctorCardData(models.Model):
    id = models.AutoField(primary_key=True)
    cabinet_no = models.CharField(max_length=4)
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=4)
    staff_name = models.CharField(max_length=100)


class DoctorCardDAO(models.Model):
    card = models.ForeignKey(DoctorCardData, on_delete=models.CASCADE)


class RegionEntity(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    is_country = models.BooleanField(default=False)


class RegionData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    country = models.IntegerField()


class RegionDAO(models.Model):
    card = models.ForeignKey(RegionData, on_delete=models.CASCADE)


class MedicalCardEntity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=5)
    passport_data = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class MedicalCardData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=5)
    passport_data = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class MedicalCardDAO(models.Model):
    card = models.ForeignKey(MedicalCardData, on_delete=models.CASCADE)


class Configures(models.Model):
    host = models.CharField(max_length=20)
    port = models.CharField(max_length=20)
    user = models.CharField(max_length=30)
    db_password = models.CharField(max_length=50)
    title = models.CharField(max_length=20)


class Constants(models.Model):
    user_table = models.CharField(max_length=50)
    user_id = models.IntegerField()
    admin = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)

    staff_table = models.CharField(max_length=50)
    staff_id = models.IntegerField()
    speciality = models.CharField(max_length=50)
    hospital_title = models.CharField(max_length=100)
    staff_name = models.CharField(max_length=100)
    staff_phone = models.CharField(max_length=12)
    staff_email = models.CharField(max_length=30)
    staff_password = models.CharField(max_length=50)

    medical_card_table = models.CharField(max_length=50)
    mc_id = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=5)
    passport_data = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    region_id = models.IntegerField()
    region_title = models.CharField(max_length=20)
    country = models.CharField(max_length=30)

    cure_id = models.IntegerField()
    cure_title = models.CharField(max_length=30)
    cure_description = models.TextField()
    cure_address = models.CharField(max_length=100)

    hospital_id = models.IntegerField()
    hospital_sections = models.CharField(max_length=40)
    hospital_info = models.TextField()









