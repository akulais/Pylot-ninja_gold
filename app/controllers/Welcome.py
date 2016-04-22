"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from flask import Flask, session, Markup
import random
import requests
from system.core.controller import *
from time import strftime
import string
string.letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
random.choice(string.letters)

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """

    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        try:
            session['gold']
        except:
            session['gold'] = 0
        try:
            session['log']
        except:
            session['log'] = []
        return self.load_view('index.html')

    def process_money(self):
        if (request.form['action'] == 'farm'):
            gold = random.randint(10,21)
            session['gold'] += gold
            log = "You have earned " + str(gold) + " from the farm"
            session['log'].append(log)

        if (request.form['action'] == 'cave'):
            gold = random.randint(5,11)
            session['gold'] += gold
            log = "You have earned " + str(gold) + " from the cave"
            session['log'].append(log)

        if (request.form['action'] == 'house'):
            gold = random.randint(2,5)
            session['gold'] += gold
            log = "You have earned " + str(gold) + " from the house"
            session['log'].append(log)

        if (request.form['action'] == 'casino'):
            gold = random.randint(-50,51)
            session['gold'] += gold
            if (gold < 0):
                log = "<font color='red'>You have lost " + str(gold) + " from the Casino</font>"
            else:
                log = "<font color='yellow'>You have earned " + str(gold) + " from the Casino</font>"
            session['log'].append(log)
         
        return redirect('/')


    def reset(self):
        session.clear()
        return redirect('/')
