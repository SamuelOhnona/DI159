import json

# Given JSON string
sampleJson = '''{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}'''

# Convert JSON string to dictionary
data = json.loads(sampleJson)

# Accessing the nested "salary" key
salary = data["company"]["employee"]["payable"]["salary"] 
print("Salary:", salary)

# Adding a new key "birth_date" at the same level as "name"
data["company"]["employee"]["birth_date"] = "1990-05-15"

# Save the updated dictionary as JSON to a file
with open("updated_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Updated JSON saved to updated_data.json")
