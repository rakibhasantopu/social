from boot.controller.boot_static_controller import boot_static_controller
from pweb import PWebComponentRegister, PWebModuleDetails
from boot.controller.friend_media_controller import friend_media_controller
from boot.controller.member_controller import member_controller


class BootModule(PWebComponentRegister):

    def app_details(self) -> PWebModuleDetails:
        return PWebModuleDetails(system_name="boot", display_name="Python Web Boot")

    def run_on_cli_init(self, pweb_app, config):
        pass

    def run_on_start(self, pweb_app, config):
        pass

    def register_model(self, pweb_db):
        pass

    def register_controller(self, pweb_app):
        pweb_app.register_blueprint(friend_media_controller)
        pweb_app.register_blueprint(member_controller)
        pweb_app.register_blueprint(boot_static_controller)

