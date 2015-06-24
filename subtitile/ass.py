# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('ab')


class Ass:
    attr = dict()
    attr_name = ('Script Info', 'V4+ Styles', 'Events', 'Fonts', 'Graphics', '', '', '', '')
    time_line = dict()
    width = 1920
    height = 1080

    def __init__(self):
        self.attr['Script Info'] = '''ScriptType: v4.00+
Collisions: Normal
PlayResX: 1920
PlayResY: 1080'''
        self.attr['V4+ Styles'] = '''Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: AcplayDefault, Microsoft YaHei, 50, &H00FFFFFF, &H00FFFFFF, &H00000000, &H00000000, 0, 0, 0, 0, 100, 100, 0.00, 0.00, 1, 1, 0, 2, 20, 20, 20, 0'''
        self.attr['Events'] = '''Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''

    def add_message(self, start, color, message, style):
        message = Message(start, color, message, style, self.add_time_line(start, len(message)))
        self.attr['Events'] += str(message)

    def add_time_line(self, start, length):
        time = int(start / 7) * 7
        length /= 10

        def add(key):
            line = self.time_line.get(key, 0)
            self.time_line[key] = line + 1
            return line

        for i in range(int(length)):
            add(time + i * 7)

        return add(time)

    def __str__(self):
        text = ''
        for name in self.attr_name:
            if name in self.attr.keys():
                text += '[{name}]\n{value}\n\n'.format(name=name, value=str(self.attr[name]))
        return text


class Message:
    start = None
    message = None
    MAX_LINE = 15
    (SCROLL, TOP, BOTTOM) = (1, 5, 4)

    def __init__(self, start, color, message, style, line):
        self.line = line
        self.start = self.to_hms(start)
        self.end = self.init_end(start, len(message))
        self.style = style
        (self.x1, self.y1, self.x2, self.y2) = self.init_position()
        self.message = self.make_msg(message, color, self.make_mode())

    @staticmethod
    def to_hms(seconds):
        if seconds < 0:
            return '0:00:00.00'

        i, d = divmod(seconds, 1)
        m, s = divmod(i, 60)
        h, m = divmod(m, 60)
        return '%d:%02d:%02d.%02d' % (h, m, s, d * 100)

    @staticmethod
    def init_end(seconds, length):
        end_seconds = seconds + 7 + (length / 2)
        return Message.to_hms(end_seconds)

    @staticmethod
    def make_msg(message, color, mode):
        # 1080 / 70
        color = Message.make_color(color)
        return "{{{2}\c&H{1}}}{0}".format(message, color, mode)

    def make_mode(self):
        if self.style == self.SCROLL:
            return "\move({x1}, {y1}, {x2}, {y2})".format(**self.__dict__)
        elif self.style in [self.TOP, self.BOTTOM]:
            return "\\a6\pos({x1}, {y1})".format(**self.__dict__)

    @staticmethod
    def make_color(color):
        return hex(color)[2:].zfill(6)

    def init_position(self):
        line, m = divmod(self.line, self.MAX_LINE)
        line += (m * 0.5 + 1)
        if self.style == self.SCROLL:
            return (1920, line * 70, 0, line * 70)
        elif self.style == self.TOP:
            return (int(1920 / 2), 50, 0, 0)
        elif self.style == self.BOTTOM:
            return (int(1920 / 2), 800, 0, 0)
        else:
            logger.error('un know style {0}'.format(self.style))
            return (1920, line * 70, 0, line * 70)

    def __str__(self):
        return "Dialogue: 3,{start},{end},AcplayDefault,,0000,0000,0000,,{message}\n".format(**self.__dict__)

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
