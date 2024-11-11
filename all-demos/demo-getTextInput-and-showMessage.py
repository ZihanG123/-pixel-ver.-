# This demos app.getTextInput(prompt) and app.showMessage(message)

# To run this, you will need a version of CMU Graphics since 23-Oct-2024.

# If you installed with pip, you can update with:
# python -m pip install --upgrade cmu-graphics

from cmu_graphics import *

def onAppStart(app):
    app.name = None

def onMousePress(app, mouseX, mouseY):
    response = app.getTextInput('What is your name?')
    app.name = 'Unknown' if response == '' else response
    message = f'This is a modal poup!  Your name is: {app.name}'
    app.showMessage(message)

def redrawAll(app):
    drawLabel('Click the mouse to enter your name',
              app.width/2, app.height/2 - 30, size=24, bold=True)
    if app.name != None:
        drawLabel(f'Hi, {app.name}',
                  app.width/2,  app.height/2 + 30, size=24, bold=True)

runApp()