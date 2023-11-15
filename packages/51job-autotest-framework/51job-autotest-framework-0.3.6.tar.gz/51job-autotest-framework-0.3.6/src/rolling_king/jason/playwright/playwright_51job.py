from playwright.sync_api import Playwright, sync_playwright, expect
from playwright_common import PlayWrightCommon, LocatorManner
import re


class TestPlaywright(object):

    def run(self, playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://ones.51job.com/project/")
        page.goto("https://ones.51job.com/project/#/")
        page.goto("https://ones.51job.com/project/#/workspace")
        page.goto(
            "https://ones.51job.com/project/#/auth/logout?backUrl=https%3A%2F%2Fones.51job.com%2Fproject%2F%23%2Fworkspace")
        page.goto(
            "https://ones.51job.com/project/#/auth/login?ones_from=https%3A%2F%2Fones.51job.com%2Fproject%2F%23%2Fworkspace")
        page.get_by_placeholder("请输入你的邮箱").click()
        page.get_by_placeholder("请输入你的邮箱").fill("jason.zheng@51job.com")
        page.get_by_placeholder("请输入你的密码").click()
        page.get_by_placeholder("请输入你的密码").fill("Jason1qaz!QAZ")
        page.get_by_role("button", name="登录").click()
        page.get_by_role("link", name="效能管理").click()
        page.get_by_role("link", name="效能管理").click(click_count=3)
        page.get_by_role("menuitem", name="效能管理").first.click()
        page.get_by_label("grid").click()
        page.get_by_role("link", name="测试管理").click()
        page.get_by_role("link", name="测试管理").click()
        page.get_by_role("link", name="测试管理").dblclick()
        page.get_by_role("link", name="测试管理").click(click_count=3)

        # ---------------------
        context.storage_state(path="51auth.json")
        context.close()
        browser.close()

    def recall_record_auth(self, playwright: Playwright) -> None:
        """
        利用上方录制的鉴权51auth.json，可以免登录代码，直接执行登录后的操作即可。
        """
        # print(playwright.devices)  # 可查看所有设备
        iphone13 = playwright.devices['iPhone 13']  # 不需要模拟指定设备则可注释掉。
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="51auth.json")  # 从51auth.json中读取登录态，然后直接开始登录后的操作即可。
        # 若使用录制，则命令为：playwright codegen --load-storage=51auth.json https://ones.51job.com/
        # context = browser.new_context(storage_state="51auth.json", **iphone13)  # 从51auth.json中读取登录态，然后直接开始登录后的操作即可。
        # context = browser.new_context(**{'storage_state':'51auth.json'}, **iphone13)  # 等同于上一行
        # 模拟指定设备：playwright codegen --load-storage=51auth.json --device="iPhone 13" https://ones.51job.com/
        page = context.new_page()
        page.goto("https://ones.51job.com/project/")
        page.goto("https://ones.51job.com/project/#/")
        page.goto("https://ones.51job.com/project/#/workspace")
        page.goto("https://ones.51job.com/project/#/workspace/home")
        PlayWrightCommon.init_by_existing_web(existing_page=page)
        PlayWrightCommon.get_locator(manner=LocatorManner.ROLE, role="link", name="效能管理").click()  # 等同下一行，只是为了验证init_by_existing_web方法正确性。
        # page.get_by_role("link", name="效能管理").click()
        page.get_by_role("link", name="效能管理").click(click_count=3)
        page.get_by_role("menuitem", name="效能管理").first.click()
        page.pause()
        page.get_by_label("grid").click()
        page.get_by_role("link", name="测试管理").click()
        page.get_by_role("link", name="测试管理").click()
        page.get_by_role("link", name="测试管理").dblclick()
        page.get_by_role("link", name="测试管理").click(click_count=3)
        page.pause()
        expect(page).to_have_url(re.compile(".*51job"))
        # ---------------------
        # context.close()
        # browser.close()
        PlayWrightCommon.close_context()
        PlayWrightCommon.close_browser()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        obj: TestPlaywright = TestPlaywright()
        obj.recall_record_auth(playwright)


