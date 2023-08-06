from localstack.utils.aws import aws_models
zhLtj=super
zhLtT=None
zhLts=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  zhLtj(LambdaLayer,self).__init__(arn)
  self.cwd=zhLtT
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.zhLts.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,zhLts,env=zhLtT):
  zhLtj(RDSDatabase,self).__init__(zhLts,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,zhLts,env=zhLtT):
  zhLtj(RDSCluster,self).__init__(zhLts,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,zhLts,env=zhLtT):
  zhLtj(AppSyncAPI,self).__init__(zhLts,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,zhLts,env=zhLtT):
  zhLtj(AmplifyApp,self).__init__(zhLts,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,zhLts,env=zhLtT):
  zhLtj(ElastiCacheCluster,self).__init__(zhLts,env=env)
class TransferServer(BaseComponent):
 def __init__(self,zhLts,env=zhLtT):
  zhLtj(TransferServer,self).__init__(zhLts,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,zhLts,env=zhLtT):
  zhLtj(CloudFrontDistribution,self).__init__(zhLts,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,zhLts,env=zhLtT):
  zhLtj(CodeCommitRepository,self).__init__(zhLts,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
