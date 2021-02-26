class Reciver:
    def __init__(self, command):
        self.command = command

    def do_command(self, command):
        command = self.command.lower()
        if command == "comer":
            return "No valid command for this robot :)"
        elif command == "encender":
            return f"Doing the task: {command}"
        elif command == "apagar":
            return f"Doing the task: {command}"
        elif command == "hablar":
            return f"Doing the task: {command}"
        elif command == "dormir":
            return f"Doing the task: {command}"
        else:
            return f"This {command} is not valid X_X"
