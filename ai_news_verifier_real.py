# { "Depends": "py-genlayer:test" }

from genlayer import *

class AINewsVerifierReal(gl.Contract):
    last_result: str

    def __init__(self):
        self.last_result = ""

    def _ask_ai(self, claim: str):
        prompt = f"""
Classify this claim:
{claim}

Return JSON only:
{{"label":"trusted","reason":"short reason"}}
or {{"label":"suspicious","reason":"short reason"}}
or {{"label":"unclear","reason":"short reason"}}
"""
        return gl.nondet.exec_prompt(prompt, response_format="json")

    def _validator(self, leader_result) -> bool:
        if not isinstance(leader_result, gl.vm.Return):
            return False

        data = leader_result.calldata
        return (
            isinstance(data, dict)
            and data.get("label") in ["trusted", "suspicious", "unclear"]
            and isinstance(data.get("reason"), str)
            and len(data.get("reason")) > 0
        )

    @gl.public.write
    def check_claim(self, claim: str):
        result = gl.vm.run_nondet_unsafe(
            lambda: self._ask_ai(claim),
            self._validator
        )
        self.last_result = str(result)

    @gl.public.view
    def get_last_result(self) -> str:
        return self.last_result
