from datetime import datetime
from ..models import Measurement
from ..models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.variable = Variable.objects.get(pk=new_var["variable"])
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.dateTime = datetime.strptime(new_var["dateTime"], "%Y-%m-%dT%H:%M:%S.%fZ")
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(variable=Variable.objects.get(pk=var["variable"]), value=var["value"], unit=var["unit"], place=var["place"], dateTime=datetime.strptime(var["dateTime"], "%Y-%m-%dT%H:%M:%S.%fZ"))
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measure = Measurement.objects.get(pk=var_pk)
    if measure:
        measure.delete()