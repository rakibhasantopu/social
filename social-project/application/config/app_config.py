from pweb import PWebAppConfig
from pweb_form_rest import PWebSSRUIHelper

from boot.common.boot_ui_helper import BootUIHelper
from boot.model.member import Member
from pweb_auth import AuthBase
from pweb_auth.model.operator_abc import OperatorAbc


class Config(PWebAppConfig):
    APP_NAME = "FriendNet"
    PORT: int = 1212
    CONNECT_MESSAGE: str = "Connect your Friends easily."
    ENABLE_REGISTRATION: bool = True
    REGISTRATION_DISABLE_MESSAGE: str = "Registration is disabled."
    DEVELOPED_BY: str = "BFE & RPI"
    DEVELOPED_BY_LINK: str = "https://github.com/rakibhasantopu"
    APP_VERSION: str = "v1.0.0"
    LOGIN_SUCCESS_END_POINT: str = "/"
    SYSTEM_AUTH_BASE: AuthBase = AuthBase.EMAIL

    OPERATOR_MODEL: OperatorAbc = Member
    SSR_UI_HELPER: PWebSSRUIHelper = BootUIHelper()
