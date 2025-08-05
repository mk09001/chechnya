import os
import shutil

# Удаляем все файлы из media/courses
courses_dir = "media/courses"
if os.path.exists(courses_dir):
    shutil.rmtree(courses_dir)
    print("Папка media/courses удалена")

# Удаляем всю папку media
media_dir = "media"
if os.path.exists(media_dir):
    shutil.rmtree(media_dir)
    print("Папка media удалена")

# Удаляем скрипты для работы с изображениями
files_to_remove = [
    "copy_all_images.py",
    "update_course_images.py", 
    "IMAGE_UPDATE_REPORT.md",
    "FINAL_IMAGE_UPDATE.md"
]

for file in files_to_remove:
    if os.path.exists(file):
        os.remove(file)
        print(f"Удален файл: {file}")

print("Все изображения и связанные файлы удалены!") 