import os
import unittest
from devbops_user_microservice import app

class BasicTestCase(unittest.TestCase):

        
    def api_test(self):
        pass

    def test_login_route(self):
        with app.test_client() as c:
            response = c.get('/login')
            self.assertEquals(response.status_code, 200)
            
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 302)
    
    
if __name__ == '__main__':
    unittest.main()