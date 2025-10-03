import subprocess
import os
import sys

# Имя выходного файла для хэша
OUTPUT_HASH_FILE = "ssh_hash_out.txt"
# Режим Hashcat для SSH Private Key (RSA/DSA/EC/OPENSSH)
HASHCAT_MODE = "22000" 

def convert_ssh_key():
    """
    Основная функция для запроса путей и конвертации ключа.
    """
    print("-" * 50)
    print("Конвертер SSH-ключа в формат для Hashcat/John")
    print("-" * 50)

    # 1. Запрашиваем путь к ssh2john.py
    while True:
        ssh2john_path = input("Введите ПОЛНЫЙ путь к скрипту ssh2john.py: ").strip()
        if not os.path.exists(ssh2john_path):
            print(f"❌ Ошибка: Файл не найден по пути: {ssh2john_path}")
        elif not ssh2john_path.endswith('ssh2john.py'):
            print("❌ Ошибка: Убедитесь, что вы указали именно файл 'ssh2john.py'.")
        else:
            break
            
    # 2. Запрашиваем путь к оригинальному ключу
    while True:
        key_path = input("Введите ПОЛНЫЙ путь к НЕКОНВЕРТИРОВАННОМУ SSH-ключу (например, ./hash.txt): ").strip()
        
        if not os.path.exists(key_path):
            print(f"❌ Ошибка: Файл не найден по пути: {key_path}")
        else:
            break
            
    # 3. Запрашиваем имя выходного файла
    output_path = input(f"Введите имя для выходного ХЭШ-файла (Enter для '{OUTPUT_HASH_FILE}'): ").strip()
    if not output_path:
        output_path = OUTPUT_HASH_FILE
        
    # 4. Выполняем конвертацию
    try:
        print(f"\n⚙️ Запускаем конвертацию: {key_path} -> {output_path}")
        
        # Используем subprocess.run для выполнения команды конвертации
        with open(output_path, "w") as outfile:
            # sys.executable гарантирует запуск скрипта через интерпретатор python
            subprocess.run(
                [sys.executable, ssh2john_path, key_path], 
                stdout=outfile,
                stderr=subprocess.PIPE,
                check=True # Выбросит ошибку, если код возврата не 0
            )

        print("-" * 50)
        print(f"✅ Конвертация прошла успешно!")
        print(f"Хэш сохранен в файл: {output_path}")
        print(f"Режим Hashcat для взлома: -m {HASHCAT_MODE}")
        print(f"Команда для Hashcat: hashcat -m {HASHCAT_MODE} -a 0 {output_path} /путь/к/wordlist.txt")
        print("-" * 50)

    except subprocess.CalledProcessError as e:
        print("-" * 50)
        print("❌ ОШИБКА КОНВЕРТАЦИИ!")
        print("Проверьте, что оригинальный ключ (hash.txt) содержит полный блок BEGIN/END.")
        print(f"Ошибка скрипта: {e.stderr.decode('utf-8').strip()}")
        print("-" * 50)
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    convert_ssh_key()