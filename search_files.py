import os

def search_word_in_folder(folder_path, word_to_find):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_num, line in enumerate(file, start=1):
                        if word_to_find in line:
                            print(f"[FOUND] '{word_to_find}' in {file_path} (line {line_num}): {line.strip()}")
            except (UnicodeDecodeError, PermissionError, FileNotFoundError) as e:
                pass


is_running=True
while is_running:
    folder_to_search = input('enter the path of the folder("q" to quit): ')
    if folder_to_search.lower() =='q':
        break
    word = input('enter the word: ')

    search_word_in_folder(folder_to_search, word)
