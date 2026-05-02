from playwright.sync_api import sync_playwright

def test_dashboard_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://127.0.0.1:5000")

        # Check title
        assert "System Health Dashboard" in page.title()

        # Check UI elements exist
        assert page.locator("text=CPU").is_visible()
        assert page.locator("text=Memory").is_visible()
        assert page.locator("text=Disk").is_visible()

        browser.close()


def test_api_data():
    import requests

    response = requests.get("http://127.0.0.1:5000/data")
    data = response.json()

    assert "cpu" in data
    assert "memory" in data
    assert "disk" in data