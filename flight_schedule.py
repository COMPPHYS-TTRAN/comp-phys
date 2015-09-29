airports = {"DCA": "Washington, D.C.", "IAD": "Dulles", "LHR": "London=Heathrow", \
           "SVO": "Moscow", "CDA": "Chicago-Midway", "SBA": "Santa Barbara", \
           "LAX": "Los Angeles", "JFK": "New York City", "MIA": "Miami", "AUM": "Austin, Minnesota"}

#airline, number, heading to, gate, time (decimal time)
flights = [("Southwest", 145, "DCA", 1, 6.00), \
          ("United", 3, "IAD", 1, 7.1), ("United", 302, "LHR", 5, 6.5), \
          ("Aeroflot", 34, "SVO", 5, 9.00), ("Southwest", 146, "CDA", 1, 9.60), \
          ("United", 46, "LAX", 5, 6.5), ("Southwest", 23, "SBA", 6, 12.5), \
          ("United", 2, "LAX", 10, 12.5), ("Southwest", 59, "LAX", 11, 14.5), \
          ("American", 1, "JFK", 12, 11.3), ("USAirways", 8, "MIA", 20, 13.1), \
          ("United", 2032, "MIA", 21, 15.1), ("SpamAir", 1, "AUM", 42, 14.4)]


#part 1.1, sort by airline
sorted_flights = sorted(flights)

print "Flight", "\t", "\t", "Destination", "\t", "\t", "Gate", "\t", "\t", "Time" 
for n in range(len(flights)):   
    flight1 = sorted_flights[n][0]
    flight2 = sorted_flights[n][1]
    destination1 = sorted_flights[n][2]
    destination2 = airports[destination1]
    gate = sorted_flights[n][3]
    time = sorted_flights[n][4]
    print flight1, flight2, "\t", destination2, "\t", "\t", gate, "\t", time
    
#part 1.2, sort by time
flights_time = sorted(flights, key=lambda flights_airline: flights_airline[4])

print "Time", "\t", "\t", "Flight", "\t", "\t", "Destination", "\t", "\t", "Gate" 
for n in range(len(flights)):
    time = flights_time[n][4]
    flight1 = flights_time[n][0]
    flight2 = flights_time[n][1]
    destination1 = flights_time[n][2]
    destination2 = airports[destination1]
    gate = flights_time[n][3]
    print time, "\t", "\t", flight1, flight2, "\t", destination2, "\t", gate