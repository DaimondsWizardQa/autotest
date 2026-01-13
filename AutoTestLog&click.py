from selene import browser

browser.config.hold_browser_open = True


def test_login_qa_guru():
    browser.open('https://school.qa.guru')

    browser.element('[name="email"]').type('qagurubot@gmail.com')
    browser.element('[name="password"]').type('somepasshere').press_enter()

    browser.element(
        '[href="/teach/control/stream/view/id/465999013"]'
    ).click()