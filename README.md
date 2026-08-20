# FactChecker  GenLayer Intelligent Contract

Verifies statements using LLM consensus. Submit any claim, AI validators return TRUE/FALSE/UNCERTAIN with confidence score and explanation. Uses `gl.eq_principle.prompt_comparative` for multi-validator consensus on GenLayer testnet.

## Usage
Deploy `fact_checker.py` in GenLayer Studio, then call:
- `check_fact("your statement")`  runs AI consensus
- `get_last_result()`  returns verdict JSON

## Example
Input: `"The Eiffel Tower is in Paris"`
Output: `{"verdict": "TRUE", "confidence": 100, "explanation": "..."}`
