__author__ = 'opticaline'
import subprocess

class MPlayer:
    exec_path = 'C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe'
    subtitle = None

    def stop(self):
        pass

    def play(self):
        self.subtitle = 'D:\Test2.ass'

        command = self.exec_path
        #if self.subtitle is not None:
        #    command += ' -ass -sub ' + self.subtitle + ' -subcp utf-8'
        #command += ' D:\Test.wmv'
        print(command)
        p = subprocess.Popen([command, 'D:\Test.wmv'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line.decode('gbk'))
        retval = p.wait()
        print(retval)

    def set_subtitle(self, file):
        self.subtitle = file


if __name__ == '__main__':
    MPlayer().play()
