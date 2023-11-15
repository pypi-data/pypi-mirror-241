from dataclasses import dataclass
from typing import Any

from flask import render_template, g

from freeplay_server.web_support import json_support


@dataclass
class ProjectInfo:
    name: str
    id: str


@dataclass
class UserInfo:
    email_address: str


def render_react(component: str, title: str,  **data: Any) -> str:
    # Use info classes!
    globals={
        "all_projects": [ProjectInfo(project.name, project.id) for project in g.get('all_projects', [])],
        "user": UserInfo(g.session_user.email_address),
    }
    if g.get('project') and g.project.name and g.project.id:
        globals["project"] = ProjectInfo(g.project.name, g.project.id)
    data = {"globals": globals, **data}
    
    return render_template(
        'component.html',
        component=component,
        title=title,
        json_data=json_support.as_str(data),
    )
