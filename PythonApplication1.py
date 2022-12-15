from tkinter import filedialog
from tkinter import *
import pygame as pg
import fnmatch
import os


pg.mixer.init()
def songdir():
    main_directory = filedialog.askdirectory()
    song = filedialog.askopenfilename(initialdir=main_directory, title='Add songs',filetypes=(('flac files', '*flac'),('wav files', '*wav'), ('mp3 files','*mp3')))
    song = song.replace(main_directory, '')
    main_listbox.insert(END, song)
def play():
    song = main_listbox.get(ACTIVE)
    pg.mixer.music.load(song)
    pg.mixer.music.play(loops = 0)
def stop():
    pg.mixer.music.stop()
def pause():
    pg.mixer.music.pause()
def unpause():
    global pause
    pg.mixer.music.unpause()
    pause = False
def insertion():
    main_directory = filedialog.askdirectory()
    path = main_directory
    pattern_for_flac = '*.flac'
    pattern_for_wav = '*.wav'
    pattern_for_mp3 = '*.mp3'
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, pattern_for_flac):
            main_listbox.insert('end', filename)  
        for filename in fnmatch.filter(files, pattern_for_wav):
            main_listbox.insert('end', filename)
        for filename in fnmatch.filter(files, pattern_for_mp3):
            main_listbox.insert('end', filename)
def check_music():
    main_directory = filedialog.askdirectory()
    directory_to_check_music = filedialog.askopenfilename(initialdir=main_directory, title='Add songs',filetypes=(('flac files', '*flac'),('wav files', '*wav'), ('mp3 files','*mp3')))

main_window = Tk()
main_window.geometry('500x600')
first_menu = Menu(main_window)
main_window.config(menu=first_menu, bg='white')
menu_mood = Menu(first_menu)
menu_check_music = Menu(first_menu)
first_menu.add_cascade(label='Выберите ваше настроение', menu=menu_mood)
menu_mood.add_cascade(label='Веселое', command = insertion)
menu_mood.add_cascade(label='Грустное', command = insertion)
menu_mood.add_cascade(label='Влюбленное ', command = insertion)
menu_mood.add_cascade(label='Зажигательное', command = insertion)
menu_mood.add_cascade(label='Расслабленное', command = insertion)
menu_mood.add_cascade(label='Меланхоличное', command = insertion)
menu_mood.add_cascade(label='Сфокусированное', command = insertion)
first_menu.add_cascade(label='Проверить наличие музыки', menu=menu_check_music)
menu_check_music.add_cascade(label='Выбрать директорию', command = check_music)
main_listbox = Listbox(main_window, bg='magenta', width=53, height=30, selectbackground='black', selectforeground='white')
main_listbox.pack(pady=20)
first_frame = Frame(main_window)
first_frame.pack()
Button(first_frame, text='play', borderwidth=2, command=play, width=10).grid(row=1, column=1, padx=0)
Button(first_frame, text='pause', borderwidth=2, command=pause, width=10).grid(row=1, column=2, padx=0)
Button(first_frame, text='continue', borderwidth=2, command=unpause, width=10).grid(row=1, column=3, padx=0)
Button(first_frame, text='stop', borderwidth=2, command=stop, width=10).grid(row=1, column=4, padx=0)
main_window.mainloop()