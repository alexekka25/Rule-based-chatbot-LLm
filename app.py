# app.py - Flask Web Application for Hybrid Chatbot

from flask import Flask, render_template, request, jsonify
from rule_based import get_rule_based_response
from llm_integration import get_llm_response
from filters import filter_query

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").strip()
    
    # Check if the query is business-related
    filter_response = filter_query(user_input)
    if filter_response:
        return jsonify({"response": filter_response})
    
    # Check for rule-based responses first
    rule_response = get_rule_based_response(user_input)
    if rule_response:
        return jsonify({"response": rule_response})
    
    # If no rule-based response, use LLM
    llm_response = get_llm_response(user_input)
    return jsonify({"response": llm_response})

if __name__ == '__main__':
    app.run(debug=True)
