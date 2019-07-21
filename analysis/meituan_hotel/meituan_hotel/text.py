import re

latlngs = "https://apis.map.qq.com/ws/staticmap/v2/?key=7DUBZ-QMI33-2HB3H-37DMO-3TUMZ-JJBFS&size=430*117&zoom=15&center=34.280435,108.924272&scale=2&markers=icon:https://p0.meituan.net/codeman/67ca1d133d8a0cd1b2749f2989dfb82f1456.png|34.280435,108.924272"
url = "https://hotel.meituan.com/1557736/"

re.search('center=(\S+)&', latlngs)
latlng = re.search('center=(*+)&', latlngs)
print(latlng)
