import factory
from .project import Project
from .duplications import Duplications
from .projectbranches import ProjectBranches
from .projectanalyses import ProjectAnalyses
from .projectpullrequests import ProjectPullRequests
from .projectlinks import ProjectLinks
from .users import Users
from .metrics import Metrics
from .issues import Issues
from .componentstree import ComponentsTree
from .supportedProgramingLanguages import SupportedProgramingLanguages


class ProjectFactory(factory.Factory):
    
    class Meta:
        model = Project
        
    personal_access_token = None
    organization = None

class IssuesFactory(factory.Factory):
    
    class Meta:
        model = Issues

    personal_access_token = None
    organization = None

class DuplicationsFactory(factory.Factory):
    
    class Meta:
        model = Duplications

    personal_access_token = None
    organization = None

class SupportedPorgramimgLanguagesFactory(factory.Factory):
    
    class Meta:
        model = SupportedProgramingLanguages

    personal_access_token = None
    organization = None

class ComponentsTreeFactory(factory.Factory):
    
    class Meta:
        model = ComponentsTree

    personal_access_token = None
    organization = None



class ProjectBranchesFactory(factory.Factory):
    
    class Meta:
        model = ProjectBranches

    personal_access_token = None
    organization = None

class ProjectAnalysesFactory(factory.Factory):
    
    class Meta:
        model = ProjectAnalyses

    personal_access_token = None
    organization = None

class ProjectPullRequestsFactory(factory.Factory):
    
    class Meta:
        model = ProjectPullRequests

    personal_access_token = None
    organization = None

class ProjectLinksFactory(factory.Factory):
    
    class Meta:
        model = ProjectLinks

    personal_access_token = None
    organization = None

class UsersFactory(factory.Factory):
    
    class Meta:
        model = Users

    personal_access_token = None
    organization = None

class MetricsFactory(factory.Factory):
    
    class Meta:
        model = Metrics

    personal_access_token = None
    organization = None
