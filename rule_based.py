# rule_based.py - Rule-Based Chatbot for Space.ai

def get_rule_based_response(user_input):
    """
    Check if user_input matches predefined rules and return response.
    """
    responses = {
        "services": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML.",
        "pricing": "Our plans: Free (limited access), Basic ($10/month), Intermediate ($50/month), Advanced ($100/month).",
        "support": "We offer 24/7 call and chat support for all our customers.",
        "complaints": "If you have service issues, please contact support at support@space.ai or call +1-800-SPACEAI.",
        "security": "We provide enterprise-grade security with encrypted data storage and secure API access.",
        "billing": "Billing and payment details can be found in your account settings.",
        "billing plan": "Billing and payment details can be found in your account settings.",
        "billing plans": "Billing and payment details can be found in your account settings.",
        "billing features": "Billing and payment details can be found in your account settings.",
        "billing feature": "Billing and payment details can be found in your account settings.",
        "contact": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "contact us": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "contact support": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "contact customer support": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "contact customer service": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "contact us for support": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "contact us for customer support": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "contact us for customer service": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "contact customer service for support": "You can contact us at support@space.ai or call +1-800-SPACEAI.",
        "plans": "Our plans: Free (limited access), Basic ($10/month), Intermediate ($50/month), Advanced ($100/month).",
        "plan": "Our plans: Free (limited access), Basic ($10/month), Intermediate ($50/month), Advanced ($100/month).",
        "features": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML.",
        "feature": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML.",
        "free": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "free plan": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "free plans": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "free features": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "free feature": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "limited": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "limited time": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "limited access": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "limited access plan": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "limited access plans": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "limited access features": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "limited access feature": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "limited time plan": "Space.ai provides high-performance GPU, CPU, and TPU cloud services for AI & ML for limited time for free plan.",
        "hi": "Hello! I am your assistant. How can I help you?",
        "hii": "Hello! I am your assistant. How can I help you?",
        "hello": "Hello! I am your assistant. How can I help you?",
        "securities": "We provide enterprise-grade security with encrypted data storage and secure API access.",
        "prices": "Our plans: Free (limited access), Basic ($10/month), Intermediate ($50/month), Advanced ($100/month).",
        "price": "Our plans: Free (limited access), Basic ($10/month), Intermediate ($50/month), Advanced ($100/month).",
        "ok": "Ok, I will take your request and forward it to our customer support team. They will get back to you soon.",
        "okk": "Ok, I will take your request and forward it to our customer support team. They will get back to you soon.",
        "okkk": "Ok, I will take your request and forward it to our customer support team. They will get back to you soon.",
        "okkkk": "Ok, I will take your request and forward it to our customer support team. They will get back to you soon.",
        "okkkkk": "Ok, I will take your request and forward it to our customer support team. They will get back to you soon.",
        


    }
    
    # Normalize input
    user_input = user_input.lower()
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return None  # Not found in rule-based responses
