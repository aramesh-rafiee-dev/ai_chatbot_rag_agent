import re
import ast
import operator



_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def _safe_eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        return _ALLOWED_OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
        return _ALLOWED_OPERATORS[type(node.op)](_safe_eval(node.operand))
    raise ValueError("Expression not allowed")


def calculator(expression):
    try:
        clean_expr = re.sub(r'[^\d\+\-\*/\.\(\)\s]', '', expression).strip()
        parsed = ast.parse(clean_expr, mode='eval')
        result = _safe_eval(parsed.body)
        return f"Result: {result}"
    except Exception as e:
        return f"ERROR in calculation: {e}"


def weather(city):
    weather_data = {
        "tehran": "sunny, 25°C",
        "rasht": "cloudy, 18°C",
        "shiraz": "clear, 22°C",
    }
    return weather_data.get(city.lower(), "City not found")


def agent(user_input):
    print(f"\nUser said: {user_input}")
    if re.search(r'[\d]+\s*[\+\-\*/]\s*[\d]+', user_input):
        print("Agent decided to use: Calculator tool.")
        return calculator(user_input)
    elif "weather" in user_input.lower():
        for city in ["tehran", "rasht", "shiraz"]:
            if city in user_input.lower():
                print(f"Agent decided to use: Weather tool for {city}.")
                return weather(city)
        return "Please specify a city."
    else:
        return "I don't know how to handle this request."


if __name__ == "__main__":
    print(agent("What is 25+17?"))
    print(agent("What is the weather in Rasht?"))
    print(agent("Tell me a joke."))
