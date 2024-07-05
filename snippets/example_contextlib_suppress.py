import contextlib


# Bad
def call_service_which_is_allowed_to_fail():
    raise RuntimeError


try:
    call_service_which_is_allowed_to_fail()
except Exception:
    pass

# Better

with contextlib.suppress(RuntimeError):
    call_service_which_is_allowed_to_fail()
