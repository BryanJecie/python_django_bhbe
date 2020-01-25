def onLoad():

    return "load"


def navBar(parent, child):

    return {
        "parent": parent,
        "child": {
            "manage": True if child == "manage" else False,
            "new": True if child == "new" else False,
        },
    }
