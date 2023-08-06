# This will put our "list_" function on the hub as "list"
# Func alias works around function names that shadow builtin python names
__func_alias__ = {"list_": "list"}


async def list_(hub, ctx):
    """"""
    return list(range(10))


async def get(hub, ctx, name: str):
    """"""


async def create(hub, ctx, name: str, **kwargs):
    """"""


async def delete(hub, ctx, name: str):
    """"""
