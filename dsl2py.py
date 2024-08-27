import json
import random
import string

dsl_symbols = json.load(open("dsl.json"))


def dsl2py(dsl_json):
    python_code = """
def arc_dsl(I):
"""

    python_code += "\n".join(
        f"    {dsl_json[function][-1]
               } = {function}({', '.join(dsl_json[function][:-1])})"
        for function in dsl_json.keys()
    )

    return python_code
