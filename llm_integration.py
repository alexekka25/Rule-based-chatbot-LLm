import requests
import config

def get_llm_response(user_input):
    """
    Fetch response from Together AI using Llama-3.3-70B-Instruct-Turbo-Free model.
    """
    url = "https://api.together.ai/v1/chat/completions"  # Correct Together AI endpoint
    headers = {
        "Authorization": f"Bearer {config.TOGETHER_AI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "messages": [{"role": "user", "content": user_input}],
        "max_tokens": 100
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        print("API Response Status Code:", response.status_code)
        print("API Response Text:", response.text)  # Print full API response for debugging
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data.get("choices", [{}])[0].get("message", {}).get("content", "No response generated.")
        else:
            return f"Error {response.status_code}: {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"
