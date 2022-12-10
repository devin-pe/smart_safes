# Devin W. Pereira 20154292
# Cisc468 Final Project: Smart Safes

# This file contains the implementation of the vault
import os
import time
import heapq
from random import random
import numpy as np
from Crypto.Protocol.KDF import scrypt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pickle

class Vault():
    def __init__(self, mpw, pt_path):
        # Check if path corresponds to the password list
        if not os.path.exists(pt_path):
            raise FileNotFoundError
        # The ciphertext path is hard coded to be vault.bin to avoid misuse
        self.ct_path = 'vault.bin'
        with open(pt_path, 'r') as f:
            pt = f.read()
            self.encrypt(pt, mpw)

    def encrypt(self, pt, password):
        """Encrypts the password list in subsequent trials"""
        # Generate new salt
        self.salt = get_random_bytes(16) # 128-bit salt (> 32 recommended by NIST)
        # Derive the key
        key = scrypt(password, self.salt, key_len=16, N=2**14, r=8, p=1)
        # Encrypt the plaintext
        cipher = AES.new(key, AES.MODE_CTR)
        ct = cipher.encrypt(pt.encode('utf-8'))
        # Store ciphertext
        with open(self.ct_path, 'wb') as f:
            f.write(ct)
        # Assign a new nonce to attribute for decryption
        self.nonce = cipher.nonce

    def decrypt(self, password_guess):
        # Check if the path corresponds to the ciphertext
        if not os.path.exists(self.ct_path):
            raise FileNotFoundError
        # Load ciphertext
        with open(self.ct_path, 'rb') as f:
            ct = f.read()
            # Generate key using the same salt
            key = scrypt(password_guess, self.salt, key_len=16, N=2**14, r=8, p=1)
            # Decrypt the plaintext
            cipher = AES.new(key, AES.MODE_CTR, nonce=self.nonce)
            try:
                pt = cipher.decrypt(ct).decode('utf-8')
                gen_decoys()
                return 0, pt
            except:
                return 1, gen_decoys()
         

def gen_decoys():
    """Generates N decoys sampled from pcfg_guesser in decoys.txt"""
    # 3038501 guesses
    size = int(np.random.normal(25, 15)) # mean = 25, std_dev = 15
    with open('decoys.txt', 'r') as f:
        decoy_list = heapq.nlargest(size, f, key=lambda _: random())
        decoy_vault = ''.join(decoy_list)
        return decoy_vault

def start(mpw, pt_path):
    """Initialize password vault"""
    obj = Vault(mpw, pt_path)
    # Save object attributes for decryption
    with open('object.f', 'wb') as object_file:
        pickle.dump(obj, object_file)

def view(password_guess):
    """View the stored password list"""
    _, pt, _ = decrypt_load(password_guess)
    print(pt)

def add(password_guess, new_pass):
    """Add a password to the password list"""
    flag, pt, obj = decrypt_load(password_guess)
    # Do not encrypt if the decryption failed
    if flag:
        return  
    new_pt = pt + '\n' + new_pass
    # Add new password to plaintext
    encrypt_save(password_guess, new_pt, obj)

def delete(password_guess, line_n):
    """Remove a password from the password list"""
    flag, pt, obj = decrypt_load(password_guess)
    # Do not encrypt if the decryption failed
    if flag:
        return
    # Remove password from plaintext
    passwords = [pw for pw in pt.splitlines()]
    if line_n > len(passwords):
        raise IndexError
    passwords.pop(line_n)
    new_pt = '\n'.join(passwords)
    encrypt_save(password_guess, new_pt, obj)

def decrypt_load(password_guess):
    """Decrypts and loads objects defined after initial save
    Modularity useful for experiments"""
    with open('object.f', 'rb') as object_file:
        obj = pickle.load(object_file)
        flag, pt = obj.decrypt(password_guess)
    return flag, pt, obj

def encrypt_save(password, pt, obj):
    """Encrypts and saves objects defined after initial save
    Modularity useful for experiments"""
    with open('object.f', 'wb') as object_file:
        # Encrypt object
        obj.encrypt(pt, password)
        pickle.dump(obj, object_file)

def demo():
    # Demo:
    start('devin', 'plaintexts/short.txt')
    print("Initial password list:")
    view('devin')

    add('devin', 'secretcode')
    print("\nOne password added:")
    view('devin')

    delete('devin', 2)
    print("\nPassword in position 2 deleted:")
    view('devin')

if __name__ == '__main__':
  demo()




        