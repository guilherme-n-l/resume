from typing import override, Union
from watchdog.events import FileSystemEventHandler, FileModifiedEvent, DirModifiedEvent
from watchdog.observers import Observer
from subprocess import run
from time import sleep


class Handler(FileSystemEventHandler):
    @override
    def on_modified(self, event: Union[FileModifiedEvent, DirModifiedEvent]):
        if event.src_path.endswith("resume.tex"):
            try:
                run(["pdflatex", "resume.tex"], check=False)
                # run(["pdflatex", "resume.tex", "-o", "resume.pdf"], check=True)
            except Exception:
                pass


if __name__ == "__main__":
    watcher = Observer()
    watcher.schedule(event_handler=Handler(), path=".")
    watcher.start()

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        watcher.stop()

    watcher.join()
