from classes.color4 import color4
from classes.udim2 import udim2
from gui.instance import instance

GUI_DEFAULT_PROPERTIES = {
    "size": lambda: udim2.fromOffset(150, 50),
    "position": lambda: udim2.fromOffset(0, 0),
    "color": lambda: color4(0, 1, 0),
    "backgroundColor": lambda: color4(1, 1, 0),
    "borderColor": lambda: color4(1, 0, 1),
    "borderRadius": lambda: 0,
    "dropShadowColor": lambda: color4(.7, .7, .7),
    "dropShadowRadius": lambda: 10
}

GUI_PROPERTY_MAP = {
    "guiObject": ["size", "position", "backgroundColor",
        "borderColor", "dropShadowColor", "dropShadowRadius"
    ]
}

def LoadDefaultGuiProperties(guiType: str, guiObject: instance):
    if GUI_PROPERTY_MAP[guiType]:
        for propKey in GUI_PROPERTY_MAP[guiType]:
            if propKey in GUI_DEFAULT_PROPERTIES:
                guiObject[propKey] = GUI_DEFAULT_PROPERTIES[propKey]()
            else:
                raise Exception(f"property {propKey} is not a valid property in the Default Properties map!")

    else:
        raise Exception(f"guiType {guiType} is not a valid type in the property map!")
