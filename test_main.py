import unittest
import main

class TestMain(unittest.TestCase):

    def test_create(self):

        self.assertEqual(main.create("kolkata",25),"Data Inserted successfully")
        self.assertEqual(main.create("upgb5@85",65695565),"error: Invalid key_name!! key_name must consists of only alphabets and no special characters or numbers")
        self.assertEqual(main.create("Delhi",100,240),"Data Inserted successfully")
        self.assertEqual(main.create("kolkata",50),"Error: given key already exists")



    def test_read(self):
        self.assertEqual(main.read("kolkata"),"kolkata:25")
        self.assertEqual(main.read("Bangalore"),"error: given key does not exist in database. Please enter a valid key")

        self.assertEqual(main.read("Delhi"),"Delhi:100")
        

    def test_delete(self):
        self.assertEqual(main.delete("Chennai"),"error: given key does not exist in database. Please enter a valid key")
        #self.assertEqual(main.delete("kolkata"),"key deleted successfully")

if __name__=='__main__':
    unittest.main();
