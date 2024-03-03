from playwright.sync_api import Page, expect


def test_wiki_1(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role('link', name='English').click()
    expect(page.get_by_text('Welcome to Wikipedia,')).to_be_visible()


def test_wiki_2(page: Page):
    page.goto("https://www.wikipedia.org/")
    page.get_by_role('link', name='English').click()
    expect(page.get_by_text('Welcome to Wikipedia,')).to_be_visible()
    page.get_by_role('link', name='View source').click()
    page.locator('#ca-talk').click()
    expect(page.locator("#firstHeading")).to_have_text('Talk:Main Page')
