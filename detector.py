import json
 
def detect_issue(text):
    with open("issues.json", "r") as f:
        issues = json.load(f)
 
    for issue in issues:
        for keyword in issue["keywords"]:
            if keyword.lower() in text:
                return issue
 
    return None
has context menu
