import StreakClient as s

# List all the stages in a pipeline
def listAllStages(pipelineKey) :
    requestURL = str("/pipelines/"+pipelineKey+"/stages")
    data = s.sendGetRequest(requestURL)
    return data


# Specific Stages in a pipeline
def getSpecificStage(pipelineKey, stageKey) :
    requestURL = str("/pipelines/"+pipelineKey+"/stages/".stageKey)
    data = s.sendGetRequest(requestURL)
    return data


# Create Stage in a pipeline
def createStage(pipelineKey,stageName) :
    inputData = {"name" : stageName}
    requestURL = str("/pipelines/"+pipelineKey+"/stages")
    data = s.sendPutRequest(requestURL,inputData)
    return data


# Delete Stage in Pipeline
def deleteStage(pipelineKey, stageKey) :
    requestURL = str("/pipelines/"+pipelineKey+"/stages/"+stageKey)
    data = s.sendDeleteRequest(requestURL)
    return data


# Edit a Pipeline
def editStage(pipelineKey, stageKey, stageName) :
    inputData = {"name" : stageName}
    requestURL = str("/pipelines/"+pipelineKey+"/stages/"+stageKey)
    data = s.sendPostRequest(requestURL, inputData)
    return data