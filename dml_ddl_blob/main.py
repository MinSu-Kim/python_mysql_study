import inspect

from dml.dml_select import query_with_fetchall
from dml_ddl_blob.blob_query import insert_blob, read_blob, update_blob, delete_blob
from dml_ddl_blob.blob_read_write import read_file_blob
from dml_ddl_blob.connection_pool import ConnectionPool


def connection_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    connect_pool = ConnectionPool.get_instance()
    connection = connect_pool.get_connection()
    print("connection : ", connection)


insert_query = "INSERT INTO images (name, pic) VALUES(%s, %s)"
update_query = "UPDATE images SET name=%s, pic=%s WHERE no=%s"
read_query = "SELECT pic FROM images WHERE no = %s"
delete_query = "delete from images where no = %s"
select_query = "select no, name from images"


def insert_blob_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    query_with_fetchall(select_query)
    insert_blob(insert_query, 'python-logo', 'img/python-logo.png')
    insert_blob(insert_query, 'google-logo', 'img/google-logo.png')
    query_with_fetchall(select_query)


def read_blob_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    query_with_fetchall(select_query)
    read_blob(read_query, 1, "img/read-python.png")
    read_blob(read_query, 2, "img/read-google.png")
    query_with_fetchall(select_query)


def update_blob_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    query_with_fetchall(select_query)
    update_blob(update_query, 'pycharm-logo', 'img/pycharm-logo.png', 1)
    query_with_fetchall(select_query)


def delete_blob_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    query_with_fetchall(select_query)
    read_blob(read_query, 1, "img/read-pycharm.png")
    delete_blob(delete_query, 1)
    query_with_fetchall(select_query)


if __name__ == "__main__":
    connection_test()

    # create_table()

    # data = read_file_blob('img/python-logo.png')
    # print(type(data))

    # insert_blob_test()
    # read_blob_test()
    # update_blob_test()
    delete_blob_test()