import mimetypes

def is_text_file_with_mimetypes(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    print(mime_type)
    return mime_type is not None and mime_type.startswith('text')

# Пример использования
file_path = '/home/greg/Documents/Материалы в ТП_v03 (доработка по замечаниям).docx'
if is_text_file_with_mimetypes(file_path):
    print(f"Файл {file_path} является текстовым.")
else:
    print(f"Файл {file_path} не является текстовым.")
