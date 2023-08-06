from queue import Queue as _Queue


class Queue(_Queue):
    @property
    def qsize(self) -> int:
        return super().qsize()