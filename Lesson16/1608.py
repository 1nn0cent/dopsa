messages = []

def print_only_new(message):
    global messages
    if not (message in messages):
        messages.append(message)
        print(message)




