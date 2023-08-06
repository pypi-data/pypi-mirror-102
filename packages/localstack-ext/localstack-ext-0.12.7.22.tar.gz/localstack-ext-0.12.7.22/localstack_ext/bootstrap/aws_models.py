from localstack.utils.aws import aws_models
haBlF=super
haBlk=None
haBlW=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  haBlF(LambdaLayer,self).__init__(arn)
  self.cwd=haBlk
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.haBlW.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,haBlW,env=haBlk):
  haBlF(RDSDatabase,self).__init__(haBlW,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,haBlW,env=haBlk):
  haBlF(RDSCluster,self).__init__(haBlW,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,haBlW,env=haBlk):
  haBlF(AppSyncAPI,self).__init__(haBlW,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,haBlW,env=haBlk):
  haBlF(AmplifyApp,self).__init__(haBlW,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,haBlW,env=haBlk):
  haBlF(ElastiCacheCluster,self).__init__(haBlW,env=env)
class TransferServer(BaseComponent):
 def __init__(self,haBlW,env=haBlk):
  haBlF(TransferServer,self).__init__(haBlW,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,haBlW,env=haBlk):
  haBlF(CloudFrontDistribution,self).__init__(haBlW,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,haBlW,env=haBlk):
  haBlF(CodeCommitRepository,self).__init__(haBlW,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
