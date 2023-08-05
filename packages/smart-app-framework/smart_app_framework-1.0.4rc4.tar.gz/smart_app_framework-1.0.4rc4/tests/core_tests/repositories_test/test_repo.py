import json
import pickle
import tempfile
import unittest
from unittest.mock import Mock, patch, PropertyMock

from core.model.registered import Registered
from core.repositories.base_repository import BaseRepository
from core.repositories.classifier_repository import ClassifierRepository
from core.repositories.dill_repository import DillRepository
from core.repositories.folder_repository import FolderRepository
from core.repositories.shard_repository import ShardRepository
from core.utils.loader import ordered_json


class MockDescriptionItem:
    def __init__(self, value):
        self.value = value


class MockBaseRepository(BaseRepository):
    def __init__(self):
        super(MockBaseRepository, self).__init__(MockDescriptionItem)

    def load(self):
        self.fill({"test": {"value": 1}})
        super(MockBaseRepository, self).load()


class MockShardRepository(ShardRepository):
    def __init__(self):
        super(MockShardRepository, self).__init__(MockSource, ordered_json)


class MockSource:
    def __init__(self, content):
        self.content = content

    def list_dir(self, path):
        return self.content.keys()

    def open(self, *args, **kwargs):
        return MockStream(self.content[args[0]]['content'])


class MockStream:
    def __init__(self, data):
        self.data = data
        self.stream = Mock()
        self.stream.read.return_value = json.dumps(self.data).encode()

    def __enter__(self):
        return self.stream

    def __exit__(self, *args):
        return None


class BaseRepositoryTest(unittest.TestCase):
    def test_base_repository_fill(self):
        data = {'test': {'value': 1}}
        repository = BaseRepository(key=None)
        repository.fill(data)
        self.assertEqual(repository.data, data)

    def test_base_repository_save(self):
        repository = BaseRepository(key=None)
        self.assertRaises(NotImplementedError, repository.save, {})

    def test_mock_repository(self):
        test_repository = MockBaseRepository()
        test_repository.load()
        self.assertEqual(test_repository.data, {'test': {'value': 1}})

    def test_base_repository_clear(self):
        test_repository = MockBaseRepository()
        test_repository.load()
        test_repository.clear()
        self.assertEqual(test_repository.data, {})


class ShardRepositoryTest(unittest.TestCase):
    def test_fill_on_top(self):
        shard_repository = MockShardRepository()
        shard_repository.fill({"test": {"value": 1}})
        self.assertEqual(shard_repository.data, {"value": 1})
        shard_repository.fill_on_top({"test": {"value2": 2}})
        self.assertEqual(shard_repository.data, {"value": 1, "value2": 2})


class RepositoryTest(unittest.TestCase):
    def test_repository(self):
        registered_repositories = Registered()
        obj = object()
        registered_repositories["test"] = obj
        self.assertEqual(registered_repositories["test"], obj)
        obj1 = object()
        registered_repositories["test"] = obj1
        self.assertEqual(registered_repositories["test"], obj1)


class FolderRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.folder_content_test_dict = {'1.json': {'content': {'a': 'b'}}, '2.json': {'content': {'c': 'd'}}}
        self.folder_content_test_list = {'1.json': {'content': ['a', 'b']}, '2.json': {'content': ['c', 'd']}}
        self.folder_wrong_content = {'1.json': {'content': {'a': 'b'}}, '2.json': {'content': ['c', 'd']}}

    def test_right_filling_with_dict(self):
        test_repository = FolderRepository('', loader=json.loads,
                                           source=MockSource(self.folder_content_test_dict))
        test_repository.load()
        self.assertDictEqual(test_repository.data, {'a': 'b', 'c': 'd'})

    def test_right_filling_with_list(self):
        test_repository = FolderRepository('', loader=json.loads,
                                           source=MockSource(self.folder_content_test_list))
        test_repository.load()
        self.assertListEqual(test_repository.data, ['a', 'b', 'c', 'd'])

    def test_repo_wrong_content(self):
        test_repository = FolderRepository('', loader=json.loads,
                                           source=MockSource(self.folder_wrong_content))
        self.assertRaises(TypeError, test_repository.load)


class TestDillRepository(unittest.TestCase):
    def test_no_file_and_required(self):
        file = ''
        rep = DillRepository(filename=file)
        self.assertRaises(FileNotFoundError, rep.load)

    def test_no_file_and_not_required(self):
        file = ''
        rep = DillRepository(filename=file, required=False)
        rep.load()
        self.assertIsNone(rep.data)

    def test_file_exists(self):
        expected = {'a': 'b'}
        file = tempfile.NamedTemporaryFile(suffix='.pkl')
        with open(file.name, 'wb') as f:
            pickle.dump(expected, f)
        rep = DillRepository(filename=file.name)
        rep.load()
        self.assertEqual(expected, rep.data)


class TestClassifierRepository(unittest.TestCase):

    def test_load_scikit_classifier(self):
        """Тест кейз на проверку загрузки моделей scikit классификаторов."""
        classifier_data = {"tests": "success"}
        model_file = tempfile.NamedTemporaryFile(suffix=".pkl")
        with open(model_file.name, "wb") as f:
            pickle.dump(classifier_data, f)

        splitted_file_name = model_file.name.split('/')
        data_path = '/'.join(splitted_file_name[:-1])
        model_file_name = splitted_file_name[-1]

        with patch("core.repositories.folder_repository.FolderRepository.data", new_callable=PropertyMock,
                   return_value={"test_classifier": {"type": "scikit", "path": model_file_name, "intents": []}}) as mock:
            classifier_repo = ClassifierRepository("", data_path, json.loads, "")
            classifier_repo.load()
            expected_result = {
                "test_classifier": {
                    "classifier": {"tests": "success"},
                    "path": model_file_name,
                    "type": "scikit",
                    "intents": []
                }
            }
            self.assertEqual(expected_result, classifier_repo.data)

    def test_load_skip_classifier(self):
        """Тест кейз на проверку загрузки skip классификатора, для этого типа классификаторов сам
        файл модели не предусматривается."""
        expected_return_obj = {"test_classifier": {"type": "skip", "intents": []}}

        with patch("core.repositories.folder_repository.FolderRepository.data", new_callable=PropertyMock,
                   return_value=expected_return_obj) as mock_folder_data:
            classifier_repo = ClassifierRepository("", "", json.loads, "")
            classifier_repo.load()
            self.assertEqual(expected_return_obj, classifier_repo.data)

    def test_load_external_classifier(self):
        """Тест кейз на проверку загрузки external классификатора."""
        model_file = tempfile.NamedTemporaryFile(suffix=".pkl")
        with open(model_file.name, "wb") as f:
            pickle.dump({"tests": "success"}, f)

        splitted_file_name = model_file.name.split('/')
        model_file_name = splitted_file_name[-1]
        expected_return_obj = {
            "test_classifier": {"type": "external", "classifier": "another_test_classifier"},
            "another_test_classifier": {"type": "scikit", "path": model_file_name, "intents": []}
        }

        with patch("core.repositories.folder_repository.FolderRepository.data", new_callable=PropertyMock,
                   return_value=expected_return_obj) as mock_folder_data:
            classifier_repo = ClassifierRepository("", "", json.loads, "")
            classifier_repo.load()
            self.assertEqual(expected_return_obj, classifier_repo.data)


if __name__ == '__main__':
    unittest.main()
