from pweb import Blueprint
from boot.service.friend_media_service import FriendMediaService

url_prefix = "/"
friend_media_controller = Blueprint(
    "friend_media_controller",
    __name__,
    url_prefix=url_prefix
)

friend_media_service = FriendMediaService()


@friend_media_controller.route("/", methods=['GET'])
def index():
    return friend_media_service.index()


@friend_media_controller.route("/create-post", methods=['POST'])
def create_post():
    return friend_media_service.create_post()


@friend_media_controller.route("/like-post/<int:id>", methods=['GET'])
def like_post(id: int):
    return friend_media_service.like_post(id)


@friend_media_controller.route("/create-comment", methods=['POST'])
def create_comment():
    return friend_media_service.create_comment()
