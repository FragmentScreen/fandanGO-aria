import json
import os
import unittest
from dotenv import load_dotenv
from fGOaria.classes.oauth import OAuth
from fGOaria.classes.file_upload_field import FileUploadField
from fGOaria.classes.data_manager import DataManager

class AriaFileUploadFieldCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        load_dotenv()
        self.test_local_file_name = 'test_aria_field_upload_fixture.txt'
        with open(self.test_local_file_name, 'w') as fixture:
            fixture.write('ARIA field upload integration test')
        self.addClassCleanup(os.remove, self.test_local_file_name)
        self.test_local_file_type = 'text/plain'
        self.test_record_id = os.getenv('TEST_RECORD_ID')

        self.oauth = OAuth()
        self.oauth.login(os.getenv('ARIA_CONNECTION_USERNAME'), os.getenv('ARIA_CONNECTION_PASSWORD'))

        self.file_upload_field = FileUploadField(
            record_id=self.test_record_id,
            file_path=self.test_local_file_name,
            file_name=self.test_local_file_name,
            file_type=self.test_local_file_type,
            options={"allowMultiple": False, "strict_mime_types": False},
            order=0,
            description="Test file upload field"
        )
        self.data_manager = DataManager(
            token=self.oauth.get_access_token(),
            entity_id=os.getenv('TEST_VISIT_ID'),
            entity_type='visit',
            populate=False
        )

    def testFileUploadField(self):
        # Test initialisation of field
        self.assertIsNotNone(self.file_upload_field.record_id, "Record ID is not set")
        self.assertEqual(self.file_upload_field._file_path, self.test_local_file_name, "File path does not match local path")
        self.assertEqual(self.file_upload_field._file_type, self.test_local_file_type, "File type does not match local file type")
        self.assertEqual(self.file_upload_field.options, {"allowMultiple": False, "strict_mime_types": False}, "Field options does not match")
        self.assertEqual(self.file_upload_field.order, 0, "Field order does not match")
        self.assertEqual(self.file_upload_field.description, "Test file upload field", "Field description does not match")
        self.assertEqual(self.file_upload_field.content, "", "Content is set before upload")

        # Test upload
        self.file_upload_field.upload(token=self.oauth.get_access_token())
        field_content = json.loads(self.file_upload_field.content)
        self.assertIsNotNone(field_content, "Content is not set after upload")
        self.assertIsNotNone(field_content.get('orig'), "Original file name is not set")
        self.assertEqual(field_content.get('orig'), self.test_local_file_name, "Original file name is not equal to test local file name")
        self.assertIsNotNone(field_content.get('name'), "External file name is not set")
        self.assertIsNotNone(field_content.get('size'), "File size is not set")
        self.assertIsNotNone(field_content.get('url'), "File url is not set")
        self.assertEqual(field_content.get('type'), self.test_local_file_type, "File type is not equal to test local file type")

        # Test push field
        created_field = self.data_manager.client.push_field(self.file_upload_field)
        self.assertIsNotNone(created_field, "Created field is not set")
        self.assertIsNotNone(created_field.get('id'), "Created field ID is not set")

        # Test post-push population of local field
        self.file_upload_field.populate(created_field)
        self.assertIsNotNone(self.file_upload_field.id, "Field ID is not set after push")
        self.assertIsNotNone(self.file_upload_field.field_type, "Field type is not set after push")
        self.assertIsNotNone(self.file_upload_field.content, "Field content is not set after push")


if __name__ == '__main__':
    unittest.main()
