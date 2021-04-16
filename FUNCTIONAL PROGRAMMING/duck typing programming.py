class Pycharm:
    def open(self):
        print("open method in pycharm")
    def run(self):
         print("run functionality in pycharm")
    def debug(self):
        print("debug functionality in pycharm")

class Vscode:
    def open(self):
        print("open method in Vscode")
    def run(self):
         print("run functionality in Vscode")
    def debug(self):
        print("debug functionality in Vscode")

class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()

py=Pycharm()
vs=Vscode()
pg=Programmer()
#pg.coding(py)
pg.coding(vs)