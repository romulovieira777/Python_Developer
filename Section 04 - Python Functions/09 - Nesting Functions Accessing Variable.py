def display_message(message):
    "Hello"
    def message_sender():
        "Nested function"
        print(message)
    message_sender()


display_message("Show me the money!")
