from selene import browser, have


# Поиск на DuckDuckGo
def test_succesfull_register_click():
    browser.open('https://duckduckgo.com/')
    browser.element('[type="text"]').type('https://jwt.io/')
    browser.element('[type="submit"]').click()
    browser.element('[id="r1-0"]').should(have.text('JWT.IO'))
    browser.element('[href="https://jwt.io/"]').click()
    browser.element('[class="container"]').should(have.text('Debugger'))
    browser.quit()