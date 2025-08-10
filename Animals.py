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
        data for name, data in zoo_dict.items()
        if all(data[key] == value for key, value in answers.items())
    ]

    if possible_animals:
        print("Possible match:")
        for animal in possible_animals:
            print(f"- {animal['animal_name']} ({animal['class_type']})")
    else:
        print("No match found")

#def for calculating statistics based on traits
def trait_stat():
    print("---CHOOSE IMPORTANT TRAITS FOR STATISTICS---")
    print("Write down what features/properties do the animals have")
    print("Choose from: hair,feathers,eggs,milk,airborne,aquatic,predator,toothed,backbone,breathes,venomous,tail,domestic,catsize")
    traits_input = input("Enter traits separated by commas (or 'no' if none): ").strip().lower()
    traits = None if traits_input == "no" else [t.strip() for t in traits_input.split(",")]

    fin_leg_input = input("Enter number of fins or legs (or 'no' if irrelevant): ").strip().lower()
    fin_leg = None if fin_leg_input == "no" else int(fin_leg_input)

    class_input = input("Enter class type (or 'no' if irrelevant): ").strip().lower()
    class_type = None if class_input == "no" else class_input

    #filter the animals, the validation of the inputs other than expected was set aside for the future
    possible_animals = []
    for data in zoo_dict.values():
        if traits and not all(data.get(trait) is True for trait in traits):
            continue
        if fin_leg is not None and not (data['fins'] == fin_leg or data['legs'] == fin_leg):
            continue
        if class_type and data['class_type'].lower() != class_type:
            continue
        possible_animals.append(data)

    if possible_animals:
        print(f"Possible matches: {len(possible_animals)}")

if __name__ == "__main__":
    while True:
        print("---ANOTHER MENU---")
        print("1. Guessing game")
        print("2. Statistics")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "3":
            print("BYE!")
            break
        elif choice == "1":
            quiz_game()
        elif choice == "2":
            trait_stat()
        else:
            print('Invalid choice')
            continue