# Imports
from consolemenu import *
from consolemenu.items import *
import Generator as Generator

GENERATOR = Generator.csvGenerator()

# -------------------------------------------------------------------------------------------------


def mainMenu():
    menu = ConsoleMenu("CSV Synthetic Data Generator", "Select an option")

    item_1 = FunctionItem("Generate CSV", menuGenCSV)
    item_2 = FunctionItem("Set columns", menuColumSelect)
    item_3 = FunctionItem("Assign columns", menuColumAssign)

    menu.append_item(item_1)
    menu.append_item(item_2)
    menu.append_item(item_3)

    menu.show()
# -------------------------------------------------------------------------------------------------


def menuGenCSV():
    menu = ConsoleMenu("CSV Synthetic Data Generator",
                       "Generate file", exit_option_text="Back")

    menu_item = MenuItem("Menu Item")

    menu.append_item(menu_item)

    menu.show()
# -------------------------------------------------------------------------------------------------


def menuColumSelect():
    menu = ConsoleMenu("CSV Synthetic Data Generator",
                       "Selected columns:\n- "+"\n- ".join(GENERATOR.COLUMNS), exit_option_text="Back")

    function_item_1 = FunctionItem("Add Column", addColumn)
    function_item_2 = FunctionItem("Remove Column", deleteColumn)

    menu.append_item(function_item_1)
    menu.append_item(function_item_2)

    menu.show()
# -------------------------------------------------------------------------------------------------


def menuColumAssign():
    menu = ConsoleMenu("CSV Synthetic Data Generator",
                       "Assign columns to data file", exit_option_text="Back")

    for i in range(0, len(GENERATOR.COLUMNS)):
        if(i < len(GENERATOR.FILES)):
            function_item = FunctionItem(
                GENERATOR.COLUMNS[i] + " - " + GENERATOR.FILES[i], setFileForColumn, [i])
        else:
            function_item = FunctionItem(
                GENERATOR.COLUMNS[i] + " - NONE", setFileForColumn, [i])
        menu.append_item(function_item)

    menu.show()
# -------------------------------------------------------------------------------------------------


def addColumn():
    newColumn = input("Enter column name: ")
    GENERATOR.COLUMNS.append(newColumn)
    GENERATOR.FILES.append("NONE")
# -------------------------------------------------------------------------------------------------


def deleteColumn():
    removeColumn = input("Enter column name: ")
    index = GENERATOR.COLUMNS.index(removeColumn)
    GENERATOR.COLUMNS.remove(removeColumn)
    GENERATOR.FILES.remove(GENERATOR.FILES[index])
# -------------------------------------------------------------------------------------------------


def setFileForColumn(index):
    filePath = input("Enter filename (File must be in 'Data' folder): ")
    if(index < len(GENERATOR.FILES)):
        GENERATOR.FILES[index] = filePath
    else:
        GENERATOR.FILES.append(filePath)
# -------------------------------------------------------------------------------------------------


mainMenu()
