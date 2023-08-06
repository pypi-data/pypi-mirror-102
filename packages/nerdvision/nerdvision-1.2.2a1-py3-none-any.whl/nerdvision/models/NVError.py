import time

from nerdvision import agent_name


class NVErrorFrame(object):
    def __init__(self, class_name, func_name, line_no, source_file):
        self.class_name = class_name
        self.func_name = func_name
        self.line_no = line_no
        self.source_file = source_file

    def as_dict(self):
        return {
            'class_name': self.class_name,
            'func_name': self.func_name,
            'line_no': self.line_no,
            'source_file': self.source_file
        }


class NVError(object):
    def __init__(self, _type, message):
        self.id = None
        self.trace = []
        self.type = _type
        self.message = message
        self.timestamp = int(time.time())

    def add_frame(self, frame):
        self.trace.append(frame)

    def push_frame(self, frame):
        self.trace.insert(0, frame)

    def pop_frame(self):
        self.trace.pop(0)

    def as_dict(self):
        return {
            'id': self.id,
            'trace': [_frame.as_dict() for _frame in self.trace],
            'type': self.type,
            'message': self.message,
            'timestamp': self.timestamp,
            'source': agent_name
        }
