import PySimpleGUIQt as sg
import random
import os
import sys
from os import listdir
from os.path import isfile, join
from PIL import Image
import tkinter
from Species_dict import species, sharks, rays, turtles, grouper, snapper
from Species_dict import emperors, parrotfish, jacks_trevally, tuna_mackerel, barracuda, species_of_interest
import PIL
from PIL import Image
import itertools
import math

def select_random_Ns(lst, n):
    random.shuffle(lst)
    return lst[0:n]

groups = [
            "Sharks", 
            "Rays", 
            "Turtles", 
            "Grouper", 
            "Snapper", 
            "Emperors", 
            "Parrotfish", 
            "Jacks & Trevally", 
            "Tuna & Mackerel", 
            "Barracuda", 
            "Species of Interest"
        ]
group_species = [
                    sharks, 
                    rays, 
                    turtles, 
                    grouper, 
                    snapper, 
                    emperors, 
                    parrotfish, 
                    jacks_trevally, 
                    tuna_mackerel, 
                    barracuda, 
                    species_of_interest
                ]

CURRENT_DIRECT = os.getcwd()
IMAGES_DIRECT = join(CURRENT_DIRECT,"images")
IMAGE_PATH = join(CURRENT_DIRECT,"images","Quail.png")

appearance = "Hi"
dist_feat= "Hello"

begin_statement = "\n"

# All the stuff inside your window.
layout_intro = [
                [sg.Text('Welcome to The Indo Ocean Study Tool! This tool is here to help you study various aquatic species for your internship with Indo Ocean.')],
                [sg.Text('\nThe way this will work is by showing you images of different species and you identifying them.\nThere are two modes: \n\n1.) Easy: Multiple choice \n2.) Hard: Type in the species name\n')],
                [sg.Text('When you are ready to begin setting up, press Next')],
                [sg.Button('Next', key='Next')]
]

layout_left = [ 
                [sg.Text('First, choose your difficulty.'), sg.Checkbox('Easy', default=False, key='-Easy-'), sg.Checkbox('Hard', default=False, key='-Hard-')],
                [sg.Text('\nNext, choose the groups of species you would like to study.')],
                [sg.Checkbox('Sharks', default=False, key='-Sharks-'), 
                    sg.Checkbox('Rays', default=False, key='-Rays-'), 
                    sg.Checkbox('Turtles', default=False, key='-Turtles-'), 
                    sg.Checkbox('Grouper', default=False, key='-Grouper-'), 
                    sg.Checkbox('Snapper', default=False, key='-Snapper-'), 
                    sg.Checkbox('Emperor', default=False, key="-Emperors-")], 
                    [sg.Checkbox('Parrotfish', default=False, key='-Parrotfish-'), 
                    sg.Checkbox('Jack and Trevally', default=False, key='-Jacks & Trevally-'), 
                    sg.Checkbox('Tuna and Mackerel', default=False, key='-Tuna & Mackerel-'), 
                    sg.Checkbox('Barracuda', default=False, key='-Barracuda-'), 
                    sg.Checkbox('Species of Interest', default=False, key='-Species of Interest-') ],
                [sg.Text('\nWhen you are ready to begin, press the "Start" button below.')],
                [sg.Button('Start', key='-Start-')],
                [sg.Output(visible=True, key='-Species Output-')],
                [sg.Text('\nBelow, type the species in the image to the right.', visible=False, key='-Species Input Text-')],
                [sg.Input(visible=False, key='-Species Input-')],
                [sg.Button('Submit', key='-Submit-'), sg.Button('Next', key='-Next Species-')]
                ]

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
    
    group_list = []
    dict_species = {}
    species_list = []

    group_buttons = [
                        values['-Sharks-'],
                        values['-Rays-'],
                        values['-Turtles-'],
                        values['-Grouper-'],
                        values['-Snapper-'],
                        values['-Emperors-'],
                        values['-Parrotfish-'],
                        values['-Jacks & Trevally-'],
                        values['-Tuna & Mackerel-'],
                        values['-Barracuda-'],
                        values['-Species of Interest-']
                    ]

    if values['-Hard-'] != True and values['-Easy-'] != True:
        print("Make sure to check a difficulty!")
        difficulty = False
    if values['-Hard-'] == True and values['-Easy-'] == True:
        print("Make sure to check only one difficulty!")
        difficulty = False
    if values['-Easy-'] == True and values['-Hard-'] != True:
        difficulty = True
        easy = True
        hard =False
    if values['-Easy-'] != True and values['-Hard-'] == True:
        difficulty = True
        easy = False
        hard = True

    # Checks buttons to see which are marked and adds species to dictionary by group
    # Also adds groups selected to list

    for (group, string, group_specie) in zip(group_buttons, groups, group_species):
        if group==True:
            dict_species[string] = group_specie
            group_list.append(string)
    group_check = 0
    group_check = sum(1 for x in group_buttons if not x)
    if group_check == 11:
        print('Make sure to choose a group of species!')
    if any(group_buttons) == True and difficulty == True:
        # Deletes extranious entries in list and dictionary

        # From the group_list created, we want to fill a list with all the species and all the images of those species
        for group in group_list:
            group_path = join(IMAGES_DIRECT,group)
            for specie in dict_species[group]:
                specie_dir = specie
                specie_path = join(group_path, specie_dir)
                for f in listdir(specie_path): 
                    if isfile(join(specie_path,f)):
                        species_input_paths = [group, specie , join(specie_path,f)]
                        species_list.append(species_input_paths)

        if easy == True:
            if event == '-Start-' or event == '-Next Species-':
                window_study["-Species Output-"].update(visible=True)
                window_study["-Species Input Text-"].update(visible=True)
                window_study["-Species Input-"].update(visible=True)
                window_study['-Appearance-'].update(visible=False)
                window_study['-Distinguishing Feature-'].update(visible=False)

                mult_choice = select_random_Ns(species_list,4)
                length = len(mult_choice)
                rand_int = random.randint(0,length-1)
                mult_choice_group_easy = mult_choice[rand_int][0]
                mult_choice_name = [mult_choice[i][1] for i in range(length)]
                mult_choice_path = mult_choice[rand_int][2]

                print("One of the species listed below is that shown in the image. Which one is it?\n")
                for name in mult_choice_name:
                    print(name)
                print("\n")
                IMAGE_PATH = mult_choice_path
                img = PIL.Image.open(IMAGE_PATH)
                wid, hgt = img.size
                if wid>=2000 or hgt>=1200:
                    continue
                window_study['-Species Image-'].update(filename=IMAGE_PATH)
            if event == '-Submit-':
                count += 1
                answer = values['-Species Input-']
                if answer == mult_choice_name[rand_int]:
                    correct_count += 1
                    print("That's correct! {}/{}\n".format(correct_count, count))
                if answer == "quit":
                    end_game = True
                if answer != mult_choice_name[rand_int]:
                    print("Nope! The correct answer is {}. {}/{}\n".format(mult_choice_name[rand_int], correct_count, count))
                    appearance_dict = species[mult_choice_group_easy][mult_choice_name[rand_int]]["Appearance"]
                    text_loops = math.floor(len(appearance_dict)/80)

                    if len(appearance_dict)>80:
                        appearance = "Appearance: \n"
                        appearance = appearance + appearance_dict[0:80] + "\n"
                        for i in range(1,text_loops):
                            appearance = appearance + appearance_dict[i*80:(i+1)*80] + "\n"
                        appearance = appearance + appearance_dict[text_loops*80:] + "\n"
                        window_study['-Appearance-'].update(value=appearance)
                    else:
                        window_study['-Appearance-'].update(value="Appearance: \n" + appearance_dict + "\n")
                    window_study['-Distinguishing Feature-'].update(value="Distinguishing Features: " + "\n" + species[mult_choice_group_easy][mult_choice_name[rand_int]]["Distinguishing Features"])
                    window_study['-Appearance-'].update(visible = True)
                    window_study['-Distinguishing Feature-'].update(visible = True)
        if hard == True:
            if event == '-Start-' or event == '-Next Species-':
                window_study["-Species Output-"].update(visible=True)
                window_study["-Species Input Text-"].update(visible=True)
                window_study["-Species Input-"].update(visible=True)
                window_study['-Appearance-'].update(visible=False)
                window_study['-Distinguishing Feature-'].update(visible=False)

                mult_choice_hard = select_random_Ns(species_list,1)
                mult_choice_group_hard = mult_choice_hard[0][0]
                mult_choice_name = mult_choice_hard[0][1]
                mult_choice_path = mult_choice_hard[0][2]

                IMAGE_PATH = mult_choice_path
                img = PIL.Image.open(IMAGE_PATH)
                wid, hgt = img.size
                if wid>=1800 or hgt>=1000:
                    continue
                window_study['-Species Image-'].update(filename=IMAGE_PATH)
            if event == '-Submit-':
                count += 1
                answer = values['-Species Input-']
                if answer == mult_choice_name:
                    correct_count += 1
                    print("That's correct! {}/{}\n".format(correct_count, count))
                if answer == "quit":
                    end_game = True
                if answer != mult_choice_name:
                    print("Nope! The correct answer is {}. {}/{}\n".format(mult_choice_name, correct_count, count))
                    appearance_dict = species[mult_choice_group_hard][mult_choice_name]["Appearance"]
                    text_loops = math.floor(len(appearance_dict)/80)

                    if len(appearance_dict)>80:
                        appearance = "Appearance: \n"
                        appearance = appearance + appearance_dict[0:80] + "\n"
                        for i in range(1,text_loops):
                            appearance = appearance + appearance_dict[i*80:(i+1)*80] + "\n"
                        appearance = appearance + appearance_dict[text_loops*80:] + "\n"
                        window_study['-Appearance-'].update(value=appearance)
                    else:
                        window_study['-Appearance-'].update(value="Appearance: \n" + appearance_dict + "\n")
                    window_study['-Distinguishing Feature-'].update(value="Distinguishing Features: " + species[mult_choice_group_hard][mult_choice_name]["Distinguishing Features"])
                    window_study['-Appearance-'].update(visible = True)
                    window_study['-Distinguishing Feature-'].update(visible = True)
        

window_study.close()