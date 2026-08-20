# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *

import json


class FactChecker(gl.Contract):
    last_result: str

    def __init__(self):
        self.last_result = ""

    @gl.public.write
    def check_fact(self, statement: str) -> None:
        prompt = f"""
You are a fact-checking AI. Verify this statement: "{statement}"

Respond using ONLY the following format:
{{
"verdict": "TRUE or FALSE or UNCERTAIN",
"confidence": 85,
"explanation": "one sentence explanation"
}}
It is mandatory that you respond only using the JSON format above,
nothing else. Don't include any other words or characters,
your output must be only JSON without any formatting prefix or suffix.
This result should be perfectly parseable by a JSON parser without errors.
"""

        def get_fact_result():
            result = gl.nondet.exec_prompt(prompt)
            result = result.replace("```json", "").replace("```", "")
            print(result)
            return result

        result = gl.eq_principle.prompt_comparative(
            get_fact_result, "The value of verdict has to match"
        )
        self.last_result = result

    @gl.public.view
    def get_last_result(self) -> str:
        return self.last_result
