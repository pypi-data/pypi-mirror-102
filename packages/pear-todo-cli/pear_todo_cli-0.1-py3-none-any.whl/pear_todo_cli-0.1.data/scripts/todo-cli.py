#!python
import curses
import os

TODO_LIST_FILE = os.path.join(os.path.expanduser("~"), ".todo_list")

def get_wh(win):

    h, w = win.getmaxyx()
    return (w, h)

def get_cmd(win):

    w, h = get_wh(win)

    win.addstr(h - 1, 0, ">")
    _cmd = win.getstr(h - 1,2, w - 2)
    _cmd = _cmd.decode()
    _cmd = _cmd.split()
    cmd = _cmd[0] if len(_cmd) >= 1 else ""
    args = " ".join(_cmd[1:]) if len(_cmd) >= 2 else ""

    return cmd, args

def load_items():

    with open(TODO_LIST_FILE, "r") as fd:
        items = fd.read().split()

    return items

def save_items(items):

    with open(TODO_LIST_FILE, "w") as fd:
        for item in items:
            fd.write(item + "\n")


def main(win):

    # Setup
    curses.echo()

    # Load todo list
    items = load_items()

    # REPL

    cmd = ""
    args = ""

    list_len = 0

    while cmd != "q":

        win.clear()

        w, h = get_wh(win)

        item_diff_size = len(items) - (h - 1)
        item_diff_size = item_diff_size if item_diff_size > 0 else 0
        for i, item in enumerate(items[item_diff_size:]):

            win.addstr(i, 1, "[{}]: {}".format(i + item_diff_size, item))

        win.refresh()

        cmd, args = get_cmd(win)

        if cmd == "add":

            items.append(args)

        elif cmd == "del":

            try:
                items.pop(int(args))
            except Exception:
                pass

        save_items(items)


if __name__ == "__main__":
    curses.wrapper(main)