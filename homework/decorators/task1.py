
def requires_permission(permission):
    def decorator(func):
        def wrapper(id_user):
            if permission.strip().lower() == 'admin':
                return func(id_user)
            else:
                return f'Access denied for {permission}'
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(id_user):
    return f'{id_user} was deleted'
    
print(delete_user(112))
print(delete_user(5782))

@requires_permission('админ')
def delete_user(id_user):
    return f'{id_user} was deleted'
    
print(delete_user(112))
print(delete_user(5782))