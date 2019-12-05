import inspect
import pandas as pd

from dml.create_procedure import create_procedure
from dml.dml_insert_update_delete import insert_product, insert_products, update_product, delete_product
from dml.dml_procedure import call_sale_stat_sp, call_order_price_by_issale
from dml.dml_select import query_with_fetchone, query_with_fetchall, query_with_fetchall2, \
    query_with_fetchall_by_code, query_with_fetchmany
from dml.connection_pool import ConnectionPool
from dml.transaction_test import transaction_fail1, transaction_fail2, transaction_success

product_select_sql = "select * from product"
sale_select_sql = "select * from sale"


def connection_pool_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    connect_pool = ConnectionPool.get_instance()
    connection = connect_pool.get_connection()
    print("connection : ", connection)


def fetch_one_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    query_with_fetchone(product_select_sql)
    query_with_fetchone(sale_select_sql)


def fetch_all_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    query_with_fetchall(product_select_sql)
    query_with_fetchall(sale_select_sql)


def fetchall2_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    res = query_with_fetchall2(product_select_sql)
    print(type(res), 'size = ', len(res))
    for pno, p_name in res:
        print(pno, p_name)
    print()
    res = query_with_fetchall2(sale_select_sql)
    print(type(res), 'size = ', len(res))
    for no, code, price, sale_cnt, m_rate in res:
        print(no, code, price, sale_cnt, m_rate)


def select_where_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    product_select_where01 = "select * from product where code = %s"
    res = query_with_fetchall_by_code(product_select_where01, 'A001')
    print(res)
    product_select_where02 = "select * from product where code = '{}'".format('A001')
    query_with_fetchall(product_select_where02)


def fetch_many_test():
    print("\n== {}() ==".format(inspect.stack()[0][3]))
    query_with_fetchmany(product_select_sql)
    query_with_fetchmany(sale_select_sql)


def select_test():
    print("\n______ {}() ______".format(inspect.stack()[0][3]))
    fetch_one_test()
    fetchall2_test()
    select_where_test()
    fetch_many_test()


insert_sql = "Insert into product values(%s, %s)"


def insert_test():
    print("\n______ {}() ______".format(inspect.stack()[0][3]))
    query_with_fetchall(product_select_sql)
    insert_product(insert_sql, 'C001', '라떼')
    query_with_fetchall(product_select_sql)
    print()
    products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼4')]
    insert_products(insert_sql, products)
    query_with_fetchall(product_select_sql)


def update_test():
    product_select_where01 = "select * from product where code = %s"
    res = query_with_fetchall_by_code(product_select_where01, 'C001')
    print(res)
    print()

    update_sql = "update product set name = %s where code = %s"
    update_product(update_sql, '라떼수정', 'C001')

    product_select_where01 = "select * from product where code = %s"
    res = query_with_fetchall_by_code(product_select_where01, 'C001')
    print(res)


def delete_test():
    select_sql = "select code, name from product where code like 'C___'"
    res = query_with_fetchall2(select_sql)
    columns_list = ['code', 'name']
    df = pd.DataFrame(res, columns=columns_list)
    print(df)
    delete_sql = "delete from product where code = %s"
    delete_product(delete_sql, 'C004')
    for code, name in (query_with_fetchall2(select_sql)):
        print(code, " ", name)


def transaction_test():
    transaction_fail1()
    transaction_fail2()
    transaction_success()


if __name__ == "__main__":
    # connection_pool_test()
    # select_test()
    # insert_test()
    # update_test()
    # delete_test()

    # transaction_test()
    # create_procedure()
    call_sale_stat_sp('proc_sale_stat')
    print()
    call_order_price_by_issale('proc_saledetail_orderby', False)
    print()
    call_order_price_by_issale('proc_saledetail_orderby', True)