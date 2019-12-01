from django.contrib import auth


def create_args_with_username(func):
    def a_wrapper_accepting_arguments(request):  # аргументы прибывают отсюда
        args = {'username': auth.get_user(request).username}
        return func(request, args)
    return a_wrapper_accepting_arguments
