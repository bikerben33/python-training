prompt = "\nPlease enter the cities you have visited:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")






