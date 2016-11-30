import PipelineMethods as p
import GetTokenKeys as g
import BoxMethods as b
import StageMethods as s

#######################
# PIPELINE TEST
#######################
# create a pipeline
p.createPipeline('python pipeline 2','this is a python pipeline')

# edit a pipeline
pk = g.getPipelineKey('python pipeline')
r = p.editPipeline('new python pipeline 3','new description for python pipeline', pk)

#user pipelines
#print p.getUserPipelines()

# delete
# p.deletePipeline(pk)

s.createStage(pk,'stage1')
s.createStage(pk,'stage2')

#######################
# BOX TEST
#######################
# create a box
a = b.createBox(pk,'box python')
print a
# list all
# print b.listAllBoxes()

# delete box
bk = g.getBoxKey('new python pipeline 3','box python')
print bk
#b.deleteBox(bk)

#p.deletePipeline(pk)