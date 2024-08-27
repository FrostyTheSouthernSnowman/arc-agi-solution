import json
import ast

"""
Loop over the contents of dsl.py and save all the DSL functions to a file.
The file will be called dsl.json
"""

with open("dsl.py", "r") as f:
    contents = f.read()

# Parse the contents of dsl.py to extract function names, their inputs, typing info, and return types
parsed_code = ast.parse(contents)
functions = {
    node.name: {
        "args": [arg.arg for arg in node.args.args],
        "types": [ast.get_source_segment(contents, arg) for arg in node.args.args],
        "returns": ast.get_source_segment(contents, node.returns) if node.returns else None
    }
    for node in ast.walk(parsed_code) if isinstance(node, ast.FunctionDef)
}

# Save the functions to dsl.json
with open("dsl.json", "w+") as json_file:
    json.dump(functions, json_file, indent=4)
