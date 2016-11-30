import StreakClient as s

# Function to List all Boxes a user has access to
def listAllBoxes() :
    requestURL = "/boxes";
    data = s.sendGetRequest(requestURL)
    return data


# Function to list all boxes in a pipeline
def getAllBoxesFromPipeline(pipelineKey) :
    requestURL = str("/pipelines/"+pipelineKey+"/boxes")
    data = s.sendGetRequest(requestURL)
    return data


# Function to get a specific box
def getSpecificBox(boxKey) :
    requestURL = str("/boxes/"+boxKey)
    data = s.sendGetRequest(requestURL)
    return data


# Function to create a box
def createBox(pipelineKey, newBox) :
    inputData = {"name" : newBox}
    requestURL = str("/pipelines/"+pipelineKey+"/boxes")
    data = s.sendPutRequest(requestURL, inputData)
    return data


# Function to Delete Box
def deleteBox(boxKey) :
    requestURL = str("/boxes/"+boxKey)
    data = s.sendDeleteRequest(requestURL)
    return data


# Function to edit a box
def editBox(boxKey,boxName,boxNotes,stageKey) :
    inputData = {"name" : boxName, "notes" : boxNotes, "stageKey" : stageKey }
    requestURL = str("/boxes/"+boxKey)
    data = s.sendPostRequest(requestURL, inputData)
    return data

