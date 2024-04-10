class TV:
    def __init__(self):
        self.power = False
        self.volume = 0
        self.channel = 1
        self.mute = False
        self.getInfo = "getInfo"
        self.selectChannel = self.channel

    def Power(self):
        self.power = not self.power
        if self.power:
            print("TV ligada")
        else:
            print("TV desligada")

    def maisvolume(self):
        if self.power:
            if not self.mute:
                if self.volume < 100:
                    self.volume += 1
                print("Volume:", self.volume)
            else:
                print("TV MUTE")
        else:
            print("TV OFF")

    def menosvolume(self):
        if self.power:
            if not self.mute:
                if self.volume > 0:
                    self.volume -= 1
                print("Volume:", self.volume)
            else:
                print("TV MUTE")
        else:
            print("TV OFF")

    def canalproximo(self):
        if self.power:
            if self.channel < 5:
                self.channel += 1
            print("Canal:", self.channel)
        else:
            print("TV OFF")

    def canalanterior(self):
        if self.power:
            if self.channel > 1:
                self.channel -= 1
            print("Canal:", self.channel)
        else:
            print("TV OFF")

    def mutetv(self):
        if self.power:
            self.mute = not self.mute
            if self.mute:
                print("TV MUTADA")
            else:
                print("MUTE DESLIGADO")
                self.volume = 0
        else:
            print("TV OFF")

    def info(self):
        if self.power:
            self.getInfo = ("Canal atual: ", self.channel, "Volume: ", self.volume)
            print(self.getInfo)
        else:
            print("TV OFF")

    def selecionarcanal(self):
        if self.power:
            print("Canal atual: ", self.channel)
            self.selectChannel = input("Select channel: ")
            self.selectChannel = int(self.selectChannel)
            print("Indo para o canal: ", self.selectChannel)
            self.channel = self.selectChannel
        else:
            print("TV OFF")



if __name__ == "__main__":
    tvPrincipal = TV()


    def menu():
        print("[1]Power")
        print("[2]Aumentar volume")
        print("[3]Diminuir volume")
        print("[4]Próximo canal")
        print("[5]Canal anterior")
        print("[6]Mute")
        print("[7]Obter informações")
        print("[8]Selecionar canal")
        print("[0]Fechar Menu")

        op = input("Selecione a opção: ")

        if op == '1':
            tvPrincipal.Power()
            return menu()
        elif op == '2':
            tvPrincipal.maisvolume()
            return menu()
        elif op == '3':
            tvPrincipal.menosvolume()
            return menu()
        elif op == '4':
            tvPrincipal.canalproximo()
            return menu()
        elif op == '5':
            tvPrincipal.canalanterior()
            return menu()
        elif op == '6':
            tvPrincipal.mutetv()
            return menu()
        elif op == '7':
            tvPrincipal.info()
            return menu()
        elif op == '8':
            tvPrincipal.selecionarcanal()
            return menu()
        elif op == '0':
            pass
        else:
            print("Opção inválida")
            return menu()


    menu()
