import json
import os
import unittest
import pytest
from unittest.mock import patch
from tests.test_case import UnitTestCase
from dotenv import load_dotenv
from fGOaria.classes.oauth import OAuth
from fGOaria.classes.file_upload_field import FileUploadField
from fGOaria.classes.data_manager import DataManager

@pytest.mark.offline
class AriaFileUploadFieldOfflineCase(UnitTestCase):
    requires_live_aria = False

    def testUploadSerialization(self):
        file_path = 'test_aria_field_upload_fixture.txt'
        file_type = 'text/plain'
        field = FileUploadField(
            record_id='test-record',
            file_path=file_path,
            file_type=file_type,
        )
        uploaded_file = {
            'orig': file_path,
            'name': 'mocked-aria-field-upload.txt',
            'size': 34,
            'url': 'https://example.invalid/mocked-aria-field-upload.txt',
            'type': file_type,
        }
        token = 'test-token'
        self.assertEqual(field.content, '')
        with patch(
            'fGOaria.classes.file_upload_field.AriaRest',
            autospec=True,
        ) as rest_client:
            rest_client.return_value.upload.return_value = {'files': [uploaded_file]}
            field.upload(token=token)
        rest_client.assert_called_once_with(token)
        rest_client.return_value.upload.assert_called_once_with(file_path, file_type)
        self.assertEqual(json.loads(field.content), uploaded_file)


@pytest.mark.integration
class AriaFileUploadFieldCase(UnitTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        load_dotenv()
        required = ('TEST_RECORD_ID', 'TEST_VISIT_ID', f"ARIA_GQL_{os.getenv('DEV', 'LOCAL')}")
        missing = [name for name in required if not os.getenv(name)]
        if missing:
            raise ValueError("Missing GraphQL test configuration: " + ", ".join(missing))

        cls.test_local_file_name = 'test_aria_field_upload_fixture.txt'
        cls.test_local_file_type = 'text/plain'
        cls.test_record_id = os.getenv('TEST_RECORD_ID')

        cls.oauth = OAuth()
        cls.oauth.login(**cls.aria_credentials)

        cls.file_upload_field = FileUploadField(
            record_id=cls.test_record_id,
            file_path=cls.test_local_file_name,
            file_name=cls.test_local_file_name,
            file_type=cls.test_local_file_type,
            options={"allowMultiple": False, "strict_mime_types": False},
            order=0,
            description="Test file upload field"
        )
        cls.data_manager = DataManager(
            token=cls.oauth.get_access_token(use_keyring=False),
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

        # Only file storage is mocked; OAuth and the GraphQL mutation remain live.
        uploaded_file = {
            'orig': self.test_local_file_name,
            'name': 'mocked-aria-field-upload.txt',
            'size': 34,
            'url': 'https://example.invalid/mocked-aria-field-upload.txt',
            'type': self.test_local_file_type,
        }
        token = self.oauth.get_access_token(use_keyring=False)
        with patch(
            'fGOaria.classes.file_upload_field.AriaRest.upload',
            autospec=True,
            return_value={'files': [uploaded_file]},
        ) as upload:
            self.file_upload_field.upload(token=token)
        upload.assert_called_once()
        rest_client, file_path, file_type = upload.call_args.args
        self.assertIs(rest_client.token, token)
        self.assertEqual(file_path, self.test_local_file_name)
        self.assertEqual(file_type, self.test_local_file_type)
        field_content = json.loads(self.file_upload_field.content)
        self.assertEqual(field_content, uploaded_file)
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
        self.assertEqual(created_field.get('type'), 'JSON_ARIA_FILE', "Created field type is not 'JSON_ARIA_FILE'")
        self.assertEqual(created_field.get('content'), uploaded_file, "Created field content is not equal to uploaded file")

        # Test post-push population of local field
        self.file_upload_field.populate(created_field)
        self.assertIsNotNone(self.file_upload_field.id, "Field ID is not set after push")
        self.assertEqual(self.file_upload_field.id, created_field['id'], "Field ID is not equal to created field ID after push")
        self.assertIsNotNone(self.file_upload_field.field_type, "Field type is not set after push")
        self.assertIsNotNone(self.file_upload_field.content, "Field content is not set after push")


if __name__ == '__main__':
    unittest.main()
