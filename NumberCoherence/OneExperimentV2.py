#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Fri Mar 18 10:46:24 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'SmallNumberExperiment3'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/Users/jennamargarites/Desktop/OneExperiment_PsychoPy/SmallNumberExperiment3.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Intermission"
IntermissionClock = core.Clock()
fixationImage = visual.ImageStim(
    win=win,
    name='fixationImage', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "anticipatoryPeriod"
anticipatoryPeriodClock = core.Clock()
LeftBox = visual.ShapeStim(
    win=win, name='LeftBox',
    size=(.6, .6), vertices='circle',
    ori=0.0, pos=(-.45, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
RightBox = visual.ShapeStim(
    win=win, name='RightBox',
    size=(0.6, 0.6), vertices='circle',
    ori=0.0, pos=(.45, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
TShape1A = visual.ShapeStim(
    win=win, name='TShape1A',
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-2.0, interpolate=True)
TShape2A = visual.ShapeStim(
    win=win, name='TShape2A',
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-3.0, interpolate=True)
TShape3A = visual.ShapeStim(
    win=win, name='TShape3A',
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-4.0, interpolate=True)
NShape1A = visual.ShapeStim(
    win=win, name='NShape1A', vertices='star7',
    size=[1.0, 1.0],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-5.0, interpolate=True)
NShape2A = visual.ShapeStim(
    win=win, name='NShape2A',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-6.0, interpolate=True)
NShape3A = visual.ShapeStim(
    win=win, name='NShape3A',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-7.0, interpolate=True)

# Initialize components for Routine "animation"
animationClock = core.Clock()
LeftBox2 = visual.ShapeStim(
    win=win, name='LeftBox2',
    size=(.6, .6), vertices='circle',
    ori=0.0, pos=(-.45, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
RightBox2 = visual.ShapeStim(
    win=win, name='RightBox2',
    size=(0.6, 0.6), vertices='circle',
    ori=0.0, pos=(.45, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
TShape1B = visual.ShapeStim(
    win=win, name='TShape1B',
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
TShape2B = visual.ShapeStim(
    win=win, name='TShape2B',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
TShape3B = visual.ShapeStim(
    win=win, name='TShape3B',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
NShape1B = visual.ShapeStim(
    win=win, name='NShape1B', vertices='star7',
    size=[1.0, 1.0],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-5.0, interpolate=True)
NShape2B = visual.ShapeStim(
    win=win, name='NShape2B',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-6.0, interpolate=True)
NShape3B = visual.ShapeStim(
    win=win, name='NShape3B',
    size=[1.0, 1.0], vertices='triangle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='dimgray', fillColor='dimgray',
    opacity=None, depth=-7.0, interpolate=True)
Sound = sound.Sound('A', secs=.875, stereo=True, hamming=True,
    name='Sound')
Sound.setVolume(1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
Trial = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MASTER_TEMPLATE.csv'),
    seed=None, name='Trial')
thisExp.addLoop(Trial)  # add the loop to the experiment
thisTrial = Trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in Trial:
    currentLoop = Trial
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
# ------Prepare to start Routine "Intermission"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    fixationImage.setImage(fixation)
    # keep track of which components have finished
    IntermissionComponents = [fixationImage]
    for thisComponent in IntermissionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    IntermissionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    num_incs = 0
    orrTracker = True
    
    # -------Run Routine "Intermission"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IntermissionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=IntermissionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if num_incs == 0:
            fixationImage.ori = 0
        
        if orrTracker:
            fixationImage.ori = fixationImage.ori + .5
            num_incs = num_incs + 1
        
        if not orrTracker:
            fixationImage.ori = fixationImage.ori - .5
            num_incs = num_incs + 1
            
        if num_incs == 44:
            orrTracker = False
        
        if num_incs == 132:
            orrTracker = True
            
        # *fixationImage* updates
        if fixationImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixationImage.frameNStart = frameN  # exact frame index
            fixationImage.tStart = t  # local t and not account for scr refresh
            fixationImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationImage, 'tStartRefresh')  # time at next scr refresh
            fixationImage.setAutoDraw(True)
        if fixationImage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixationImage.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationImage.tStop = t  # not accounting for scr refresh
                fixationImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationImage, 'tStopRefresh')  # time at next scr refresh
                fixationImage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IntermissionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Intermission"-------
    for thisComponent in IntermissionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trial.addData('fixationImage.started', fixationImage.tStartRefresh)
    Trial.addData('fixationImage.stopped', fixationImage.tStopRefresh)
    
    # ------Prepare to start Routine "anticipatoryPeriod"-------
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    if shape==6:
        TShape1A.vertices=6
        TShape2A.vertices=6
        TShape3A.vertices=6
        NShape1A.vertices=6
        NShape2A.vertices=6
        NShape3A.vertices=6
    else:
        TShape1A.setVertices(shape)
        TShape2A.setVertices(shape)
        TShape3A.setVertices(shape)
        NShape1A.setVertices(shape)
        NShape2A.setVertices(shape)
        NShape3A.setVertices(shape)
    TShape1A.setPos((targetX, targetY))
    TShape1A.setSize((targetSize, targetSize))
    TShape2A.setPos((targetX2, targetY2))
    TShape2A.setSize((targetSize, targetSize))
    TShape3A.setPos((targetX3, targetY3))
    TShape3A.setSize((targetSize, targetSize))
    NShape1A.setPos((nontargetX, nontargetY))
    NShape1A.setSize((nontargetSize, nontargetSize))
    NShape2A.setPos((nontargetX2, nontargetY2))
    NShape2A.setSize((nontargetSize, nontargetSize))
    NShape3A.setPos((nontargetX3, nontargetY3))
    NShape3A.setSize((nontargetSize, nontargetSize))
    # keep track of which components have finished
    anticipatoryPeriodComponents = [LeftBox, RightBox, TShape1A, TShape2A, TShape3A, NShape1A, NShape2A, NShape3A]
    for thisComponent in anticipatoryPeriodComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    anticipatoryPeriodClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "anticipatoryPeriod"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = anticipatoryPeriodClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=anticipatoryPeriodClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LeftBox* updates
        if LeftBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftBox.frameNStart = frameN  # exact frame index
            LeftBox.tStart = t  # local t and not account for scr refresh
            LeftBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftBox, 'tStartRefresh')  # time at next scr refresh
            LeftBox.setAutoDraw(True)
        if LeftBox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > LeftBox.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                LeftBox.tStop = t  # not accounting for scr refresh
                LeftBox.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LeftBox, 'tStopRefresh')  # time at next scr refresh
                LeftBox.setAutoDraw(False)
        
        # *RightBox* updates
        if RightBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RightBox.frameNStart = frameN  # exact frame index
            RightBox.tStart = t  # local t and not account for scr refresh
            RightBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RightBox, 'tStartRefresh')  # time at next scr refresh
            RightBox.setAutoDraw(True)
        if RightBox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > RightBox.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                RightBox.tStop = t  # not accounting for scr refresh
                RightBox.frameNStop = frameN  # exact frame index
                win.timeOnFlip(RightBox, 'tStopRefresh')  # time at next scr refresh
                RightBox.setAutoDraw(False)
        
        # *TShape1A* updates
        if TShape1A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TShape1A.frameNStart = frameN  # exact frame index
            TShape1A.tStart = t  # local t and not account for scr refresh
            TShape1A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TShape1A, 'tStartRefresh')  # time at next scr refresh
            TShape1A.setAutoDraw(True)
        if TShape1A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TShape1A.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                TShape1A.tStop = t  # not accounting for scr refresh
                TShape1A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TShape1A, 'tStopRefresh')  # time at next scr refresh
                TShape1A.setAutoDraw(False)
        
        # *TShape2A* updates
        if TShape2A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TShape2A.frameNStart = frameN  # exact frame index
            TShape2A.tStart = t  # local t and not account for scr refresh
            TShape2A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TShape2A, 'tStartRefresh')  # time at next scr refresh
            TShape2A.setAutoDraw(True)
        if TShape2A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TShape2A.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                TShape2A.tStop = t  # not accounting for scr refresh
                TShape2A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TShape2A, 'tStopRefresh')  # time at next scr refresh
                TShape2A.setAutoDraw(False)
        
        # *TShape3A* updates
        if TShape3A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TShape3A.frameNStart = frameN  # exact frame index
            TShape3A.tStart = t  # local t and not account for scr refresh
            TShape3A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TShape3A, 'tStartRefresh')  # time at next scr refresh
            TShape3A.setAutoDraw(True)
        if TShape3A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TShape3A.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                TShape3A.tStop = t  # not accounting for scr refresh
                TShape3A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TShape3A, 'tStopRefresh')  # time at next scr refresh
                TShape3A.setAutoDraw(False)
        
        # *NShape1A* updates
        if NShape1A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NShape1A.frameNStart = frameN  # exact frame index
            NShape1A.tStart = t  # local t and not account for scr refresh
            NShape1A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NShape1A, 'tStartRefresh')  # time at next scr refresh
            NShape1A.setAutoDraw(True)
        if NShape1A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NShape1A.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                NShape1A.tStop = t  # not accounting for scr refresh
                NShape1A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NShape1A, 'tStopRefresh')  # time at next scr refresh
                NShape1A.setAutoDraw(False)
        
        # *NShape2A* updates
        if NShape2A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NShape2A.frameNStart = frameN  # exact frame index
            NShape2A.tStart = t  # local t and not account for scr refresh
            NShape2A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NShape2A, 'tStartRefresh')  # time at next scr refresh
            NShape2A.setAutoDraw(True)
        if NShape2A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NShape2A.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                NShape2A.tStop = t  # not accounting for scr refresh
                NShape2A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NShape2A, 'tStopRefresh')  # time at next scr refresh
                NShape2A.setAutoDraw(False)
        
        # *NShape3A* updates
        if NShape3A.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NShape3A.frameNStart = frameN  # exact frame index
            NShape3A.tStart = t  # local t and not account for scr refresh
            NShape3A.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NShape3A, 'tStartRefresh')  # time at next scr refresh
            NShape3A.setAutoDraw(True)
        if NShape3A.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NShape3A.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                NShape3A.tStop = t  # not accounting for scr refresh
                NShape3A.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NShape3A, 'tStopRefresh')  # time at next scr refresh
                NShape3A.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in anticipatoryPeriodComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "anticipatoryPeriod"-------
    for thisComponent in anticipatoryPeriodComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trial.addData('LeftBox.started', LeftBox.tStartRefresh)
    Trial.addData('LeftBox.stopped', LeftBox.tStopRefresh)
    Trial.addData('RightBox.started', RightBox.tStartRefresh)
    Trial.addData('RightBox.stopped', RightBox.tStopRefresh)
    Trial.addData('TShape1A.started', TShape1A.tStartRefresh)
    Trial.addData('TShape1A.stopped', TShape1A.tStopRefresh)
    Trial.addData('TShape2A.started', TShape2A.tStartRefresh)
    Trial.addData('TShape2A.stopped', TShape2A.tStopRefresh)
    Trial.addData('TShape3A.started', TShape3A.tStartRefresh)
    Trial.addData('TShape3A.stopped', TShape3A.tStopRefresh)
    Trial.addData('NShape1A.started', NShape1A.tStartRefresh)
    Trial.addData('NShape1A.stopped', NShape1A.tStopRefresh)
    Trial.addData('NShape2A.started', NShape2A.tStartRefresh)
    Trial.addData('NShape2A.stopped', NShape2A.tStopRefresh)
    Trial.addData('NShape3A.started', NShape3A.tStartRefresh)
    Trial.addData('NShape3A.stopped', NShape3A.tStopRefresh)
    
    
    
# completed 1.0 repeats of 'Trial'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# Save movie
# FIX ME
#win.saveMovieFrames('myMovie.mp4')

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
