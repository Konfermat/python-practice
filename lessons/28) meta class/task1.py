
class FinalClassError(TypeError):
    '''
        пользовательское исключение при попытке наследования от
        финального класса
        TypeError - шика в системе типов и наследования
    '''
    pass

class FinalMeta(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        default_message = f'НЕЛЬЗЯ НАСЛЕДОВАТЬ'
        for base in bases:
            if isinstance(base, FinalMeta):
                base_message = getattr(base, 'FinalMeta__message', default_message)
                allowed_subclasses = getattr(base, 'FinalMeta__allowed_subclasses', ())
                if name not in allowed_subclasses:
                    raise FinalClassError(base_message)
        return super().__new__(cls, name, bases, attrs, **kwargs)

class BaseFinal(metaclass=FinalMeta):
    def final_method(self):
        return 'финальный метод'

class ConfigError(metaclass=FinalMeta):
    FinalMeta__message = ' наследование от класса ConfigError запрещено'
    pass

class AllowedFinal(metaclass=FinalMeta):
    FinalMeta__allowed_subclasses = ('Spec', )

base_instance = BaseFinal()
try:
    class ChildBase(BaseFinal):
        pass
    # пользовательсое исключениие
except FinalClassError as e:
    print(e)

try:
    class ChildConfig(ConfigError):
        pass
except FinalClassError as e:
    print(e)

class Spec(AllowedFinal):
    pass


