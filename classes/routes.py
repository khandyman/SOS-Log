from flask import render_template, redirect, url_for
from classes.database import Database

class Routes:
    def __init__(self, app):
        self._app = app
        self._database = Database()

    def totals(self):
        characters = self._database.find_all_mains()

        return render_template('totals.html', characters=characters)

    def ep_log(self):
        return render_template('ep_log.html')

    def gp_log(self):
        return render_template('gp_log.html')
