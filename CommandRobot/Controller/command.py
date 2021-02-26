from CommandRobot.Controller.controller import Controller
from CommandRobot.Controller.Reciver import Reciver


class Command_bot(Controller):
    def __init__(self,  command):
        self.command = command
        self.reciver = Reciver(self.command)

    def executebot(self):
        command = self.reciver.do_command(self.command)
        print(f"Command received:  {self.command}")
        print(command)
