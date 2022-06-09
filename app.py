from urllib import response
import streamlit as st
from streamlit_lottie import st_lottie
import json
import datetime

import requests

'''
# Dispatcher Prediction Website
'''

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_bqojdbmn.json")
st_lottie(lottie_hello, key="hello")




warehouse_id = st.number_input('Warehouse Id')#, value=673)
relation_distance = st.number_input('Relation Distance')#, value=559.70127)
carrier_company_id = st.number_input('Carrier Company ID')#, value=673)
pickup_date = st.date_input('Pickup datetime')#, value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('Pickup datetime')#, value=datetime.datetime(2012, 10, 6, 12, 10, 20))
planned_pickup_timestamp = f'{pickup_date} {pickup_time}'

shipment_created_date = st.date_input('Shipment datetime')#, value=datetime.datetime(2012, 10, 6, 12, 10, 20))
shipment_created_time = st.time_input('Shipment datetime')#, value=datetime.datetime(2012, 10, 6, 12, 10, 20))
timestamp_created_at_shipment = f'{shipment_created_date} {shipment_created_time}'




url = 'https://my-image-2drx54htbq-ew.a.run.app/predict'


params = dict(
    warehouse_id=warehouse_id,
    relation_distance=relation_distance,
    carrier_company_id=carrier_company_id,
    planned_pickup_timestamp=planned_pickup_timestamp,
    timestamp_created_at_shipment=timestamp_created_at_shipment)

response = requests.get(url, params=params)

prediction = response.json()

pred = int(prediction['Prediction'])


st.write("The expected FHA delay is ", pred, " days.")

#a = int(pickup_date.strftime('%Y%m%d'))

#new_var = int(pred + a)
#pickup_date
#type(pickup_date)

#st.write("The shipment is expected to be picked up by the Truck arriving", new_var, "at the first hub scan location.")
#"""The shipment is expected to be picked up by the Truck arriving {created_at_date + prediction}
#at the first hub scan location."""
