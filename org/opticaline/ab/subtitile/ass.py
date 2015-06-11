__author__ = 'opticaline'

# mplayer.exe -sub ../Community.S06E08.720p.WEBRip.x264-BATV.简体.ass -subcp utf-8 http://localhost:63342/AB/Wildlife.wmv

class Ass:
    attr = dict()
    attr_name = ('Script Info', 'V4+ Styles', 'Events', 'Fonts', 'Graphics', '', '', '', '')

    def __init__(self):
        self.attr['Script Info'] = '''; // 此字幕由AB生成
Title:Opticaline
Original Script:Opticaline
Synch Point:1
ScriptType:v4.00+
Collisions:Normal'''
        self.attr['V4+ Styles'] = '''Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,微软雅黑,22,&H00FFFFFF,&HF0000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0.00,1,2,0,2,30,30,5,134'''
        self.attr['Events'] = '''Format: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:00:10.00,*Default,NTP,0000,0000,0000,,(Test)'''

    def __str__(self):
        text = ''
        for name in self.attr_name:
            if name in self.attr.keys():
                text += '[{name}]\n{value}\n'.format(name=name, value=str(self.attr[name]))
        return text

if __name__ == '__main__':
    print(Ass())
