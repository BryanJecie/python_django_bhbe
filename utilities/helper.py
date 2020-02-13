def onLoad():

    return "load"


def navigation(parent, childs):
    items = []
    for child in childs:
        if isinstance(child, list):
            for value in child:
                items.append(value)
        else:
            items.append(child)

    # resp = items

    return {"parent": parent, "child": items}


def navBar(parent, child):

    return {
        "parent": parent,
        "child": {
            "manage": True if child == "manage" else False,
            "new": True if child == "new" else False,
        },
    }

