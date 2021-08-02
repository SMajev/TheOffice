from datetime import datetime


class TimeLog:
    def __init__(self, Operation="Start"):
        self.now = datetime.now().strftime(f'   *      Date: %d, %b %Y, Time: %H:%M:%S\n'
                                           f'          Operation: {Operation}')

    def __repr__(self):
        return f"{self.now}"
