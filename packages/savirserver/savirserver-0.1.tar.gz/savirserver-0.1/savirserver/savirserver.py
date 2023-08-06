from flask import *
import logging
import click
logger = logging.getLogger("savirsocial")
logger.propagate = False

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def secho(text, file=None, nl=None, err=None, color=None, **styles):
    pass

def echo(text, file=None, nl=None, err=None, color=None, **styles):
    pass

click.echo = echo
click.secho = secho

class Savir:
    Savir = Flask(__name__)
    def __init__(self, name, template):
        self.template = template
        self.name = name
        @self.Savir.route("/")
        def home():
            try:
                return render_template(template)
            except:
                print(template, "couldn't be found by SavirServer.")
                return 'The required template could not be found by SavirServer.'

    def place(self, slash, template2):
        self.slash = slash
        self.template2 = template2

    def stats(self):
        print("Website Name: ", self.name, "Homepage: ", self.template, ", Subpages: ", self.template2) 

    def Savirplay(self):
        print("The SavirServer app is running on localhost:80. I recommend using a service such as PageKite or Ngrok for localhost tunneling, and exposing your website to the internet. Thanks, Savir Singh.")
        self.Savir.run(port=80)
