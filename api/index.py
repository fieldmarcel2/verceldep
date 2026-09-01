
from flask import Flask, request
import requests

app = Flask(__name__)


# Home route
@app.get("/")
def get_home():
    return "Welcome to Product Rating API"


# Test route
@app.get("/test")
def test():
    return {
        "status": "success",
        "message": "API is working!"
    }


# Blueprint route — unique interactive API docs page
@app.get("/blueprint")
def blueprint():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Product Rating API — Blueprint</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #0a0a0f;
      --surface: #111118;
      --border: #1e1e2e;
      --accent: #7c6af7;
      --accent2: #a78bfa;
      --green: #34d399;
      --blue: #60a5fa;
      --text: #e2e8f0;
      --muted: #64748b;
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', sans-serif;
      min-height: 100vh;
    }

    /* Animated grid background */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(124,106,247,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(124,106,247,0.04) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
      z-index: 0;
    }

    .wrapper { position: relative; z-index: 1; max-width: 860px; margin: 0 auto; padding: 60px 24px; }

    /* Header */
    .header { text-align: center; margin-bottom: 64px; }
    .badge {
      display: inline-flex; align-items: center; gap: 8px;
      background: rgba(124,106,247,0.12); border: 1px solid rgba(124,106,247,0.3);
      color: var(--accent2); padding: 6px 16px; border-radius: 999px;
      font-size: 0.75rem; font-weight: 600; letter-spacing: 0.08em;
      text-transform: uppercase; margin-bottom: 24px;
    }
    .badge-dot { width: 7px; height: 7px; background: var(--green); border-radius: 50%; animation: pulse 2s infinite; }
    @keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.5;transform:scale(1.3)} }

    h1 {
      font-size: clamp(2rem, 5vw, 3.2rem); font-weight: 900; line-height: 1.1;
      background: linear-gradient(135deg, #fff 0%, var(--accent2) 60%, var(--blue) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      margin-bottom: 16px;
    }
    .subtitle { color: var(--muted); font-size: 1rem; line-height: 1.6; max-width: 520px; margin: 0 auto; }

    /* Info strip */
    .info-strip {
      display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; margin-bottom: 56px;
    }
    .chip {
      display: flex; align-items: center; gap: 8px;
      background: var(--surface); border: 1px solid var(--border);
      border-radius: 10px; padding: 10px 18px; font-size: 0.82rem; color: var(--muted);
    }
    .chip strong { color: var(--text); }
    .chip-icon { font-size: 1rem; }

    /* Section label */
    .section-label {
      font-size: 0.7rem; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase;
      color: var(--muted); margin-bottom: 20px; display: flex; align-items: center; gap: 12px;
    }
    .section-label::after { content:''; flex:1; height:1px; background: var(--border); }

    /* Endpoint card */
    .card {
      background: var(--surface); border: 1px solid var(--border); border-radius: 16px;
      padding: 28px; margin-bottom: 16px;
      transition: border-color .25s, transform .2s, box-shadow .2s;
    }
    .card:hover {
      border-color: rgba(124,106,247,0.4);
      transform: translateY(-2px);
      box-shadow: 0 8px 32px rgba(124,106,247,0.08);
    }

    .card-top { display: flex; align-items: flex-start; gap: 16px; flex-wrap: wrap; }
    .method {
      font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; font-weight: 600;
      padding: 4px 12px; border-radius: 6px; letter-spacing: 0.05em; flex-shrink: 0;
    }
    .method.GET { background: rgba(52,211,153,0.12); color: var(--green); border: 1px solid rgba(52,211,153,0.3); }

    .path {
      font-family: 'JetBrains Mono', monospace; font-size: 1rem; font-weight: 600; color: var(--text);
    }
    .param { color: var(--accent2); }

    .desc { color: var(--muted); font-size: 0.88rem; margin-top: 10px; line-height: 1.6; }

    .tags { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px; }
    .tag {
      font-size: 0.7rem; padding: 3px 10px; border-radius: 999px;
      background: rgba(96,165,250,0.08); border: 1px solid rgba(96,165,250,0.2); color: var(--blue);
    }

    /* Example block */
    .example {
      margin-top: 20px; border-top: 1px solid var(--border); padding-top: 18px;
    }
    .example-label { font-size: 0.7rem; font-weight: 600; color: var(--muted); letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 8px; }
    .code {
      font-family: 'JetBrains Mono', monospace; font-size: 0.82rem;
      background: rgba(0,0,0,0.4); border: 1px solid var(--border); border-radius: 10px;
      padding: 14px 18px; color: #a5f3fc; line-height: 1.6; overflow-x: auto;
    }
    .code .comment { color: var(--muted); }
    .code .keyword { color: var(--accent2); }

    /* Try it button */
    .try-btn {
      display: inline-flex; align-items: center; gap: 8px; margin-top: 16px;
      background: linear-gradient(135deg, var(--accent), #6366f1);
      color: #fff; border: none; border-radius: 8px; padding: 9px 20px;
      font-size: 0.82rem; font-weight: 600; cursor: pointer; text-decoration: none;
      transition: opacity .2s, transform .15s;
    }
    .try-btn:hover { opacity: 0.88; transform: translateY(-1px); }

    /* Response demo */
    .resp-demo {
      background: rgba(0,0,0,0.5); border: 1px solid var(--border); border-radius: 10px;
      padding: 14px 18px; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem;
      color: #86efac; margin-top: 12px; display: none;
    }
    .resp-demo.visible { display: block; animation: fadeIn .3s ease; }
    @keyframes fadeIn { from{opacity:0;transform:translateY(4px)} to{opacity:1;transform:translateY(0)} }

    /* Footer */
    .footer { text-align: center; margin-top: 64px; color: var(--muted); font-size: 0.8rem; line-height: 1.8; }
    .footer a { color: var(--accent2); text-decoration: none; }
    .footer a:hover { text-decoration: underline; }
  </style>
</head>
<body>
<div class="wrapper">

  <!-- Header -->
  <div class="header">
    <div class="badge"><span class="badge-dot"></span> Live API</div>
    <h1>Product Rating API</h1>
    <p class="subtitle">Filter and retrieve products by category and minimum rating. Powered by Flask &amp; DummyJSON.</p>
  </div>

  <!-- Info chips -->
  <div class="info-strip">
    <div class="chip"><span class="chip-icon">⚡</span> Base URL: <strong>/</strong></div>
    <div class="chip"><span class="chip-icon">📦</span> Source: <strong>dummyjson.com</strong></div>
    <div class="chip"><span class="chip-icon">🔓</span> Auth: <strong>None required</strong></div>
    <div class="chip"><span class="chip-icon">📄</span> Format: <strong>JSON</strong></div>
  </div>

  <!-- Endpoints -->
  <div class="section-label">Endpoints</div>

  <!-- GET / -->
  <div class="card">
    <div class="card-top">
      <span class="method GET">GET</span>
      <span class="path">/</span>
    </div>
    <p class="desc">Health / welcome endpoint. Returns a greeting message confirming the API is alive.</p>
    <div class="tags"><span class="tag">health</span><span class="tag">root</span></div>
    <div class="example">
      <div class="example-label">Response</div>
      <div class="code">"Welcome to Product Rating API"</div>
    </div>
  </div>

  <!-- GET /test -->
  <div class="card">
    <div class="card-top">
      <span class="method GET">GET</span>
      <span class="path">/test</span>
    </div>
    <p class="desc">Smoke test route. Confirms the server is running and returning structured JSON responses.</p>
    <div class="tags"><span class="tag">health</span><span class="tag">test</span></div>
    <div class="example">
      <div class="example-label">Response</div>
      <div class="code">{\n  <span class="keyword">"status"</span>: "success",\n  <span class="keyword">"message"</span>: "API is working!"\n}</div>
    </div>
  </div>

  <!-- GET /<category>/<n> -->
  <div class="card">
    <div class="card-top">
      <span class="method GET">GET</span>
      <span class="path">/<span class="param">{category_type}</span>/<span class="param">{n}</span></span>
    </div>
    <p class="desc">Returns all products in <code style="color:var(--accent2)">{category_type}</code> with a rating ≥ <code style="color:var(--accent2)">{n}</code>. Both path parameters are required.</p>
    <div class="tags"><span class="tag">products</span><span class="tag">filter</span><span class="tag">rating</span><span class="tag">category</span></div>
    <div class="example">
      <div class="example-label">Path Parameters</div>
      <div class="code"><span class="comment"># category_type  string  Product category (e.g. smartphones)</span>\n<span class="comment"># n              float   Minimum rating threshold (e.g. 4.5)</span></div>
      <div class="example-label" style="margin-top:14px">Example Request</div>
      <div class="code">GET /smartphones/4.5</div>
      <div class="example-label" style="margin-top:14px">Example Response</div>
      <div class="code">[
  {
    <span class="keyword">"id"</span>: 1,
    <span class="keyword">"title"</span>: "iPhone 9",
    <span class="keyword">"category"</span>: "smartphones",
    <span class="keyword">"rating"</span>: 4.69,
    <span class="keyword">"price"</span>: 549.99,
    ...
  }
]</div>
      <button class="try-btn" onclick="tryIt()">▶ Try it live</button>
      <div class="resp-demo" id="demo">Fetching from /smartphones/4.5 ...</div>
    </div>
  </div>

  <!-- GET /blueprint -->
  <div class="card">
    <div class="card-top">
      <span class="method GET">GET</span>
      <span class="path">/blueprint</span>
    </div>
    <p class="desc">You are here. Interactive API Blueprint — a self-hosted documentation page for this API.</p>
    <div class="tags"><span class="tag">docs</span><span class="tag">blueprint</span></div>
  </div>

  <!-- Footer -->
  <div class="footer">
    Built with <strong style="color:var(--accent2)">Flask</strong> &amp; deployed on
    <a href="https://vercel.com" target="_blank">Vercel</a> &nbsp;·&nbsp;
    Data from <a href="https://dummyjson.com" target="_blank">DummyJSON</a>
  </div>

</div>

<script>
  async function tryIt() {
    const demo = document.getElementById('demo');
    demo.classList.add('visible');
    demo.textContent = 'Fetching /smartphones/4.5 …';
    try {
      const res = await fetch('/smartphones/4.5');
      const data = await res.json();
      if (data.length === 0) {
        demo.textContent = '[] — No results found for this filter.';
      } else {
        demo.textContent = JSON.stringify(data.slice(0, 2), null, 2) + (data.length > 2 ? '\\n  ... and ' + (data.length - 2) + ' more' : '');
      }
    } catch(e) {
      demo.textContent = 'Error: ' + e.message;
    }
  }
</script>
</body>
</html>"""
    return html


# Product API
URL = "https://dummyjson.com/products"


@app.get("/<category_type>/<n>")
def get_ratings(category_type, n):

    response = requests.get(URL)
    data = response.json()

    prod = []

    for i in data["products"]:
        if (
            i["category"] == category_type
            and float(i.get("rating", 0)) >= float(n)
        ):
            prod.append(i)

    return prod


if __name__ == "__main__":
    app.run(debug=True)