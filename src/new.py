import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth.json") # codegen에서 save한 auth.json을 사용한 로그인 
    page = context.new_page()
    page.goto("https://www.instagram.com/")
    page.get_by_role("link", name="새로운 게시물 만들기").click()
    page.set_input_files('input[type="file"]', f"오늘의_급식.png")
    page.get_by_role("button", name="다음").click()
    page.get_by_role("button", name="다음").click()
    page.get_by_label("문구를 입력하세요").click()
    page.get_by_label("문구를 입력하세요").fill("")
    page.get_by_role("img", name="위치 추가").click()
    page.get_by_placeholder("위치 추가").fill("푸른중학교")
    page.get_by_role("button", name="푸른중학교 Osan, Kyonggi-Do, Korea").click()
    page.get_by_role("button", name="공유하기").click()
    time.sleep(1000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
