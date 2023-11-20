from pweb_orm import PwebModel, pweb_orm, Integer, LONGTEXT


class Comment(PwebModel):
    memberId = pweb_orm.Column("member_id", pweb_orm.BigInteger().with_variant(Integer, "sqlite"), pweb_orm.ForeignKey('member.id'), nullable=False)
    postId = pweb_orm.Column("post_id", pweb_orm.BigInteger().with_variant(Integer, "sqlite"), pweb_orm.ForeignKey('post.id'), nullable=False)
    image = pweb_orm.Column("image", pweb_orm.String(350))
    content = pweb_orm.Column("content", pweb_orm.Text().with_variant(LONGTEXT, "mysql"))
    likeCount = pweb_orm.Column("like_count", pweb_orm.Integer())
    visibility = pweb_orm.Column("visibility", pweb_orm.String(20))

    member = pweb_orm.relationship(
        "Member",
        lazy="joined",
        remote_side="Member.id",
        primaryjoin="and_(Comment.memberId==Member.id)", uselist=False)