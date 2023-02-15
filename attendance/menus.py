from django.urls import reverse

from simple_menu import Menu, MenuItem


def profile_title(request):
    """Return a personalized title for our profile menu item
    """
    # we don't need to check if the user is authenticated because our menu
    # item will have a check that does that for us
    name = request.user.get_full_name() or request.user

    return f"{name}'s Profile"



# this item will be shown to users who are not logged in
Menu.add_item("user", MenuItem("Sign in",
                               reverse('account_login'),
                               icon='box-arrow-in-right',
                               check=lambda r: not r.user.is_authenticated))

# this will only be shown to logged in users and also demonstrates how to use
# a callable for the title to return a customized title for each request


# this only shows to superusers
Menu.add_item("user", MenuItem("Create Occupant°",
                               reverse("account_login"),
                               icon='incognito',
                               check=lambda r: r.user.is_superuser))
Menu.add_item("user", MenuItem(profile_title,
                               reverse('account_logout'),
                               icon='person-circle',
                               check=lambda r: r.user.is_authenticated))

Menu.add_item("user", MenuItem("Sign out",
                               reverse('account_logout'),
                               icon='box-arrow-right',
                               check=lambda r: r.user.is_authenticated))
