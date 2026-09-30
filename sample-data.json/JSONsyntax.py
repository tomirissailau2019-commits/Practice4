import json


# 1. JSON string

json_string = '''
{
    "name": "Tomiris",
    "age": 18,
    "student": true,
    "subjects": ["Python", "Math", "English"]
}
'''


# 2. Parsing JSON with json.loads()

student = json.loads(json_string)

print("Parsed JSON:")
print(student)

print("\nStudent name:")
print(student["name"])

print("\nStudent subjects:")
print(student["subjects"])


# 3. Converting Python to JSON with json.dumps()

student_data = {
    "name": "Tomiris",
    "age": 18,
    "student": True,
    "subjects": ["Python", "Math", "English"]
}

json_data = json.dumps(student_data, indent=4)

print("\nPython converted to JSON:")
print(json_data)


# 4. Writing JSON to a file

new_data = {
    "course": "Programming Principles 2",
    "practice": 4,
    "topics": [
        "Iterators",
        "Generators",
        "Dates",
        "Math",
        "JSON"
    ]
}

with open("new-data.json", "w", encoding="utf-8") as file:
    json.dump(new_data, file, indent=4)

print("\nJSON file was created.")


# 5. Reading JSON from a file

with open("new-data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("\nData read from JSON file:")
print(loaded_data)


# 6. Working with sample-data.json

with open("../sample-data.json", "r", encoding="utf-8") as file:
    sample_data = json.load(file)

print("\nSample data:")
print(sample_data)


# 7. Working with data from sample-data.json

if "students" in sample_data:
    print("\nStudents:")

    for student in sample_data["students"]:
        print(
            student["id"],
            student["name"],
            student["age"],
            student["major"]
        )