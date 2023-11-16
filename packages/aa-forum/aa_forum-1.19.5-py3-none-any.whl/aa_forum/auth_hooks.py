"""
Hook into AA
"""

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# AA Forum
from aa_forum import __title__, urls
from aa_forum.views.forum import unread_topics_count


class AaForumMenuItem(MenuItemHook):  # pylint: disable=too-few-public-methods
    """
    This class ensures only authorized users will see the menu entry
    """

    def __init__(self):
        # Setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            text=__title__,
            classes="fas fa-comments fa-fw",
            url_name="aa_forum:forum_index",
            navactive=["aa_forum:"],
        )

    def render(self, request):
        """
        Check if the user has the permission to view this app

        :param request:
        :return:
        """

        if request.user.has_perm(perm="aa_forum.basic_access"):
            count_unread_topics = unread_topics_count(request=request)

            self.count = (
                count_unread_topics
                if count_unread_topics and count_unread_topics > 0
                else None
            )

            return MenuItemHook.render(self, request=request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """
    Register our menu item

    :return:
    """

    return AaForumMenuItem()


@hooks.register("url_hook")
def register_urls():
    """
    Register our base url

    :return:
    """

    return UrlHook(urls=urls, namespace="aa_forum", base_url=r"^forum/")
