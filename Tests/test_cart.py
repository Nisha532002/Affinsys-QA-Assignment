from playwright.sync_api import sync_playwright

def test_add_product_to_cart():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            args=["--start-maximized"]
        )

        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        # Open Website
        page.goto("https://sauce-demo.myshopify.com/")

        page.wait_for_timeout(3000)

        # Open first product
        page.locator("a[href*='/products/']").first.click()

        page.wait_for_timeout(3000)

        # Capture product name
        product_name = page.locator("h1[itemprop='name']").text_content().strip()

        print("Selected Product:", product_name)

        # Add to Cart
        page.locator("#add").click()

        page.wait_for_timeout(3000)

        # Open Cart
        page.goto("https://sauce-demo.myshopify.com/cart")

        page.wait_for_timeout(3000)

        # Verify Product Exists
        cart_text = page.locator("body").inner_text()

        assert product_name in cart_text

        print("Product successfully added to cart")

        browser.close()