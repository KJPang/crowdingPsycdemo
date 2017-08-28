#k.
import psychopy.visual
import psychopy.event
import psychopy.core
import psychopy.gui
import random
import sys
import time

#initialize variables
timestr = time.strftime("%Y%m%d-%H%M%S")
goeshere = open(timestr + ".txt", 'w')
sys.stdout = goeshere
targlist = ["T", "L", "R", "Y", "F"]
distlist = ["T", "L", "R", "Y", "F"]
choice = range(4)
trials = range(4)
random.shuffle(trials)
clock = psychopy.core.Clock()
whichone = 0
correctans1 = 0
correctans2 = 0
correctans3 = 0
correctans4 = 0
confidence1 = []
confidence2 = []
confidence3 = []
confidence4 = []
exptrials = range(60)
random.shuffle(exptrials)
condition = int(0)


#main letters and stuff
win = psychopy.visual.Window(size=[1920, 1080], units="pix", fullscr=True, color=[-1, -1, -1])
un = psychopy.visual.TextStim(win=win, pos=(-475, 225), color=[1, 1, 1], height = 50)
du = psychopy.visual.TextStim(win=win, pos=(474, 225), color=[1, 1, 1], height = 50)
tr = psychopy.visual.TextStim(win=win, pos=(-475, -225), color=[1, 1, 1], height = 50)
qu = psychopy.visual.TextStim(win=win, pos=(475, -225), color=[1, 1, 1], height = 50)
targdis = psychopy.visual.TextStim(win=win, wrapWidth=1000, height = 50)
#top left
q11 = psychopy.visual.TextStim(win=win, pos=(-400, 150), color=[1, 1, 1], height = 50)
q12 = psychopy.visual.TextStim(win=win, pos=(-550, 150), color=[1, 1, 1], height = 50)
q13 = psychopy.visual.TextStim(win=win, pos=(-550, 300), color=[1, 1, 1], height = 50)
q14 = psychopy.visual.TextStim(win=win, pos=(-400, 300), color=[1, 1, 1], height = 50)
#top right
q21 = psychopy.visual.TextStim(win=win, pos=(400, 150), color=[1, 1, 1], height = 50)
q22 = psychopy.visual.TextStim(win=win, pos=(550, 150), color=[1, 1, 1], height = 50)
q23 = psychopy.visual.TextStim(win=win, pos=(550, 300), color=[1, 1, 1], height = 50)
q24 = psychopy.visual.TextStim(win=win, pos=(400, 300), color=[1, 1, 1], height = 50)
#bottom left
q31 = psychopy.visual.TextStim(win=win, pos=(-400, -150), color=[1, 1, 1], height = 50)
q32 = psychopy.visual.TextStim(win=win, pos=(-550, -150), color=[1, 1, 1], height = 50)
q33 = psychopy.visual.TextStim(win=win, pos=(-550, -300), color=[1, 1, 1], height = 50)
q34 = psychopy.visual.TextStim(win=win, pos=(-400, -300), color=[1, 1, 1], height = 50)
#bottom right
q41 = psychopy.visual.TextStim(win=win, pos=(400, -150), color=[1, 1, 1], height = 50)
q42 = psychopy.visual.TextStim(win=win, pos=(550, -150), color=[1, 1, 1], height = 50)
q43 = psychopy.visual.TextStim(win=win, pos=(550, -300), color=[1, 1, 1], height = 50)
q44 = psychopy.visual.TextStim(win=win, pos=(400, -300), color=[1, 1, 1], height = 50)

#lazy
def flipdist():
    q11.flipVert = True
    q11.flipHoriz = True
    q12.flipVert = True
    q12.flipHoriz = True
    q13.flipVert = True
    q13.flipHoriz = True    
    q14.flipVert = True
    q14.flipHoriz = True
    q21.flipVert = True
    q21.flipHoriz = True
    q22.flipVert = True
    q22.flipHoriz = True
    q23.flipVert = True
    q23.flipHoriz = True
    q24.flipVert = True
    q24.flipHoriz = True
    q31.flipVert = True
    q31.flipHoriz = True
    q32.flipVert = True
    q32.flipHoriz = True
    q33.flipVert = True
    q33.flipHoriz = True
    q34.flipVert = True
    q34.flipHoriz = True
    q41.flipVert = True
    q41.flipHoriz = True
    q42.flipVert = True
    q42.flipHoriz = True
    q43.flipVert = True
    q43.flipHoriz = True
    q44.flipVert = True
    q44.flipHoriz = True 
    
#display text
midcross = psychopy.visual.TextStim(win=win, wrapWidth=100, height = 25)
midcross.text = " + "
inst1 = psychopy.visual.TextStim(win=win, wrapWidth=1000)
inst1.text = """
In each trial, you will first be shown a target symbol.\n
You may press any key to continue after studying this symbol.
\n
A cross will then be displayed in the center of the screen.
You are not to shift gaze away from this cross during the next phase of the trial.
\n
After a short delay, a stimulus will be briefly displayed on the screen.
After it has disappeared, select the quadrant in which the target symbol was displayed using the 1-4 keys.
You will then be required to rate the confidence of your choice by using the 1-8 keys.
\n
Press any key to begin a series of sample trials.
"""
inst2 = psychopy.visual.TextStim(win=win, wrapWidth=1000,)
inst2.text = "Press a key (1-4) corresponding to which quadrant the target symbol appeared in.\n 1 = Top Left \n 2 = Top Right \n 3 = Bottom Left \n 4 = Bottom Right \n"
inst3 = psychopy.visual.TextStim(win=win, wrapWidth=1000)
inst3.text = "Press a key (1-8) corresponding your confidence in this selection.\n 1 = Lowest Confidence \n 8 = Highest Confidence"
inst4 = psychopy.visual.TextStim(win=win, wrapWidth=1000)
inst4.text = "The experiment will now begin.\n Press any key to continue."
inst5 = psychopy.visual.TextStim(win=win, wrapWidth=1000)
inst5.text = "Note that the sample trials will be lower in difficulty compared to the experimental trials."
inst6 = psychopy.visual.TextStim(win=win, wrapWidth=1000)
inst6.text = "Thank you for participating."

#instructions and practice trials
inst1.draw()
win.flip()
psychopy.event.waitKeys()
inst5.draw()
win.flip()
psychopy.event.waitKeys()

#sample
s1 = psychopy.visual.TextStim(win=win, pos=(-475, 225), color=[1, 1, 1], height = 50, text = "1")
s2 = psychopy.visual.TextStim(win=win, pos=(474, 225), color=[1, 1, 1], height = 50, text = "2")
s3 = psychopy.visual.TextStim(win=win, pos=(-475, -225), color=[1, 1, 1], height = 50, text = "3")
s4 = psychopy.visual.TextStim(win=win, pos=(475, -225), color=[1, 1, 1], height = 50, text = "4")
stargdis = psychopy.visual.TextStim(win=win, wrapWidth=1000, height = 50, text = "2")
stargdis.draw()
win.flip()
psychopy.event.waitKeys()
clock.reset()
while clock.getTime() < 2:
    midcross.draw()
    win.flip()
clock.reset()    
while clock.getTime() < 3:
    midcross.draw()
    s1.draw()
    s2.draw()
    s3.draw()
    s4.draw()
    win.flip()
clock.reset()   
while clock.getTime() < 0.5:
    win.flip()
inst2.draw()
win.flip()
psychopy.event.waitKeys()
s1.text = "T"
s2.text = "T"
s3.text = "Q"
s4.text = "T"
stargdis.text = "Q"
stargdis.draw()
win.flip()
psychopy.event.waitKeys()
clock.reset()
while clock.getTime() < 2:
    midcross.draw()
    win.flip()
clock.reset()    
while clock.getTime() < 3:
    midcross.draw()
    s1.draw()
    s2.draw()
    s3.draw()
    s4.draw()
    win.flip()
clock.reset()   
while clock.getTime() < 0.5:
    win.flip()
inst2.draw()
win.flip()
psychopy.event.waitKeys()
inst4.draw()
win.flip()
psychopy.event.waitKeys()

#run trials
for i in exptrials:
    #choose target and distractors, make sure they arent the same for non-flip trials, pick position
    whichone = 0
    clock.reset()
    tt = random.choice(targlist)
    dd = random.choice(distlist)
    if i >= 0 and i < 15:    
        while tt == dd:
            tt = random.choice(targlist)
            dd = random.choice(distlist)
    if i > 44:    
        while tt == dd:
            tt = random.choice(targlist)
            dd = random.choice(distlist) 
    cc = random.choice(choice)
    targdis.text = tt
    q11.text = dd
    q11.flipVert = False
    q11.flipHoriz = False
    q12.text = dd
    q12.flipVert = False
    q12.flipHoriz = False
    q13.text = dd
    q13.flipVert = False
    q13.flipHoriz = False    
    q14.text = dd
    q14.flipVert = False
    q14.flipHoriz = False
    q21.text = dd
    q21.flipVert = False
    q21.flipHoriz = False
    q22.text = dd
    q22.flipVert = False
    q22.flipHoriz = False
    q23.text = dd
    q23.flipVert = False
    q23.flipHoriz = False
    q24.text = dd
    q24.flipVert = False
    q24.flipHoriz = False
    q31.text = dd
    q31.flipVert = False
    q31.flipHoriz = False
    q32.text = dd
    q32.flipVert = False
    q32.flipHoriz = False
    q33.text = dd
    q33.flipVert = False
    q33.flipHoriz = False
    q34.text = dd
    q34.flipVert = False
    q34.flipHoriz = False
    q41.text = dd
    q41.flipVert = False
    q41.flipHoriz = False
    q42.text = dd
    q42.flipVert = False
    q42.flipHoriz = False
    q43.text = dd
    q43.flipVert = False
    q43.flipHoriz = False
    q44.text = dd
    q44.flipVert = False
    q44.flipHoriz = False
    
    if cc == 0:
        realans = ["1"]
    elif cc == 1:
        realans = ["2"]
    elif cc == 2:
        realans = ["3"]
    elif cc == 3:
        realans = ["4"]
          
    if cc == 0:
        un.text = tt
    else:
        un.text = dd
    if cc == 1:
        du.text = tt
    else:
        du.text = dd
    if cc == 2:
        tr.text = tt
    else:
        tr.text = dd
    if cc == 3:
        qu.text = tt
    else:
        qu.text = dd
        
    un.flipVert = False
    du.flipVert = False
    tr.flipVert = False
    qu.flipVert = False
    un.flipHoriz = False
    du.flipHoriz = False
    tr.flipHoriz = False
    qu.flipHoriz = False  
    targdis.flipVert = False
    targdis.flipHoriz = False

    if i > 14 and i < 30:
        whichone = 1
        if cc == 0:
            du.flipVert = True
            du.flipHoriz = True
            tr.flipVert = True
            tr.flipHoriz = True
            qu.flipVert = True
            qu.flipHoriz = True 
        elif cc == 1:
            un.flipVert = True
            un.flipHoriz = True
            tr.flipVert = True
            tr.flipHoriz = True
            qu.flipVert = True
            qu.flipHoriz = True  
        elif cc == 2:
            un.flipVert = True
            un.flipHoriz = True
            du.flipVert = True
            du.flipHoriz = True
            qu.flipVert = True
            qu.flipHoriz = True 
        elif cc == 3:
            un.flipVert = True
            un.flipHoriz = True
            du.flipVert = True
            du.flipHoriz = True
            tr.flipVert = True
            tr.flipHoriz = True 
        flipdist()
    elif i > 29 and i < 45:
        whichone = 2
        targdis.flipVert = True
        targdis.flipHoriz = True
        if cc == 0:
            un.flipVert = True
            un.flipHoriz = True
        elif cc == 1:
            du.flipVert = True
            du.flipHoriz = True
        elif cc == 2:
            tr.flipVert = True
            tr.flipHoriz = True
        elif cc == 3:
            qu.flipVert = True
            qu.flipHoriz = True  
    elif i > 44:
        whichone = 3
        targdis.flipVert = True
        targdis.flipHoriz = True
        if cc == 0:
            un.flipVert = True
            un.flipHoriz = True
            du.flipVert = True
            du.flipHoriz = True
            tr.flipVert = True
            tr.flipHoriz = True
            qu.flipVert = True
            qu.flipHoriz = True 
        elif cc == 1:
            un.flipVert = True
            un.flipHoriz = True
            du.flipVert = True
            du.flipHoriz = True
            tr.flipVert = True
            tr.flipHoriz = True
            qu.flipVert = True
            qu.flipHoriz = True 
        elif cc == 2:
            un.flipVert = True
            un.flipHoriz = True
            du.flipVert = True
            du.flipHoriz = True
            tr.flipVert = True
            tr.flipHoriz = True
            qu.flipVert = True
            qu.flipHoriz = True 
        elif cc == 3:
            un.flipVert = True
            un.flipHoriz = True
            du.flipVert = True
            du.flipHoriz = True
            tr.flipVert = True
            tr.flipHoriz = True
            qu.flipVert = True
            qu.flipHoriz = True 
        flipdist()
    #stuff on the screen first
    targdis.draw()
    win.flip()
    psychopy.event.waitKeys()
    clock.reset()
    while clock.getTime() < 2:
        midcross.draw()
        win.flip()
    clock.reset()
    
    #stuff onto the screen big
    while clock.getTime() < 0.5:
        midcross.draw()
        un.draw()
        du.draw()
        tr.draw()
        qu.draw()
        q11.draw()
        q12.draw()
        q13.draw()
        q14.draw()
        q21.draw()
        q22.draw()
        q23.draw()
        q24.draw()
        q31.draw()
        q32.draw()
        q33.draw()
        q34.draw()
        q41.draw()
        q42.draw()
        q43.draw()
        q44.draw()
        win.flip()
    clock.reset()   
    #wait a bit     
    clock.reset()
    while clock.getTime() < 0.5:
        win.flip()
    #two selection options
    inst2.draw()
    win.flip()
    selection = psychopy.event.waitKeys(keyList=["1", "2", "3", "4", "q"])
    if selection == ["q"]:
        win.close()
    print selection
    print realans
    if selection == realans:
        print "why"
        if whichone == 0:
            correctans1 = correctans1 + 1
        elif whichone == 1:
            correctans2 = correctans2 + 1
        elif whichone == 2:
            correctans3 = correctans3 + 1
        elif whichone == 3:
            correctans4 = correctans4 + 1
    inst3.draw()
    win.flip()
    cselection = psychopy.event.waitKeys(keyList=["1", "2", "3", "4", "5", "6", "7", "8"])
    if whichone == 0:
        confidence1 = confidence1 + cselection
    elif whichone == 1:
        confidence2 = confidence2 + cselection
    elif whichone == 2:
        confidence3 = confidence3 + cselection
    elif whichone == 3:
        confidence4 = confidence4 + cselection
    whichone = 0
        
#print to screen
win.close()
print "Accuracy"
print correctans1
print correctans2
print correctans3
print correctans4
print "Confidence List"
print confidence1
print confidence2
print confidence3
print confidence4

