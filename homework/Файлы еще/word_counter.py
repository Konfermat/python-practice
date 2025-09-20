import string

def only_words(text):
    tmp = text
    separators = list(string.punctuation)
    separators.append('\n')
    for i in separators:
        if i in tmp:
            tmp = tmp.split(i)
            tmp = ' '.join(tmp)
    return tmp.split()
    
def word_count(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        file_text = only_words(f.read().lower())
        
        while True:
            separators = ['и', 'в', 'на', 'с', 'у', 'о']
            cnt = 0
            for i in separators:
                if i in file_text:
                    file_text.pop(file_text.index(i))
                if not i in file_text:
                    cnt += 1
            if cnt == len(separators):
                break
        return len(file_text)
        
def find_word(file_name, word):
    with open(file_name, 'r', encoding='utf-8') as f:
        cnt = 0
        text = f.read().lower()
        text = only_words(text)

        while word.lower() in text:
            text.pop(text.index(word))
            cnt += 1
        return cnt
        
def top_five(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words_for_key = set(only_words(text))
        words_cnt = {}
        for i in words_for_key:
            words_cnt[i] = find_word('book.txt', i)
        words_cnt_dict = dict(sorted(words_cnt.items(), key=lambda item: item[1], reverse=True))
        result = [[i, j] for i, j in words_cnt_dict.items()][:5]
        return result
        
def save_stats(file_name):
    file_name_stats = file_name[:-4] + '_stats.txt'
    wc = word_count(file_name)
    tf = top_five(file_name)
    with open(f'{file_name_stats}', 'w', encoding='utf-8') as f:
        f.write(f'Общее количество слов: {wc}\n\n')
        f.write('Топ пять самых встречающихся слов:\n')
        for i in range(5):
            f.write(f'{i+1}: Слово: "{tf[i][0]}". Количество слов: {tf[i][1]}\n')

save_stats('book.txt')
