from argparse import Namespace

from .data import *


def handle_list(
    args: Namespace,
    user_id: int,
    group_id: int,
    is_admin: bool,
    is_superuser: bool,
) -> str:
    todo_list = get_todo_list(group_id=group_id)
    if todo_list is None:
        return "本群暂无待办事项列表!"
    return "\n".join(
        f"[{'o' if todo_list[job]['enable'] else 'x'}] {job}" for job in todo_list
    )


def handle_add(
    args: Namespace,
    user_id: int,
    group_id: int,
    is_admin: bool,
    is_superuser: bool,
) -> str:

    job = {args.name: {"cron": args.cron, "message": args.message, "enable": True}}

    add_todo_list(job, user_id=user_id, group_id=group_id)


def handle_remove(
    args: Namespace,
    user_id: int,
    group_id: int,
    is_admin: bool,
    is_superuser: bool,
) -> str:

    job = args.name

    remove_todo_list(job, user_id=user_id, group_id=group_id)


def handle_pause(
    args: Namespace,
    user_id: int,
    group_id: int,
    is_admin: bool,
    is_superuser: bool,
) -> str:

    job = args.name

    pause_todo_list(job, user_id=user_id, group_id=group_id)


def handle_resume(
    args: Namespace,
    user_id: int,
    group_id: int,
    is_admin: bool,
    is_superuser: bool,
) -> str:
    job = args.name

    resume_todo_list(job, user_id=user_id, group_id=group_id)
