import random

def generate_first_name():
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    length = random.randint(2, 4)
    name = ''
    
    for i in range(length):
        name += random.choice(consonants)
        name += random.choice(vowels)
    
    return name.capitalize()

def generate_last_name():
    suffixes = ['son', 'ton', 'ford', 'wood', 'ley', 'man', 'field']
    base = generate_first_name().lower()
    if random.random() < 0.5:
        base += random.choice(suffixes)
    return base.capitalize()

def generate_full_name(count=1):
    names = []
    for _ in range(count):
        full_name = f"{generate_first_name()} {generate_last_name()}"
        names.append(full_name)
    return names

# Example usage
if __name__ == "__main__":
    names = generate_full_name(5)
    for name in names:
        print(name)