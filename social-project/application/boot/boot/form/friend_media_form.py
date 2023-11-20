from pweb_form_rest import PWebForm, fields, FileField

from boot.model.comment import Comment
from boot.model.post import Post


class PostDetails(PWebForm):
    member = fields.String(dump_only=True)
    image = fields.String(dump_only=True)
    content = fields.String(dump_only=True)
    likeCount = fields.Integer(dump_only=True)
    commentCount = fields.Integer(dump_only=True)
    visitCount = fields.Integer(dump_only=True)
    visibility = fields.String(dump_only=True)


class CreatePostForm(PWebForm):
    content = fields.String(allow_none=True)
    memberId = fields.Integer(allow_none=True)
    visibility = fields.String(allow_none=True)
    image = FileField(allow_none=True).set_allowed_extension(["jpg", "png", "jpeg"])

    class Meta:
        model = Post
        load_instance = True


class UpdatePostForm(PWebForm):
    visibility = fields.String(allow_none=True)
    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)
    content = fields.String(allow_none=True)
    image = FileField(allow_none=True).set_allowed_extension(["jpg", "png", "jpeg"])

    class Meta:
        model = Post
        load_instance = True


class CommentDetails(PWebForm):
    content = fields.String(dump_only=True)
    image = fields.String(dump_only=True)


class CreateCommentForm(PWebForm):
    content = fields.String(allow_none=True)
    postId = fields.String(required=True, error_messages={"required": "Please give post"})
    memberId = fields.Integer(allow_none=True)
    image = FileField(allow_none=True).set_allowed_extension(["jpg", "png", "jpeg"])

    class Meta:
        model = Comment
        load_instance = True


class UpdateCommentForm(PWebForm):
    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)
    content = fields.String(required=True, error_messages={"required": "Please enter content"})
    image = FileField(allow_none=True).set_allowed_extension(["jpg", "png", "jpeg"])

    class Meta:
        model = Comment
        load_instance = True
