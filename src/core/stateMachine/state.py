__author__ = 'Matt Holland'
from src.core.stateMachine.transition import *


#TODO: enforce state requirements (We won't go into transfer state when excavator is still on board the transport)
class state:

    nextStateId = 0

    ##
    # state
    #
    # Parameters:
    #   name - The human readable name of the state
    #   onTick - lambda function to execute when this state is run
    #
    def __init__(self, name, onTick):
        self.transitions = []
        self.name = name
        self.onTick = onTick
        self.id = ++state.nextStateId
        return

    ##
    # addTransition
    #
    # Description: Adds a transition to the state. This is how the current state gets to another state.
    #
    # Parameters:
    #   name - the human readable name of the transition
    #   canTransition - function to check if criteria have been met to transition to the next state
    #   nextState - The state object to transition to
    #
    # Returns: the newly created state
    #
    def addTransition(self, name, canTransition, nextState):

        newTransition = transition(name, canTransition, nextState)

        self.transitions.append(newTransition)

        return newTransition

    ##
    # getNextState
    #
    # Description: iterates through all transitions. The first transition to pass its canTransition function is
    #   returned. If no transitions pass their canTransition function then this state is returned.
    #
    # Returns: the fist state to pass its canTransition function
    #
    def getNextState(self):

        for t in self.transitions:
            if t.canTransition():
                return t.nextState

        return self