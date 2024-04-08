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

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        return print(self.volume)

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        return print(self.volume)


if __name__ == "__main__":
    tvPrincipal = TV(False, 0, 1, False, "Sem informações", int)

    tvPrincipal.Power()
    tvPrincipal.aumentarVolume()


