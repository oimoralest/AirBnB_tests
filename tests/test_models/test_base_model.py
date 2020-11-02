import unittest
import json
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class Test_BaseModel(unittest.TestCase):
    """Test for baseModel"""
    def setUp(self):
        """Clean code after each test"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def test_create(self):
        """Test create"""
        n_bm = BaseModel()
        self.assertTrue(type(n_bm.id) == str)
        self.assertTrue(type(n_bm.created_at) == datetime.datetime)
        self.assertTrue(type(n_bm.updated_at) == datetime.datetime)

    def test_str(self):
        """Test BaseModel representation"""
        n_bm = BaseModel()
        self.assertIsInstance(n_bm, BaseModel)
        self.assertTrue(type(n_bm.__str__()) == str)
        args = ["wa", 4, 5, "creo", ["dwa", 4]]
        n_bm = BaseModel(*args)
        self.assertIsInstance(n_bm, BaseModel)
        n_bm = BaseModel("wa", 4, 5, "creo", ["dwa", 4])
        self.assertIsInstance(n_bm, BaseModel)
        
    def test_dict(self):
        """Test BaseModel to_dict method."""
        n_bm = BaseModel()
        dictionary = n_bm.to_dict()
        self.assertTrue(type(dictionary), dict)
        for key in n_bm.__dict__:
            self.assertTrue(key in dictionary)
        self.assertTrue(type(dictionary["created_at"]) == str)
        self.assertTrue(type(dictionary["updated_at"]) == str)
        self.assertTrue(dictionary["__class__"])
        self.assertTrue(dictionary["__class__"] == "BaseModel")

    def test_kwargs(self):
        """test for Kwargs"""
        n_bm = BaseModel({})
        self.assertTrue(type(n_bm.id) == str)
        n_bm = BaseModel(**{"age": 315, "food": 4554})
        self.assertTrue(n_bm.__dict__["age"])
        self.assertTrue(n_bm.__dict__["food"] == 4554)
        my_dict = {"id": "097ca1e6-b8b2-4a9e-90ac-d04695eb1622",
                "created_at": "2016-05-14T21:11:03.285259",
                "updated_at":
                datetime.datetime(2020, 11, 2, 10, 00, 00, 459045),
                "__class__": "death"}
        n_bm = BaseModel(**my_dict)
        with self.assertRaises(KeyError) as err:
            self.assertTrue(n_bm.__dict__["__class__"])
        id = "097ca1e6-b8b2-4a9e-90ac-d04695eb1622"
        self.assertTrue(n_bm.__dict__["id"] == id)
        self.assertIsInstance(n_bm.__dict__["created_at"], datetime.datetime)
        self.assertIsInstance(n_bm.__dict__["updated_at"], datetime.datetime)

    def test_storagemodules(self):
        """test storemodules for modules"""
        FS = FileStorage()
        FS.new(BaseModel())
        n_bm = BaseModel()
        id = n_bm.id
        bm_id = "BaseModel.{}".format(id)
        self.assertTrue(FS._FileStorage__objects[bm_id])
        FS.save()
        with open("file.json", mode="r", encoding="utf-8") as fd:
            self.assertIsInstance(json.load(fd), dict)
            entro = 0
        self.assertTrue(entro == 0)

if __name__ == "__main__":
    unittest.main()