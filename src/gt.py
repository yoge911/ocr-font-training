import random
import string
import time
import pathlib


def generate_word():
    prefix = random.choice(['A', 'V', 'N'])
    length = random.randint(11, 14)
    numbers_count = random.randint(5, 7)

    # Generating mixed letters and numbers
    mixed_characters = random.sample(string.ascii_uppercase + string.digits, length)
    word = prefix + ''.join(mixed_characters[:numbers_count]) + ''.join(mixed_characters[numbers_count:])

    return word


def add_hyphen(word):
    if random.choice([True, False]):  # 50% chance of adding a hyphen
        index = random.randint(1, len(word) - 1)
        word = word[:index] + '-' + word[index:]
    return word


def generate_words(n):
    words = []
    for i in range(1, n + 1):
        word = generate_word()
        word = add_hyphen(word) if i % 6 == 0 or i % 7 == 0 else word
        words.append(word)
    return words


def write_to_file(words, filename='generated_words.txt'):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')


# Measure script execution time
start_time = time.time()

# Example: Generate 20 words and write them to a file
generated_words = generate_words(20000)
write_to_file(generated_words, "words.txt")

end_time = time.time()
execution_time = end_time - start_time

print(f"Words have been written to 'generated_words.txt'")
print(f"Script execution time: {execution_time:.4f} seconds")
