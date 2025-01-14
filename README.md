Below is an example Python code to implement a JSON Validator Service that checks for null values in a given JSON object. It uses a recursive approach to ensure all levels of the JSON are checked for null values.

Key Features:
Recursive Validation: The validate_json method checks for null values at all levels of the JSON structure.
Path Tracking: Keeps track of where null values are found using dot notation for dictionaries and index-based notation for lists.
JSON Validation: Ensures the input is a valid JSON string before attempting to process it.

Sample Input and Output

Input: 1
  Enter JSON string:
  Sample for Invalid JSON
  json_input = {"name": "John", "age": null, "address": {"city": "New York", "zipcode": null}, "hobbies": ["reading", null, {"type": "sports", "name": null}]}
  ignore_fields = Enter fields to ignore (comma-separated): age, address.zipcode

Output: 1
  {'status': 'error', 'invalid_fields': ['age', 'address.zipcode', 'hobbies[1]', 'hobbies[2].name']}

Input: 2
  Enter JSON string:
  Sample for Invalid JSON
  json_input = {"name": "John", "age": 23, "address": {"city": "New York"}, "hobbies": ["reading", {"type": "sports", "name": "Kavida"}]}
  ignore_fields = Enter fields to ignore (comma-separated): 

Output: 2
  {'status': 'success'}

