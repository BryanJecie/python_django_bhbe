from django.shortcuts import render


def index(response):

    context = {"navbar": navBar("dashboard", False)}

    return render(response, "views/dashboard/index.html", {"context": context})


def navBar(parent, child):

    return {
        "parent": parent,
        "child": {
            "manage": True if child == "manage" else False,
            "new": True if child == "new" else False,
        },
    }
