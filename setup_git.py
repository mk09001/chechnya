import os
import subprocess
import sys

def run_command(command):
    """Выполняет команду и возвращает результат"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды '{command}': {e}")
        return None

def setup_git_repository():
    """Настраивает Git репозиторий для проекта"""
    
    print("🚀 Настройка Git репозитория для проекта Физика Плюс")
    print("=" * 60)
    
    # 1. Инициализация Git
    print("1. Инициализация Git репозитория...")
    if run_command("git init"):
        print("✅ Git репозиторий инициализирован")
    else:
        print("❌ Ошибка инициализации Git")
        return False
    
    # 2. Добавление всех файлов
    print("2. Добавление файлов в Git...")
    if run_command("git add ."):
        print("✅ Файлы добавлены в индекс")
    else:
        print("❌ Ошибка добавления файлов")
        return False
    
    # 3. Первый коммит
    print("3. Создание первого коммита...")
    if run_command('git commit -m "Initial commit: Физика Плюс - интернет-магазин курсов теоретической физики"'):
        print("✅ Первый коммит создан")
    else:
        print("❌ Ошибка создания коммита")
        return False
    
    # 4. Создание основной ветки
    print("4. Переименование ветки в main...")
    if run_command("git branch -M main"):
        print("✅ Основная ветка переименована в 'main'")
    else:
        print("❌ Ошибка переименования ветки")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Git репозиторий успешно настроен!")
    print("\n📋 Следующие шаги:")
    print("1. Создайте репозиторий на GitHub:")
    print("   - Перейдите на https://github.com/new")
    print("   - Назовите репозиторий: physics-courses")
    print("   - Сделайте его публичным")
    print("   - НЕ инициализируйте с README")
    print("\n2. Подключите локальный репозиторий к GitHub:")
    print("   git remote add origin https://github.com/YOUR_USERNAME/physics-courses.git")
    print("   git push -u origin main")
    print("\n3. Деплой на Render.com:")
    print("   - Подключите GitHub репозиторий к Render")
    print("   - Создайте новый Web Service")
    print("   - Настройте переменные окружения")
    print("   - Укажите команды сборки из README.md")
    
    return True

if __name__ == "__main__":
    setup_git_repository() 