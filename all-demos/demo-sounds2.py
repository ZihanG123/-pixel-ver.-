# From: https://academy.cs.cmu.edu/cpcs-docs/images_and_sounds

from cmu_graphics import *

def onAppStart(app):
    # Original sound: "Electronic Drum Beat Loop 1" by audiosoundclips.com
    url = 'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/sounds/Drum1.mp3'
    app.sound = Sound(url)
    app.paused = True

def onKeyPress(app, key):
    if key == 'p':
        if app.paused:
            app.paused = False
            app.sound.play(loop=True)
        else:
            app.paused = True
            app.sound.pause()

def redrawAll(app):
    if app.paused:
        drawLabel('Sound is Paused (not playing)', 200, 120, size=24)
        drawLabel('Press p to play the sound', 200, 170, size=24)
    else:
        drawLabel('Sound is Playing', 200, 120, size=24)
        drawLabel('Press p to pause the sound', 200, 170, size=24)

    drawLabel('Notice the sound does not restart when it is played', 200, 220, size=14)
    drawLabel('Notice the sound starts over once it ends', 200, 260, size=14)

def main():
    runApp()

main()