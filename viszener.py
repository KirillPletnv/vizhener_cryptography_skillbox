import random
#  Алфавит и символы
alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!@#$%^&*()_+=<>|/?{}[]:;".,\\\''


#  Матрица алфавитов смещенных на 1 значение на каждой новой строке
lists = [i for i in alph]
mut_lists = []
for i in range(len(lists)):
    mut_lists.append((lists[i:] + lists[:i]))

# Тензор алфавитов, а каждой новой матрице которого одна строка смещена на строку вниз
tensor_alph = [mut_lists[k:] + mut_lists[:k] for k in range(len(lists))]
#print(tensor_alph[2][26])

#  Вводим фразу и ключевое слово
orig_text = input('Enter origin text: ')
keyword = input('Keyword: ')
#orig_text = 'attackatdown123!!@#$%^&*()_+={}:">?|||\?/'
#orig_text = 'hfdgjknhkjads.n {}{}{()#&%(*(*&(**(*()#@&_)(@!#&%*#@?>>?>?"":}|'
#orig_text = 'hfdgjknhkjads.n {}{}{()#&%(*(*&(**(*()#@&_DFSFSDFDS)(@!DSGFDSF#&%*#@?>>?>?"":}|'
#orig_text = 'hfdgjknhkjads.n {}{}{()#&%(*(*&(**(*()#@&_DFSFSDFDS)(@!DSGFDSF#&%*#@?>>?>?"":}|ds hewiucbi7t37tc roC3c''U'
#keyword = 'lemon'

#  Реплицируем ключевое слово на длину фразы
def keyword_keys(keyword, orig_text):
    key = ''
    while len(key) < len(orig_text):
        key = key + keyword
    keys = key[:len(orig_text)]
    return keys

keys = keyword_keys(keyword, orig_text)



# print(keys)

#  Шифруем введенную фразу с ключевым словом по индексам алфавита
def encrypt(keys, orig_text):
    k = 0
    encrypted_phrase = ''
    for i in keys:
        # print(alph.index(i))
        indx = alph.index(i)
        wraps_index = alph.index(orig_text[k])
        lst = mut_lists[indx]
        k += 1
        encrypted_phrase = encrypted_phrase + lst[wraps_index]
    # print(mut_lists[indx])
    return encrypted_phrase

#  Расшифровываем
def decrypt(keys, encrypt_phrase):
    k = 0
    decrypted_phrase = ''
    for i in keys:
        # print(alph.index(i))
        indx = alph.index(i)
        # mut_lists[indx]
        wraps_index = mut_lists[indx].index(encrypt_phrase[k])
        # lst = mut_lists[indx]
        # print(alph[wraps_index])
        k += 1
        decrypted_phrase = decrypted_phrase + alph[wraps_index]

    return decrypted_phrase


# Модифицированный 3d шифровальщик виженера, вместо листа смещенных алфавитов - 26 листов смещенных алфавитов,
# каждый из которых в свою очередь смещен еще и построчно, кроме как посимвольно.
# на каждую k(букву следующую по счету у ключа и фразы)
# выдавать новую матрицу смещенных алфавитов - номер матрицы = индекс очередной буквы ключа
def encrypt_modified(keys, orig_text):
    k = 0
    encrypted_phrase = ''
    for i in keys:
        # print(alph.index(i))
        indx = alph.index(i)
        wraps_index = alph.index(orig_text[k])
        #lst = mut_lists[indx]
        lst = tensor_alph[indx][indx]
        k += 1
        encrypted_phrase = encrypted_phrase + lst[wraps_index]
    # print(mut_lists[indx])
    return encrypted_phrase

#Дешифратор модифицированного виженера
def decrypt_modified(keys, encrypt_phrase):
    k = 0
    decrypted_phrase = ''
    for i in keys:
        # print(alph.index(i))
        indx = alph.index(i)
        # mut_lists[indx]
        wraps_index = tensor_alph[indx][indx].index(encrypt_phrase[k])
        # lst = mut_lists[indx]
        # print(alph[wraps_index])
        k += 1
        decrypted_phrase = decrypted_phrase + alph[wraps_index]

    return decrypted_phrase

assert decrypt(keys, encrypt(keys, orig_text)) == orig_text
assert decrypt_modified(keys, encrypt_modified(keys, orig_text)) == orig_text

print("Зашифрованный текст: ", encrypt(keys, orig_text))
print("Расшифрованный обратно текст: ", decrypt(keys, encrypt(keys, orig_text)))

print("------------------------------")
print("Зх-мерный виженер - зашифрованный текст: ", encrypt_modified(keys, orig_text))
print("3х-мерный виженер - расшифрованный текст: ", decrypt_modified(keys, encrypt_modified(keys,  orig_text)))


#Тестовые слова для ключей и текста
def test_data():
    strcs = ''
    for i in range(random.randint(800, 7000)):
        strcs = strcs + random.choice(alph)
    return strcs


# Тесты
def tests():
    for i in range(1, random.randint(100, 300)):
        print("--------------------------")
        print("Тест ", i, ":")
        a_word = test_data()
        k_word = test_data()
        print("-------------------------")
        print("текст: ", a_word[:10] + "......." + a_word[-3:], " : ", len(a_word), "символов")
        print("ключ: ", k_word[:10] + "......." + k_word[-3:], " : ", len(k_word), "символов")
        print("-------------------------")
        print("Зашифрованный текст: ", encrypt(keyword_keys(k_word, a_word), a_word)[:10] + "...")
        print("Расшифрованный обратно текст: ", decrypt(keyword_keys(k_word, a_word), encrypt(keyword_keys(k_word, a_word), a_word))[:10] + "...")
        print("Зашифрованный текст 3d виженера: ", encrypt_modified(keyword_keys(k_word, a_word), a_word)[:10] + "...")
        print("Расшифрованный обратно текст 3d виженера: ", decrypt_modified(keyword_keys(k_word, a_word), encrypt_modified(keyword_keys(k_word, a_word), a_word))[:10] + "...")
        assert decrypt(keyword_keys(k_word, a_word), encrypt(keyword_keys(k_word, a_word), a_word)) == a_word
        assert decrypt_modified(keyword_keys(k_word, a_word), encrypt_modified(keyword_keys(k_word, a_word), a_word)) == a_word
    return True
tests()