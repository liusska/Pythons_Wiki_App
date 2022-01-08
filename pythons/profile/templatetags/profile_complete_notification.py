from django.template import Library
from pythons.profile.models import Profile

register = Library()


@register.inclusion_tag('tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    is_complete = True
    if context.request.user.id:
        profile = Profile.objects.get(pk=user_id)
        is_complete = profile.is_complete
    return {
        'is_complete': is_complete,
    }
