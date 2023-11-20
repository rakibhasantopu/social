PWeb.SN = (function () {

    return {
        createPost: function () {
            let form = jQuery("#create-post-modal-form")
            form.submit(function (event) {
                event.preventDefault();
                let data = new FormData(this);
                for (const value of data.entries()) {
                    if (value[0] === "image" && value[1].size === 0) {
                        data.delete("image")
                    }
                }
                PWeb.ajax.call({
                    data: data,
                    processData: false,
                    contentType: false,
                    url: PWeb.baseURL + "/create-post",
                    complete: function (content) {
                        if (content == "") {
                            PWeb.messageBox.showMessage(false, "Opps! Something went wrong.")
                        } else {
                            location.reload()
                        }
                    }
                })
            })
        },
        createComment: function () {
            let createComment = jQuery(".create-comment")
            createComment.submit(function (event) {
                let _this = jQuery(this)
                event.preventDefault();
                let data = new FormData(this);
                PWeb.ajax.call({
                    data: data,
                    dataType: "html",
                    processData: false,
                    contentType: false,
                    url: PWeb.baseURL + "/create-comment",
                    success: function (content) {
                        if (content == "") {
                            PWeb.messageBox.showMessage(false, "Opps! Something went wrong.")
                        } else {
                            _this.find(".comment-content").val("")
                            let postId = _this.attr("data-post")
                            let commentArea = jQuery("#post-" + postId + "-comment-list")
                            commentArea.html("")
                            commentArea.html(content)
                        }
                    }
                })
            })
        },
        likePost: function () {
            let likeButton = jQuery(".like-click")
            likeButton.click(function (event) {
                event.preventDefault();
                let _this = jQuery(this)
                let postId = _this.attr("data-post")
                PWeb.ajax.call({
                    method: "GET",
                    dataType: "html",
                    url: PWeb.baseURL + "/like-post/" + postId,
                    success: function (content) {
                        if (content == "") {
                            PWeb.messageBox.showMessage(false, "Invalid post")
                        } else {
                            let counterPanel = jQuery("#like-comment-count-" + postId)
                            counterPanel.html("")
                            counterPanel.html(content)
                        }
                    }
                })
            })
        },
        init: function () {
            PWeb.SN.createPost()
            PWeb.SN.likePost()
            PWeb.SN.createComment()
        }
    }

}());

jQuery(document).ready(function () {
    PWeb.SN.init();
});
