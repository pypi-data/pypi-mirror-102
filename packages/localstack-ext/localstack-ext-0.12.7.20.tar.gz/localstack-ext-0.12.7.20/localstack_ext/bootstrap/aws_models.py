from localstack.utils.aws import aws_models
sIjRW=super
sIjRN=None
sIjRq=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  sIjRW(LambdaLayer,self).__init__(arn)
  self.cwd=sIjRN
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.sIjRq.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,sIjRq,env=sIjRN):
  sIjRW(RDSDatabase,self).__init__(sIjRq,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,sIjRq,env=sIjRN):
  sIjRW(RDSCluster,self).__init__(sIjRq,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,sIjRq,env=sIjRN):
  sIjRW(AppSyncAPI,self).__init__(sIjRq,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,sIjRq,env=sIjRN):
  sIjRW(AmplifyApp,self).__init__(sIjRq,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,sIjRq,env=sIjRN):
  sIjRW(ElastiCacheCluster,self).__init__(sIjRq,env=env)
class TransferServer(BaseComponent):
 def __init__(self,sIjRq,env=sIjRN):
  sIjRW(TransferServer,self).__init__(sIjRq,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,sIjRq,env=sIjRN):
  sIjRW(CloudFrontDistribution,self).__init__(sIjRq,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,sIjRq,env=sIjRN):
  sIjRW(CodeCommitRepository,self).__init__(sIjRq,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
