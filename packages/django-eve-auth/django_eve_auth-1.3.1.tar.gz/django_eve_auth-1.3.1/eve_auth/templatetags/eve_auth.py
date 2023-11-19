"""Template tags for Eve Auth."""

from django import template

from eve_auth import app_settings
from eve_auth.models import UserEveCharacter

register = template.Library()


@register.inclusion_tag("eve_auth/user_icon.html")
def user_icon(user, size=None) -> str:
    """Render an icon for the given user with his/her Eve portrait."""
    if not size:
        size = app_settings.EVE_AUTH_USER_ICON_DEFAULT_SIZE
    size = int(size)
    if size <= 32:
        portrait_size = 32
    elif size <= 64:
        portrait_size = 64
    elif size <= 128:
        portrait_size = 128
    elif size <= 256:
        portrait_size = 256
    elif size <= 512:
        portrait_size = 512
    else:
        portrait_size = 1024
    try:
        url = user.eve_character.character_portrait_url(size=portrait_size)
        alt = user.eve_character.character_name
    except AttributeError:
        url = UserEveCharacter.generic_character_portrait_url(1, size=portrait_size)
        try:
            alt = user.username
        except AttributeError:
            alt = ""
    return {"url": url, "alt": alt, "size": size}
