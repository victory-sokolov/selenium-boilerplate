from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.Config import Config
from utils.helpers import get_random_file_entry, read_configs


class Driver:
    config = Config()
    extension_path = ""

    @staticmethod
    def chrome():
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-notifications')
        options.add_argument('--verbose')
        options.add_argument("user-data-dir=selenium")
        options.add_argument(f'--proxy-server=')
        # Load Chrome extension
        # Reference: https://coreygoldberg.blogspot.com/2018/09/python-using-chrome-extensions-with.html
        options.add_argument(
            '--load-extension={}'.format(Driver.extension_path)
        )
        options.add_argument(
            f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
        options.add_experimental_option("prefs", {
            'download.default_directory': Driver.config.DOWNLOAD_DIR,
            'download.prompt_for_download': False,
            'download.directory_upgrade': True,
            'safebrowsing.enabled': True,
            'useAutomationExtension': False,
            'excludeSwitches': ['enable-automation'],
            'disk-cache-size': 4096
        })
        driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=options
        )
        driver.set_page_load_timeout(120)
        driver.execute_script(
            "var s=window.document.createElement('script'); s.src='javascript.js';window.document.head.appendChild(s);")
        return driver

    @staticmethod
    def firefox():
        profile = webdriver.FirefoxOptions()
        profile.set_preference("dom.push.enabled", False)
        profile.headless = Driver.config.INTERFACE
        profile.set_preference("browser.download.panel.shown", False)
        profile.set_preference(
            "browser.helperApps.neverAsk.openFile", "text/csv,application/vnd.ms-excel")
        profile.set_preference(
            "browser.helperApps.neverAsk.saveToDisk", "text/csv,application/vnd.ms-excel")
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference(
            "browser.download.dir", Driver.config.DOWNLOAD_DIR)

        driver = webdriver.Firefox(
            GeckoDriverManager().install(),
            firefox_options=profile
        )

        driver.maximize_window()
        driver.set_page_load_timeout(120)
        #firefox_set_proxy()
        return driver

    def firefox_set_proxy(self):
        driver = Driver.firefox()
        proxy = get_random_file_entry(Driver.config.PROXY_FILE)
        proxy = get_proxy()['proxy'].split(":")
        host = proxy[0]
        port = int(proxy[1])
        driver.execute("SET_CONTEXT", {"context": "chrome"})

        try:
            driver.execute_script("""
            Services.prefs.setIntPref('network.proxy.type', 1);
            Services.prefs.setCharPref("network.proxy.http", arguments[0]);
            Services.prefs.setIntPref("network.proxy.http_port", arguments[1]);
            Services.prefs.setCharPref("network.proxy.ssl", arguments[0]);
            Services.prefs.setIntPref("network.proxy.ssl_port", arguments[1]);
            """, host, port)
        finally:
            driver.execute("SET_CONTEXT", {"context": "content"})
