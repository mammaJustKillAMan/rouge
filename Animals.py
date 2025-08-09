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

