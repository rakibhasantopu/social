from pweb_form_rest import ValidationError, validates_schema, PWebOrmDTO, FileField, BaseEnum, EnumField
from pweb import PWebForm, fields
from pweb_orm import PWebORMUtil
from boot.model.member import Member


class Sex(BaseEnum):
    Male = "Male"
    Female = "Female"
    Not_Specified = "Not Specified"


class MemberForm(PWebForm):
    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    title = fields.String(allow_none=True)
    sex = EnumField(Sex, allow_none=True, placeholder="Select Sex")
    dob = fields.Date(allow_none=True)

    @validates_schema
    def validates_schema(self, data, **kwargs):
        PWebORMUtil.enum_to_string(data, "sex")


class MemberUsernameBasedForm(MemberForm):
    username = fields.String(required=True, error_messages={"required": "Please enter username"})

    class Meta:
        model = Member
        load_instance = True


class MemberEmailBasedForm(MemberForm):
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})

    class Meta:
        model = Member
        load_instance = True


class ChangePasswordForm(PWebForm):
    currentPassword = fields.String(required=True, error_messages={"required": "Please enter current password."}, type="password")
    newPassword = fields.String(required=True, error_messages={"required": "Please enter new password."}, type="password")
    confirmPassword = fields.String(required=True, error_messages={"required": "Please enter confirm password."}, type="password")

    @validates_schema
    def validate_schema(self, data, **kwargs):
        if data["newPassword"] != data["confirmPassword"]:
            raise ValidationError("New password & confirm password not matched!", "confirmPassword")


class UploadCoverForm(PWebOrmDTO):
    coverPhoto = FileField(required=True, error_messages={"required": "Please upload file."}).set_allowed_extension(["jpg", "png", "jpeg"])

    class Meta:
        model = Member
        load_instance = True


class UploadProfileForm(PWebOrmDTO):
    profilePhoto = FileField(required=True, error_messages={"required": "Please upload file."}).set_allowed_extension(["jpg", "png", "jpeg"])

    class Meta:
        model = Member
        load_instance = True
