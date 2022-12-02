###################################################################################################
##################################BLACK MAGIC DO NOT TOUCH#########################################
###################################################################################################
##################################BLACK MAGIC DO NOT TOUCH#########################################
###################################################################################################
##################################BLACK MAGIC DO NOT TOUCH#########################################
###################################################################################################
import os
import glob
import platform

from browser_cookie3 import chrome, firefox, safari


DOMAIN_NAME = 'adventofcode'


def get_cookies():
    if 'microsoft-standard' in platform.uname().release:
        WSL_ROOT_DIR = os.path.join('/mnt', 'c',)
        WINDOWS_CHROME_COOKIES = os.path.join(WSL_ROOT_DIR, 'Users', '*', 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Network', 'Cookies')
        WINDOWS_FIREFOX_COOKIES = os.path.join(WSL_ROOT_DIR, 'Users', '*', 'AppData', 'Roaming', 'Mozilla', 'Firefox', 'Profiles', '*', 'cookies.sqlite')

        for file, cookie_jar in [
            (WINDOWS_CHROME_COOKIES, chrome),
            (WINDOWS_FIREFOX_COOKIES, firefox)
        ]:
            for cookie_file in glob.glob(file):
                cookie = cookie_jar(domain_name=DOMAIN_NAME, cookie_file=cookie_file)
                if cookie:
                    return cookie
        raise Exception('Could not find the cookie for WSL')

    for browser_cookies in [chrome, firefox, safari]:
        cookie = browser_cookies(domain_name='adventofcode')
        if cookie:
            return cookie


COOKIES = get_cookies()

if __name__ == '__main__':
    print(COOKIES)
