from werkzeug.exceptions import BadRequest

from dora.store.models.settings.configuration_settings import SettingType


def settings_type_validator(setting_type: str):
    if setting_type == SettingType.INCIDENT_SETTING.value:
        return SettingType.INCIDENT_SETTING

    if setting_type == SettingType.EXCLUDED_PRS_SETTING.value:
        return SettingType.EXCLUDED_PRS_SETTING

    if setting_type == SettingType.INCIDENT_TYPES_SETTING.value:
        return SettingType.INCIDENT_TYPES_SETTING

    if setting_type == SettingType.INCIDENT_SOURCES_SETTING.value:
        return SettingType.INCIDENT_SOURCES_SETTING

    raise BadRequest(f"Invalid Setting Type: {setting_type}")
