people_database = [
    ("Alice", 0.95, (120, 200)),
    ("Bob", 0.87, (300, 150)),
    ("Charlie", 0.92, (450, 180))
]

names = [ person[0] for person in people_database]
print(f"Known people: { names }")


#Filter high-confidence detections (like AI does)
confident_detections = [person for person in people_database if person[1] > 0.9]

#Transform data (extract just coordinates)
all_location = [person[2] for person in people_database]

#Calculate averages (basic AI analytics)
average_confidence = sum(person[1] for person in people_database)
len(people_database)
