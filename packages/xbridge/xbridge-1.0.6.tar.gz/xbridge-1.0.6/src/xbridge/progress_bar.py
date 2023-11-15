

from progress.bar import Bar

class TranferBar(Bar):
    suffix='%(percent)d%% | %(eta_td)s/%(elapsed_td)s | %(size)s | %(speed)s ' 
    width = 12
    fill = '█'

    @property
    def speed(self):
        # if self.elapsed < 1:
        #     return '--'
        # bps = 1.0 / self.avg
        if self.elapsed < 10 or self.index < self.max:
            bps = 1.0 / self.avg
        else:
            bps = self.index / self.elapsed   
        return size_string(bps, 1) + '/s'
        
    @property
    def size(self):
        return size_string(float(self.max), 0)
    
    bar_diff = 0
    def next_lazy(self, diff : int):
        self.bar_diff += diff
        if self.bar_diff > 5 * 1024 * 1024:
            self.next(self.bar_diff)
            self.bar_diff = 0
        pass

    def finish_lazy(self):
        if self.bar_diff > 0:
            self.next(self.bar_diff)
            self.bar_diff = 0
        self.finish()

def size_string(byte: float, fraction: int):

    fmt = '%%.%d' % fraction + 'f'
    
    if byte < 1024:
        return fmt % byte + ' B'
    
    KB = byte / 1024
    if KB < 1024:
        return fmt % KB + ' KB'

    MB = KB / 1024
    if MB < 1024:
        return fmt % MB + ' MB'

    GB = MB / 1024
    return fmt % GB + ' GB'
