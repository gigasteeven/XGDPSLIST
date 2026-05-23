import json
import os

def main():
    print("=== Утилита для добавления уровня в XGDPS List ===")
    
    file_name = input("Введите внутреннее имя файла (например, Bloodbath, без .json): ").strip()
    if not file_name:
        print("Имя файла не может быть пустым.")
        return
        
    level_id = input("ID уровня в игре: ").strip()
    name = input("Название уровня: ").strip()
    author = input("Автор уровня (паблишер): ").strip()
    creators_raw = input("Соавторы (через запятую, если один - просто введите его): ").strip()
    creators = [c.strip() for c in creators_raw.split(',')] if creators_raw else []
    verifier = input("Кто верифицировал (verifier): ").strip()
    verification = input("Ссылка на видео верификации: ").strip()
    percent = input("Процент для попадания в лист (обычно 100): ").strip()
    if not percent:
        percent = "100"
    password = input("Пароль уровня (Free to copy или цифры, можно пропустить): ").strip()
    
    level_data = {
        "id": int(level_id) if level_id.isdigit() else level_id,
        "name": name,
        "author": author,
        "creators": creators,
        "verifier": verifier,
        "verification": verification,
        "percentToQualify": int(percent) if percent.isdigit() else percent,
        "password": password,
        "records": []
    }
    
    # Сохраняем файл уровня
    file_path = os.path.join("data", f"{file_name}.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(level_data, f, indent=4, ensure_ascii=False)
    print(f"\n[+] Файл уровня {file_path} успешно создан.")
    
    # Добавляем в лист
    list_path = os.path.join("data", "_list.json")
    if os.path.exists(list_path):
        with open(list_path, 'r', encoding='utf-8') as f:
            gdps_list = json.load(f)
            
        print(f"\nТекущее количество уровней в листе: {len(gdps_list)}")
        pos_raw = input(f"На какое место поставить {name}? (1-{len(gdps_list)+1}): ").strip()
        
        try:
            pos = int(pos_raw)
            pos = max(1, min(pos, len(gdps_list) + 1))
            gdps_list.insert(pos - 1, file_name)
            
            with open(list_path, 'w', encoding='utf-8') as f:
                json.dump(gdps_list, f, indent=4, ensure_ascii=False)
            print(f"[+] Уровень {name} добавлен на {pos} место в {list_path}.")
        except ValueError:
            print("[-] Ошибка: введено не число. Уровень создан, но не добавлен в _list.json. Вам придется добавить его в _list.json вручную.")
    else:
        print(f"[-] Файл {list_path} не найден.")

    print("\nГотово! Нажмите Enter, чтобы выйти.")
    input()

if __name__ == "__main__":
    main()
