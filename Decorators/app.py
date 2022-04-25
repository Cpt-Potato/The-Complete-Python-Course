from functools import wraps


def access_control(access_level: int):
    def my_decorator(func):
        @wraps(func)
        def secure_func(*args, **kwargs):
            if get_current_user_role() <= access_level:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have the proper access level.")

        return secure_func

    return my_decorator


def get_current_user_role() -> int:
    # return the current user's role, represented by an int
    # for example, 0 - admin, 1 - user, 2 - guest
    return 0
