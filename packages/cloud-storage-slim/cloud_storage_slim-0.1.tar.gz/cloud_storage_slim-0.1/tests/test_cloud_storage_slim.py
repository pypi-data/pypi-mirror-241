import os
import unittest
from cloud_storage_slim import CloudStorageSlim


class TestCloudStorageSlim(unittest.TestCase):
    def setUp(self):
        self.cloud_storage_slim = CloudStorageSlim()
        self.test_file_path = "test_file.txt"
        with open(self.test_file_path, "w") as file:
            file.write("this is cloud_storage_slim test file")

    def tearDown(self):
        self.cloud_storage_slim.destroy()
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_copyto_local_to_local(self):
        source_path = self.test_file_path
        # change name to test_file_copy.txt
        dest_path = "test_file_copy_from_local.txt"
        self.cloud_storage_slim.copyto(source_path, dest_path)
        self.assertTrue(os.path.exists(dest_path))
        self.assertEqual(os.path.getsize(source_path), os.path.getsize(dest_path))

    def test_copyto_local_to_remote(self):
        source_path = self.test_file_path
        dest_path = "oss://haiper-cn-shanghai/file.txt"
        # dest_path = "az://haiper_test/file.txt"
        self.cloud_storage_slim.copyto(source_path, dest_path)
        list_blobs = self.cloud_storage_slim.ls(dest_path)
        self.assertEqual(len(list_blobs), 1)

    def test_copyto_remote_to_remote(self):
        source_path = "gs://haiper_test/test_file_copy_from_local.txt"
        dest_path = "az://haiper_test/test_file_copy_from_local.txt"
        self.cloud_storage_slim.copyto(source_path, dest_path)
        list_blobs = self.cloud_storage_slim.ls(dest_path)
        self.assertEqual(len(list_blobs), 1)

    def test_copyto_remote_to_local(self):
        # source_path = "gs://haiper_test/test_file_copy_from_local.txt"
        source_path = "oss://haiper-cn-shanghai/file.txt"
        # source_path = "az://haiper_test/test_file_copy_from_local.txt"
        dest_path = "test_file_copy_from_remote_2.txt"
        self.cloud_storage_slim.copyto(source_path, dest_path)
        self.assertTrue(os.path.exists(dest_path))

    def test_copyto_invalid_source_path(self):
        source_path = "/invalid/source/path"
        dest_path = "test_file_copy_from_random.txt"
        with self.assertRaises(Exception):
            self.cloud_storage_slim.copyto(source_path, dest_path)

    def test_copyto_invalid_dest_path(self):
        source_path = "/path/to/source/file"
        dest_path = "/invalid/destination/path"
        with self.assertRaises(Exception):
            self.cloud_storage_slim.copyto(source_path, dest_path)


if __name__ == "__main__":
    unittest.main()
