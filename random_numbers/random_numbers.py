import random


def main ():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")

    words = []
    append_random_words(words, 6)
    print(f"words {words}")

    return


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        numbers_list.append(round(random.uniform(0, 100), 1))

    return


def append_random_words(words_list, quantity=1):
    word_bank = [
    "apple",
    "river",
    "chair",
    "window",
    "garden",
    "bottle",
    "mountain",
    "paper",
    "clock",
    "friend",
    "street",
    "candle",
    "forest",
    "pillow",
    "school",
    "ocean",
    "basket",
    "camera",
    "bridge",
    "flower"
    ]

    for _ in range(quantity):
        words_list.append(random.choice(word_bank))
        
    return


if __name__ == "__main__":
    main()