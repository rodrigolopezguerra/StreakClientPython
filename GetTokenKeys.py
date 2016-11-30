import StreakClient as s
import PipelineMethods as p
import BoxMethods as b
import StageMethods as m
import FieldMethods as f
import json

# The pipeline, stage and field access require their individual keys.
# This Class code aims at extracting each of the individual keys so to be used in method classes.

errorMessage = "Sorry! Not Found"

def getPipelineKey(nameOfThePipeline) :
    userPipelineKey = ""
    userPipelines = p.getUserPipelines()
    for pipeline in userPipelines :
        if(unicode.lower(pipeline['name']) == str.lower(nameOfThePipeline)) :
            userPipelineKey = pipeline['pipelineKey']
    if userPipelineKey :
        return userPipelineKey
    else :
        return errorMessage



def getBoxKey(nameOfThePipeline, nameOfTheBox) :
    userPipelineKey = getPipelineKey(nameOfThePipeline);
    userBoxKey = ""
    userBoxes = b.getAllBoxesFromPipeline(userPipelineKey)
    for userBox in userBoxes :
        if(unicode.lower(userBox['name']) == str.lower(nameOfTheBox)) :
            userBoxKey = userBox['boxKey']
    if userBoxKey :
        return userBoxKey
    else :
        return errorMessage



def getStageKey(nameOfThePipeline, nameOfTheStage) :
    # Seems this one is a bit tight.
    userPipelineKey = getPipelineKey(nameOfThePipeline)
    userStageKey = ""
    userStages = m.listAllStages(userPipelineKey)
    counter=len(userStages)
    while(counter!=0) :
        if(unicode.lower(userStages[(counter+5000)]['name']) == str.lower(nameOfTheStage)) :
            userStageKey = userStages[(counter+5000)]['key']
        counter = counter-1
  	if userStageKey :
		return userStageKey
    else :
		return errorMessage


def getFieldKey(nameOfThePipeline, nameOfTheField) :
    userPipelineKey = getPipelineKey(nameOfThePipeline)
    userFieldKey = ""
    userFields = f.listAllFields(userPipelineKey)
    for userField in userFields :
        if(unicode.lower(userField['name']) == str.lower(nameOfTheField)) :
            userFieldKey = userField['key']
	if userFieldKey :
		return userFieldKey
    else :
		return errorMessage

