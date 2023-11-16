from Configs import exconf
from Runner import AutoRunner

def main():
    runner = AutoRunner(exconf)
    runner.run()

if __name__=="__main__":
    main()