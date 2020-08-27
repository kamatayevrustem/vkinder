import unittest
from unittest.mock import patch
from VKinder.main import VK
import vk
import time


class Test_VKinder(unittest.TestCase):
    def setUp(self):
        with open('token.txt', 'r', encoding='UTF-8') as f:
            token = f.read()
        session = vk.Session(access_token=token)
        self.api = vk.API(session)
        self.user_id = 547302144
        self.user_info = self.api.users.get(v='5.101', user_ids=self.user_id,
                                            fields='interests, sex, city, music')
        time.sleep(0.34)
        self.fake_user_info = ['try', 'la', 2]
        self.break_api = 'not session'

    @patch('builtins.input', lambda *args: 'string11111')
    def test_set_city_for_search_whith_incorrect_input(self):
        time.sleep(0.34)
        with self.assertRaises(IndexError):
            VK.set_city_for_search(self, self.api, self.user_info)

    def test_set_sex_for_search(self):
        time.sleep(0.34)
        self.assertEqual(VK.set_sex_for_search(self, self.user_info), 1)

    def test_get_interests(self):
        with self.assertRaises(TypeError):
            VK.get_interests(self, self.fake_user_info)

    def test_get_groups(self):
        self.assertGreater(VK.get_groups(self, self.api, self.user_id), [1])


if __name__ == '__main__':
    unittest.main()
