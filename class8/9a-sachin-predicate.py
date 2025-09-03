# Define the relationships
sachin_predicate = "batsman"
batsman_predicate = "cricketer"

# Derive the predicate
if sachin_predicate == "batsman":
    derived_predicate = batsman_predicate
    result = f"Sachin is {derived_predicate}."
else:
    result = "No derivation found."

# Print the result
print(result)