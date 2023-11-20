from pweb_orm import pweb_orm, LONGTEXT
from pweb_auth.model.operator_abc import OperatorAbc


class Member(OperatorAbc):
    title = pweb_orm.Column("title", pweb_orm.String(200))
    sex = pweb_orm.Column("sex", pweb_orm.String(20))
    dob = pweb_orm.Column("dob", pweb_orm.Date())
    totalPost = pweb_orm.Column("total_post", pweb_orm.Integer())
