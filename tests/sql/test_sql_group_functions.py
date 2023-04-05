import json
import os
import unittest

import psycopg2

from .test_sql_functions import GeoDBSqlTest
from .test_sql_functions import get_app_dir


class GeoDBSQLGroupTest(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.base_test = GeoDBSqlTest()
        cls.base_test.setUp()
        cls._cursor = cls.base_test._cursor
        cls._set_role = cls.base_test._set_role
        cls._conn = cls.base_test._conn

        app_path = get_app_dir()
        fn = os.path.join(app_path, '..', 'tests', 'sql', 'setup-groups.sql')
        with open(fn) as sql_file:
            cls.base_test._cursor.execute(sql_file.read())

    def tearDown(self) -> None:
        self.base_test.tearDown()

    def test_basic_group_actions(self):
        self.admin = "test_admin"
        self.member = "test_member"
        self.member_2 = "test_member_2"
        self.nomember = "test_nomember"
        self.table_name = "test_member_table_for_group"

        self.grant_group_to(self.member)
        self.grant_group_to(self.member_2)

        self.create_table_as_user(self.member)
        self.access_table_with_user_fail(self.member_2)
        self.access_table_with_user_fail(self.nomember)
        self.publish_table_to_group(self.member)
        self.access_table_with_user_success(self.member_2)
        self.access_table_with_user_fail(self.nomember)

        self.revoke_group_from(self.member_2)
        self.access_table_with_user_fail(self.member_2)

        self.grant_group_to(self.member_2)
        self.access_table_with_user_success(self.member_2)

        self.unpublish_from_group(self.member)
        self.access_table_with_user_fail(self.member_2)

    def execute(self, sql):
        self._cursor.execute(sql)
        self._conn.commit()

    def revoke_group_from(self, user):
        self._set_role(self.admin)
        sql = f"REVOKE \"test_group\" FROM \"{user}\"; "
        self.execute(sql)

    def grant_group_to(self, user):
        self._set_role(self.admin)
        sql = f"GRANT \"test_group\" TO \"{user}\"; "
        self.execute(sql)

    def unpublish_from_group(self, user):
        self._set_role(user)
        sql = f"SELECT geodb_group_unpublish_collection('{self.table_name}'," \
              f" 'test_group')"
        self.execute(sql)

    def publish_table_to_group(self, user):
        self._set_role(user)
        sql = f"SELECT geodb_group_publish_collection('{self.table_name}'," \
              f"'test_group')"
        self.execute(sql)

    def access_table_with_user_fail(self, user):
        self._set_role(user)
        sql = f"SELECT geodb_get_collection_bbox('{self.table_name}')"
        with self.assertRaises(psycopg2.errors.InsufficientPrivilege):
            self.execute(sql)
        # necessary so we can keep using the connection after the failed query
        self._conn.rollback()

    def access_table_with_user_success(self, user):
        self._set_role(user)
        sql = f"SELECT geodb_get_collection_bbox('{self.table_name}')"
        self.execute(sql)

    def create_table_as_user(self, user):
        self._set_role(user)
        sql = f"SELECT geodb_create_database('test_member')"
        self.execute(sql)
        self._set_role(user)
        props = {}
        sql = f"SELECT geodb_create_collection('{self.table_name}', " \
              f"'{json.dumps(props)}', '4326')"
        self.execute(sql)
