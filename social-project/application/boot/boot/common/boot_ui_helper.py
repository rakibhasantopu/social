from pweb_form_rest import PWebSSRUIHelper

from boot.service.quick_service import QuickService
from pweb_auth.security.pweb_ssr_auth import PWebSSRAuth
from pweb import url_for
from pweb_auth.service.operator_ssr_service import OperatorSSRService


class AuthSessionHelper:
    pweb_ssr_auth = PWebSSRAuth()
    operator_ssr_service = OperatorSSRService()
    quick_service = QuickService()

    @property
    def name(self):
        name = "Unknown User"
        if self.pweb_ssr_auth.get_auth_session().name:
            name = self.pweb_ssr_auth.get_auth_session().name
        return name

    @property
    def title(self):
        title = "I am social media person"
        if self.pweb_ssr_auth.get_auth_session().title:
            title = self.pweb_ssr_auth.get_auth_session().title
        return title

    def get_profile_photo(self, member=None):
        image_name = url_for('boot-static.static', filename='img/default-img.jpg')
        if not member:
            member = self.pweb_ssr_auth.get_auth_session()
        if member.profilePhoto:
            image_name = f"/assets/profile/{member.profilePhoto}"
        return image_name

    @property
    def profile_photo(self):
        return self.get_profile_photo()

    @property
    def post_count(self):
        member = self.operator_ssr_service.get_logged_in_operator()
        if member and member.totalPost:
            return member.totalPost
        return 0

    @property
    def recent_member(self):
        return self.quick_service.recent_member()


class BootUIHelper(PWebSSRUIHelper):

    def get_helper(self) -> dict:
        return {"auth": AuthSessionHelper()}
