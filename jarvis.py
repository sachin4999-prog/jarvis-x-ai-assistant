def understand_command(command):
    command = command.lower()

    if "open" in command and "project" in command:
        return "OPEN_PROJECT"

    elif "open" in command and "presentation" in command:
        return "OPEN_PRESENTATION"

    elif "find" in command:
        return "SEARCH_FILES"

    elif "prepare" in command and "workspace" in command:
        return "PREPARE_WORKSPACE"

    elif "hello" in command or "hi" in command:
        return "GREETING"

    else:
        return "UNKNOWN"


print("JARVIS-X v0.1")
print("System online. Type a command.")

while True:
    user_command = input("\nYou: ")

    if user_command.lower() == "exit":
        print("JARVIS: Shutting down.")
        break

    intent = understand_command(user_command)

    if intent == "GREETING":
        print("JARVIS: Hello. How can I assist you?")

    elif intent == "OPEN_PROJECT":
        print("JARVIS: I understand. You want to open your project.")

    elif intent == "OPEN_PRESENTATION":
        print("JARVIS: I understand. You want to open your presentation.")

    elif intent == "SEARCH_FILES":
        print("JARVIS: I understand. You want me to find a file.")

    elif intent == "PREPARE_WORKSPACE":
        print("JARVIS: Understood. You want me to prepare your workspace.")

    else:
        print("JARVIS: I'm not sure what you want me to do yet.")
