__author__ = 'opticaline'


class Ass:
    attr = dict()
    attr_name = ('Script Info', 'V4+ Styles', 'Events', 'Fonts', 'Graphics', '', '', '', '')

    def __init__(self):
        self.attr['Script Info'] = '''ScriptType: v4.00+
Collisions: Normal
PlayResX: 1920
PlayResY: 1080'''
        self.attr['V4+ Styles'] = '''Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: AcplayDefault, Microsoft YaHei, 64, &H00FFFFFF, &H00FFFFFF, &H00000000, &H00000000, 0, 0, 0, 0, 100, 100, 0.00, 0.00, 1, 1, 0, 2, 20, 20, 20, 0'''
        self.attr['Events'] = '''Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''

    def add_message(self, message):
        self.attr['Events'] += str(message)

    def __str__(self):
        text = ''
        for name in self.attr_name:
            if name in self.attr.keys():
                text += '[{name}]\n{value}\n\n'.format(name=name, value=str(self.attr[name]))
        return text


class Message:
    start = None
    message = None

    def __init__(self, start, color, message):
        self.start = self.to_hms(start)
        self.end = self.to_hms(start + (len(message) / 10 + 1) * 60)
        self.message = self.make_msg(message, color)

    @staticmethod
    def to_hms(seconds):
        if seconds < 0:
            return '0:00:00.00'

        i, d = divmod(seconds, 1)
        m, s = divmod(i, 60)
        h, m = divmod(m, 60)
        return '%d:%02d:%02d.%02d' % (h, m, s, d * 100)

    @staticmethod
    def make_msg(message):
        return message

    def __str__(self):
        return "Dialogue: 3,{start},{end},AcplayDefault,,0000,0000,0000,," \
               "{{\move(2016, 64, -96, 64)}}{message}\n".format(**self.__dict__)

        # def init_styled_text(self, ):
        #     if self.nico_subtitle.font_color == 'FFFFFF':
        #         color_markup = ''
        #     else:
        #         color_markup = '\\c&H%s' % self.nico_subtitle.font_color
        #     if self.nico_subtitle.white_border:
        #         border_markup = '\\3c&HFFFFFF'
        #     else:
        #         border_markup = ''
        #     if self.font_size == self.base_font_size:
        #         font_size_markup = ''
        #     else:
        #         font_size_markup = '\\fs%d' % self.font_size
        #     if self.nico_subtitle.style == NicoSubtitle.SCROLL:
        #         style_markup = '\\move(%d, %d, %d, %d)' % (self.x1, self.y1, self.x2, self.y2)
        #     else:
        #         style_markup = '\\a6\\pos(%d, %d)' % (self.x1, self.y1)
        #     markup = ''.join([style_markup, color_markup, border_markup, font_size_markup])
        #     return '{%s}%s' % (markup, self.nico_subtitle.text)


if __name__ == '__main__':
    ass = Ass()
    ass.add_message(Message(915.66, 16777215, 'Test'))
    print(ass)
