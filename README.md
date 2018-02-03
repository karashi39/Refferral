# Refferral Tool.

Tool for searching new employees.
As of now, use it on Qiita only.

### INSTALL

1. prepare Python 2.x.
1. prepare library for python with a good feeling.
1. prepare MySQL.
1. rewrite connection setting for MySQL on db.py
1. run db.py for initialize Database  
`$ python db.py`

### USAGE

1. run __main__.py for searching Qiita users. type Qiita Tag.
1. quit input phase with `Ctrl + C` (KeyboardInterrupt)
1. then qiita_users.html will be generated. open it with webbrowzer.

#### EXAMPLE

```
$ python __main__.py
Ruby
(log will flow)
^CSELECT qiita_id, qiita_name, qiita_address, qiita_profile, qiita_image_url, qiita_site_url, qiita_github_url, qiita_twitter_url, qiita_facebook_url, qiita_google_url, qiita_linkedin_url FROM m_qiita_users WHERE delete_flg = 0
```

### TEST

None. 

**TODO: write test code.**

------
Masamichi Sato 2018. PSF Lisence.
