# filters.py - Filter Non-Business Queries

def is_business_related(user_input):
    """
    Check if the user query is related to Space.ai services.
    """
    business_keywords = [
    "gpu", "cpu", "tpu", "machine learning", "ai services", "pricing",
    "support", "billing", "cloud computing", "subscription", "plan",
    "plans", "features", "feature", "contact", "contact us", "customer support",
    "customer service", "free", "free plan", "limited", "limited access",
    "hello", "hi","services","service","security","securities","contacts","free plan","ai service","price","prices","hii","ok","okk"
]



    
    user_input = user_input.lower()
    
    for keyword in business_keywords:
        if keyword in user_input:
            return True  # Query is related to Space.ai services
    
    return False  # Query is unrelated

def filter_query(user_input):
    """
    Return appropriate response based on query relevance.
    """
    if is_business_related(user_input):
        return None  # Allowed, proceed with rule-based or LLM response
    else:
        return "Sorry, I can only answer questions related to Space.ai business services."
