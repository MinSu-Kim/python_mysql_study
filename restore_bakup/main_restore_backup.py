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
/etc/apparmor.d/usr.sbin.mysqld를 편집

추가
**/home/hyunmu/DB/sampdb/ r, 
/home/hyunmu/DB/sampdb/* rw,**

MySQL 재실행 후 외부 파일 읽기가 정상동작하는 것을 확인


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
