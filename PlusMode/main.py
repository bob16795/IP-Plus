import BigNumber
import SeededRand
import GameController

class Data:
    """
    This is a class for storing data, this is required

    Attributes:
        id (int): the id of the module
    """
    def __init__(self, id):
        """
        The constructor for the Data class
        Parameters:
            id (int): the id
        """
        self.mods = GameController.GetModList()
        self.id = id

    def update(self):
        if self.id > len(self.mods): self.id = 0
        elif self.id < 0: self.id = len(self.mods)
        self.selectedModule = self.mods[self.id]

def onLoad():
    """
    loads the mod, only ran when the game is started
    """
    return  "Success Loading"

def onUnload():
    """
    unloads the mod, only ran when the home button is pressed
    """
    return "Success Unloading"

def createModule(id):
    """
    creates a module

    Parameters:
        id (int): the id

    Returns:
        data: the new data variable
    """
    data = Data(id)
    data.result = "Created Template"
    GameController.SetChance("Plus Mode", -1)
    return data

def tick(data):
    """
    processes one tick

    Parameters:
        data (Data): the data variable

    Returns:
        data: the new data variable
    """
    return data

def bulkTick(data, amount):
    """
    processes multiple ticks

    Parameters:
        data (Data): the data variable
        amount (BigNumber): the amount of ticks to run

    Returns:
        data: the new data variable
    """
    return data

def destroyModule(data):
    """
    destroys the module currently not run

    Parameters:
        data (Data): the data variable

    Returns:
        data: the new data variable
    """
    return data

def prestige(data):
    """
    processes prestige

    Parameters:
        data (Data): the data variable

    Returns:
        data: the new data variable
    """
    return data

def loadSave(save, id):
    """
    loads a save

    Parameters:
        save (string): the save Data
        id (int): the id of the module

    Returns:
        data: the new data variable
    """
    data = createModule(id)
    return data

def saveData(data):
    """
    gets save data

    Parameters:
        data (Data): the data variable

    Returns:
        string: the save Data
    """
    result = ""
    return result

def nextClick(data):
    data.selected -= 1
    data.update()
    return data

def prevClick(data):
    data.selected -= 1
    data.update()
    return data

def enaTrue(data): return True