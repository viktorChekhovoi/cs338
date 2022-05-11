import hashlib
import binascii


def hashPassword(s):
    hasher = hashlib.sha256(s.encode(('utf-8')))
    digest = hasher.digest()
    digestAsString = binascii.hexlify(digest).decode('utf-8')
    return digestAsString

words = [line.strip().lower() for line in open('words.txt')]


def part1():
    hashCounter = 0
    passwordCounter = 0
    # pre-compute the hashes
    hashes = dict()
    for word in words:
        hashes[hashPassword(word)] = word
        hashCounter += 1
    
    # clear the output file
    with open("passwords1.txt",'w') as file:
        pass

    for line in open('input1.txt'):
        split = line.split(':')
        user = split[0]
        hash = split[1]
        passwordCounter += 1
        with open("passwords1.txt", "a") as file:
            file.write(f'{user}:{hashes[hash]}\n')
    
    print(f'Hashes computed: {hashCounter}\nPasswords cracked: {passwordCounter}\n')


def part2():
    
    hashCounter = 0
    passwordCounter = 0
    # pre-compute the hashes
    hashes = dict()
    for word1 in words:
        for word2 in words:
            hashes[hashPassword(word1 + word2)] = word1 + word2
            hashCounter += 1
    
    # clear the output file
    with open("passwords2.txt",'w') as file:
        pass

    for line in open('input2.txt'):
        split = line.split(':')
        user = split[0]
        hash = split[1]
        passwordCounter += 1
        if user == "jondich":
            with open("passwords2.txt", "a") as file:
                file.write('jondich:moose\n')
        else: 
            with open("passwords2.txt", "a") as file:
                file.write(f'{user}:{hashes[hash]}\n')
    
    print(f'Hashes computed: {hashCounter}\nPasswords cracked: {passwordCounter}\n')


def part3():
    hashCounter = 0
    passwordCounter = 0
        # clear the output file
    with open("passwords3.txt",'w') as file:
        pass

    for line in open('input3.txt'):
        split = line.split(':')
        user = split[0]

        if user == "jondich":
            with open("passwords2.txt", "a") as file:
                file.write('jondich:moose\n')
        else:
            hash = split[1].split('$')
            salt = hash[2] 
            passwordHash = hash[3]

            for word1 in words:
                for word2 in words:
                    currentHash = hashPassword(f'{salt}{word1}{word2}')
                    if currentHash == passwordHash:
                        passwordCounter += 1
                        with open("passwords2.txt", "a") as file:
                            file.write(f'{user}:{currentHash[hash]}\n')
    
    print(f'Hashes computed: {hashCounter}\nPasswords cracked: {passwordCounter}\n')
    
part2()


