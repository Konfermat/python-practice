import time
import functools
from collections import defaultdict

# ==========================
# 1️⃣ Базовая функция ядра
# ==========================

def process_transaction(account_id: int, amount: float, transaction_type: str) -> dict:
    """Эмуляция выполнения банковской операции."""
    # Здесь мог бы быть реальный вызов к базе данных
    if transaction_type == "deposit":
        result = {"account_id": account_id, "balance": amount, "status": "OK"}
    elif transaction_type == "withdraw":
        result = {"account_id": account_id, "balance": -amount, "status": "OK"}
    elif transaction_type == "balance":
        result = {"account_id": account_id, "balance": 10_000, "status": "OK"}
    else:
        result = {"account_id": account_id, "status": "ERROR", "message": "Unknown transaction type"}
    return result


# ==========================
# 2️⃣ Декоратор логирования
# ==========================

def log_transaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        result = func(*args, **kwargs)
        print(f"[{start_time}] TRANSACTION: {kwargs.get('transaction_type') or args[2]}, "
              f"Account={kwargs.get('account_id') or args[0]}, "
              f"Amount={kwargs.get('amount') or args[1]}, Result={result}")
        return result
    return wrapper


# ==========================
# 3️⃣ Контроль доступа
# ==========================

def require_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(account_id: int, amount: float, transaction_type: str, user_role: str = "client"):
            # Проверяем права
            if user_role == "client" and transaction_type == "withdraw" and amount > 50_000:
                raise PermissionError("Клиент не имеет права снимать более 50,000 за раз!")
            if user_role not in ["client", "manager", "admin"]:
                raise PermissionError(f"Неизвестная роль: {user_role}")
            return func(account_id, amount, transaction_type)
        return wrapper
    return decorator


# ==========================
# 4️⃣ Ограничение по количеству вызовов
# ==========================

def limit(rate: int, period: int):
    """Не более `rate` вызовов за `period` секунд для одного account_id."""
    calls = defaultdict(list)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(account_id: int, amount: float, transaction_type: str):
            now = time.time()
            # Удаляем старые вызовы
            calls[account_id] = [t for t in calls[account_id] if now - t < period]
            if len(calls[account_id]) >= rate:
                raise RuntimeError(f"Превышен лимит обращений ({rate} за {period} секунд)")
            calls[account_id].append(now)
            return func(account_id, amount, transaction_type)
        return wrapper
    return decorator


# ==========================
# 5️⃣ Кэширование баланса
# ==========================

def cache_balance(ttl: int):
    """Кэширует результат запроса баланса на ttl секунд."""
    cache = {}

    def decorator(func):
        @functools.wraps(func)
        def wrapper(account_id: int, amount: float, transaction_type: str):
            if transaction_type == "balance":
                if account_id in cache:
                    value, timestamp = cache[account_id]
                    if time.time() - timestamp < ttl:
                        print(f"[CACHE] Возврат кэшированного баланса для счета {account_id}")
                        return value
                result = func(account_id, amount, transaction_type)
                cache[account_id] = (result, time.time())
                return result
            else:
                return func(account_id, amount, transaction_type)
        return wrapper
    return decorator


# ==========================
# 6️⃣ Объединяем всё
# ==========================

@log_transaction
@cache_balance(ttl=10)
@limit(rate=3, period=10)
@require_role(role="client")
def secure_process_transaction(account_id: int, amount: float, transaction_type: str, user_role: str = "client"):
    return process_transaction(account_id, amount, transaction_type)


# ==========================
# 7️⃣ Тестирование
# ==========================

if __name__ == "__main__":
    print("=== Пример работы системы ===")

    # 1. Баланс (кэшируется)
    print(secure_process_transaction(1, 0, "balance", user_role="client"))
    time.sleep(2)
    print(secure_process_transaction(1, 0, "balance", user_role="client"))  # Из кэша

    # 2. Вклад
    print(secure_process_transaction(1, 20000, "deposit", user_role="client"))

    # 3. Снятие
    try:
        print(secure_process_transaction(1, 60000, "withdraw", user_role="client"))
    except Exception as e:
        print("Ошибка доступа:", e)

    # 4. Лимит вызовов
    for i in range(4):
        try:
            print(secure_process_transaction(2, 100, "deposit", user_role="client"))
        except Exception as e:
            print("Лимит:", e)
