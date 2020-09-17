from MoneyModel import *

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

#Adding a chart
from mesa.visualization.modules import ChartModule


def agent_portrayal(agent): #shows how agent will be represented in the grid
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}

    if agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal

#we instantiate a grid of 500px * 500px
grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

#Add a chart element to the server to appear under the grid
chart = ChartModule([{
                    "Label": "Gini",
                    "Color": "Black"}],
                    data_collector_name="datacollector")

server = ModularServer(
                    MoneyModel, #model class we are running
                    [grid, chart],     # a list of module objects to include in the visualisation
                    "Money Model", # title
                    {"N": 100, "width": 10,"height": 10} # inputs for the model itself
                    )


server.port = 8521 # default

server.launch()
#ctrl + c in terminal to terminate

