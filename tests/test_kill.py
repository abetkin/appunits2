from g_context.util import case
from g_context.base import green_method
from g_context.handles import stop_before, stop_after
from g_context import getcontext

class A:
    x = 3

    @green_method
    def run(self):
        return B().walk() + 1

class B:

    @green_method
    def walk(self):
        return getcontext()['x']


class C(A):

    @green_method
    def run(self):
        with stop_after(A.run):
            with stop_before(B.walk) as stopped:
                b, = super().run()
                stopped.kill()
        return b


o = C()
res = o.run()
case.assertIsInstance(res, B)


# TODO check that handles are parent greenlets
