class PainterBot:
    def __init__(self, name, style, efficiency):
        self.name = name
        self.style = style
        self.efficiency = efficiency
    
    def paint(self, length):
        if not isinstance(length, int):
            raise TypeError('Ошибка. Аргумент должен быть целым числом.')
        return '#' * length
    def __add__(self, other):
        tmp = ComboPainterBot(self, other)
        return tmp
    def __str__(self):
        return f'Имя: {self.name}\nСтиль: {self.style}\nЭффективность: {self.efficiency}'
class LinePainterBot(PainterBot):
    def paint(self, length):
        if not isinstance(length, int):
            raise TypeError('Ошибка. Аргумент должен быть целым числом.')        
        return '=' * length
 
class WavePainterBot(PainterBot):
    def paint(self, length):
        if not isinstance(length, int):
            raise TypeError('Ошибка. Аргумент должен быть целым числом.')
        flag = True
        ch1 = '~'
        ch2 = '-'
        result = ''
        for i in range(length):
            if flag:
                result += ch1
                flag = False
            else:
                result += ch2
                flag = True
        return result

class ComboPainterBot:
    def __init__(self, bot1, bot2):
        self.name = f'Комбо [{bot1.name} + {bot2.name}]'
        self.style = 'Комбинированный'
        if bot1.efficiency <= bot2.efficiency: 
            self.efficiency = bot1.efficiency
        else:
            self.efficiency = bot2.efficiency
        self.bot1 = bot1
        self.bot2 = bot2
    def paint(self, length):
        if not isinstance(length, int):
            raise TypeError('Ошибка. Аргумент должен быть целым числом.')
        return f'{self.bot1.paint(length)}|{self.bot2.paint(length)}'
    def __str__(self):
        return f'Имя: {self.name}\nСтиль: {self.style}\nЭффективность: {self.efficiency}'
def gallery_exhibibtion(painter_list, length):
    for i in painter_list:
        print(i.paint(length))

# создаем ботов
pb1 = PainterBot('Pedro', 'Pixel', 10)
lpb1 = LinePainterBot('Ernesto', 'Linar', 5)
wpb1 = WavePainterBot('Ricardo', 'Camel', 7)

# создаем комбинированные версии ботов
cpb1 = pb1 + lpb1
cpb2 = lpb1 + wpb1
cpb3 = wpb1 + pb1

# проверка роботов
print(pb1)
print(pb1.paint(3))
print()
print(lpb1)
print(lpb1.paint(3))
print()
print(wpb1)
print(wpb1.paint(3))
print()

# проверка комбинированных ботов
print(cpb1)
print(cpb1.paint(3))
print()
print(cpb2)
print(cpb2.paint(3))
print()
print(cpb3)
print(cpb3.paint(3))
print()

# проверка функции gallery_exhibition
bot_list = [pb1, lpb1, wpb1, cpb1, cpb2, cpb3]
gallery_exhibibtion(bot_list, 4)