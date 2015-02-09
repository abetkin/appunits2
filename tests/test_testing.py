from applets.base import GreenletWrapper
from applets import from_context
from applets.testing import TestCase, StopAfterSubTest, StopBeforeSubTest
# from applets.util import case

class A:
    x = 3

    @GreenletWrapper
    def run(self):
        return B().walk() + 1

class B:

    def __init__(self):
        self.__b__ = True

    @GreenletWrapper
    def walk(self):
        return from_context('x')


# class T(TestCase):

#     def test(self):

#         @self.stop_before(B.walk, 'walking')
#         def f(obj):
#             self.assertFalse(obj.__b__)

#         @self.stop_after(A.run, 'running A')
#         def f(a, _result_):
#             self.assertNotEqual(_result_, 4)

#         o = A()
#         ss = o.run()

@StopBeforeSubTest(B.walk, 'walking')
def f(case, obj):
    case.assertFalse(obj.__b__)

@StopAfterSubTest(A.run, 'running A')
def f(case, a, _result_):
    case.assertNotEqual(_result_, 4)

o = A()
ss = o.run()
