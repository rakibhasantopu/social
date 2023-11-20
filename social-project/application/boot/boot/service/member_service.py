from flask import flash
from pweb import url_for, redirect
from pweb_form_rest import FileDataCRUD, ssr_ui_render
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD
from application.config.asset_config import AssetConfig
from boot.form.member_form import UploadProfileForm, MemberEmailBasedForm, MemberUsernameBasedForm
from boot.model.member import Member
from pweb_auth import PWebAuthConfig, AuthBase
from pweb_auth.form_dto.pweb_auth_dto import ChangePasswordDefaultDTO
from pweb_auth.service.operator_ssr_service import OperatorSSRService


class MemberService:
    file_data_crud = FileDataCRUD(model=Member)
    operator_ssr_service = OperatorSSRService()
    form_data_crud: FormDataCRUD = FormDataCRUD(model=Member)

    def upload_profile_photo(self):
        member = self.operator_ssr_service.get_logged_in_operator()
        override_name = {"profilePhoto": f"profile-{member.uuid}"}
        response = self.file_data_crud.update_upload_file_data(request_dto=UploadProfileForm(), upload_path=AssetConfig.profile, existing_model=member, override_names=override_name)
        self.operator_ssr_service.update_session_data(member)
        return response

    def profile(self):
        params = {
            "member": self.operator_ssr_service.get_logged_in_operator(),
            "auth_base": PWebAuthConfig.SYSTEM_AUTH_BASE.name
        }
        form = ChangePasswordDefaultDTO()
        return ssr_ui_render(view_name="member/profile", params=params, form=form)

    def edit_profile(self):
        form = MemberEmailBasedForm()
        auth_base = PWebAuthConfig.SYSTEM_AUTH_BASE
        if auth_base == AuthBase.USERNAME:
            form = MemberUsernameBasedForm()
        params = {"auth_base": auth_base.name}
        if form.is_valid_data_submit():
            member = self.operator_ssr_service.get_logged_in_operator()
            data = self.operator_ssr_service.check_unique(form=form, model_id=member.id)
            if data:
                member = self.form_data_crud.edit(model_id=member.id, data=data, request_dto=form, existing_model=member)
                if member:
                    flash("Successfully Updated", "success")
                    self.operator_ssr_service.update_session_data(member)
                    return redirect(url_for("member_controller.profile"))
            flash("Unable to update profile", "error")
        elif form.is_get_data():
            member = self.operator_ssr_service.get_logged_in_operator()
            form.set_model_value(member)
        return self.form_data_crud.render(view_name="member/edit-profile", params=params, form=form)

    def change_password(self):
        return self.operator_ssr_service.change_password(view_name="member/profile", success_redirect=url_for("member_controller.profile"))
