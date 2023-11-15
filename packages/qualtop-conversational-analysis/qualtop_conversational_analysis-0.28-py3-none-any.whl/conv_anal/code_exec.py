
def check_for_code(response):
    code = ""
    if "```python\n" in response:
        started_code = False
        for line in response.split("\n"):
            if started_code and "```" in line:
                break
            if started_code:
                code += f"{line}\n"
            elif "```python" in line:
                started_code = True
    if code != "":
        return True, code
    return False, code
