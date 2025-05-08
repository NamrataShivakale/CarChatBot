import json

def load_data(file_path):
    """Load JSON data from a given file path."""
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)

def find_feature(query, features):
    """Find and return the description of a car feature from the features dataset."""
    for key, desc in features.items():
        # Case-insensitive search for the feature key in the query
        if key.replace('_', ' ').lower() in query.lower():
            return desc
    return None

def find_problem(query, problems):
    """Find and return the troubleshooting steps for a car problem from the problems dataset."""
    for key, desc in problems.items():
        # Case-insensitive search for the problem key in the query
        if key.replace('_', ' ').lower() in query.lower():
            return desc
    return None

def retrieve_answer(query, features, problems):
    """Retrieve the answer for a query either from car features or problem troubleshooting."""
    # First, try to find in car features
    feature_answer = find_feature(query, features)
    if feature_answer:
        return f"Feature Answer: {feature_answer}"

    # If not found, try finding in car problems
    problem_answer = find_problem(query, problems)
    if problem_answer:
        return f"Problem Answer: {problem_answer}"

    # If no match found in either, return None
    return None
