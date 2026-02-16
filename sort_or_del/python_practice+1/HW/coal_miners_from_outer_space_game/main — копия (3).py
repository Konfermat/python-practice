import threading
import multiprocessing as mp
import asyncio
import random
import time
from queue import Queue, Empty

from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.console import Console

console = Console()

# ---------------------- Глобальное состояние ----------------------

WAREHOUSE_LOCK = threading.Lock()
STATE_LOCK = threading.Lock()

WAREHOUSE = {
    "Energy": 1000,
    "Metal": 1000,
    "Crystals": 1000,
    "Parts": 1000,
}

money = 5000
health = 100
target_money = 10_000

# Планеты и цены (4x4)
PLANETS = ["Ice-9", "Fire", "Mechanicus", "Neutral"]
RESOURCES = ["Energy", "Metal", "Crystals", "Parts"]

PRICES = {
    "Ice-9":      {"Energy": 10, "Metal": 25, "Crystals": 80, "Parts": 30},
    "Fire":       {"Energy": 20, "Metal": 40, "Crystals": 100, "Parts": 0},
    "Mechanicus": {"Energy": 15, "Metal": 30, "Crystals": 90, "Parts": 10},
    "Neutral":    {"Energy": 18, "Metal": 35, "Crystals": 95, "Parts": 20},
}

EVENT_LOG = []           # последние события для вывода
MAX_EVENTS = 5

game_running = True

# ---------------------- Шахты (Threading) ----------------------

class Mine(threading.Thread):
    def __init__(self, name, resource, base_rate):
        super().__init__(daemon=True)
        self.name = name
        self.resource = resource
        self.base_rate = base_rate
        self.level = 1
        self.broken = False
        self.running = True
        self.lock = threading.Lock()
        self._next_break_time = time.time() + random.randint(30, 90)

    @property
    def rate(self):
        return int(self.base_rate * self.level)

    def run(self):
        while self.running:
            now = time.time()
            with self.lock:
                if not self.broken:
                    # добыча
                    with WAREHOUSE_LOCK:
                        WAREHOUSE[self.resource] += self.rate
                    # случайная поломка
                    if now >= self._next_break_time:
                        self.broken = True
                        add_event(f"[АВАРИЯ] {self.name} сломалась!")
                else:
                    # если сломана — ничего не делаем
                    pass
            time.sleep(1)

    def repair(self):
        global money
        with self.lock:
            if not self.broken:
                return "Шахта не сломана."
            # расход запчастей
            with WAREHOUSE_LOCK:
                if WAREHOUSE["Parts"] < 10:
                    return "Недостаточно запчастей."
                WAREHOUSE["Parts"] -= 10
            add_event(f"[РЕМОНТ] Ремонт {self.name} (5 сек)...")
            time.sleep(5)
            self.broken = False
            self._next_break_time = time.time() + random.randint(30, 90)
        add_event(f"[РЕМОНТ] {self.name} отремонтирована.")
        return "ОК"

    def upgrade(self):
        global money
        with self.lock:
            cost = 1000 * self.level
            if money < cost:
                return "Недостаточно денег."
            add_event(f"[УЛУЧШЕНИЕ] {self.name} улучшается (5 сек)...")
            money -= cost
            time.sleep(5)
            self.level += 1
        add_event(f"[УЛУЧШЕНИЕ] {self.name} теперь уровень {self.level}.")
        return "ОК"


mines = [
    Mine("Mine #1 (Energy)", "Energy", 5),
    Mine("Mine #2 (Metal)", "Metal", 2),
    Mine("Mine #3 (Crystals)", "Crystals", 1),
]

# ---------------------- Корабль и asyncio ----------------------

class ShipState:
    def __init__(self):
        self.lock = threading.Lock()
        self.is_flying = False
        self.destination = None
        self.eta = 0
        self.cargo = {r: 0 for r in RESOURCES}

ship_state = ShipState()

async def fly_to(planet: str, flight_time: int = None):
    """Асинхронный полёт корабля."""
    if flight_time is None:
        flight_time = random.randint(3, 7)
    with ship_state.lock:
        if ship_state.is_flying:
            add_event("[КОРАБЛЬ] Уже в полёте.")
            return
        ship_state.is_flying = True
        ship_state.destination = planet
        ship_state.eta = flight_time
    add_event(f"[ПОЛЁТ] Корабль вылетел на {planet} ({flight_time} сек).")

    for _ in range(flight_time):
        await asyncio.sleep(1)
        with ship_state.lock:
            ship_state.eta -= 1

    with ship_state.lock:
        ship_state.is_flying = False
    add_event(f"[ПРИБЫТИЕ] Корабль прибыл на {planet}.")

async def update_prices():
    """Асинхронное обновление цен каждые 3 сек."""
    while game_running:
        await asyncio.sleep(3)
        for planet in PLANETS:
            for res in RESOURCES:
                old = PRICES[planet][res]
                delta = random.randint(-3, 3)
                new = max(1, old + delta)
                PRICES[planet][res] = new
        add_event("[РЫНОК] Цены обновлены.")

async def random_events():
    """Случайные события каждые 10–20 сек (упрощённо)."""
    global health
    while game_running:
        await asyncio.sleep(random.randint(10, 20))
        event_type = random.choice(["meteor", "solar", "nothing"])
        if event_type == "meteor":
            # -10% цены
            for planet in PLANETS:
                for r in RESOURCES:
                    PRICES[planet][r] = max(1, int(PRICES[planet][r] * 0.9))
            add_event("[СОБЫТИЕ] Метеоритный дождь! Цены -10%.")
        elif event_type == "solar":
            # просто логируем; влияние на шахты можете дописать
            add_event("[СОБЫТИЕ] Солнечная вспышка! Шахты временно замедлены.")
        else:
            add_event("[СОБЫТИЕ] Космическая тишина.")

# ---------------------- Multiprocessing: бой ----------------------

def battle_process(strength_player: int, strength_pirates: int, result_queue: mp.Queue):
    """Простая симуляция боя в отдельном процессе."""
    player_hp = 100
    pirate_hp = 80
    random.seed()
    while player_hp > 0 and pirate_hp > 0:
        # ход игрока
        pirate_hp -= random.randint(5, strength_player)
        if pirate_hp <= 0:
            break
        # ход пиратов
        player_hp -= random.randint(5, strength_pirates)
        time.sleep(0.2)
    if player_hp > 0 and pirate_hp <= 0:
        result_queue.put(("win", player_hp))
    elif player_hp <= 0 and pirate_hp > 0:
        result_queue.put(("lose", 0))
    else:
        result_queue.put(("draw", max(player_hp, 0)))

def start_battle():
    global health, money
    add_event("[ПИРАТЫ] Нападение пиратов! Запуск процесса боя...")
    q = mp.Queue()
    p = mp.Process(target=battle_process, args=(25, 20, q))
    p.start()
    result, hp_left = q.get()   # игра ждёт
    p.join()

    if result == "win":
        lost = 100 - hp_left
        health -= lost
        add_event(f"[БОЙ] Победа! Потеряно {lost} HP.")
    elif result == "lose":
        health = 0
        add_event("[БОЙ] Поражение! Станция уничтожена.")
    else:
        lost = 50
        health -= lost
        add_event(f"[БОЙ] Ничья. Потеряно {lost} HP.")
    if health <= 0:
        add_event("[ИГРА] Здоровье упало до 0.")

# ---------------------- Ввод команд в отдельном потоке ----------------------

input_queue: Queue[str] = Queue()

def input_thread():
    while game_running:
        try:
            cmd = input("> ")
        except EOFError:
            break
        input_queue.put(cmd.strip())

# ---------------------- Вспомогательные функции ----------------------

def add_event(text: str):
    EVENT_LOG.append(text)
    if len(EVENT_LOG) > MAX_EVENTS:
        EVENT_LOG.pop(0)

def build_status_table() -> Table:
    table = Table(title="Станция космического шахтёра")
    table.add_column("Параметр", style="cyan", no_wrap=True)
    table.add_column("Значение", style="magenta")

    with STATE_LOCK:
        global money, health
        table.add_row("Деньги", str(money))
        table.add_row("Здоровье", str(health))
    with WAREHOUSE_LOCK:
        for r in RESOURCES:
            table.add_row(f"Склад {r}", str(WAREHOUSE[r]))

    for i, m in enumerate(mines, start=1):
        with m.lock:
            status = "Сломана" if m.broken else "Работает"
            table.add_row(
                f"{m.name}",
                f"{status}, уровень {m.level}, +{m.rate}/сек"
            )
    with ship_state.lock:
        if ship_state.is_flying:
            table.add_row(
                "Корабль",
                f"Летит на {ship_state.destination}, ETA: {ship_state.eta} сек"
            )
        else:
            table.add_row("Корабль", "На станции")

    return table

def build_market_table() -> Table:
    table = Table(title="Рынок")
    table.add_column("Планета", style="green", no_wrap=True)
    for r in RESOURCES:
        table.add_column(r)

    for planet in PLANETS:
        row = [planet]
        for r in RESOURCES:
            row.append(str(PRICES[planet][r]))
        table.add_row(*row)
    return table

def build_events_panel() -> Panel:
    text = "\n".join(EVENT_LOG[-MAX_EVENTS:])
    return Panel(text or "Пока что ничего не произошло.", title="События")

def build_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="upper", ratio=3),
        Layout(name="events", ratio=1),
    )
    layout["upper"].split_row(
        Layout(name="status"),
        Layout(name="market"),
    )
    layout["status"].update(build_status_table())
    layout["market"].update(build_market_table())
    layout["events"].update(build_events_panel())
    return layout

# ---------------------- Обработка команд ----------------------

async def handle_command(cmd: str):
    global money, health
    parts = cmd.split()
    if not parts:
        return

    op = parts[0].lower()

    if op == "help":
        add_event("Команды: help, upgrade <1|2|3>, repair <1|2|3>, fly <planet>, battle, quit")
    elif op == "upgrade" and len(parts) == 2:
        idx = int(parts[1]) - 1
        if 0 <= idx < len(mines):
            result = mines[idx].upgrade()
            if result != "ОК":
                add_event(result)
    elif op == "repair" and len(parts) == 2:
        idx = int(parts[1]) - 1
        if 0 <= idx < len(mines):
            result = mines[idx].repair()
            if result != "ОК":
                add_event(result)
    elif op == "fly" and len(parts) == 2:
        planet = parts[1]
        if planet not in PLANETS:
            add_event("Неизвестная планета.")
        else:
            asyncio.create_task(fly_to(planet))
    elif op == "battle":
        # синхронный запуск процесса (игра ждёт)
        start_battle()
    elif op == "quit":
        add_event("Выход из игры.")
        global game_running
        game_running = False
    else:
        add_event("Неизвестная команда. help для списка.")

# ---------------------- Основной цикл с Rich Live ----------------------

async def main_async():
    # запуск шахт
    for m in mines:
        m.start()

    # запуск фоновых async задач
    asyncio.create_task(update_prices())
    asyncio.create_task(random_events())

    # поток ввода
    t_in = threading.Thread(target=input_thread, daemon=True)
    t_in.start()

    with Live(build_layout(), refresh_per_second=10, console=console, screen=True) as live:
        while game_running and health > 0 and money < target_money:
            # обновление интерфейса
            live.update(build_layout())

            # обработка команд
            try:
                cmd = input_queue.get_nowait()
            except Empty:
                cmd = None

            if cmd:
                await handle_command(cmd)

            await asyncio.sleep(0.1)

    # остановка шахт
    for m in mines:
        m.running = False

    console.clear()
    if health <= 0:
        console.print("[red]Игра окончена: станция уничтожена.[/red]")
    elif money >= target_money:
        console.print("[green]Поздравляем! Цель по деньгам достигнута.[/green]")
    else:
        console.print("[yellow]Игра завершена пользователем.[/yellow]")


def main():
    mp.freeze_support()  # на Windows
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
