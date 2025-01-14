# Code generated by Lark OpenAPI.

from typing import Any, Optional, Union, Dict, List, Set, IO, Callable, Type
from lark_oapi.core.construct import init
from .profile_setting_employment_basic_info import ProfileSettingEmploymentBasicInfo
from .profile_setting_probation_info import ProfileSettingProbationInfo
from .profile_setting_employment_record import ProfileSettingEmploymentRecord
from .profile_setting_emp_contract_record import ProfileSettingEmpContractRecord
from .profile_setting_custom_group import ProfileSettingCustomGroup


class ProfileSettingEmploymentInfo(object):
    _types = {
        "basic_info": ProfileSettingEmploymentBasicInfo,
        "probation_info": ProfileSettingProbationInfo,
        "employment_record": ProfileSettingEmploymentRecord,
        "emp_contract_record": ProfileSettingEmpContractRecord,
        "custom_groups": List[ProfileSettingCustomGroup],
    }

    def __init__(self, d=None):
        self.basic_info: Optional[ProfileSettingEmploymentBasicInfo] = None
        self.probation_info: Optional[ProfileSettingProbationInfo] = None
        self.employment_record: Optional[ProfileSettingEmploymentRecord] = None
        self.emp_contract_record: Optional[ProfileSettingEmpContractRecord] = None
        self.custom_groups: Optional[List[ProfileSettingCustomGroup]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProfileSettingEmploymentInfoBuilder":
        return ProfileSettingEmploymentInfoBuilder()


class ProfileSettingEmploymentInfoBuilder(object):
    def __init__(self) -> None:
        self._profile_setting_employment_info = ProfileSettingEmploymentInfo()

    def basic_info(self, basic_info: ProfileSettingEmploymentBasicInfo) -> "ProfileSettingEmploymentInfoBuilder":
        self._profile_setting_employment_info.basic_info = basic_info
        return self

    def probation_info(self, probation_info: ProfileSettingProbationInfo) -> "ProfileSettingEmploymentInfoBuilder":
        self._profile_setting_employment_info.probation_info = probation_info
        return self

    def employment_record(self,
                          employment_record: ProfileSettingEmploymentRecord) -> "ProfileSettingEmploymentInfoBuilder":
        self._profile_setting_employment_info.employment_record = employment_record
        return self

    def emp_contract_record(self,
                            emp_contract_record: ProfileSettingEmpContractRecord) -> "ProfileSettingEmploymentInfoBuilder":
        self._profile_setting_employment_info.emp_contract_record = emp_contract_record
        return self

    def custom_groups(self, custom_groups: List[ProfileSettingCustomGroup]) -> "ProfileSettingEmploymentInfoBuilder":
        self._profile_setting_employment_info.custom_groups = custom_groups
        return self

    def build(self) -> "ProfileSettingEmploymentInfo":
        return self._profile_setting_employment_info
