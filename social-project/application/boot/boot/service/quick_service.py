from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD
from boot.model.member import Member


class QuickService:
    form_data_crud: FormDataCRUD = FormDataCRUD(model=Member)

    def recent_member(self):
        return self.form_data_crud.read_all(item_per_page=5)
