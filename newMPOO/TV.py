class TV:
    def __init__(self, power, volume, channel, mute, getInfo, selectChannel):
        self.power = power
        self.volume = volume
        self.channel = channel
        self.mute = mute
        self.getInfo = getInfo
        self.selectChannel = selectChannel

    def Power(self):
        if self.power == False:
            self.power = True
            print("TV ligada")
        else:
            self.power = False
            print("TV desligada")

    def maisVolume(self):
        if self.power == True:
            if self.mute == False:
                if self.volume < 100:
                    self.volume += 1
                return print(self.volume)
            else:
                print("TV MUTE")
        else:
            print("TV OFF")
            pass

    def menosVolume(self):
        if self.power == True:
            if self.mute == False:
                if self.volume > 0:
                    self.volume -= 1
                return print(self.volume)
            else:
                print("TV MUTE")
        else:
            print("TV OFF")
            pass

    def canalProximo(self):
        if self.power == True:
            if self.channel < 5:
                self.channel += 1
            return print(self.channel)
        else:
            print("TV OFF")
            pass

    def canalAnterior(self):
        if self.power == True:
            if self.channel > 1:
                self.channel -= 1
            return print(self.channel)
        else:
            print("TV OFF")
            pass

    def muteTV(self):
        if self.power == True:
            if self.mute == True:
                self.mute = False
            elif self.mute == False:
                self.mute = True
                self.volume = 0
        else:
            print("TV OFF")
            pass



if __name__ == "__main__":
    tvPrincipal = TV(False, 0, 1, False, "Sem informações", int)

    tvPrincipal.Power()
    tvPrincipal.maisVolume()
    tvPrincipal.maisVolume()
    tvPrincipal.maisVolume()
    tvPrincipal.muteTV()
    tvPrincipal.maisVolume()


