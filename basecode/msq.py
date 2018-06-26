from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

config = {
     'user' : 'root',
     'password' : 'root',
     'host' : '127.0.0.1',
     'raise_on_warnings' : True,
 }


DB_NAME = 'bitch'

Tables = {}
Tables['test1'] = (
    '''
    create table  test1(
        test1id int(12) not null auto_increment,
        testname varchar(20) not null,
        testdate date not null,
        testyn enum('Y','N') not null,
        primary key(test1id)
    )ENGINE=InnoDB'''
)

Tables['test2'] = (
    '''
    create table test2(
        test2id int(12) not null auto_increment,
        test2name varchar(20) not null,
        test1relid int(12) not null,
        primary key(test2id),
        constraint t1t2 foreign key (test1relid) 
        references test1 (test1id) on delete cascade
    )ENGINE=InnoDB'''
)

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def createdatabase(cursor):
    try:
        cursor.execute('create database {} default character set "utf8"'.format(DB_NAME))
    except mysql.connector.Error as err:
        print('Failed creating database: {}'.format(err))
        exit(1)


try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        createdatabase(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)