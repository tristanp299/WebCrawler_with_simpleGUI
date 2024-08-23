# Name: Tristan Pereira
# Github UN: tristanp299
# Date: 10/20/2022

import PySimpleGUI as sg
from PIL import Image, ImageTk
from requests_html import HTMLSession
import requests
import urllib
from requests_html import HTML

session = HTMLSession()
r = session.get('https://google.com/')


global keywords
def get_source(url):

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
def make_window1():
    menu_def = [['&Settings', ['&File', '&Save As','&New File path', 'About']], ]
    layout = [
        [sg.Menu(menu_def)],
        [sg.Text('HomePage')],
              [sg.Text("Keywords "), sg.InputText(key = '-keywords-')],
              [sg.Button('Submit'), sg.Button('Exit'), sg.Button('About')]]
    window = sg.Window('HomePage', layout, finalize=True)
    window.maximize()
    return window

def make_window2():
    im = Image.open('./earth-space-best-internet-concept-global-business-concepts-series-elements-image-furnished-earth-118874930.jpeg')
    im = im.resize((300,300), resample=Image.BICUBIC)

    layout = [[sg.Text('Thank you for submitting your search!')],
              [sg.Image(size=(300,300), key='-image-')],
               [sg.Button('Go Back'), sg.Button('Visited Sites'), sg.Button('Current Site'), sg.Button('Exit')]]
    window = sg.Window('Submit', layout, finalize=True)
    image = ImageTk.PhotoImage(image=im)
    window['-image-'].update(data=image)
    window.maximize()

    return window

def make_window3():
    layout = [[sg.Text("This program uses your inputted keywords and searches the internet for information you need.\n"
                       " All the information is stored on C://user/app/a_searches/ default folder. \n If you would like to change the desination,"
                       " please go to settings.")],
              [sg.Button('Go Back')]]
    window = sg.Window('About', layout, finalize = True)
    window.maximize()
    return window

def make_window4():
    layout = [[sg.Text("Welcome to your visited sites!")],
              [sg.Button('Go Back')]]
    window = sg.Window('Visited Sites', layout, finalize = True)
    window.maximize()
    return window

window, now = make_window1(), 1

def web_crawl(keywords):
    pass

while True:

    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break

    elif event == 'About':
        win, now = (make_window3(), 3)
        window.close()
        window = win

    elif event == 'Submit':
        win, now = (make_window2(), 2)
        window.close()
        window = win
        keywords = values['-keywords-']
        web_crawl(values['-keywords-'])
        print(values['-keywords-'])
        query = urllib.parse.quote_plus(values['-keywords-'])
        response = get_source("https://www.google.co.uk/search?q=" + values['-keywords-'])

        links = list(response.html.absolute_links)
        google_domains = ('https://www.google.',
                          'https://google.',
                          'https://webcache.googleusercontent.',
                          'http://webcache.googleusercontent.',
                          'https://policies.google.',
                          'https://support.google.',
                          'https://maps.google.')

        for url in links[:]:
            if url.startswith(google_domains):
                links.remove(url)

        print(links)



    elif event == 'Go Back':
        win, now = (make_window1(), 1)
        window.close()
        window = win

    elif event == 'Visited Sites':
        win, now = (make_window4(), 4)
        window.close()
        window = win

window.close()
