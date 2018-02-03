#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~
"""
main script in Referral tools.

search user infomation from tag as command line input.
"""

import html

import db

import scraping


def main():
    """main function do search and generate html. """
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
    user_list = db.select_all_m_qiita_users()
    html.update_page(user_list)


if __name__ == '__main__':
    main()
