#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
db.py in Referral tools.

as of now, use for qiita only.
"""

import re

import mysql.connector


HOST = ''
DATABASE = ''
USER = ''
PASSWORD = ''


def main():
    """when executed as script, do initialize."""
    init_tables()


def init_tables():
    """initialize with creating tables."""
    # drop_table_m_candidates()
    # drop_table_m_qiita_users()
    create_table_m_candidates()
    create_table_m_qiita_users()


def drop_table_m_candidates():
    """drop m_candidates table."""
    sql = 'DROP TABLE m_candidates;'
    exe_ddl(sql)


def drop_table_m_qiita_users():
    """drop m_qiita_users table."""
    sql = 'DROP TABLE m_qiita_users;'
    exe_ddl(sql)


def create_table_m_candidates():
    """create m_candidates table."""
    sql = 'CREATE TABLE m_candidates'
    sql += '( candidate_id INT AUTO_INCREMENT'
    sql += ', candidate_name VARCHAR(100) NOT NULL'
    sql += ', wantedly_id VARCHAR(100) UNIQUE'
    sql += ', qiita_id VARCHAR(100) UNIQUE'
    sql += ', teratail_id VARCHAR(100) UNIQUE'
    sql += ', github_id VARCHAR(100) UNIQUE'
    sql += ', twitter_id VARCHAR(100) UNIQUE'
    sql += ', facebook_id VARCHAR(100) UNIQUE'
    sql += ', delete_flg TINYINT NOT NULL'
    sql += ', PRIMARY KEY (candidate_id)'
    sql += ') ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    exe_ddl(sql)


def create_table_m_qiita_users():
    """create m_qiita_users table."""
    sql = 'CREATE TABLE m_qiita_users'
    sql += '( qiita_id VARCHAR(100)'
    sql += ', qiita_name VARCHAR(100) NOT NULL'
    sql += ', qiita_image_url VARCHAR(100) NOT NULL'
    sql += ', qiita_profile VARCHAR(200)'
    sql += ', qiita_address VARCHAR(100)'
    sql += ', qiita_site_url VARCHAR(100)'
    sql += ', qiita_github_url VARCHAR(100)'
    sql += ', qiita_twitter_url VARCHAR(100)'
    sql += ', qiita_facebook_url VARCHAR(100)'
    sql += ', qiita_linkedin_url VARCHAR(100)'
    sql += ', qiita_google_url VARCHAR(100)'
    sql += ', delete_flg TINYINT NOT NULL'
    sql += ', PRIMARY KEY (qiita_id)'
    sql += ') ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    exe_ddl(sql)


def insert_into_m_qiita_users(qiita_user_profile):
    """insert user infomation into m_qiita_users from arg dict qiita_user_profile."""
    sql = 'INSERT INTO m_qiita_users'
    sql += ' (qiita_id'
    sql += ', qiita_name'
    sql += ', qiita_address'
    sql += ', qiita_profile'
    sql += ', qiita_image_url'
    sql += ', qiita_site_url'
    sql += ', qiita_github_url'
    sql += ', qiita_twitter_url'
    sql += ', qiita_facebook_url'
    sql += ', qiita_google_url'
    sql += ', qiita_linkedin_url'
    sql += ', delete_flg'
    sql += ') VALUES '
    sql += '( "' + qiita_user_profile['qiita_id'] + '"'
    sql += ', "' + qiita_user_profile['qiita_name'] + '"'
    sql += ', "' + qiita_user_profile['qiita_address'] + '"'
    sql += ', "' + re.sub('"', '', qiita_user_profile['qiita_profile']) + '"'
    sql += ', "' + qiita_user_profile['qiita_image_url'] + '"'
    sql += ', "' + qiita_user_profile['qiita_site_url'] + '"'
    sql += ', "' + qiita_user_profile['qiita_github_url'] + '"'
    sql += ', "' + qiita_user_profile['qiita_twitter_url'] + '"'
    sql += ', "' + qiita_user_profile['qiita_facebook_url'] + '"'
    sql += ', "' + qiita_user_profile['qiita_google_url'] + '"'
    sql += ', "' + qiita_user_profile['qiita_linkedin_url'] + '"'
    sql += ', 0'
    sql += ');'

    exe_dml(sql)


def select_all_m_qiita_users():
    """select all m_qiita_users and return as dict."""
    sql = 'SELECT'
    sql += ' qiita_id'
    sql += ', qiita_name'
    sql += ', qiita_address'
    sql += ', qiita_profile'
    sql += ', qiita_image_url'
    sql += ', qiita_site_url'
    sql += ', qiita_github_url'
    sql += ', qiita_twitter_url'
    sql += ', qiita_facebook_url'
    sql += ', qiita_google_url'
    sql += ', qiita_linkedin_url'
    sql += ' FROM m_qiita_users'
    sql += ' WHERE delete_flg = 0'
    list_results = exe_select_fetch_all(sql)

    dict_results = []
    for result in list_results:
        user = {}
        user.update({'qiita_id': result[0]})
        user.update({'qiita_name': result[1]})
        user.update({'qiita_address': result[2]})
        user.update({'qiita_profile': result[3]})
        user.update({'qiita_image_url': result[4]})
        user.update({'qiita_site_url': result[5]})
        user.update({'qiita_github_url': result[6]})
        user.update({'qiita_twitter_url': result[7]})
        user.update({'qiita_facebook_url': result[8]})
        user.update({'qiita_google_url': result[9]})
        user.update({'qiita_linkedin_url': result[10]})
        dict_results.append(user)

    return dict_results


def logical_delete_m_qiita_users(qiita_id):
    """delete an user logically from m_qiita_users."""
    sql = 'UPDATE m_qiita_users'
    sql += ' SET delete_flg = 1'
    sql += ' WHERE qiita_id = "' + qiita_id + '"'
    exe_dml(sql)


def exe_select_fetch_all(sql):
    """execute SELECT statement and return results of fetch all."""
    print sql

    conn = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    conn.close

    return results


def exe_ddl(sql):
    """execute DDL statement."""
    print sql

    conn = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except mysql.connector.errors.ProgrammingError as error:
        print error
    conn.close


def exe_dml(sql):
    """execute INSERT/UPDATE/DELETE statement and commit."""
    print sql

    conn = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close

if __name__ == '__main__':
    main()
