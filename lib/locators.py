from selenium.webdriver.common.by import By


class LoginPageLocators:

    sign_in_button = (By.XPATH, '//android.widget.Button[@resource-id="com.linkedin.android:id/growth_prereg_fragment_login_button"]')
    email_input = (By.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="com.linkedin.android:id/growth_login_join_fragment_email_address"]')
    password_input = (By.XPATH, '//android.widget.EditText[@resource-id="com.linkedin.android:id/growth_login_join_fragment_password"]')
    continue_button = (By.XPATH, '//android.widget.Button[@resource-id="com.linkedin.android:id/growth_login_fragment_sign_in"]')
    skip_button = (By.XPATH, '//android.widget.Button[@resource-id="com.linkedin.android:id/notif_permission_signin_text"]')


