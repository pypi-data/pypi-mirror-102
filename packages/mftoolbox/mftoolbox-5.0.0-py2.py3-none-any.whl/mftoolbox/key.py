import uuid
import math
import random

class Key:

    def __init__(self, key='', base_chave_hex='', secret_4_digits = '1772'):
        if key == '':
            self.key= self.generate()
        else:
            #self.key = key.lower()
            self.key = key
            self.base_chave_hex = base_chave_hex.hex
            self.secret_4_digits = secret_4_digits

    def gerar_base(base_chave_hex):
        chars = len(base_chave_hex)
        soma = 0
        for i in range(chars):
            soma += ord(base_chave_hex[i])
        return soma

    def verify(self, base_chave_hex):
        score = 0
        check_digit = self.key[5]
        check_digit_count = 0
        chunks = self.key.split('-')
        for chunk in chunks:
            if len(chunk) != 4:
                return False
            for char in chunk:
                if char == check_digit and chunk.count(char) == 1:
                    check_digit_count += 1
                score += ord(char)
        score_esperado = 1808 +  math.floor(math.sqrt(base_chave_hex))
        if score == score_esperado and check_digit_count == 4:
            return True
        return False

    def generate(base_chave_hex):
        key = ''
        chunk = ''
        check_digit_count = 0
        tries = 0
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        while True:
            while len(key) < 25:
                char = random.choice(alphabet)
                key += char
                chunk += char
                if len(chunk) == 4:
                    key += '-'
                    chunk = ''
            key = key[:-1]

            if Key(key).verify(base_chave_hex):
                return key
            else:
                tries +=1
                print(f'Testou chave {key} (tentativas = {tries}, {datetime.now() - INICIO_EXECUCAO})')
                key = ''

    def __str__(self):
        valid = 'Invalid'
        if self.verify():
            valid = 'Valid'
        return self.key + ':' + valid