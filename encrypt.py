def encryptThis(message):
    words = message.split()

    def encryptWord(word):
        if len(word) == 0:
            return ""
        ascii_code = str(ord(word[0]))
        if len(word) == 1:
            return ascii_code
        if len(word) == 2:
            return ascii_code + word[1] + word[0]
        return ascii_code + word[-1] + word[2:-1] + word[1]

    encrypted_words = [encryptWord(word) for word in words]
    encrypted_message = " ".join(encrypted_words)

    return encrypted_message
