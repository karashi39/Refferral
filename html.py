#!/usr/bin/env python
# ~*~ coding:utf-8 ~*~
"""
html.py in Referral tools.

generate user info in Qiita only.
"""

import db


def main():
    """main function for execute as script."""
    user_list = db.select_all_m_qiita_users()
    update_page(user_list)


def update_page(user_list):
    """over write qiita_users.html with user_list."""
    # header
    html = '<html>'
    html += '<head>'
    html += '  <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css">'
    html += '  <link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css">'
    html += '  <link rel="stylesheet" href="referral.css">'
    html += '  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js">'
    html += '  </script>'
    html += '  <script>function hidev(qiita_id){$(qiita_id).hide()}</script>'
    html += '</head>'
    html += '<body>'
    html += '<div class="user_area">'
    html += '<div class="pure-g">'

    # user_card
    for user in user_list:
        qiita_url = 'https://qiita.com/' + user['qiita_id']
        html += '  <div id="div' + user['qiita_id'] + '" class="pure-u-1-4">'
        html += '    <div class="user_card">'
        html += '      <div class="user_card_right" style="float:right">'
        html += '        <a href="' + qiita_url + '" target="_blank">'
        html += '          <img src="' + user['qiita_image_url'] + '">'
        html += '        </a>'
        html += '      </div>'
        html += '      <div class="user_card_left">'
        html += '        <h4>@' + user['qiita_id'] + '</h4>'
        html += '        <h3>' + user['qiita_name'] + '</h3>'
        html += '        <p>' + user['qiita_profile'] + '</p>'
        html += '        <p>' + user['qiita_address'] + '</p>'
        html += '      </div>'
        html += '      <div class="user_card_bottom" style="clear:both">'
        if user['qiita_site_url'] != '':
            html += '    <a href="' + user['qiita_site_url'] + '" target="_blank">'
            html += '      <img src="image/link.png" style="width:25px"></a>'
        if user['qiita_github_url'] != '':
            html += '    <a href="' + user['qiita_github_url'] + '" target="_blank">'
            html += '<img src="image/github.png" style="width:25px"></a>'
        if user['qiita_facebook_url'] != '':
            html += '    <a href="' + user['qiita_facebook_url'] + '" target="_blank">'
            html += '<img src="image/facebook.png" style="width:25px"></a>'
        if user['qiita_twitter_url'] != '':
            html += '    <a href="' + user['qiita_twitter_url'] + '" target="_blank">'
            html += '<img src="image/twitter.png" style="width:25px"></a>'
        if user['qiita_google_url'] != '':
            html += '    <a href="' + user['qiita_google_url'] + '" target="_blank">'
            html += '<img src="image/google.png" style="width:25px"></a>'
        if user['qiita_linkedin_url'] != '':
            html += '    <a href="' + user['qiita_linkedin_url'] + '" target="_blank">'
            html += '<img src="image/linkedin.png" style="width:25px"></a>'
        html += '        <input type="button" value="bye" class="button-error pure-button"'
        html += '          onClick="hidev(\'#div' + user['qiita_id'] + '\')"/><br/>'
        html += '      </div>'
        html += '    </div>'
        html += '  </div>'

    # footer
    html += '</div>'
    html += '</div>'
    html += '</body>'
    html += '</html>'
    with open('qiita_users.html', 'w') as f:
        f.write(html.encode('utf-8'))


if __name__ == '__main__':
    main()
