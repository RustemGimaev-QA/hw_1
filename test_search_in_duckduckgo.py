from selene import browser, have


# Поиск на DuckDuckGo
def test_succesfull_register_click():
    browser.open('https://duckduckgo.com/')
    browser.element('[type="text"]').type('https://jwt.is/')
    browser.element('[type="submit"]').click()
    browser.element('[id="r1-0"]').should(have.text('jwt.is'))
    browser.element('[href="https://jwt.is/"]').click()
    browser.element('[class="decoded"]').should(have.text('Decoded'))
    browser.quit()