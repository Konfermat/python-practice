import random
from abc import ABC, abstractmethod

# дескриптор для проверки на отрицательность числа
class PositiveNumDescriptor:
    def __set_name__(self, owner, name):
        self.name = name #запоминаем имя атрибута

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f'{self.name} должно быть положительным')
        instance.__dict__[self.name] = value

#класс для заклинаний
class Spell(ABC):
    def __init__(self, name, cost):
        self.name = name #название заклинания
        self.cost = cost # стоимость заклинания

    @abstractmethod
    def cast(self, caster, target):
        pass

    def __str__(self):
        return f'{self.name} (стоимость: {self.cost})'

class Fireball(Spell):
    def __init__(self):
        super().__init__('Огненный шар', 15)

    def cast(self, caster, target):
        damage = random.randint(10, 25) #урон
        target.health = max(0, target.health - damage)
        caster.magic_power -= damage
        print(f'{caster.name} запускает {self.name} в '
              f'{target.name} и наносит {damage} урона!')
        return target.health == 0 #если цель побеждена True

class Lightning(Spell):
    def __init__(self):
        super().__init__('Молния', 25)

    def cast(self, caster, target):
        damage = random.randint(20, 35) #урон
        target.health = max(0, target.health - damage)
        caster.magic_power -= damage
        print(f'{caster.name} запускает {self.name} в '
              f'{target.name} и наносит {damage} урона!')
        return target.health == 0 #если цель побеждена True

class Healing(Spell):
    def __init__(self):
        super().__init__('Исцеление', 20)

    def cast(self, caster, target):
        heal_amount = random.randint(15, 30)
        caster.health += heal_amount
        caster.magic_power -= heal_amount
        print(f'{caster.name} исцеляет себя на '
              f'{heal_amount} единиц здоровья')
        return False #так как никто не побеждает

class Mage:
    health = PositiveNumDescriptor()
    magic_power = PositiveNumDescriptor()

    def __init__(self, name, health, magic_power):
        self.name = name
        self.health = health
        self.magic_power = magic_power
        self._spells = []

    def learn_spell(self, spell):
        #знает ли маг это заклинание
        if spell not in self._spells:
            self._spells.append(spell)
            print(f'{self.name} выучил заклинание {spell.name}')
        else:
            print(f'{self.name} уже знает это заклинание')

    def cast_spell(self, spell, target):
        if spell not in self._spells:
            print(f'{self.name} не знает этого заклинания!')
            return False
        if self.magic_power < spell.cost:
            print(f'У {self.name} недостаточно силы')
            return False

        return spell.cast(self, target)

    @property
    def spells(self):
        return self._spells.copy()

    @classmethod
    def get_available_spells(cls):
        return [Fireball(), Healing(), Lightning()]
    #список доступных заклинаний

    @staticmethod
    def create_random_mage(name):
        health = random.randint(70, 120)
        magic_power = random.randint(50, 100)
        return Mage(name, health, magic_power)

    def is_dead(self):
        return self.health == 0 #побежден ли маг

    def __str__(self):
        return (f'{self.name} (Здоровье: {self.health},'
                f'Магия: {self.magic_power})')

#доступные заклинания мага
def show_available_spells(mage):
    available_spells = [spell for spell in mage.spells
                        if spell.cost <= mage.magic_power]
    if not available_spells:
        print('нет доступных заклинаний')
        return False

    print('\nДоступные заклинания')
    for i, spell in enumerate(available_spells, 1):
        print(f'{i}. {spell}')

    while True:
        try:
            choice = input('Выберите номер заклинания '
                           'или "п" для пропуска хода').strip().lower()
            if choice == 'п':
                return None
            choice = int(choice) - 1
            if 0 <= choice < len(available_spells):
                return available_spells[choice]
            print('неккоретный номер, попробуйте еще раз раз')
        except ValueError:
            print('Введите число или "п"')

def magic_duel(player1, player2):
    print('Игра начинается')

    current_player, opponent = player1, player2

    while True:
        print(f'\nХодит {current_player.name}')
        print(player1)
        print(player2)

        spell = show_available_spells(current_player)

        if spell:
            damage = current_player.cast_spell(spell, opponent)
            if damage:
                print(f'\n{current_player} побеждает в магической битве')
                return
        current_player, opponent = opponent, current_player

def main():
    mage1 = Mage.create_random_mage(input('Введите имя первого мага ') or 'Гендальф')
    mage2 = Mage.create_random_mage(input('Введите имя второго мага: ') or 'Саруман')

    for spell in Mage.get_available_spells():
        mage1.learn_spell(spell)
        mage2.learn_spell(spell)
    magic_duel(mage1, mage2)

if __name__ == '__main__':
    main()




