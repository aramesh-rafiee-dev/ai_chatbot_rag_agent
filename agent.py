import re
def calculator(expression):
    try:
        clean_expr=re.sub(r'[^\d\+\-\*/\.\(\)]','',expression)
        result=eval(clean_expr)
        return f"Result:{result}"
    except Exception as e:
        return f"ERROR in calculation: {e}"
def weather(city):
    weather_data={
        "tehran":"sunny,25°C",
        "rasht":"cloudy,18°C",
        "shiraz":"clear,22°C"
    }
    return weather_data.get(city.lower(),"City not found")
def agent(user_input):
    print(f"\nUser said:{user_input}")
    if re.search(r'[\d]+[\+\-\*/][\d]+',user_input):
        print("Agent decided to use:Caculator tool.")
        return calculator(user_input)
    elif "weather" in user_input.lower():
        for city in ["tehran","rasht","shiraz"]:
            if city in user_input.lower():
                print(f"Agent decided to use:Weather tool for {city}.")
                return weather(city)
        return "Please specify a city."
    else:
        return "I don't know how to handel this request."
print(agent("What is 25+17?"))
print(agent("What is the weather in Rasht?"))
print(agent("Tell me a joke."))