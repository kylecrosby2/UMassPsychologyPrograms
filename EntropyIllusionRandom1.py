#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on July 19, 2022, at 19:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""
#import random
from random import randint
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from math import floor



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'EntropyIllusion'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\kerry\\Documents\\Park Internship\\EntropyIllusion\\EntropyIllusion.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Reference"
ReferenceClock = core.Clock()
image_phaseA = visual.ImageStim(
    win=win,
    name='image_phaseA', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win,
    name='fixation_cross', 
    image='images/cross.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
#Rows of the Loop Selection Sheet
maxRows = 4 
#Substract a small number to avoid floor(maxRows)==maxRows
maxRows = maxRows-0.0001
# Returns values only between 0 and maxRows 
sheetRowIndex = str(floor(random()*(maxRows)))
print(sheetRowIndex)

# Initialize components for Routine "Probe"
ProbeClock = core.Clock()
imagePhaseB = visual.ImageStim(
    win=win,
    name='imagePhaseB', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fixation_cross_2 = visual.ImageStim(
    win=win,
    name='fixation_cross_2', 
    image='images/cross.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
centralLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('EntropyConditions1.xlsx', selection=sheetRowIndex),
    seed=None, name='centralLoop')
thisExp.addLoop(centralLoop)  # add the loop to the experiment
thisCentralLoop = centralLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCentralLoop.rgb)
if thisCentralLoop != None:
    for paramName in thisCentralLoop:
        exec('{} = thisCentralLoop[paramName]'.format(paramName))

#randVar = randint(1, 2)
for thisCentralLoop in centralLoop:
    currentLoop = centralLoop
    # abbreviate parameter names if possible (e.g. rgb = thisCentralLoop.rgb)
    if thisCentralLoop != None:
        for paramName in thisCentralLoop:
            exec('{} = thisCentralLoop[paramName]'.format(paramName))
    randVar = randint(1, 3)
    #randVar = 1
    print("randVar HERE:")
    print(randVar)
    for i in range(2):
        print("Loop beginning!")
        if (randVar == 1 and i == 0) or (randVar == 2 and i == 1):
            print("First loop running")
            # ------Prepare to start Routine "Reference"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            image_phaseA.setPos(positionA)
            image_phaseA.setImage(imageA)
            # keep track of which components have finished
            ReferenceComponents = [image_phaseA, fixation_cross]
            '''
            for thisComponent in ReferenceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            '''
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ReferenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Reference"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ReferenceClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ReferenceClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_phaseA* updates
                if image_phaseA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_phaseA.frameNStart = frameN  # exact frame index
                    image_phaseA.tStart = t  # local t and not account for scr refresh
                    image_phaseA.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_phaseA, 'tStartRefresh')  # time at next scr refresh
                    image_phaseA.setAutoDraw(True)
                if image_phaseA.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_phaseA.tStartRefresh + .05-frameTolerance:
                        # keep track of stop time/frame for later
                        image_phaseA.tStop = t  # not accounting for scr refresh
                        image_phaseA.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_phaseA, 'tStopRefresh')  # time at next scr refresh
                        image_phaseA.setAutoDraw(False)
                
                # *fixation_cross* updates
                if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross.frameNStart = frameN  # exact frame index
                    fixation_cross.tStart = t  # local t and not account for scr refresh
                    fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
                    fixation_cross.setAutoDraw(True)
                if fixation_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross.tStop = t  # not accounting for scr refresh
                        fixation_cross.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
                        fixation_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ReferenceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Reference"-------
            for thisComponent in ReferenceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            centralLoop.addData('image_phaseA.started', image_phaseA.tStartRefresh)
            centralLoop.addData('image_phaseA.stopped', image_phaseA.tStopRefresh)
            centralLoop.addData('fixation_cross.started', fixation_cross.tStartRefresh)
            centralLoop.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
        
        if (randVar == 2 and i == 0) or (randVar == 1 and i == 1):
            print("Second loop running")
            # ------Prepare to start Routine "Probe"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            imagePhaseB.setPos(positionA)
            imagePhaseB.setImage(imageB)
            # keep track of which components have finished
            ProbeComponents = [imagePhaseB, fixation_cross_2]
            for thisComponent in ProbeComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            ProbeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Probe"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = ProbeClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=ProbeClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *imagePhaseB* updates
                if imagePhaseB.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    imagePhaseB.frameNStart = frameN  # exact frame index
                    imagePhaseB.tStart = t  # local t and not account for scr refresh
                    imagePhaseB.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(imagePhaseB, 'tStartRefresh')  # time at next scr refresh
                    imagePhaseB.setAutoDraw(True)
                if imagePhaseB.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > imagePhaseB.tStartRefresh + 0.05-frameTolerance:
                        # keep track of stop time/frame for later
                        imagePhaseB.tStop = t  # not accounting for scr refresh
                        imagePhaseB.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(imagePhaseB, 'tStopRefresh')  # time at next scr refresh
                        imagePhaseB.setAutoDraw(False)
                
                # *fixation_cross_2* updates
                if fixation_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross_2.frameNStart = frameN  # exact frame index
                    fixation_cross_2.tStart = t  # local t and not account for scr refresh
                    fixation_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross_2, 'tStartRefresh')  # time at next scr refresh
                    fixation_cross_2.setAutoDraw(True)
                if fixation_cross_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross_2.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross_2.tStop = t  # not accounting for scr refresh
                        fixation_cross_2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(fixation_cross_2, 'tStopRefresh')  # time at next scr refresh
                        fixation_cross_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ProbeComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Probe"-------
            for thisComponent in ProbeComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            centralLoop.addData('imagePhaseB.started', imagePhaseB.tStartRefresh)
            centralLoop.addData('imagePhaseB.stopped', imagePhaseB.tStopRefresh)
            centralLoop.addData('fixation_cross_2.started', fixation_cross_2.tStartRefresh)
            centralLoop.addData('fixation_cross_2.stopped', fixation_cross_2.tStopRefresh)
            thisExp.nextEntry()
    
# completed 1.0 repeats of 'centralLoop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
