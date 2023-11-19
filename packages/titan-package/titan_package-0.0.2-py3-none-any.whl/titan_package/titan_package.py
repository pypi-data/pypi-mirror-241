from titan_package.lib import Ext, Ext2


class Hello:
  def print(self):
    print("Hello world!")

  def ext(self):
    ex = Ext()
    ex.print()

  def ext2(self):
    ex = Ext2()
    ex.print()

