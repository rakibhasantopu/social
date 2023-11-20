from pweb_orm import PwebModel, pweb_orm, Integer, LONGTEXT


class Post(PwebModel):
    memberId = pweb_orm.Column("member_id", pweb_orm.BigInteger().with_variant(Integer, "sqlite"), pweb_orm.ForeignKey('member.id'), nullable=False)
    image = pweb_orm.Column("image", pweb_orm.String(350))
    content = pweb_orm.Column("content", pweb_orm.Text().with_variant(LONGTEXT, "mysql"))
    likeCount = pweb_orm.Column("like_count", pweb_orm.Integer())
    commentCount = pweb_orm.Column("comment_count", pweb_orm.Integer())
    visibility = pweb_orm.Column("visibility", pweb_orm.String(20))
    visitCount = pweb_orm.Column("visit_count", pweb_orm.Integer())

    member = pweb_orm.relationship(
        "Member",
        lazy="joined",
        remote_side="Member.id",
        primaryjoin="and_(Post.memberId==Member.id)", uselist=False)

    comment = pweb_orm.relationship(
        "Comment",
        lazy="joined",
        viewonly=True,
        remote_side="Comment.postId",
        primaryjoin="and_(Post.id==Comment.postId)")
