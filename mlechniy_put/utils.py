from rest_framework.response import Response


def response_create(instance):
    """
    Return uuid of new created entity
    """
    return Response(data={"uuid": instance.uuid}, status=201)


def response_update_delete():
    """
    Return status true on successful manipulation under entity
    """
    return Response(data={"status": True}, status=200)
