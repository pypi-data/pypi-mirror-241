import sys,os
# print(sys.path)
# sys.path.append(os.getcwd())
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(os.path.abspath(__file__))
# print(sys.path)

import greatlibrarian.Logs
from greatlibrarian.Configs import exconf
import greatlibrarian.confi
import testfolder.test2

from Runner import AutoRunner

quit()
def main():
    runner = AutoRunner(exconf)
    runner.run()

if __name__=="__main__":
    main()