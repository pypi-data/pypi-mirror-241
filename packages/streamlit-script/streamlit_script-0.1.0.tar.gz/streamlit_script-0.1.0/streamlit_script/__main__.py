import argparse
import atexit
import glob
import os.path
import pathlib
import shutil
import sys
import tempfile
import textwrap

from streamlit.web.cli import main as s_main
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from watchdog.observers import Observer


def change_for_streamlit(file):
    with open(file, "r", encoding="utf8", errors="ignore") as f:
        text = f.read()
    with open(file, "w", encoding="utf8") as f:
        f.write(textwrap.dedent("""
            import streamlit as st
            __print = print
            def input(prompt = ""):
                return st.text_input(prompt)
            def print(*args):
                __print(*args)
                st.markdown(" ".join(args))
        """) + text)


class SyncHandler(FileSystemEventHandler):
    def __init__(self, src_path, dest_path):
        self.src_path = pathlib.Path(src_path)
        self.dest_path = pathlib.Path(dest_path)
        if os.path.exists(dest_path): shutil.rmtree(dest_path)
        shutil.copytree(src_path, dest_path)
        for file in glob.glob(self.dest_path.as_posix() + "/**", recursive=True):
            if os.path.isfile(file):
                change_for_streamlit(file)

    def on_modified(self, event: FileModifiedEvent):
        if event.is_directory: return
        file = pathlib.Path(event.src_path)
        if pathlib.Path(event.src_path).exists():
            change_for_streamlit(file)
            shutil.copyfile(event.src_path, self.dest_path.joinpath(file.relative_to(self.src_path)))


def run(script, local_temp_dir=False, **_):
    target = pathlib.Path(script)

    if local_temp_dir:
        td = ".streamlit_script"
        atexit.register(lambda: shutil.rmtree(td))
    else:
        t = tempfile.TemporaryDirectory()
        atexit.register(lambda: t.cleanup())
        td = t.name
    handler = SyncHandler(target.parent.as_posix(), td)
    observer = Observer()
    observer.schedule(handler, target.parent.as_posix())
    observer.start()
    atexit.register(lambda: observer.stop())
    sys.argv[2] = pathlib.Path(td).joinpath(target).as_posix()
    sys.argv = sys.argv[:3]
    s_main(prog_name="streamlit_script")


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser_run = subparsers.add_parser("run")
    parser_run.add_argument("script")
    parser_run.add_argument("--local_temp_dir", action="store_true")
    parser_run.set_defaults(func=run)
    args = parser.parse_args().__dict__
    if args.get("func") is None:
        parser.print_help()
    else:
        args["func"](**args)


if __name__ == '__main__':
    main()
