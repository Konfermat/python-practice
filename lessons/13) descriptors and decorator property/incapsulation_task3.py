class RoleDescriptor:

    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def __set__(self, instance, value):
        current_role = instance.current_role
        #instance экземпляр класса user
        if 'admin' in self.allowed_roles:
            #разрешает изменение
            instance.__dict__[self.name] = value
            # self.name устанавливается в get как атрибут
        elif 'editor' in self.allowed_roles or 'viewer' in self.allowed_roles:
            raise PermissionError(f'1Role {current_role} cannot be modified')
        else:
            raise PermissionError(f'2Role {current_role} cannot be modified')

    def __get__(self, instance, owner):
        current_role = instance.current_role

        if current_role in self.allowed_roles:
            return instance.__dict__[self.name] #возвращаем значение атрибута
        raise PermissionError(f'Role {current_role} access denied')

    # для установки имени атрибута
    def __set_name__(self, owner, name):
        self.name = name # сохраняет имя атрибута

class User:
    # определяем атрибуты с контролем доступа через дискриптор
    field1 = RoleDescriptor(allowed_roles=['admin', 'editor'])
    field2 = RoleDescriptor(allowed_roles=['editor'])
    field3 = RoleDescriptor(allowed_roles=['admin', 'viewer'])

    def __init__(self, role):
        self.current_role = role # текущая роль
        # начальные значения атрибутов
        self.field1 = 'default value field 1'
        self.field2 = 'default value field 2'
        self.field3 = 'default value field 3'

try:
    admin_user = User('admin')
    print(admin_user.field3)
    admin_user.field3 = 'new value field 3'
    print(admin_user.field3)

    # viewer_user = User('viewer')
    # print(viewer_user.field3)
    # viewer_user.field3 = 'trying modify'
except PermissionError as e:
    print(e)
