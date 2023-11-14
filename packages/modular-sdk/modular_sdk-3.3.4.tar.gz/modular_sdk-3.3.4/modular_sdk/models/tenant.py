from typing import Optional

from pynamodb.attributes import (UnicodeAttribute, ListAttribute, MapAttribute)
from pynamodb.indexes import AllProjection

from modular_sdk.commons.constants import ALLOWED_TENANT_PARENT_MAP_KEYS
from modular_sdk.models.base_meta import BaseMeta, TABLES_PREFIX
from modular_sdk.models.pynamodb_extension.base_model import M3BooleanAttribute, \
    BaseGSI
from modular_sdk.models.pynamodb_extension.base_role_access_model import \
    BaseRoleAccessModel
from modular_sdk.models.region import RegionAttr

CREDENTIALS_FORMAT_ERROR_PATTERN = 'Credentials was not fully registered ' \
                                   'for tenant {0}: {1} is absent'

TENANT_NAME = 'n'
MANAGEMENT_PARENT_ID = 'mpid'
DISPLAY_NAME = 'dn'
ACTIVATION_DATE = 'ad'

DNTL_NAME_KEY = 'dntl'
GENERAL_PROJECT_ID = 'acc'
GOOGLE_ACCOUNT_NUMBER = 'accN'
PRIMARY_CONTACTS = 'pc'
SECONDARY_CONTACTS = 'sc'
TENANT_MANAGER = 'tmc'
DEFAULT_INSTANCE_OWNER = 'do'
TENANT_CONTACT = 'ct'

REGIONS = 'r'

READ_ONLY = 'ro'
IS_ACTIVE = 'act'
CUSTOMER_NAME = 'ctmr'
CLOUD = 'c'
PARENT_MAP = 'pid'

MODULAR_TENANTS_TABLE_NAME = 'Tenants'


class Contacts(MapAttribute):
    primary_contacts = ListAttribute(attr_name=PRIMARY_CONTACTS, null=True)
    secondary_contacts = ListAttribute(attr_name=SECONDARY_CONTACTS, null=True)
    tenant_manager_contacts = ListAttribute(attr_name=TENANT_MANAGER,
                                            null=True)
    default_owner = UnicodeAttribute(attr_name=DEFAULT_INSTANCE_OWNER,
                                     null=True)


class DisplayNameToLowerCloudIndex(BaseGSI):
    """
    This class represents a Tenant display name + Cloud global secondary index
    """

    class Meta(BaseMeta):
        index_name = 'dntl-c-index'
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    display_name_to_lower = UnicodeAttribute(attr_name=DNTL_NAME_KEY,
                                             hash_key=True)
    cloud = UnicodeAttribute(attr_name=CLOUD, range_key=True)


class ProjectIndex(BaseGSI):
    """
    This class represents a Project global secondary index
    """

    class Meta(BaseMeta):
        index_name = 'ac-index'
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    project = UnicodeAttribute(attr_name=GENERAL_PROJECT_ID, hash_key=True)


class AccountNumberIndex(BaseGSI):
    """
    This class represents an Account Number global secondary index
    """

    class Meta(BaseMeta):
        index_name = F'{GOOGLE_ACCOUNT_NUMBER}-index'
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    account_number = UnicodeAttribute(attr_name=GOOGLE_ACCOUNT_NUMBER,
                                      hash_key=True)


class CustomerNameIndex(BaseGSI):
    class Meta(BaseMeta):
        index_name = f"{CUSTOMER_NAME}-index"
        read_capacity_units = 1
        write_capacity_units = 1
        projection = AllProjection()

    customer_name = UnicodeAttribute(hash_key=True, attr_name=CUSTOMER_NAME)


class Tenant(BaseRoleAccessModel):
    class Meta(BaseMeta):
        table_name = f'{TABLES_PREFIX}{MODULAR_TENANTS_TABLE_NAME}'

    name = UnicodeAttribute(hash_key=True, attr_name=TENANT_NAME)
    display_name = UnicodeAttribute(attr_name=DISPLAY_NAME)
    display_name_to_lower = UnicodeAttribute(attr_name=DNTL_NAME_KEY)
    read_only = M3BooleanAttribute(attr_name=READ_ONLY, null=True)
    is_active = M3BooleanAttribute(attr_name=IS_ACTIVE, null=True)
    customer_name = UnicodeAttribute(attr_name=CUSTOMER_NAME)
    cloud = UnicodeAttribute(attr_name=CLOUD)
    activation_date = UnicodeAttribute(attr_name=ACTIVATION_DATE, null=True)
    management_parent_id = UnicodeAttribute(attr_name=MANAGEMENT_PARENT_ID,
                                            null=True)
    project = UnicodeAttribute(attr_name=GENERAL_PROJECT_ID, null=True)
    regions = ListAttribute(of=RegionAttr, attr_name=REGIONS, default=list)
    contacts = Contacts(attr_name=TENANT_CONTACT, null=True)
    parent_map = MapAttribute(attr_name=PARENT_MAP, default=dict)
    account_number = UnicodeAttribute(attr_name=GOOGLE_ACCOUNT_NUMBER,
                                      null=True)

    customer_name_index = CustomerNameIndex()
    project_index = ProjectIndex()
    dntl_c_index = DisplayNameToLowerCloudIndex()
    accN_index = AccountNumberIndex()

    def get_parent_id(self, type_: str) -> Optional[str]:
        assert type_ in ALLOWED_TENANT_PARENT_MAP_KEYS
        if type_ in self.parent_map:
            return self.parent_map[type_]
        return
