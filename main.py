import hashlib


# 32941766
def find_salt(phones, numbers):
    for phone in phones:
        salt = phone - numbers[0]
        for number in numbers[1:]:
            if number + salt not in phones:
                break
        else:
            return salt
    return 0


def hash_number(number, salt, func):
    data = (number + str(salt)).encode('utf-8')
    dict_funcs = {'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha256': hashlib.sha256}
    a = dict_funcs[func](data).hexdigest()
    return a


with open('decoded_hashes.txt', 'r') as file:
    cracked_phones = set(map(int, [i.split(':')[1] for i in file]))

known_numbers = [89156311602, 89678395615, 89859771985, 89109807351, 89108471943]

salt = find_salt(cracked_phones, known_numbers)
print(salt)
with open('cracked.txt', 'w') as file:
    for i in cracked_phones:
        file.write(str(i + salt) + '\n')

with open('cracked.txt', 'r') as f:
    phones = [x.strip() for x in f]

salts = [1, 1234, 123456789, 222]
algorithms = ['md5', 'sha1', 'sha256']

for algorithm in algorithms:
    for salt in salts:
        with open(f'{algorithm}_{salt}.txt', 'w') as f:
            for phone in phones:
                f.write(hash_number(phone, salt, algorithm) + ':' + str(salt) + '\n')
