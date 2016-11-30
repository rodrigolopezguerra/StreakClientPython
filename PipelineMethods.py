import StreakClient as s

# Will fetch the current user with the input API Key
def getCurrentUser() :
    requestURL = str("/users/me")
    data = s.sendGetRequest(requestURL)
    return data


# Get all the pipelines for that user
def getUserPipelines() :
    requestURL = "/pipelines"
    data = s.sendGetRequest(requestURL)
    return data

# Get Specific pipeline out of the all the pipelines
def getSpecificPipeline(pipelineKey) :
    requestURL = "/pipelines/"+pipelineKey
    data = s.sendGetRequest(requestURL)
    return data


# Create a Pipeline based on user inputs
def createPipeline(name,description) :
    inputData = {"name" : name, "description" : description}
    requestURL = "/pipelines";
    data = s.sendPutRequest(requestURL, inputData)
    return data


# Delete a Pipeline of the user
def deletePipeline(pipelineKey) :
    requestURL = "/pipelines/"+pipelineKey
    data = s.sendDeleteRequest(requestURL)
    return data


# Function to edit a Pipeline
def editPipeline(newName, newDescription, pipelineKey) :
    inputData = {"name" : newName, "description" : newDescription }
    requestURL = "/pipelines/"+pipelineKey
    data = s.sendPostRequest(requestURL, inputData)
    return data
