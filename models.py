import peewee as pw
from flask import jsonify
import psycopg2
import json
from config import BaseModel, db
import csv

class Speciality(BaseModel):
    id = pw.IntegerField(primary_key=True)
    specialit = pw.CharField(max_length=1000, null=False)


class Doctor(BaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=1000, null=False)
    surname = pw.CharField(max_length=1000, null=False)
    patronimic = pw.CharField(max_length=1000, null=False)
    phone = pw.CharField(max_length=11, null=False)
    parol = pw.CharField(max_length=100, null=False)
    adress = pw.CharField(max_length=1000, null=False)
    speciality = pw.ForeignKeyField(Speciality, on_delete='RESTRICT')


class Admin(BaseModel):
    id = pw.IntegerField(primary_key=True)
    parol = pw.CharField(max_length=100, null=False)


class Patient(BaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=1000, null=False)
    surname = pw.CharField(max_length=1000, null=False)
    patronimic = pw.CharField(max_length=1000, null=False)
    phone = pw.CharField(max_length=11, null=False)
    parol = pw.CharField(max_length=100, null=False)
    adress = pw.CharField(max_length=1000, null=False)


class Registrator(BaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=1000, null=False)
    surname = pw.CharField(max_length=1000, null=False)
    patronimic = pw.CharField(max_length=1000, null=False)
    phone = pw.CharField(max_length=11, null=False)
    parol = pw.CharField(max_length=100, null=False)
    adress = pw.CharField(max_length=1000, null=False)


class Schedule(BaseModel):
    id = pw.IntegerField(primary_key=True)
    doctor = pw.ForeignKeyField(Doctor, on_delete='RESTRICT')
    days = pw.CharField(max_length=1000, null=False)
    times_s = pw.TimeField(null=False)
    times_f = pw.TimeField(null=False)
    cabinet = pw.IntegerField(null=False)


class Talon(BaseModel):
    id = pw.IntegerField(primary_key=True)
    patient = pw.ForeignKeyField(Patient, on_delete='CASCADE')
    day = pw.DateField(null=False)
    times = pw.TimeField()
    cabinet = pw.IntegerField(null=False)
    doctor = pw.ForeignKeyField(Doctor, on_delete='RESTRICT')


class Receipt(BaseModel):
    id = pw.IntegerField(primary_key=True)
    recomendation = pw.CharField(max_length=1000, null=False)
    day = pw.DateField(null=False)
    doctor = pw.ForeignKeyField(Doctor, on_delete='RESTRICT')
    patient = pw.ForeignKeyField(Patient, on_delete='CASCADE')


class Seek_history(BaseModel):
    id = pw.IntegerField(primary_key=True)
    patient = pw.ForeignKeyField(Patient, on_delete='CASCADE')
    day = pw.DateField(null=False)
    diagnos = pw.CharField(max_length=1000, null=False)
    conclusion = pw.CharField(max_length=1000, null=False)
    doctor = pw.ForeignKeyField(Doctor, on_delete='RESTRICT')


class Patient_card(BaseModel):
    id = pw.IntegerField(primary_key=True)
    patient = pw.ForeignKeyField(Patient, on_delete='CASCADE', null=False)


# Создание таблиц для всех моделей
with db:
    db.create_tables([
        Doctor, Patient, Receipt, Registrator, Speciality, Schedule, Seek_history, Patient_card, Talon, Admin
    ])

def create_talon(patient, date, times, cabinet_num, doctor):
    Talon.create_table()
    rec1 = Talon.create(patient=patient, day=date, times=times, cabinet=cabinet_num, doctor=doctor)
    rec1.save()


def delete_talon(patient, date, times, cabinet_num, doctor):
    rec1 = Talon.get(Talon.patient == patient, Talon.day == date, Talon.times == times, Talon.cabinet == cabinet_num, Talon.doctor == doctor)
    rec1.delete_instance()


def create_patient(name, surname, patronimic, adress, phone, parol, id):
    Patient.create_table()
    rec1 = Patient.create(id=id, name=name, surname=surname, patronimic=patronimic, phone=phone,
                          parol=parol, adress=adress)
    print(rec1)
    rec1.save()
    Patient_card.create_table()
    rec1 = Patient_card.create(patient=id)
    print(rec1)
    rec1.save()


def create_spec(id, specialit):
    Speciality.create_table()
    rec1 = Speciality.create(id=id, specialit=specialit)
    rec1.save()


def create_registrator(name, surname, patronimic, adress, phone, parol, id):
    Registrator.create_table()
    rec1 = Registrator.create(id=id, name=name, surname=surname, patronimic=patronimic, phone=phone,
                          parol=parol, adress=adress)
    rec1.save()


def create_schedule(doctor, days, times_s, times_f, cabinet):
    Schedule.create_table()
    rec1 = Schedule.create(doctor=doctor, days=days, times_s=times_s, times_f=times_f, cabinet=cabinet)
    rec1.save()


def update_doctor(id, pol, name, surname, patronimic, phone, parol, adress, speciality):
    row = Doctor.get(Doctor.id == id)
    if pol != '':
        row.id = pol
    if name != '':
        row.name = name
    if surname != '':
        row.surname = surname
    if patronimic != '':
        row.patronimic = patronimic
    if phone != '':
        row.phone = phone
    if parol != '':
        row.parol = parol
    if adress != '':
        row.adress = adress
    if speciality != '':
        row.speciality = speciality
    row.save()


def update_registrator(key, name, surname, patronimic, adress, phone, parol, id):
    row = Registrator.get(Registrator.id == key)
    if id != '':
        row.id = id
        row.save()
    if name != '':
        row.name = name
        row.save()
    if surname != '':
        row.surname = surname
        row.save()
    if patronimic != '':
        row.patronimic = patronimic
        row.save()
    if phone != '':
        row.phone = phone
        row.save()
    if parol != '':
        row.parol = parol
        row.save()
    if adress != '':
        row.adress = adress
        row.save()
    row.save()


def update_patient(key, name, surname, patronimic, adress, phone, parol, id):
    row = Patient.get(Patient.id == key)
    if id != '':
        row.id = id
    if name != '':
        row.name = name
        print(name)
        print(row.name)
    if surname != '':
        row.surname = surname
    if patronimic != '':
        row.patronimic = patronimic
    if phone != '':
        row.phone = phone
    if parol != '':
        row.parol = parol
    if adress != '':
        row.adress = adress
    row.save()


def update_schedule(key, doctor, days, times_s, times_f, cabinet):
    row = Schedule.get(Schedule.id == key)
    if doctor != '':
        row.doctor = doctor
    if days != '':
        row.days = days
    if times_s != '':
        row.times_s = times_s
    if times_f != '':
        row.times_f = times_f
    if cabinet != '':
        row.cabinet = cabinet
    row.save()


def create_doctor(name, surname, patronimic, adress, phone, parol, id, speciality):
    Doctor.create_table()
    rec1 = Doctor.create(id=id, name=name, surname=surname, patronimic=patronimic, phone=phone,
                          parol=parol, adress=adress, speciality=speciality)
    rec1.save()


def delete_patient_(id):
    rec1 = Patient_card.get(Patient_card.patient == id)
    rec1.delete_instance()
    rec1 = Patient.get(Patient.id == id)
    rec1.delete_instance()


def create_receipt(patient, doctor, recomendation, day):
    Receipt.create_table()
    rec1 = Receipt.create(recomendation=recomendation, day=day, doctor=doctor, patient=patient)
    rec1.save()


def create_seek_history(patient, doctor, diagnos, day, conclusion):
    Seek_history.create_table()
    rec1 = Seek_history.create(patient=patient, day=day, diagnos=diagnos,  conclusion=conclusion, doctor=doctor)
    rec1.save()


def find_patient(key):
    qur = Patient.select(Patient.name, Patient.surname, Patient.patronimic, Patient.adress, Patient.phone, Patient.id).where(Patient.id == key)
    data = []
    for q in qur:
        data.append({
            'Имя:': q.name,
            'Фамилия:': q.surname,
            'Отчество:': q.patronimic,
            'Адрес:': q.adress,
            'Телефон:': q.phone,
            'Полис:': q.id,
        })
    to_json(data)
    items = ['Имя:', 'Фамилия:', 'Отчество:', 'Адрес:', 'Телефон:', 'Полис:']
    to_cvs(data, items)
    print(data)
    return data


def find_talon(key, date, time):
    qur = Talon.select(Talon.patient, Talon.day, Talon.times, Talon.cabinet, Talon.doctor).where(Patient.id == key and Talon.patient == key and Talon.day == date and Talon.times == time)
    doc = []

    for q in qur:
        a = Doctor.select(Doctor.name, Doctor.surname, Doctor.patronimic).where(Doctor.id == q.doctor)
        for k in a:
            doc.append({'Врач:': k.surname + " " + k.name + " " + k.patronimic})
    data = []
    k = 0
    for q in qur:
        d = str(q.day.day)
        m = str(q.day.month)
        y = str(q.day.year)
        h = str(q.times.hour)
        mm = str(q.times.minute)
        if mm < '10':
            mm = '0' + mm
        data.append({
            'Врач:': doc[k]['Врач:'],
            'Дата:': d + "-" + m + "-" + y,
            'Время:': h + "." + mm,
            'Кабинет:': q.cabinet,
        })
        k += 1
    print(data)
    to_json(data)
    items = ['Врач:', 'Дата:', 'Время:', 'Кабинет:']
    to_cvs(data, items)
    return data


def find_date(key):
    qur = Talon.select(Talon.patient, Talon.day, Talon.times, Talon.cabinet, Talon.doctor).where(Patient.id == key and Talon.patient == key)
    data = []
    for q in qur:
        d = str(q.day.day)
        m = str(q.day.month)
        y = str(q.day.year)
        s = d + "-" + m + "-" + y
        flag = True
        for c in data:
            if c == s:
                flag = False

        if flag:
            data.append(s)
    return data


def find_time(key, date):
    qur = Talon.select(Talon.patient, Talon.day, Talon.times, Talon.cabinet, Talon.doctor).where(Patient.id == key and Talon.patient == key and Talon.day == date)
    data = []
    for q in qur:
        h = str(q.times.hour)
        mm = str(q.times.minute)
        if mm < '10':
            mm = '0' + mm
        s = h + ":" + mm
        flag = True
        for c in data:
            if c == s:
                flag = False
        if flag:
            data.append(s)
    return data


def find_receipt(key, date):
    qur = Receipt.select(Receipt.patient, Receipt.day, Receipt.recomendation, Receipt.doctor).where(Receipt.patient == key and Receipt.day == date)
    doc = []
    print(qur)
    for q in qur:
        a = Doctor.select(Doctor.name, Doctor.surname, Doctor.patronimic).where(Doctor.id == q.doctor)
        for k in a:
            doc.append({'Врач:': k.surname + " " + k.name + " " + k.patronimic})
    data = []
    print(doc)
    k = 0
    for q in qur:
        d = str(q.day.day)
        m = str(q.day.month)
        y = str(q.day.year)
        data.append({
            'Врач:': doc[k]['Врач:'],
            'Дата:': d + "-" + m + "-" + y,
            'Рекомендации и назначенные лекарства:': q.recomendation
        })
        k += 1
    print(data)
    to_json(data)
    items = ['Врач:', 'Дата:', 'Рекомендации и назначенные лекарства:']
    to_cvs(data, items)
    return data


def find_date_r(key):
    qur = Receipt.select(Receipt.patient, Receipt.day, Receipt.recomendation, Receipt.doctor).where(Receipt.patient == key)
    data = []
    for q in qur:
        d = str(q.day.day)
        m = str(q.day.month)
        y = str(q.day.year)
        s = y + "-" + m + "-" + d
        flag = True
        for c in data:
            if c == s:
                flag = False
        if flag:
            data.append(s)
    return data


def find_seek_his(key, date):
    qur = Seek_history.select(Seek_history.day, Seek_history.diagnos, Seek_history.doctor, Seek_history.conclusion).where(Seek_history.patient == key and Seek_history.day == date)
    doc = []
    print(qur)
    for q in qur:
        a = Doctor.select(Doctor.name, Doctor.surname, Doctor.patronimic).where(Doctor.id == q.doctor)
        for k in a:
            doc.append({'Врач:': k.surname + " " + k.name + " " + k.patronimic})
    data = []
    print(doc)
    k = 0
    for q in qur:
        d = str(q.day.day)
        m = str(q.day.month)
        y = str(q.day.year)
        data.append({
            'Врач:': doc[k]['Врач:'],
            'Дата:': d + "-" + m + "-" + y,
            'Диагноз:': q.diagnos,
            'Заключение:': q.conclusion
        })
        k += 1
    print(data)
    to_json(data)
    items = ['Врач:', 'Дата:', 'Диагноз:', 'Заключение:']
    to_cvs(data, items)
    return data


def find_date_sh(key):
    qur = Seek_history.select(Seek_history.day).where(Seek_history.patient == key)
    data = []
    for q in qur:
        d = str(q.day.day)
        m = str(q.day.month)
        y = str(q.day.year)
        s = y + "-" + m + "-" + d
        flag = True
        for c in data:
            if c == s:
                flag = False
        if flag:
            data.append(s)
    return data


def is_doctor(key):
    qur = Doctor.select(Doctor.id).where(Doctor.id == key)
    data = []
    for q in qur:
        data.append({
            'Имя:': q.id,
        })
    if len(data) != 0:
        return True
    else:
        return False


def true_parol_d(key, parol):
    qur = Doctor.select(Doctor.parol).where(Doctor.id == key)
    for q in qur:
        print(q.surname)
        if (q.parol == parol):
            return True
        else:
            return False


def is_patient(key):
    qur = Patient.select(Patient.id).where(Patient.id == key)
    data = []
    for q in qur:
        data.append({
            'Имя:': q.id,
        })
    if len(data) != 0:
        return True
    else:
        return False


def true_parol_p(key, parol):
    qur = Patient.select(Patient.parol, Patient.surname).where(Patient.id == key)
    for q in qur:
        print(q.surname)
        if (q.parol == parol):
            return True
        else:
            return False


def is_registrator(key):
    qur = Registrator.select(Registrator.id).where(Registrator.id == key)
    data = []
    for q in qur:
        data.append({
            'Имя:': q.id,
        })
    if len(data) != 0:
        return True
    else:
        return False


def true_parol_r(key, parol):
    qur = Registrator.select(Registrator.parol).where(Registrator.id == key)
    for q in qur:
        print(q.surname)
        if (q.parol == parol):
            return True
        else:
            return False


def is_admin(key):
    qur = Admin.select(Admin.id).where(Admin.id == key)
    data = []
    for q in qur:
        data.append({
            'Имя:': q.id,
        })
    if len(data) != 0:
        return True
    else:
        return False

def is_sc(key):
    qur = Schedule.select(Schedule.id).where(Schedule.id == key)
    data = []
    for q in qur:
        data.append({
            'Имя:': q.id,
        })
    if len(data) != 0:
        return True
    else:
        return False


def true_parol_a(key, parol):
    qur = Admin.select(Admin.parol).where(Admin.id == key)
    for q in qur:
        if (q.parol == parol):
            return True
        else:
            return False


def get_all_doc():
    qur1 = Schedule.select(Schedule.doctor)
    date = []
    for q in qur1:
        qur = Doctor.select(Doctor.name, Doctor.surname, Doctor.patronimic, Doctor.id).where(Doctor.id == q.doctor)
        for qq in qur:
            date.append([qq.id, qq.surname + ' ' + qq.name + ' ' + qq.patronimic])
    return date


def get_schedule(key):
    qur = Schedule.select(Schedule.doctor, Schedule.days, Schedule.times_s, Schedule.times_f, Schedule.cabinet).where(Schedule.doctor == key)
    data = []
    for q in qur:
        h = str(q.times_s.hour)
        mm = str(q.times_s.minute)
        if mm < '10':
            mm = '0' + mm
        h1 = str(q.times_f.hour)
        mm1 = str(q.times_f.minute)
        if mm1 < '10':
            mm1 = '0' + mm1
        data.append({
            'Время:': h + "." + mm + '-' + h1 + "." + mm1,
            'Дни недели:': q.days,
            'Кабинет:': q.cabinet,
        })
    print(data)
    to_json(data)
    items = ['Время:', 'Дни недели:', 'Кабинет:']
    to_cvs(data, items)
    return data


def to_json(data):
    for k, f in enumerate(data):
        with open("data_file.json", "w") as write_file:
            json.dump(f, write_file, ensure_ascii=False, indent=2)
        write_file.close()


def to_cvs(data, items):
    with open("data_file.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(w_file, delimiter=",",
                                     lineterminator="\r", fieldnames=items)
        file_writer.writeheader()
        for k, f in enumerate(data):
            file_writer.writerow(f)

