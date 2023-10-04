import pygame

class Config:

    #default configs
    width=900
    height=900
    fps = 90

    max_cap= 7
    n_points = 800
    startingPoints = False


    #game configs
    updatePoints = False
    updateGrids = True
    drawPoints = True
    drawPointsLines = False
    showPointsLength = False
    showFps = True

    drawFunction = True
    pointsDraw = 2
    drawArea = 150


    #grid configs
    showGridPoints=False

    showBorders= True
    showBackground= False
    backgroundAlpha = 50

    #sidebar configs
    showSidebar = False
    sidebarAlpha = 190

    #font configs
    font = 'arial'
    title = 25
    subTitle = 20

    options = {
        'max_cap':max_cap
        ,'n_points':n_points
        ,'startingPoints':startingPoints
        # ,'updatePoints':updatePoints
        ,'updateGrids':updateGrids
        ,'drawPoints':drawPoints
        ,'drawPointsLines':drawPointsLines
        ,'showPointsLength':showPointsLength
        ,'showFps':showFps
        ,'drawFunction':drawFunction
        ,'pointsDraw':pointsDraw
        ,'drawArea':drawArea
        ,'showGridPoints':showGridPoints
        ,'showBorders':showBorders
        ,'showBackground':showBackground
        ,'showBackground':showBackground
    }