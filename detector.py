from utils import best_match
 
 
def detect_error(extracted_text, issues):
    """
    Detect the most likely DMS issue from OCR text.
 
    Parameters:
        extracted_text (str): Text extracted from screenshot.
        issues (list): Issues loaded from issues.json
 
    Returns:
        dict:
        {
            "found": True/False,
            "confidence": score,
            "issue": matched_issue
        }
    """
 
    if not extracted_text:
        return {
            "found": False,
            "confidence": 0,
            "issue": None
        }
 
    issue, score = best_match(extracted_text, issues)
 
    if issue:
        return {
            "found": True,
            "confidence": score,
            "issue": issue
        }
 
    return {
        "found": False,
        "confidence": score,
        "issue": None
    }
 
 
def format_solution(issue):
    """
    Convert solution list into readable text.
    """
 
    if not issue:
        return "No solution available."
 
    steps = issue.get("solution", [])
 
    if not steps:
        return "No solution available."
 
    output = ""
 
    for i, step in enumerate(steps, start=1):
        output += f"{i}. {step}\n"
 
    return output

