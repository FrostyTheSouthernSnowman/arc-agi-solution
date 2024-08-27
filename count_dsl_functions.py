import json


def count_functions_in_dsl():
    with open("dsl.json") as f:
        dsl_data = json.load(f)
    return len(dsl_data)


function_count = count_functions_in_dsl()
print(f"Number of functions in dsl.json: {function_count}")
