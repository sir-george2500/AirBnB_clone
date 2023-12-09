import unittest
import sys
import os
from datetime import datetime
from uuid import uuid4
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_id_is_unique(self):
        mock_uuid = uuid4()
        with patch('uuid.uuid4', return_value=mock_uuid):
            model1 = BaseModel()
            model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_update_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)
