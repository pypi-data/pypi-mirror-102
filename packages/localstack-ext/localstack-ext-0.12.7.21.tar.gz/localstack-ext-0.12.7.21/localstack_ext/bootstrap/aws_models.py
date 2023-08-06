from localstack.utils.aws import aws_models
agtsE=super
agtsR=None
agtsC=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  agtsE(LambdaLayer,self).__init__(arn)
  self.cwd=agtsR
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.agtsC.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,agtsC,env=agtsR):
  agtsE(RDSDatabase,self).__init__(agtsC,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,agtsC,env=agtsR):
  agtsE(RDSCluster,self).__init__(agtsC,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,agtsC,env=agtsR):
  agtsE(AppSyncAPI,self).__init__(agtsC,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,agtsC,env=agtsR):
  agtsE(AmplifyApp,self).__init__(agtsC,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,agtsC,env=agtsR):
  agtsE(ElastiCacheCluster,self).__init__(agtsC,env=env)
class TransferServer(BaseComponent):
 def __init__(self,agtsC,env=agtsR):
  agtsE(TransferServer,self).__init__(agtsC,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,agtsC,env=agtsR):
  agtsE(CloudFrontDistribution,self).__init__(agtsC,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,agtsC,env=agtsR):
  agtsE(CodeCommitRepository,self).__init__(agtsC,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
