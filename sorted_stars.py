
import pprint

data = [
    ('Alpha Centauri A', 4.3, 0.26, 1.56), #element 1 in data 
    ('Alpha Centauri B', 4.3, 0.077, 0.45), #element 2 in data
    ('Alpha centauri C', 4.2, 0.000001, 0.000006), #element 3 in data
    ("Barnard's Star", 6.0, 0.00004, 0.0005), #element 4 in data
    ('Wolf 359', 7.7, 0.000001, 0.00002), #element 5 in data
    ('Bd +36 degrees 2147', 8.2,  0.0003, 0.006), #element 6 in data
    ('Luyten 726-8 A', 8.4, 0.0000003, 0.000006), #element 7 in data
    ('Luyten 726-8 B', 8.4, 0.0000002, 0.000004), #element 8 in data
    ('Sirius A', 8.6, 1.00, 23.6), #element 9 in data
    ('Sirius B', 8.6, 0.001, 0.003), #elemenet 10 in data
    ('Ross 154', 9.4, 0.00002, 0.0005), #element 11 in data
]

data_edit = [[row[i] for row in data] for i in range(4)]

star_name = data_edit[0]
distance = data_edit[1]
apparent_brightness = data_edit[2]
absolute_brightness = data_edit[3]
pp = pprint.PrettyPrinter(indent = 5)

print('Ranked by Distance')
#for n in range(11):
#    print star_name[n], distance[n]
ranked_by_distance = [[star_name[x], distance[x]] for x in range(11)] 
pp.pprint(ranked_by_distance)


print('Ranked by Apparent Brightness')
#for n in range(11):
#    print star_name[n], apparent_brightness[n]
ranked_by_apparent_brightness = [[star_name[y], apparent_brightness[y]] for y in range(11)] 
pp.pprint(ranked_by_apparent_brightness) 

print('Ranked by Absolute Brightness')
#for n in range(11):
#    print star_name[n], absolute_brightness[n]
ranked_by_absolute_brightness = [[star_name[z], absolute_brightness[z]] for z in range(11)] 
pp.pprint(ranked_by_absolute_brightness)
