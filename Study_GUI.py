import PySimpleGUIQt as sg
import random
import os
import PIL
from PIL import Image, ImageOps
import math
import csv
from pathlib import Path

def wrap_text(text, wrap_length=80):
    wrapped_text = ''
    if len(text)>wrap_length:
        while text != '':
            if len(text) > wrap_length:
                if text[wrap_length-1].isalnum() and text[wrap_length].isalnum():
                    word_index = text[0:wrap_length-1].rfind(' ')
                else:
                    word_index = wrap_length
                wrapped_text += text[0:word_index] + "\n"
                text = text[word_index:]
            else: 
                wrapped_text += text
                text = ''
    return wrapped_text

def select_random_Ns(lst, n):
    random.shuffle(lst)
    return lst[0:n]

def reshape_image(path, x_size, y_size, fill_color):
        im = Image.open(path)
        im = ImageOps.pad(im, (x_size, y_size), color=fill_color)
        im.save(path)

class Species:
    '''
    Class to describe a species

    :param name (str): The name of the species
    :param group (str): The group of the species
    :param size (str): The size of the species
    :param position (str): Where the species can be commonly found
    :param group_size (str): How many of the species tend to stay together
    :param appearance (str): The appearance of the species
    :param dist_feats (str): The main features that make this species stand out
    :param occurence (str): How often the species occurs in any given region
    '''

    def __init__(self, name, scientific_name, group, size, position, group_size, appearance, dist_feats, occurence, interest):
        self.name = name
        self.scientific_name = scientific_name
        self.group = group
        self.size = size
        self.position = position
        self.group_size = group_size
        self.appearance = appearance
        self.dist_feats =dist_feats
        self.occurence = occurence
        self.interest = interest

    def get_path(self):
        '''
        Grabs the path of the species' directory in the image/[group] directory

        returns a string with the path
        '''
        CURRENT_PATH = os.getcwd()
        SPECIES_PATH = os.path.join(CURRENT_PATH,"images", self.group, self.name)
        return SPECIES_PATH
    
    def get_rand_image_path(self):
        '''
        Grabs the path to a random image in the species' image folder

        returns a string with the path
        '''
        SPECIES_PATH = self.get_path()
        species_list = [os.path.join(SPECIES_PATH,f) for f in os.listdir(SPECIES_PATH) if os.path.isfile(os.path.join(SPECIES_PATH, f)) and os.path.join(SPECIES_PATH, f)[-4:] != "xlsx" and os.path.join(SPECIES_PATH, f)[-3:] != "csv"]
        IMAGE_PATH = random.choice(species_list)
        reshape_image(IMAGE_PATH, 1000, 1000, "black")
        return IMAGE_PATH


class Group:
    '''
    The species are assigned to groups. This class contains infomation about the group of
    and all the species within that group

    :param name (str): The name of the group
    :param species (list): List of Species class objects
    '''

    def __init__(self, name, species=[]):
        self.name = name
        self.species = species

    def add_species(self, a_species):
        self.species.append(a_species)

class Study_Session:
    '''
    The environment everything plays in. Contains routines that create the study tool
    '''

    def read_species_csv(self, path):
        '''
        Creates dictionary with info on species from csv file at the given path

        :parma path (str): A string to a csv file with species info in it
        returns dictionary with info on species
        '''
        inpath = Path(path)
        with inpath.open("r", newline="", encoding="utf-8-sig") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                output = row
            return output

    def grab_groups_species(self):
        '''
        From the current directory, this function uses the names of the directories in images
        to obtain a dictionary of the of species for each group along with information associated with
        each species

        returns a dictionary of information on each species within all groups dictionary[group][species][info]
        '''
        species_dict = {}
        CURRENT_PATH = os.getcwd()
        IMAGES_PATH = os.path.join(CURRENT_PATH,"images")
        group_list = [f for f in os.listdir(IMAGES_PATH) if not os.path.isfile(os.path.join(IMAGES_PATH, f))]
        for group in group_list:
            species_dict[group] = {}
            GROUP_PATH = os.path.join(IMAGES_PATH, group)
            species_list = [f for f in os.listdir(GROUP_PATH) if not os.path.isfile(os.path.join(GROUP_PATH, f))]
            for species_element in species_list:
                FILE_PATH = os.path.join(IMAGES_PATH, group, species_element, "Species_Properties.csv")
                species_dict[group][species_element] = {}
                species_dict[group][species_element] = self.read_species_csv(FILE_PATH)
        return species_dict
        
    def mk_group_species_classes(self, group_name, species_dict):
        '''
        Creates a Group class object for the given group name and creates a list of Species class objects
        for each species of that group

        returns Group class object and list of Species class objects
        '''
        species_class_list = []
        group_var = vars() 
        species_list = species_dict[group_name].keys()
        group_var[group_name.replace(" ","_")] = Group(group_name, species_list)
        for species in species_dict[group_name]:
            species_var = vars()
            try:
                interest = species_dict[group_name][species]['Interest']
            except:
                interest = None
            species_var[species.replace(" ","_")] = Species(name=species,
                                                            scientific_name=species_dict[group_name][species]['Scientific Name'], 
                                                            group=group_name, 
                                                            size=species_dict[group_name][species]['Size'], 
                                                            position=species_dict[group_name][species]['Position'], 
                                                            group_size=species_dict[group_name][species]['Group Size'], 
                                                            appearance=species_dict[group_name][species]['Appearance'], 
                                                            dist_feats=species_dict[group_name][species]['Distinguishing Features'], 
                                                            occurence=species_dict[group_name][species]['Occurence'], 
                                                            interest=interest
                                                            )
            species_class_list.append(species_var[species.replace(" ","_")])
        return group_var[group_name.replace(" ","_")], species_class_list

    def begin_study_sess(self):
        '''
        Begins a study session where one practices identifying species
        '''
        CURRENT_DIRECT = os.getcwd()
        IMAGE_PATH = os.path.join(CURRENT_DIRECT,"images","Quail.png")
        appearance = ""
        dist_feat= ""
        species_dict = self.grab_groups_species()
        group_list = species_dict.keys()

        # Creating intro window
        layout_intro = [
                        [sg.Text('Welcome to The Species Study Tool! This tool is here to help you study various aquatic species.')],
                        [sg.Text('\nThe way this will work is by showing you images of different species and you identifying them.\nThere are two modes: \n\n1.) Easy: Multiple choice \n2.) Hard: Type in the species name\n')],
                        [sg.Text('When you are ready to begin setting up, press Next')],
                        [sg.Button('Next', key='Next')]
                        ]

        # Creating study window with two sections: a options/input side and an image side
        layout_left = [ 
                        [sg.Text('First, choose your difficulty.'), sg.Checkbox('Easy', default=False, key='-Easy-'), sg.Checkbox('Hard', default=False, key='-Hard-')],
                        [sg.Text('\nNext, choose the groups of species you would like to study.')]]

        checkbox_list = []
        for i, group in enumerate(group_list):
            checkbox_list.append(sg.Checkbox(group.replace("&","&&"), default=False, key='-{}-'.replace("&","&&").format(group)))
            if (i+1) % 5 == 0:
                layout_left.append(checkbox_list)
                checkbox_list = []
        layout_left.append(checkbox_list)
        layout_left.append([sg.Text('\nWhen you are ready to begin, press the "Start" button below.')])
        layout_left.append([sg.Button('Start', key='-Start-')])
        layout_left.append([sg.Output(visible=True, key='-Species Output-')])
        layout_left.append([sg.Text('\nBelow, type the species in the image to the right.', visible=False, key='-Species Input Text-')])
        layout_left.append([sg.Input(visible=False, key='-Species Input-')])
        layout_left.append([sg.Button('Submit', key='-Submit-'), sg.Button('Next', key='-Next Species-')])

        layout_right = [
                    [sg.Image(IMAGE_PATH, key='-Species Image-')],
                    [sg.Text(text = appearance, visible=False, key='-Appearance-')],
                    [sg.Text(text = dist_feat, visible=False, key='-Distinguishing Feature-')]
                    ]

        layout_study = [
                    [sg.Column(layout_left),
                     sg.VerticalSeparator(),
                    sg.Column(layout_right)]
                    ]
        # Initalizing intro window
        window_intro = sg.Window('Species Study Tool: Intro', layout_intro)

        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event_intro, values_intro = window_intro.read()
            if event_intro == sg.WIN_CLOSED or event_intro == 'Next': # closes window if user closes window of clicks "Next"
                break
        window_intro.close()

        #Initalizing study window
        window_study = sg.Window('Species Study Tool', layout_study, size=(500,500))

        correct_count = 0
        count = 0
        end_game = False
        # Study window while loop
        while end_game != True:
            event, values = window_study.read()
            if event == sg.WIN_CLOSED: # closes window if user closes window
                break
            
            # Checking whether student chooses easy, hard, both, or neither
            if values['-Hard-'] != True and values['-Easy-'] != True:
                print("Make sure to check a difficulty!")
                easy = False
                hard =False
            if values['-Hard-'] == True and values['-Easy-'] == True:
                print("Make sure to check only one difficulty!")
                easy = False
                hard =False
            if values['-Easy-'] == True and values['-Hard-'] != True:
                easy = True
                hard =False
            if values['-Easy-'] != True and values['-Hard-'] == True:
                easy = False
                hard = True

            # Creating list of all checkboxes names 
            group_checkboxes = []
            for group in group_list:
                group_checkboxes.append(values['-{}-'.format(group)])

            # From all the checked checkboxes, generates a list Species class objects for all species
            group_class_var = vars()
            species_class_list_var = vars()
            full_species_list = []
            for (group_button, group) in zip(group_checkboxes, group_list):
                if group_button==True:
                    group_class_var[group] , species_class_list_var[group] = self.mk_group_species_classes(group, species_dict)
                    full_species_list.extend(species_class_list_var[group])

            # If you didn't check anything
            if not full_species_list:
                print('Make sure to choose a group of species!')
                continue

            # If you checked the easy option, this starts a multiple choice version of the study sessionn
            if easy == True:
                # If you press "Start" or "Next Species", this does another run
                if event == '-Start-' or event == '-Next Species-':
                    window_study["-Species Output-"].update(visible=True)
                    window_study["-Species Input Text-"].update(visible=True)
                    window_study["-Species Input-"].update(visible=True)
                    window_study['-Appearance-'].update(visible=False)
                    window_study['-Distinguishing Feature-'].update(visible=False)

                    # Get 4 random species from our list
                    mult_choice = select_random_Ns(full_species_list,4)
                    multi_group = []
                    multi_name = []
                    for choice in mult_choice:
                        multi_group.append(choice.group)
                        multi_name.append(choice.name)
                    
                    # Gets random image for the chosen species
                    correct_answer = mult_choice[0]
                    IMAGE_PATH = correct_answer.get_rand_image_path()

                    # Shuffles list of species
                    random.shuffle(multi_name)

                    print("One of the species listed below is that shown in the image. Which one is it?\n")
                    for name in multi_name:
                        print(name)
                    print("\n")

                    # The images are all different sizes, some of them are too big, so this dimisses
                    # images that are too large
                    img = PIL.Image.open(IMAGE_PATH)
                    wid, hgt = img.size
                    if wid>=2000 or hgt>=1200:
                        continue

                    # Updates the image
                    window_study['-Species Image-'].update(filename=IMAGE_PATH)

                # When you click "Submit" you are checked if you are correct or not
                if event == '-Submit-':
                    count += 1
                    answer = values['-Species Input-'].lower()
                    # Checks if your answer is correct
                    if answer == correct_answer.name.lower():
                        correct_count += 1
                        print("That's correct! {}/{}\n".format(correct_count, count))
                    if answer == "quit":
                        end_game = True
                    if answer != correct_answer.name.lower():
                        print("Nope! The correct answer is {}. {}/{}\n".format(correct_answer.name, correct_count, count))
                        # If you are wrong, we get a prompt that tells us info about the species to help us learn
                        appearance_text = correct_answer.appearance
                        appearance = ''
                        wrap_length = 80
                        if len(appearance_text)>wrap_length:
                            appearance = "Appearance: \n"
                            appearance += wrap_text(appearance_text, wrap_length=wrap_length)
                            window_study['-Appearance-'].update(value=appearance)
                            window_study['-Appearance-'].update(value=appearance)
                        else:
                            window_study['-Appearance-'].update(value="Appearance: \n" + appearance_text + "\n")
                        window_study['-Distinguishing Feature-'].update(value="\nDistinguishing Features: " + "\n" + correct_answer.dist_feats)
                        window_study['-Appearance-'].update(visible = True)
                        window_study['-Distinguishing Feature-'].update(visible = True)
            if hard == True:
                # If you press "Start" or "Next Species", this does another run
                if event == '-Start-' or event == '-Next Species-':
                    window_study["-Species Output-"].update(visible=True)
                    window_study["-Species Input Text-"].update(visible=True)
                    window_study["-Species Input-"].update(visible=True)
                    window_study['-Appearance-'].update(visible=False)
                    window_study['-Distinguishing Feature-'].update(visible=False)

                    # Gets a random species class object from our list of species
                    mult_choice = select_random_Ns(full_species_list,1)
                    multi_group = []
                    multi_name = []
                    for choice in mult_choice:
                        multi_group.append(choice.group)
                        multi_name.append(choice.name)
                    

                    print("What species is it?\n")
                    print("\n")
                    IMAGE_PATH = mult_choice[0].get_rand_image_path()
                    img = PIL.Image.open(IMAGE_PATH)
                    wid, hgt = img.size
                    if wid>=2000 or hgt>=1200:
                        continue
                    window_study['-Species Image-'].update(filename=IMAGE_PATH)
                if event == '-Submit-':
                    count += 1
                    answer = values['-Species Input-'].lower()
                    if answer == multi_name[0].lower():
                        correct_count += 1
                        print("That's correct! {}/{}\n".format(correct_count, count))
                    if answer == "quit":
                        end_game = True
                    if answer != multi_name[0].lower():
                        print("Nope! The correct answer is {}. {}/{}\n".format(multi_name[0], correct_count, count))
                        appearance_text = mult_choice[0].appearance
                        appearance = ''
                        wrap_length = 80
                        if len(appearance_text)>wrap_length:
                            appearance = "Appearance: \n"
                            appearance += wrap_text(appearance_text, wrap_length=wrap_length)
                            window_study['-Appearance-'].update(value=appearance)
                            window_study['-Appearance-'].update(value=appearance)
                        else:
                            window_study['-Appearance-'].update(value="Appearance: \n" + appearance_text + "\n")
                        window_study['-Distinguishing Feature-'].update(value="\nDistinguishing Features: " + "\n" + correct_answer.dist_feats)
                        window_study['-Appearance-'].update(visible = True)
                        window_study['-Distinguishing Feature-'].update(visible = True)
        window_study.close()

study_sess = Study_Session()
study_sess.begin_study_sess()