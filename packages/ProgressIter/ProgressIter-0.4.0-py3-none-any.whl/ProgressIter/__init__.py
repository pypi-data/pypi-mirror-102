import time


def time_str(sec):
    h = int(sec / 3600)
    m = int(sec % 3600 / 60)
    s = sec % 60
    if h > 0:
        str = '%d:%02d:%02d' % (h, m, s)
    elif m > 0:
        str = '%02d:%02d' % (m, s)
    elif s >= 1.0:
        str = '%.2fs' % s
    else:
        str = '%.2fms' % (s * 1000)
    return str


global_on = True
global_time_on = False
global_bar_len = 100


class Progressbar:
    def __init__(self, iter, length=0, on: bool = None, time_on:bool=None, bar_len:int=None):
        if on == None:
            on = global_on
        if time_on == None:
            time_on = global_time_on
        if bar_len == None:
            bar_len = global_bar_len
        self.on = on
        self.time_on = time_on
        self.bar_len = bar_len
        self.i = -1
        self.iter = iter
        if length > 0:
            self.len = length
        else:
            self.len = len(self.iter)
        self.last_message_len = 0
        self.message = ''
        if on:
            self.time = time.time()
            self.str = '[' + ' ' * self.bar_len + ']0%%(0/%d)' % self.len
            print(self.str, end='', flush=True)
        else:
            self.str = ''

    def __iter__(self):
        self.iter__ = self.iter.__iter__()
        return self

    def __next__(self):
        self.i += 1
        try:
            next = self.iter__.__next__()
            if self.on:
                ratio = self.i / self.len
                percentage = int(100 * ratio)
                sub_number = int(((100*ratio) % 1) * 10)
                star_len = int(ratio*self.bar_len)
                if star_len == self.bar_len:
                    sub_number = ''
                else:
                    sub_number = chr(48 + sub_number)
                str_b = '\b' * len(self.str)
                self.str = '[' + '#' * star_len + sub_number + ' ' * (self.bar_len - star_len) + ']'
                self.str += '%d%%(%d/%d)' % (percentage, self.i, self.len)
                if self.time_on and self.i > 0:
                    time_end = time.time()
                    total_time = time_end - self.time
                    avg_time = total_time / self.i
                    rest_time = avg_time * (self.len - self.i)
                    self.str += '[' + time_str(avg_time) + '/' + time_str(total_time) + '/' + time_str(rest_time) + ']'
                self.str += self.message
                self.message = ''
                self.str += ' ' * (len(str_b) - len(self.str))
                print(str_b + self.str, end='', flush=True)
            return next
        except StopIteration:
            self.done()
            raise StopIteration

    def done(self):
        if self.on:
            str_b = '\b' * len(self.str)
            self.str = '[' + '#' * self.bar_len + ']'
            self.str += '100%%(%d/%d)' % (self.len, self.len)
            if self.time_on and self.i > 0:
                time_end = time.time()
                total_time = time_end - self.time
                avg_time = total_time / self.i
                self.str += '[' + time_str(avg_time) + '/' + time_str(total_time) + ']'
            self.str += self.message
            self.str += ' ' * (len(str_b) - len(self.str))
            print(str_b + self.str, end='', flush=True)
            print('', flush=True)

    def show_message(self, str: str):
        self.message = str

    @classmethod
    def global_on(cls, on: bool):
        global global_on
        global_on = on

    @classmethod
    def global_time_on(cls, on: bool):
        global global_time_on
        global_time_on = on

    @classmethod
    def global_bar_len(cls, length: int):
        global global_bar_len
        global_bar_len = length