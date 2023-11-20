from pweb import Blueprint
from boot.service.member_service import MemberService

url_prefix = "/member"
member_controller = Blueprint(
    "member_controller",
    __name__,
    url_prefix=url_prefix
)

member_service = MemberService()


@member_controller.route("/profile", methods=['GET'])
def profile():
    return member_service.profile()


@member_controller.route("/edit-profile", methods=['GET', 'POST'])
def edit_profile():
    return member_service.edit_profile()


@member_controller.route("/upload-profile-photo", methods=['POST'])
def upload_profile_photo():
    return member_service.upload_profile_photo()


@member_controller.route("/change-password", methods=['POST', 'GET'])
def change_password():
    return member_service.change_password()
