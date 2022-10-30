import time
from math import sin, cos, sqrt, atan2, radians

st = time.time()


def calculate_distance(pointA, pointB):

    # approximate radius of earth in km
    R = 6371.0

    lat1 = radians(pointA[0])
    lon1 = radians(pointA[1])
    lat2 = radians(pointB[0])
    lon2 = radians(pointB[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


aaa = [53.2296756, 21.0122287]
aa1 = [[52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.406374, 16.65656], 
        [52.406374, 16.65656], 
        [52.406374, 16.65656], 
        [52.406374, 16.65656], 
        [52.406374, 16.65656],
        [52.406374, 16.65656],
        [52.40637, 16.5454], 
        [52.36666, 16.43434],
        [52.406374, 16.434343],
        [52.3, 16.434343],
        [52.406374, 16.4343],
        [52.494, 16.4999],
        [52.2222, 16.33],
        [52.4444, 16.55], 
        [52.3333, 16.5555],
        [52.555, 16.656565]]

# aa1=[[52.406374, 16.9251681]]
result = []
for value in aa1:

    result.append(calculate_distance(aaa, value))

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


print("with raw code")
# print(sorted(result))


def str2list(rawstr):
    temp = rawstr.split(",")
    return [float(temp[0]), float(temp[1])]


listuser = [
    {'username': "huyen",
     "location": "52.40633374,16.65656"
     },
    {'username': "huyen1",
     "location": "52.40336374,16.656434356"
     },
    {'username': "huyen2",
     "location": "52.443,16.65643456"
     },
    {'username': "huyen3",
     "location": "52.4323206374,16.65656"
     },
    {'username': "huyen4",
     "location": "52.47606374,16.6565986"
     },
    {'username': "huyen5",
     "location": "52.4989806374,16.65656"
     },
    {'username': "huyen6",
     "location": "52.498906374,16.656656556"
     },
    {'username': "huyen7",
     "location": "52.65406374,16.665655656"
     },
    {'username': "huyen8",
     "location": "52.4006374,16.065656"
     },
    {'username': "huyen9",
     "location": "52.0406374,16.865656"
     },
    {'username': "huyen10",
     "location": "52.8406374,16.1165656"
     }
]

a={}
for i in listuser:
    # print(i.get("location"))  

    temp_username = i.get("username")
    temp_location = i.get("location")
    
    print(f"the distance from Meee to {temp_username} la "+str(calculate_distance(aaa, str2list(temp_location))))
    # print(temp_username)

    a.update({temp_username:temp_location+"|"+str(calculate_distance(aaa, str2list(temp_location)))})


# del listuser


for i,j in a.items():
    print(i,j)
# print(a)
