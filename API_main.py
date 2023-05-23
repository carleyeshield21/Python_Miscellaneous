import requests

latitude_sjdm_bul = 14.805674
longitude_sjdm_bul = 121.065528

iss_req = requests.get('http://api.open-notify.org/iss-now.json')
sunset_sunrise_req = requests.get('https://api.sunrise-sunset.org/json')
iss_req.raise_for_status()
sunset_sunrise_req.raise_for_status()
# print(iss_req)
# print(sunset_sunrise_req)
# print(iss_req.raise_for_status())
# print(iss_req.cookies)
# print(iss_req.url)
# print(iss_req.reason)
# print(iss_req.elapsed)
# print(iss_req.json())

# iss_json_dict = iss_req.json()
# print(iss_json_dict)
#
# sunset_sunrise_json_dict = sunset_sunrise_req.json()
# print(sunset_sunrise_json_dict['results'])
# print(sunset_sunrise_req.elapsed)
# print(sunset_sunrise_json_dict['results']['sunrise'])
# print(sunset_sunrise_json_dict['results']['sunset'])

parameters = {
    'lat': latitude_sjdm_bul,
    'lng': longitude_sjdm_bul,
    'formatted': 0
}
sunset_sunrise_req_latlong = requests.get('https://api.sunrise-sunset.org/json',params=parameters)
print(sunset_sunrise_req_latlong)
sunrise_sunset_data = sunset_sunrise_req_latlong.json()
print(sunrise_sunset_data)
print(sunrise_sunset_data['results']['sunrise'])
print(sunrise_sunset_data['results']['sunset'])
print(sunrise_sunset_data['results']['sunrise'].split('T'))
print(sunrise_sunset_data['results']['sunrise'].split('T')[1])
print(sunrise_sunset_data['results']['sunrise'].split('T')[1].split(':'))
print(sunrise_sunset_data['results']['sunrise'].split('T')[1].split(':')[0])