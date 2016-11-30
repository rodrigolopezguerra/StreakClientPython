import StreakClient as s

# List all the Fields in a pipeline
def listAllFields(pipelineKey) :
    requestURL =str("/pipelines/"+pipelineKey+"/fields")
    data = s.sendGetRequest(requestURL)
    return data;


# Specific Fields in a pipeline
def getSpecificField(pipelineKey, fieldKey) :
    requestURL = str("/pipelines/"+pipelineKey+"/fields/{"+fieldKey+"}")
    data = s.sendGetRequest(requestURL)
    return data


# Create Field in a pipeline
def createField(pipelineKey,fieldName,textInput) :
    inputData = { "name" : fieldName, "type" : textInput }
    requestURL = str("/pipelines/"+pipelineKey+"/fields")
    data = s.sendPutRequest(requestURL, inputData)
    return data


# Delete Field in Pipeline
def deleteField(pipelineKey, fieldKey) :
    requestURL = str("/pipelines/"+pipelineKey+"/fields/"+fieldKey)
    data = s.sendDeleteRequest(requestURL)
    return data;


# Edit a Field
def editField(pipelineKey, fieldKey, fieldName) :
    inputData = {"name":fieldName}
    requestURL = str("/pipelines/"+pipelineKey+"/fields/"+fieldKey)
    data = s.sendPostRequest(requestURL, inputData)
    return data;
