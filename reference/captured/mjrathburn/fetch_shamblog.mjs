import { chromium } from 'playwright';

const urls = [
  'https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/',
  'https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/',
  'https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-3/',
  'https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/',
];

const browser = await chromium.launch({ headless: true });

for (const url of urls) {
  const page = await browser.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
    // Wait a bit for any JS rendering
    await page.waitForTimeout(2000);
    
    // Try to get the article content
    const content = await page.evaluate(() => {
      // Try common article selectors
      const selectors = ['article', '.entry-content', '.post-content', '.content', 'main', '#content'];
      for (const sel of selectors) {
        const el = document.querySelector(sel);
        if (el && el.innerText.trim().length > 200) {
          return el.innerText.trim();
        }
      }
      // fallback to body
      return document.body.innerText.trim();
    });
    
    const slug = url.split('/').filter(Boolean).pop();
    const fs = await import('fs');
    fs.writeFileSync(`/tmp/shamblog_${slug}.txt`, content);
    console.log(`OK: ${slug} (${content.length} chars)`);
  } catch (e) {
    console.log(`FAIL: ${url} - ${e.message}`);
  }
  await page.close();
}

await browser.close();
