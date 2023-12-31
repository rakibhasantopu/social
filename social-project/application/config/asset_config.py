from application.config.app_config import Config
from ppy_file_text import FileUtil


class AssetConfig:
    profile = FileUtil.join_path(Config.UPLOADED_STATIC_RESOURCES, "profile")
    post = FileUtil.join_path(Config.UPLOADED_STATIC_RESOURCES, "post")
    comment = FileUtil.join_path(Config.UPLOADED_STATIC_RESOURCES, "comment")
