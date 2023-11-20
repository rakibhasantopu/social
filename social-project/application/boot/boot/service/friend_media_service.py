from ppy_common import DataUtil
from pweb_form_rest import FileDataCRUD, ssr_ui_render
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD
from application.config.asset_config import AssetConfig
from boot.form.friend_media_form import CreatePostForm, CreateCommentForm
from boot.model.comment import Comment
from boot.model.post import Post
from pweb_auth.service.operator_ssr_service import OperatorSSRService
from pweb_orm import and_


class FriendMediaService:
    post_file_data_crud: FileDataCRUD = FileDataCRUD(model=Post)
    post_data_crud: FormDataCRUD = FormDataCRUD(model=Post)
    comment_data_crud: FormDataCRUD = FormDataCRUD(model=Comment)
    operator_ssr_service = OperatorSSRService()

    def create_post(self):
        form = CreatePostForm()
        if form.is_valid_data_submit():
            data = form.get_request_data()
            member = self.operator_ssr_service.get_logged_in_operator()
            data["memberId"] = member.id
            post = self.post_file_data_crud.get_model_by_upload_file_data(form, upload_path=AssetConfig.post, form_data=data)
            if post:
                if not member.totalPost:
                    member.totalPost = 0
                member.totalPost += 1
                member.save()
                params = {"post": post}
                return ssr_ui_render(view_name="friend-media/post", params=params)
        return ""

    def index(self):
        return self.post_data_crud.list(view_name="friend-media/index")

    def like_post(self, model_id: int):
        post = self.post_data_crud.get_by_id(model_id=model_id, exception=False)
        if not post:
            return ""
        if not post.likeCount:
            post.likeCount = 0
        post.likeCount += 1
        post.save()
        return self.post_data_crud.render("friend-media/snippet/like-comment-count", params={"post": post})

    def update_post(self):
        pass

    def delete_post(self):
        pass

    def get_post_comments(self, post_id):
        query = Comment.query.filter(and_(Comment.postId == post_id, Comment.isDeleted == False))
        return self.comment_data_crud.read_all(query=query)

    def create_comment(self):
        form = CreateCommentForm()
        comments = []
        if form.is_valid_data_submit():
            member = self.operator_ssr_service.get_logged_in_operator()
            data = form.get_request_data()
            data["memberId"] = member.id
            post_id = DataUtil.get_dict_value(data, "postId")
            self.comment_data_crud.save(data=data, request_dto=form)
            comments = self.get_post_comments(post_id=post_id)
            post = self.post_data_crud.get_by_id(model_id=post_id, exception=False)
            if post:
                if not post.commentCount:
                    post.commentCount = 0
                post.commentCount += 1
                post.save()
        else:
            return ""
        return self.post_data_crud.render("friend-media/snippet/comment", params={"comments": comments})

    def update_comment(self):
        pass

    def delete_comment(self):
        pass

    def get_top_post(self):
        pass
