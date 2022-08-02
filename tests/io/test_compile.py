'''
test compile
'''
import pytest
from tenable.io import TenableIO
from tenable.io.access_groups import AccessGroupsIterator, AccessGroupsAPI
from tenable.io.access_groups_v2 import AccessGroupsIteratorV2, AccessGroupsV2API
from tenable.io.agent_config import AgentConfigAPI
from tenable.io.agent_exclusions import AgentExclusionsAPI
from tenable.io.agent_groups import AgentGroupsAPI
from tenable.io.agents import AgentsAPI, AgentsIterator
from tenable.io.assets import AssetsAPI
from tenable.io.audit_log import AuditLogAPI
from tenable.io.base import TIOEndpoint, TIOIterator
from tenable.io.credentials import CredentialsIterator, CredentialsAPI
from tenable.io.editor import EditorAPI
from tenable.io.exclusions import ExclusionsAPI
from tenable.io.exports import ExportsIterator, ExportsAPI
from tenable.io.files import FileAPI
from tenable.io.filters import FiltersAPI
from tenable.io.folders import FoldersAPI
from tenable.io.groups import GroupsAPI
from tenable.io.networks import NetworksIterator, NetworksAPI
from tenable.io.permissions import PermissionsAPI
from tenable.io.plugins import PluginsAPI, PluginIterator
from tenable.io.policies import PoliciesAPI
from tenable.io.scanner_groups import ScannerGroupsAPI
from tenable.io.scanners import ScannersAPI
from tenable.io.scans import ScansAPI, ScanHistoryIterator
from tenable.io.server import ServerAPI
from tenable.io.session import SessionAPI
from tenable.io.tags import TagsAPI, TagsIterator
from tenable.io.target_groups import TargetGroupsAPI
from tenable.io.users import UsersAPI
from tenable.io.workbenches import WorkbenchesAPI
#from tests.io.conftest import api
from tenable.errors import UnexpectedValueError, AuthenticationWarning


def test_io_compile(api):
    '''
    test to raise the exception when value for api keys is not passed correctly
    '''
    try:
        TenableIO()
        AccessGroupsIterator(api)
        AccessGroupsAPI(api)
        AccessGroupsIteratorV2(api)
        AccessGroupsV2API(api)
        AgentConfigAPI(api)
        AgentExclusionsAPI(api)
        AgentGroupsAPI(api)
        AgentsAPI(api)
        AgentsIterator(api)
        AssetsAPI(api)
        AuditLogAPI(api)
        TIOIterator(api)
        TIOEndpoint(api)
        CredentialsAPI(api)
        CredentialsIterator(api)
        EditorAPI(api)
        ExclusionsAPI(api)
        ExportsAPI(api)
        ExportsIterator(api)
        FileAPI(api)
        FiltersAPI(api)
        FoldersAPI(api)
        GroupsAPI(api)
        NetworksAPI(api)
        NetworksIterator(api)
        PermissionsAPI(api)
        PluginsAPI(api)
        PluginIterator(api)
        PoliciesAPI(api)
        ScannerGroupsAPI(api)
        ScannersAPI(api)
        ScansAPI(api)
        ScanHistoryIterator(api)
        ServerAPI(api)
        SessionAPI(api)
        TagsAPI(api)
        TagsIterator(api)
        TargetGroupsAPI(api)
        UsersAPI(api)
        WorkbenchesAPI(api)
    except NameError as error:
        print(f'\n The following name error exists: {error}')
        pytest.raises(NameError)
    except UnexpectedValueError as error:
        print(f'\n The following value error exists: {error}')
        pytest.raises(UnexpectedValueError)
