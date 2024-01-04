from selenium.webdriver.common.by import By


#class DesktopLocators:

    #downloaded_app = (By.XPATH, '//android.widget.TextView[@content-desc="Predicted app: Play Store"]')


class LoginPageLocators:

    sign_in_button = (By.XPATH, '//android.widget.Button[@resource-id="com.linkedin.android:id/growth_prereg_fragment_login_button"]')
    email_input = (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.linkedin.android:id/growth_login_join_fragment_email_address"]')
    password_input = (By.XPATH, '//android.widget.EditText[@resource-id="com.linkedin.android:id/growth_login_join_fragment_password"]')
    continue_button = (By.XPATH, '//android.widget.Button[@resource-id="com.linkedin.android:id/growth_login_fragment_sign_in"]')
    skip_button = (By.XPATH, '//android.widget.Button[@resource-id="com.linkedin.android:id/notif_permission_signin_text"]')


class MainPageLocators:

    search_bar = (By.XPATH, '//android.widget.TextView[@resource-id="com.linkedin.android:id/search_bar_text"]')
    my_profile_button = (By.XPATH, '//android.widget.ImageView[@content-desc="My Profile and Communities"]')


class ViewProfileLocators:

    settings_button = (By.XPATH, '//android.widget.Button[@resource-id="com.linkedin.android:id/home_nav_premium_upsell_text_view"]')
    sign_out_button = (By.XPATH, '//android.webkit.WebView[@resource-id="com.linkedin.android:id/infra_web_viewer_webview"]')
    sign_out_button2 = (By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')


class SignOutLocators:
    sign_out_header = (By.XPATH, "//android.widget.TextView[@text=\"Don't miss your next opportunity. Sign in to stay updated on your professional world.\"]")

