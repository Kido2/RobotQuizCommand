from controller import Controller


class Func_robot(Controller):
    def Turn_off(self):
        return "Encendido"

    def Turn_on(self):
        return "Apagado"

    def Speak(self):
        return "Hola Mundo"

    def Sleep(self):
        return "Z zZ z z zZ X|"
