from sds011 import *
import time
import aqi
sensor = SDS011("COM3")
# Turn-on sensor
sensor.sleep(sleep=False)
time.sleep(10)
pmt_2_5, pmt_10 = sensor.query()
print(f"    PMT2.5: {pmt_2_5} ug/m3     ", end='')
print(f"PMT10: {pmt_10} ug/m3")
sensor.sleep(sleep=True)

aqi_2_5 = aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pmt_2_5))
aqi_10 = aqi.to_iaqi(aqi.POLLUTANT_PM10, str(pmt_10)) 

print(f"    AQI (PMT2.5): {aqi_2_5}     ", end='')
print(f"AQI(PMT10): {aqi_10}")