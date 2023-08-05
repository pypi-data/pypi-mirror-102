from .util import *


class Command:
    command_g_counter = 0
    command_G_counter = 0
    resolution_mode = 0

    def __init__(self, type: PSDTypes):
        self.type = type

    """
    Zx - Initialize PSD/4, Assign Valve Output to Right
    Yx - Initialize PSD/4, Assign Valve Output to Left
    Wx - Initialize PSD/4, Configure for No Valve
    """

    def initialize(self, drive: str, value=0):
        cmd: str = ''
        if drive == 'Z' or drive == 'Y' or drive == 'W':
            cmd += drive
        else:
            print("Error! Incorrect drive!")
            cmd = 'cmdError'
            return cmd
        if (value == 1) or (value >= 10 and value <= 40):
            cmd += str(value)
        return cmd

    def resetInternalParams(self):
        self.command_g_counter = 0
        self.command_G_counter = 0

    """
    R - Execute Command Buffer
    X - Execute Command Buffer from Beginning
    """

    def executeCommandBuffer(self, type='R'):
        cmd: str = ''
        if type == 'R' or type == 'X':
            cmd += type
        else:
            print("Error! Incorrect type!")
            cmd = 'cmdError'
        return cmd

    """
        Syringe Commands
    """

    def setCounterPosition(self):
        return 'z'

    def absolutePosition(self, value):
        cmd: str = 'A'
        cmd += str(value)
        print("ajung aici?")
        return cmd

    def relativePickup(self, value: int):
        cmd: str = 'P'
        cmd += str(value)
        return cmd

    def relativeDispense(self, value: int):
        cmd: str = 'D'
        cmd += str(value)
        return cmd

    def returnSteps(self, value: int):
        cmd: str = 'K'
        cmd += str(value)
        return cmd

    def backoffSteps(self, value: int):
        cmd: str = 'k'
        cmd += str(value)
        return cmd

    '''
        Valve Commands
    '''

    def vMoveValveToInputPosition(self, value=0):
        cmd: str = 'I'
        if value == 0:
            print("Default command!")
        elif 1 <= value <= 8:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Move valve to input position command!")
        return cmd

    def vMoveValveToOutputPosition(self, value=0):
        cmd: str = 'O'
        if value == 0:
            print("Default command!")
        elif 1 <= value <= 8:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Move valve to output position command!")
        return cmd

    def vMoveValveToBypass(self):
        return 'B'

    def vMoveValveToExtraPosition(self):
        return 'E'

    """
        Action commands
    """

    def aDefinePositionInCommandString(self):
        cmd: str = 'g'
        self.command_g_counter += 1
        print("actual value of g command: " + str(self.command_g_counter))
        if self.command_g_counter > 10:
            print("Using g command exceed maximum number of usage!")
            cmd = 'cmdError'
            self.command_g_counter = 0
        return cmd

    # Gx - Repeat Commands
    def aRepeatCommands(self, value=0):
        cmd: str = 'G'
        self.command_G_counter += 1
        if value == 0:
            print("default value for Repeat Commands")
        elif 1 <= value <= 65535:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Repeat Commands command!")

        print("actual value of G command: " + str(self.command_G_counter))
        if self.command_G_counter > 10:
            print("Using g command exceed maximum number of usage!")
            cmd = 'cmdError'
            self.command_G_counter = 0

        return cmd

    # Mx - Delay - performs a delay of x milliseconds.where 5 ≤ x ≤ 30,000 milliseconds.
    def aDelay(self, value: int):
        cmd: str = 'M'
        if 5 <= value <= 30000:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Delay command!")
        return cmd

    # Hx - Halt Command Execution
    def aHalt(self, value: int):
        cmd: str = 'H'
        if 0 <= value <= 2:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Halt command!")
        return cmd

    # Jx - Auxiliary Outputs
    def aAuxiliaryOutputs(self, value: int):
        cmd: str = 'J'
        if 0 <= value <= 7:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Auxiliary Outputs command!")
        return cmd

    # sx - Store Command String
    def aStoreCommandString(self, location: int, command: str):
        cmd: str = 's'
        if 0 <= location <= 14:
            cmd += str(location)
            cmd += command
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Store Command String command!")
        return cmd

    # ex - Execute Command String in EEPROM Location
    def aExecuteCommandStringInEEPROMLocation(self, location: int):
        cmd: str = 'e'
        if 0 <= location <= 14:
            cmd += str(location)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Execute Command String in EEPROM Location command!")
        return cmd

    def aTerminateCommandBuffer(self):
        return 'T'

    """
        Motor Commands
    """

    def mSetAcceleration(self, value: int):
        cmd: str = 'L'
        if 0 <= value <= 20:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for set acceleration command!")
        return cmd

    def mSetSpeed(self, value: int):
        cmd: str = 'S'
        if 1 <= value <= 40:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for set speed command!")
        return cmd

    def mIncreaseStopVelocityBySteps(self, value: int):
        cmd: str = 'C'
        if 0 <= value <= 25:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for Increase Stop Velocity by Steps command!")
        return cmd

    def mSetStartVelocity(self, value: int):
        cmd: str = 'v'
        if 50 <= value <= 1000:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for set start velocity command!")
        return cmd

    def mSetMaximumVelocity(self, value: int):
        cmd: str = 'V'
        if 2 <= value <= 5800:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for set maximum velocity command!")
        return cmd

    def mStopVelocity(self, value: int):
        cmd: str = 'c'
        if 50 <= value <= 2700:
            cmd += str(value)
        else:
            cmd = 'cmdError'
            print("Wrong parameter value for stop velocity command!")
        return cmd

    """
        h30001 - Enable h Factor Commands and Queries
        h30000 - Disable h Factor Commands and Queries
    """

    def hEnableFactorCommands(self, bValue: bool):
        cmd: str = 'h3000'
        cmd += str(int(bValue))
        return cmd

    def hResetPSD(self):
        return "h30003"

    def hInitializeValve(self):
        return "h20000"

    def hInitializeSyringeOnly(self, speedCode: int):
        cmd: str = 'h'
        cmdValue = 10000
        # permitted values between 0-40
        if 0 <= speedCode <= 40:
            cmdValue += speedCode
        cmd += str(cmdValue)
        return cmd

    def hSetSyringeMode(self, mode: int):
        cmd: str = 'h'
        cmdValue = 11000
        # permitted values between 0-15
        if 0 <= mode <= 15:
            cmdValue += mode
        cmd += str(cmdValue)
        print("default syringe mode method call")
        print(cmd)
        return cmd

    def hEnableValveMovement(self, bValue: bool):
        cmd: str = 'h2000'
        if bValue is True:
            cmd += '1'
        else:
            cmd += '2'
        return cmd

    def hSetValveType(self, type: int):
        cmd: str = 'h2100'
        # permitted values between 0-6
        if 0 <= type <= 6:
            cmd += str(type)
        return cmd

    def hMoveValveToSpecificPositionInShortestDirection(self, specificPosition: PositionInShortestDirection):
        cmd: str = 'h2300'
        cmd += str(specificPosition.value)
        return cmd

    def hMoveValveClockwiseDirection(self, position: int):
        cmd: str = 'h2400'
        # permitted values between 1-8
        if 1 <= position <= 8:
            cmd += str(position)
        return cmd

    def hMoveValveCounterclockwiseDirection(self, position: int):
        cmd: str = 'h2500'
        # permitted values between 1-8
        if 1 <= position <= 8:
            cmd += str(position)
        return cmd

    def hMoveValveInShortestDirection(self, position: int):
        cmd: str = 'h2600'
        # permitted values between 1-8
        if 1 <= position <= 8:
            cmd += str(position)
        return cmd

    def valveMovementHelper(self, cmdValue: int, incrementWith: int):
        cmd: str = 'h'
        # permitted values between 0-345 incremented by 15
        if 345 >= incrementWith >= 0 == incrementWith % 15:
            cmdValue += incrementWith
        cmd += str(cmdValue)
        return cmd

    def hClockwiseAngularValveMove(self, position: int):
        return self.valveMovementHelper(27000, position)

    def hCounterclockwiseAngularValveMove(self, position: int):
        return self.valveMovementHelper(28000, position)

    def hShortestDirectAngularValveMove(self, position: int):
        return self.valveMovementHelper(29000, position)

    """
        Query Commands
    """

    def commandBufferStatusQuery(self):
        return QueryCommandsEnumeration.BUFFER_STATUS.value

    def pumpStatusQuery(self):
        return QueryCommandsEnumeration.PUMP_STATUS.value

    def firmwareVersionQuery(self):
        return QueryCommandsEnumeration.FIRMWARE_VERSION.value

    def firmwareChecksumQuery(self):
        return QueryCommandsEnumeration.FIRMWARE_CHECKSUM.value

    def startVelocityQuery(self):
        return QueryCommandsEnumeration.START_VELOCITY.value

    def maximumVelocityQuery(self):
        return QueryCommandsEnumeration.MAXIMUM_VELOCITY.value

    def stopVelocityQuery(self):
        return QueryCommandsEnumeration.STOP_VELOCITY.value

    def actualPositionOfSyringeQuery(self):
        return QueryCommandsEnumeration.ACTUAL_SYRINGE_POSITION.value

    def numberOfReturnStepsQuery(self):
        return QueryCommandsEnumeration.NUMBER_OF_RETURN_STEPS.value

    def statusOfAuxiliaryInput1Query(self):
        return QueryCommandsEnumeration.STATUS_AUXILIARY_INPUT_1.value

    def statusOfAuxiliaryInput2Query(self):
        return QueryCommandsEnumeration.STATUS_AUXILIARY_INPUT_2.value

    def returns255Query(self):
        return QueryCommandsEnumeration.RETURNS_255.value

    def numberOfBackoffStepsQuery(self):
        return QueryCommandsEnumeration.NUMBER_OF_BACKOFF_STEPS.value

    def syringeStatusQuery(self):
        return QueryCommandsEnumeration.SYRINGE_STATUS.value

    def syringeModeQuery(self):
        return QueryCommandsEnumeration.SYRINGE_MODE.value

    def valveStatusQuery(self):
        return QueryCommandsEnumeration.VALVE_STATUS.value

    def valveTypeQuery(self):
        return QueryCommandsEnumeration.VALVE_TYPE.value

    def valveLogicalPositionQuery(self):
        return QueryCommandsEnumeration.VALVE_LOGICAL_POSITION.value

    def valveNumericalPositionQuery(self):
        return QueryCommandsEnumeration.VALVE_NUMERICAL_POSITION.value

    def valveAngleQuery(self):
        return QueryCommandsEnumeration.VALVE_ANGLE.value

    def lastDigitalOutValueQuery(self):
        return QueryCommandsEnumeration.LAST_DIGITAL_OUT_VALUE.value