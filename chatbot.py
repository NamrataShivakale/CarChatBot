from retriever import find_feature, find_problem, load_data
from llama_cpp import Llama  # or wherever you load your LLaMA model

# Load your local data
features = load_data("data/car_features_usage.json")
problems = load_data("data/car_features.json")
problems = load_data("data/car_problems.json")

# Initialize your LLaMA model
llm = Llama(model_path="models/llama-2-7b-chat.Q4_K_M.gguf", n_ctx=4096)

def get_response(message):
    # First try local retrieval
    feature_info = find_feature(message, features)
    if feature_info:
        return feature_info["title"] + "\n" + "\n".join(feature_info["steps"])

    problem_info = find_problem(message, problems)
    if problem_info:
        return problem_info["title"] + "\n" + "\n".join(problem_info["steps"])

    # Else, fallback to LLaMA inference
    prompt = f"User: {message}\nAssistant:"
    result = llm(prompt, max_tokens=200, stop=["User:"])
    return result["choices"][0]["text"].strip()
