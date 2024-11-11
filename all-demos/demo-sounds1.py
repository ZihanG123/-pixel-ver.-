# From: https://academy.cs.cmu.edu/cpcs-docs/images_and_sounds

from cmu_graphics import *

def onAppStart(app):
    # Original sound: "Electronic Drum Beat Loop 1" by audiosoundclips.com
    url = 'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/Drum1.mp3'
    app.sound = Sound(url)

def onKeyPress(app, key):
    if key == 'p':
        # Plays the sound starting from the beginning
        app.sound.play(restart=True)

def redrawAll(app):
    drawLabel('Press p to play the sound', 200, 150, size=24)
    drawLabel('Press p while the sound is playing and notice it restarts', 200, 200, size=14)
    drawLabel('Also notice the sound does not start over once it ends', 200, 240, size=14)

def main():
    runApp()

main()