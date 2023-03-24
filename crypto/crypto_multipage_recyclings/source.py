from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random, os

FLAG = b'HTB{??????????????????????}'


class CAES:

    def __init__(self):
        self.key = os.urandom(16)
        print("================================KEY================================")
        print(self.key.hex())
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def blockify(self, message, size):
        return [message[i:i + size] for i in range(0, len(message), size)]

    def xor(self, a, b):
        return b''.join([bytes([_a ^ _b]) for _a, _b in zip(a, b)])

    def encrypt(self, message):
        iv = os.urandom(16)

        ciphertext = b''
        plaintext = iv
        print("==========IV============")
        print(iv)

        blocks = self.blockify(message, 16)
        print("==========Blockly message============")
        print(blocks)
        for block in blocks:
            print(plaintext)
            ct = self.cipher.encrypt(plaintext)
            print("===xor===")
            print(block)
            encrypted_block = self.xor(block, ct)
            ciphertext += encrypted_block
            print("===cipher===")
            print(ciphertext)
            print("============")
            plaintext = encrypted_block

        return ciphertext

    def leak(self, blocks):
        # r = random.randint(0, len(blocks) - 2)
        r = 3
        print("==========leak block=============")
        print(blocks[r])
        print(blocks[r].hex())
        print(blocks[r + 1])
        print(blocks[r + 1].hex())
        leak = [self.cipher.encrypt(blocks[i]).hex() for i in [r, r + 1]]
        return r, leak


def main():
    aes = CAES()
    message = pad(FLAG * 4, 16)

    print("==========original message============")
    print(message)

    ciphertext = aes.encrypt(message)
    print("==========ciphertext============")
    print(ciphertext)

    ciphertext_blocks = aes.blockify(ciphertext, 16)

    print("==========ciphertext_blocks============")
    print(ciphertext_blocks[3].hex())
    print(ciphertext_blocks[3+1].hex())

    r, leak = aes.leak(ciphertext_blocks)
    print("==========leak============")
    print(leak)

    with open('output1.txt', 'w') as f:
        f.write(f'ct = {ciphertext.hex()}\nr = {r}\nphrases = {leak}\n')

    plain = aes.xor(b'\xfd^\x7fw\xf4\x06c\xd7\x85Q\xdc\x1dQ\xdd\xf4\xaa', b'm\xcf\x07\xc3\r\x84#\xdfx\x90\xa6\xff2\xact\x80')
    print(plain)

    ct = "bc9bc77a809b7f618522d36ef7765e1cad359eef39f0eaa5dc5d85f3ab249e788c9bc36e11d72eee281d1a645027bd96a363c0e24efc6b5caa552b2df4979a5ad41e405576d415a5272ba730e27c593eb2c725031a52b7aa92df4c4e26f116c631630b5d23f11775804a688e5e4d5624"
    ct = aes.blockify(ct, 32)
    print(ct[5])

if __name__ == "__main__":
    main()
