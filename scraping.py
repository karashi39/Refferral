#!/usr/bin/env python
# ~*~ coding:utf-8 ~*~
"""
scraping.py in Referral tools.

as of now, use for Qiita only.
"""

import urllib2

from bs4 import BeautifulSoup


def main():
    """main function only called when script executed."""
    while True:
        try:
            tag = raw_input()
            print get_user_list_from_tag(tag)
        except Exception:
            exit()


def get_user_list_from_tag(tag):
    """search user ids from tag."""
    user_list = []
    try:
        tag_top_show_users = list_tag_top_show_users(tag)
        for user in tag_top_show_users:
            user_id = user['qiita_id']
            try:
                user.update(get_user_profile(user_id))
                user_list.append(user)
            except AttributeError as error:
                print 'old format profile in Qiita.'
    except ValueError as error:
        print(error)
    return user_list


def get_user_profile(user_id):
    """scrape user page and return user info as dict."""
    print '[INFO] scraping user page of ' + user_id
    user_profile = {}
    user_profile.update({'qiita_id': user_id})
    url = 'https://qiita.com/' + user_id
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    # user profile
    try:
        profile_class = 'newUserPageProfile_info_body'
        profiles = soup.find_all('div', class_=profile_class)
    except AttributeError as error:
        # when error occurr with this attribute, profile page is old format.
        print(error)
        raise

    site_url = ''
    address = ''
    for profile in profiles:
        try:
            url_icon = profile.find('i', class_='fa-link')
            if url_icon is not None:
                site_url = profile.find('a').get('href')
        except AttributeError as error:
            pass
        try:
            address_icon = profile.find('i', class_='fa-map-marker')
            if address_icon is not None:
                address_icon = profile.find('i', class_='fa-map-marker').unwrap()
                address = profile.string
        except AttributeError as error:
            pass
    user_profile.update({'qiita_site_url': site_url})
    user_profile.update({'qiita_address': address})

    description = ''
    try:
        description = soup.find('div', class_='newUserPageProfile_description').string
        if description is None:
            description = ''
    except AttributeError as error:
        pass
    finally:
        user_profile.update({'qiita_profile': description})

    user_name = ''
    try:
        fullname = soup.find('h3', class_='newUserPageProfile_fullName').find_all('span')
        for name in fullname:
            if name.string is not None:
                user_name += name.string
    except AttributeError as error:
        pass
    finally:
        user_profile.update({'qiita_name': user_name})

    # social link
    try:
        github_class = 'newUserPageProfile_socialLink-github'
        github_url = soup.find('li', class_=github_class).find('a').get('href')
        user_profile.update({'qiita_github_url': github_url})
    except AttributeError as error:
        user_profile.update({'qiita_github_url': ''})
    try:
        twitter_class = 'newUserPageProfile_socialLink-twitter'
        twitter_url = soup.find('li', class_=twitter_class).find('a').get('href')
        user_profile.update({'qiita_twitter_url': twitter_url})
    except AttributeError as error:
        user_profile.update({'qiita_twitter_url': ''})
    try:
        facebook_class = 'newUserPageProfile_socialLink-facebook'
        facebook_url = soup.find('li', class_=facebook_class).find('a').get('href')
        user_profile.update({'qiita_facebook_url': facebook_url})
    except AttributeError as error:
        user_profile.update({'qiita_facebook_url': ''})
    # [todo] more items, more abstract.
    try:
        linkedin_class = 'newUserPageProfile_socialLink-linkedin'
        linkedin_url = soup.find('li', class_=linkedin_class).find('a').get('href')
        user_profile.update({'qiita_linkedin_url': linkedin_url})
    except AttributeError as error:
        user_profile.update({'qiita_linkedin_url': ''})
    try:
        google_class = 'newUserPageProfile_socialLink-googlePlus'
        google_url = soup.find('li', class_=google_class).find('a').get('href')
        user_profile.update({'qiita_google_url': google_url})
    except AttributeError as error:
        user_profile.update({'qiita_google_url': ''})

    return user_profile


def list_tag_top_show_users(tag):
    """scrape tag page and get top show user ids."""
    print '[INFO] scraping tag page of ' + tag
    url = 'https://qiita.com/tags/' + urllib2.quote(tag)
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')

    tag_show_top_list = soup.find('section', class_='tagShowTopList')
    users = tag_show_top_list.find_all('td', class_='tagShowTopList_targetName')

    users_detail = []
    for user in users:
        user_id = user.find('a').get('href').split('/')[1]
        user_image_url = user.find('img').get('src')
        users_detail.append({'qiita_id': user_id, 'qiita_image_url': user_image_url})
    return users_detail


if __name__ == '__main__':
    main()
