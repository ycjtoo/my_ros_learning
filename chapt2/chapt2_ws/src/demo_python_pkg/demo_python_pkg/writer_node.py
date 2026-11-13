from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self,name:str,age:int,book:str) ->None:
        print('WriterNode __init__ 方法被调用了')
        super().__init__(name,age)
        self.book=book
        

   
def main():
    node=WriterNode ('唐家三骚',20,'论兔子')
    node.eat("烤兔腿")   