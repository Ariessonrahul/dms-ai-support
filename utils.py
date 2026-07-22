from rapidfuzz import fuzz
 
 
def normalize(text):
    """Convert text to lowercase and remove extra spaces."""
    if text is None:
        return ""
    return str(text).strip().lower()
 
 
def search_issue(query, issues):
    """
    Search issues by error name or keywords.
    Returns matching issues.
    """
    query = normalize(query)
    results = []
 
    for item in issues:
        error = normalize(item.get("error", ""))
        keywords = [normalize(k) for k in item.get("keywords", [])]
 
        if query in error:
            results.append(item)
            continue
 
        if any(query in k for k in keywords):
            results.append(item)
 
    return results
 
 
def best_match(query, issues, threshold=70):
    """
    Find the best matching issue using fuzzy matching.
    Returns (issue, score)
    """
    query = normalize(query)
 
    best_issue = None
    best_score = 0
 
    for item in issues:
        error = normalize(item.get("error", ""))
 
        score = fuzz.ratio(query, error)
 
        if score > best_score:
            best_score = score
            best_issue = item
 
        for keyword in item.get("keywords", []):
            score = fuzz.ratio(query, normalize(keyword))
 
            if score > best_score:
                best_score = score
                best_issue = item
 
    if best_score >= threshold:
        return best_issue, best_score
 
    return None, best_score
 
 
def get_statistics(issues):
    """
    Return simple dashboard statistics.
    """
    return {
        "total_issues": len(issues),
        "total_keywords": sum(len(i.get("keywords", [])) for i in issues),
    }

