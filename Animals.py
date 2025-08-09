import csv

#def to change 1 and 0 to boolean values
def str_to_bool(s):
    return s.strip().lower() in ("yes", "true", "t", "1")

def load_animals(filename):
    animals = {}
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            for key in line:
                if key != 'animal_name' and key != 'fins' and key != 'legs' and key != 'class_type':
                    line[key] = str_to_bool(line[key])
            animals[line['animal_name']]=line
    return animals

zoo_dict = load_animals("zoo.csv")

