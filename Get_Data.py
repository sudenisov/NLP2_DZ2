
def GetData(dialogues_file_path = './data/dialogs.txt', yoda_file_path = './data/yoda_text.txt'):
    # Список для хранения диалогов
    dialogues_1 = []
    dialogues_2 = []

    # Чтение диалогов из файла и удаление префиксов
    with open(dialogues_file_path, 'r', encoding='utf-8') as file_1, open(yoda_file_path, 'r', encoding='utf-8') as file_2:
        lines = file_1.readlines()
        alist_1 = []
        for i in lines:
            alist_1.append(i.rstrip('\n'))
        lines = file_2.readlines()
        alist_2 = []
        for i in lines:
            alist_2.append(i.rstrip('\n'))

        # Обработка строк с диалогами
        for i in range(len(alist_1)):
            line_1 = alist_1[i]
            line_2 = alist_2[i]
            parts = line_1.split('\t')
            if len(parts) > 1:
                dialogues_1.append(parts[0])
                dialogues_2.append(line_2)

    return dialogues_1, dialogues_2
