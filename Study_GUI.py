import PySimpleGUIQt as sg
import random
import os
import PIL
from PIL import Image
import math
import csv
from pathlib import Path

def select_random_Ns(lst, n):
    random.shuffle(lst)
    return lst[0:n]

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
        return IMAGE_PATH


class Group:
    '''
    The species are assigned to groups. This class contains infomation about the group of
    and all the species within that group

    :param name (str): The name of the group
    '''
    species = []

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def add_species(self, a_species, species):
        species.append(a_species)

class Study_Session:
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
        From the current directory, this function uses the folder names of the directories in images
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
        CURRENT_DIRECT = os.getcwd()
        IMAGE_PATH = os.path.join(CURRENT_DIRECT,"images","Quail.png")
        appearance = "Hi"
        dist_feat= "Hello"
        species_dict = self.grab_groups_species()
        group_list = species_dict.keys()

        # All the stuff inside your window.
        layout_intro = [
                        [sg.Text('Welcome to The Indo Ocean Study Tool! This tool is here to help you study various aquatic species for your internship with Indo Ocean.')],
                        [sg.Text('\nThe way this will work is by showing you images of different species and you identifying them.\nThere are two modes: \n\n1.) Easy: Multiple choice \n2.) Hard: Type in the species name\n')],
                        [sg.Text('When you are ready to begin setting up, press Next')],
                        [sg.Button('Next', key='Next')]
                        ]

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
        # Create the Window
        window_intro = sg.Window('Indo Ocean Study Tool: Intro', layout_intro)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event_intro, values_intro = window_intro.read()
            if event_intro == sg.WIN_CLOSED or event_intro == 'Next': # if user closes window or clicks cancel
                break

        window_intro.close()

        # Create the Window
        window_study = sg.Window('Indo Ocean Study Tool', layout_study, size=(500,500))
        # Event Loop to process "events" and get the "values" of the inputs
        correct_count = 0
        count = 0
        while True:
            event, values = window_study.read()
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
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

            group_buttons = []
            for group in group_list:
                group_buttons.append(values['-{}-'.format(group)])

            group_class_var = vars()
            species_class_list_var = vars()
            full_species_list = []
            for (group_button, group) in zip(group_buttons, group_list):
                if group_button==True:
                    group_class_var[group] , species_class_list_var[group] = self.mk_group_species_classes(group, species_dict)
                    full_species_list.extend(species_class_list_var[group])

            if not full_species_list:
                print('Make sure to choose a group of species!')
                continue

            if easy == True:
                if event == '-Start-' or event == '-Next Species-':
                    window_study["-Species Output-"].update(visible=True)
                    window_study["-Species Input Text-"].update(visible=True)
                    window_study["-Species Input-"].update(visible=True)
                    window_study['-Appearance-'].update(visible=False)
                    window_study['-Distinguishing Feature-'].update(visible=False)

                    mult_choice = select_random_Ns(full_species_list,4)
                    multi_group = []
                    multi_name = []
                    for choice in mult_choice:
                        multi_group.append(choice.group)
                        multi_name.append(choice.name)
                    

                    print("One of the species listed below is that shown in the image. Which one is it?\n")
                    for name in multi_name:
                        print(name)
                    print("\n")
                    IMAGE_PATH = mult_choice[0].get_rand_image_path()
                    img = PIL.Image.open(IMAGE_PATH)
                    wid, hgt = img.size
                    if wid>=2000 or hgt>=1200:
                        continue
                    window_study['-Species Image-'].update(filename=IMAGE_PATH)
                if event == '-Submit-':
                    count += 1
                    answer = values['-Species Input-']
                    if answer == multi_name[0]:
                        correct_count += 1
                        print("That's correct! {}/{}\n".format(correct_count, count))
                    if answer == "quit":
                        end_game = True
                    if answer != multi_name[0]:
                        print("Nope! The correct answer is {}. {}/{}\n".format(multi_name[0], correct_count, count))
                        appearance_text = mult_choice[0].appearance
                        text_loops = math.floor(len(appearance_text)/80)

                        if len(appearance_text)>80:
                            appearance = "Appearance: \n"
                            appearance = appearance + appearance_text[0:80] + "\n"
                            for i in range(1,text_loops):
                                appearance = appearance + appearance_text[i*80:(i+1)*80] + "\n"
                            appearance = appearance + appearance_text[text_loops*80:] + "\n"
                            window_study['-Appearance-'].update(value=appearance)
                        else:
                            window_study['-Appearance-'].update(value="Appearance: \n" + appearance_text + "\n")
                        window_study['-Distinguishing Feature-'].update(value="Distinguishing Features: " + "\n" + mult_choice[0].dist_feats)
                        window_study['-Appearance-'].update(visible = True)
                        window_study['-Distinguishing Feature-'].update(visible = True)
            if hard == True:
                if event == '-Start-' or event == '-Next Species-':
                    window_study["-Species Output-"].update(visible=True)
                    window_study["-Species Input Text-"].update(visible=True)
                    window_study["-Species Input-"].update(visible=True)
                    window_study['-Appearance-'].update(visible=False)
                    window_study['-Distinguishing Feature-'].update(visible=False)

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
                    answer = values['-Species Input-']
                    if answer == multi_name[0]:
                        correct_count += 1
                        print("That's correct! {}/{}\n".format(correct_count, count))
                    if answer == "quit":
                        end_game = True
                    if answer != multi_name[0]:
                        print("Nope! The correct answer is {}. {}/{}\n".format(multi_name[0], correct_count, count))
                        appearance_text = mult_choice[0].appearance
                        text_loops = math.floor(len(appearance_text)/80)

                        if len(appearance_text)>80:
                            appearance = "Appearance: \n"
                            appearance = appearance + appearance_text[0:80] + "\n"
                            for i in range(1,text_loops):
                                appearance = appearance + appearance_text[i*80:(i+1)*80] + "\n"
                            appearance = appearance + appearance_text[text_loops*80:] + "\n"
                            window_study['-Appearance-'].update(value=appearance)
                        else:
                            window_study['-Appearance-'].update(value="Appearance: \n" + appearance_text + "\n")
                        window_study['-Distinguishing Feature-'].update(value="Distinguishing Features: " + "\n" + mult_choice[0].dist_feats)
                        window_study['-Appearance-'].update(visible = True)
                        window_study['-Distinguishing Feature-'].update(visible = True)
        window_study.close()

study_sess = Study_Session()
study_sess.begin_study_sess()