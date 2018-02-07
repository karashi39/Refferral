#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~
"""
main script in Referral tools.

search user infomation from tag as command line input.
"""


import html

import sys

import db

import scraping


def main(mode="add"):
    """switch functions by the command line option."""
    if mode == "add":
        add_users()
    elif mode == "del":
        delete_users()
    update_html()


def add_users():
    """search and add user."""
    while True:
        try:
            tag = raw_input()
            user_list = scraping.get_user_list_from_tag(tag)
            for user in user_list:
                try:
                    db.insert_into_m_qiita_users(user)
                except db.mysql.connector.errors.IntegrityError as error:
                    # when the user registered already.
                    print error
        except KeyboardInterrupt:
            break


def delete_users():
    """delete user."""
    while True:
        try:
            user_id = raw_input()
            user_id = user_id.replace('https://qiita.com/', '')
            user_id = user_id.replace('@', '')
            db.logical_delete_m_qiita_users(user_id)
        except KeyboardInterrupt:
            break


def update_html():
    """update html by all un-deleted users."""
    user_list = db.select_all_m_qiita_users()
    html.update_page(user_list)


if __name__ == '__main__':
    mode = sys.argv[1]
    main(mode)
