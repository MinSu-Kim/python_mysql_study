from restore_bakup.backup_restore import BackupRestore

if __name__ == "__main__":
    backup_restore = BackupRestore()
    # backup_restore.data_backup('product')
    # backup_restore.data_backup('sale')
    backup_restore.data_restore('product')
    backup_restore.data_restore('sale')


"""
Ubuntu Linux 

SHOW VARIABLES LIKE "secure_file_priv";

/*
확인후 추가
[mysqld]
secure_file_priv=""
*/

원하는 경로에 (Errcode: 13 - Permission denied) 해결책 https://dreamlog.tistory.com/563

SELECT * FROM product
INTO OUTFILE '/tmp/product.txt'
CHARACTER SET 'UTF8'
FIELDS TERMINATED by ','
LINES TERMINATED by '\r\n';

delete from product;
select * from product;

LOAD DATA LOCAL INFILE '/tmp/product.txt'
INTO TABLE product
character set 'UTF8'
fields TERMINATED by ','
LINES TERMINATED by '\r\n';

단 /tmp/product.txt, /tmp/sale.txt 소유자는 mysql.mysql 삭제 필요
"""
