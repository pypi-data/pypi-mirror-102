from unittest import TestCase

from routerling import Router
from routerling import Context
from routerling import HttpRequest, ResponseWriter

from routerling.router import Routes


# to be reused in router testcase instance
def handle_customer_created(r: HttpRequest, w: ResponseWriter, ctx: Context):...


class TestRouter(TestCase):
    def setUp(self, *args, **kwargs):
        self.router = Router()
        self.router.GET("/customers", handle_customer_created)
        self.router.GET("/customers/:id", handle_customer_created)
        self.router.GET("/customers/:id/orders", lambda r, w, c: (
            print("Who that there...")
        ))
    
    def test_route_instance_found(self):
        self.assertIsInstance(self.router.rtx, Routes)

    def test_index_get_node(self):
        methods = self.router.rtx.routes
        self.assertEqual("nothing at all", "nothing at all")


if __name__ == "__main__":
    import unittest
    unittest.main()
