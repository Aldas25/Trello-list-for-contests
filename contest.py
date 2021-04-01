class Contest:
    def __init__ (self, platform, name, start_time, link):
        self.platform = platform
        self.name = name
        self.start_time = start_time
        self.link = link
        # self.duration = duration

    def __str__ (self):
        ret = f'Contest at {self.platform}: {self.name}, starting at {self.start_time}'
        # ret += '\nlink: {}'.format(self.link)
        return ret