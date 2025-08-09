import csv

#def to change 1 and 0 to boolean values
def str_to_bool(s):
    s = s.strip().lower()
    if s in ("yes", "true", "t", "y", "1"):
        return True
    elif s in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise ValueError("invalid boolean value")

#def to change class type from numbers to names
def class_type_to_name(class_type):
    no = float(class_type)
    if no == 1:
        return "Mammal"
    elif no == 2:
        return "Bird"
    elif no == 3:
        return "Reptile"
    elif no == 4:
        return "Fish"
    elif no == 5:
        return "Amphibian"
    elif no == 6:
        return "Bug/Invertebrate"

#def for loading csv to dictionary
def load_animals(filename):
    animals = {}
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            for key in line:
                #other than few values the rest is boolean
                if key != 'animal_name' and key != 'fins' and key != 'legs' and key != 'class_type':
                    line[key] = str_to_bool(line[key])
                if key == 'class_type':
                    line[key] = class_type_to_name(line[key])
            animals[line['animal_name']]=line
    return animals

#load csv
zoo_dict = load_animals("zoo.csv")

#try/except to make sure user inputs a yes or no
def get_bool(prompt):
    while True:
        try:
            return str_to_bool(input(prompt))
        except ValueError:
            print("Please enter yes or no")

#try/except to make sure user inputs a number
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number")

#game to find the animal one is thinking about
def quiz_game():
    print("---ANSWER YES, NO OR WITH SPECIFIC NUMBER---")
    print("Think of an animal and answer the questions")

    answers = {
        'hair': get_bool("Does the animal have hair? "),
        'feathers': get_bool("Does the animal have feathers? "),
        'eggs': get_bool("Does the animal lay eggs? "),
        'milk': get_bool("Does the animal give milk? "),
        'airborne': get_bool("Is the animal airborne? "),
        'aquatic': get_bool("Is the animal aquatic? "),
        'predator': get_bool("Is the animal a predator? "),
        'toothed': get_bool("Is the animal toothed? "),
        'backbone': get_bool("Does the animal have a backbone? "),
        'breathes': get_bool("Does the animal breathe? "),
        'venomous': get_bool("Is the animal venomous? "),
        'fins': get_number("How many fins does the animal have? "),
        'legs': get_number("How many legs does the animal have? "),
        'tail': get_bool("Does the animal have a tail? "),
        'domestic': get_bool("Is the animal domestic? "),
        'catsize': get_bool("Is the animal cat-sized? ")
    }

    #filter the animals
    possible_animals = [
        animal for animal in zoo_dict
        if all(animal[key] == value for key, value in answers.items())
    ]

    if possible_animals:
        print("Possible match:")
        for animal in possible_animals:
            print(f"- {animal['animal_name']} ({animal['class_type']})")
    else:
        print("No match found")
