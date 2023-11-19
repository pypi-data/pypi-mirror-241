###########################################################################################################
# KineticForms API Engine
#
# Copyright (c) 2023 - Kinetic Seas Inc.
# by Edward Honour and Joseph Lehman.
#
#
###########################################################################################################
import json
import pymysql
import pymysql.cursors
from .db import Db


class KineticForms():
    # This is the a basic CRUD class for MySQL.  If you are using a different database
    # change this function to perform these operations.

    def __init__(self, connection_vault_path):
        self.connection_vault_path = connection_vault_path

    def connect(self):
        try:
            with open(self.connection_vault_path, 'r') as connection_file:
                connection_dict = json.load(connection_file)

            return pymysql.connect(
                host=connection_dict['host'],
                user=connection_dict['user'],
                password=connection_dict['password'],
                database=connection_dict['database'],
                cursorclass=pymysql.cursors.DictCursor
            )
        except FileNotFoundError:
            return {"error_code": "5501", "error_msg": "Connection Vault " + str(connection_vault_path) + " not found.", "data": {}}
        except json.JSONDecodeError as e:
            return {"error_code": "5502", "error_msg": "Error decoding JSON" + str(e), "data": {}}

    # execute any query and return the results.
    def sql(self, s, errors=True):
        try:
            conn = self.connect()
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Connecting: " + str(err), "data": []}
            else:
                return []

        try:
            cursor = conn.cursor()
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9998", "error_msg": "Error Creating Cursor: " + str(err), "data": []}
            else:
                return []

        try:
            cursor.execute(s)
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Executing: " + str(err), "data": []}
            else:
                return []

        try:
            records = cursor.fetchall()
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Fetching: " + str(err), "data": []}
            else:
                return []

        if errors:
            return {"error_code": "0", "error_msg": "", "data": records}
        else:
            return records

    def sql0(self, s, errors=True):
        try:
            conn = self.connect()
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Connecting: " + str(err), "data": {}}
            else:
                return {}

        try:
            cursor = conn.cursor()
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Creating Cursor: " + str(err), "data": {}}
            else:
                return {}

        try:
            cursor.execute(s)
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Executing: " + str(err), "data": {}}
            else:
                return []
        try:
            records = cursor.fetchone()
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Fetching: " + str(err), "data": {}}
            else:
                return []

        if errors:
            return {"error_code": "0", "error_msg": "", "data": records}
        else:
            return records

    def execute(self, s, errors=True):
        try:
            conn = Db.connect()
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Connecting: " + str(err), "data": {}}
            else:
                return {}

        try:
            cursor = conn.cursor()
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Creating Cursor: " + str(err), "data": {}}
            else:
                return {}

        try:
            cursor.execute(s)
        except pymysql.err.MySQLError as err:
            if errors:
                return {"error_code": "9999", "error_msg": "Error Executing: " + str(err), "data": []}
            else:
                return []

        try:
            conn.commit()
            return {"error_code": "0", "error_msg": "" + str(e), "data": {}}
        except Exception as e:
            return {"error_code": "9999", "error_msg": "Database Error: " + str(e), "data": {}}

    def save(self, my_dict, table_name):
        if isinstance(my_dict, dict):
            my_dict['table_name'] = table_name
            my_dict['action'] = "insert"
            return KineticForms.post(my_dict)
        else:
            return {"error_code": "9999", "error_msg": "Parameter must be a dict", "data": {}}

    def merge(self, my_dict, table_name, keys):

        if isinstance(my_dict, dict):
            pass
        else:
            return {"error_code": "9999", "error_msg": "Parameter must be a dict", "data": {}}

        if isinstance(keys, list):
            pass
        else:
            return {"error_code": "9999", "error_msg": "Keys must be a list of columns", "data": {}}

        try:
            conn = self.connect()
        except pymysql.err.MySQLError as err:
            return {"error_code": "9999", "error_msg": "Error Connecting: " + str(err), "data": {}}

        try:
            cursor = conn.cursor()
        except pymysql.err.MySQLError as err:
            return {"error_code": "9999", "error_msg": "Error Creating Cursor: " + str(err), "data": {}}

        columns = []
        sql = "SHOW COLUMNS FROM " + table_name
        try:
            cursor.execute(sql)
            columns = cursor.fetchall()
        except Exception as e:
            return {"error_code": "9999", "error_msg": "General Error: " + str(e), "data": {}}

        sql = "select id from " + str(table_name) + " where 1 = 1 "
        # Make the rest of the where clause.
        for i in keys:
            for k in columns:
                if k['Field'] == i:
                    if 'int' in k['Type']:
                        sql += " and " + str(i) + " = " + my_dict[i] + " "
                    if 'varchar' in k['Type']:
                        sql += " and " + str(i) + " = '" + my_dict[i] + "' "
                    if 'date' in k['Type']:
                        sql += " and " + str(i) + " = '" + my_dict[i] + "' "

        # look for existing data
        cursor.execute(sql)
        existing = cursor.fetchall()
        if existing is None:
            my_dict['id'] = ""
        else:
            my_dict['id'] = existing[0]['id']

        my_dict['table_name'] = table_name
        my_dict['action'] = "insert"
        return KineticForms.post(my_dict)

    def post(self, my_dict):
        # id is required to be an autonumber primary key.
        # if it does not exist, is 0, or is "", this is a new record.
        try:
            if 'id' not in my_dict:
                my_id = 0
            else:
                my_id = my_dict['id']
        except Exception as e:
            return {"error_code": "9999", "error_msg": "General Error: " + str(e), "data": {"id": "0"}}

        # action is a reserved word.  insert/delete
        try:
            if 'action' not in my_dict:
                my_action = "insert"
            else:
                my_action = my_dict['action']
        except Exception as e:
            return {"error_code": "9999", "error_msg": "General Error: " + str(e), "data": {}}

        # table name is a reserved word.
        try:
            if 'table_name' not in my_dict:
                return {"error_code": "9000", "error_msg": "Table Name not in post dictionary", "data": {}}
            else:
                table_name = my_dict['table_name']
        except Exception as e:
            return {"error_code": "9999", "error_msg": "General Error: " + str(e), "data": {}}

        try:
            conn = Db.connect()
        except pymysql.err.MySQLError as err:
            return {"error_code": "9999", "error_msg": "Error Connecting: " + str(err), "data": {}}

        try:
            cursor = conn.cursor()
        except pymysql.err.MySQLError as err:
            return {"error_code": "9999", "error_msg": "Error Creating Cursor: " + str(err), "data": {}}

        # process insert and update
        if my_action == 'insert' or my_action == 'update':
            if my_id == 0 or my_id == '':
                sql = "insert into " + table_name + "(create_timestamp) values (now())"
                cursor.execute(sql)
                conn.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                m = cursor.fetchone()
                my_id = m['LAST_INSERT_ID()']

            # Get columns in the table.
            columns = []
            sql = "SHOW COLUMNS FROM " + table_name
            try:
                cursor.execute(sql)
                columns = cursor.fetchall()
            except Exception as e:
                return {"error_code": "9999", "error_msg": "General Error: " + str(e), "data": {}}

            for key in my_dict:
                if key != 'table_name' and key != 'id' and key != 'action':
                    column_exists = False
                    for column in columns:
                        if column['Field'] == key:
                            column_exists = True

                    if column_exists:
                        cursor = conn.cursor()
                        sql = "update " + table_name + " set " + key + " = %s where id = %s"
                        v = (my_dict[key], my_id)
                        cursor.execute(sql, v)
                        conn.commit()
        if my_action == 'delete':
            try:
                sql = "delete from " + table_name + " where id = " + my_id
                cursor.execute(sql)
            except Exception as e:
                return {"error_code": "9999", "error_msg": "General Error: " + str(e), "data": {}}

        return {"error_code": "0", "error_msg": "", "data": {"id": str(my_id)}}

