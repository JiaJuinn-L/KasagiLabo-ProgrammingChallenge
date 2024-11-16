import re

def determine_type(obj):
    obj = obj.strip()  # Remove spaces for alphanumerics
    if obj.isalpha():
        return "Alphabetic String"
    elif re.match(r"^[+-]?\d+\.\d+$", obj):  # Real number regex
        return "Real Number"
    elif obj.isdigit():
        return "Integer"
    else:
        return "Alphanumeric"

# Read and identify objects from file
filename = "test.txt"
output_filename = "output_processed.txt"

with open(filename, "r") as f, open(output_filename, "w") as out:
    content = f.read().strip(",").split(",")
    for obj in content:
        obj_type = determine_type(obj.strip())
        out.write(f"{obj.strip()} - {obj_type}\n")
