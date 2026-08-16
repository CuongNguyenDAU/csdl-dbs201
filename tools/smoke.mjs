/* smoke.mjs — bấm thật vào site đã build, trong Chrome headless.
 *
 *   node tools/smoke.mjs                    (tự build, tự dựng server, tự tắt)
 *   node tools/smoke.mjs -o ./anh           (kèm chụp ảnh màn hình)
 *
 * Kiểm những thứ mà mkdocs build --strict không thấy được: sơ đồ mermaid có
 * render ra SVG thật không, trắc nghiệm chấm đúng chưa, tiến độ có được nhớ
 * sau khi tải lại trang không, và quan trọng nhất — các khối tương tác có gắn
 * lại được sau khi chuyển trang bằng navigation.instant hay không.
 */
import { spawn, spawnSync } from "node:child_process";
import { createServer } from "node:http";
import { readFileSync, existsSync, mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const SITE = path.join(ROOT, "site");
const PORT = 8791;
const flag = (n) => { const i = process.argv.indexOf(n); return i > 0 ? process.argv[i + 1] : null; };
const shotDir = flag("-o");
const R = [];
const ok = (ten, dat, ghi) => {
  R.push(dat);
  console.log(`  ${dat ? "✔" : "✖"} ${ten}${ghi ? "  — " + ghi : ""}`);
};
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function findChrome() {
  const c = [process.env.CHROME_PATH,
    "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    "/usr/bin/google-chrome", "/usr/bin/chromium"].filter(Boolean);
  for (const p of c) if (existsSync(p)) return p;
  console.error("✖ Không tìm thấy Chrome/Edge. Đặt biến môi trường CHROME_PATH.");
  process.exit(2);
}

const MIME = {
  ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8", ".json": "application/json; charset=utf-8",
  ".png": "image/png", ".svg": "image/svg+xml", ".woff2": "font/woff2",
  ".ico": "image/x-icon", ".xml": "application/xml"
};

function serve() {
  return new Promise((res) => {
    const s = createServer((req, rep) => {
      let p = decodeURIComponent(req.url.split("?")[0]);
      let f = path.join(SITE, p);
      if (p.endsWith("/")) f = path.join(f, "index.html");
      if (!existsSync(f)) { rep.writeHead(404); return rep.end("404"); }
      rep.writeHead(200, { "Content-Type": MIME[path.extname(f)] || "application/octet-stream" });
      rep.end(readFileSync(f));
    });
    s.listen(PORT, () => res(s));
  });
}

/* ---- CDP tối giản ---- */
async function connect(chrome) {
  const child = spawn(chrome, ["--headless=new", "--disable-gpu", "--no-first-run",
    "--no-default-browser-check", "--remote-debugging-port=9333",
    "--user-data-dir=" + path.join(ROOT, ".chrome-smoke"), "about:blank"],
    { stdio: "ignore" });
  let list = null;
  for (let i = 0; i < 60; i++) {
    try { list = await (await fetch("http://127.0.0.1:9333/json/list")).json(); break; }
    catch { await sleep(200); }
  }
  const page = list.find((t) => t.type === "page");
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((r) => (ws.onopen = r));
  let id = 0; const waits = new Map();
  ws.onmessage = (m) => {
    const d = JSON.parse(m.data);
    if (d.id && waits.has(d.id)) { waits.get(d.id)(d); waits.delete(d.id); }
  };
  const send = (method, params = {}) => new Promise((r) => {
    const i = ++id; waits.set(i, r);
    ws.send(JSON.stringify({ id: i, method, params }));
  });
  await send("Page.enable"); await send("Runtime.enable");
  await send("Emulation.setDeviceMetricsOverride",
    { width: 1280, height: 900, deviceScaleFactor: 1, mobile: false });
  return {
    send, child, ws,
    goto: async (url) => {
      await send("Page.navigate", { url });
      await sleep(700);
    },
    /* chờ tới khi biểu thức trả về true, tối đa `hạn` mili-giây */
    doi: async function (expr, han = 8000) {
      const t0 = Date.now();
      while (Date.now() - t0 < han) {
        try {
          const r = await send("Runtime.evaluate", {
            expression: `(function(){${expr}})()`, returnByValue: true });
          if (r.result?.result?.value) return true;
        } catch { }
        await sleep(150);
      }
      return false;
    },
    ev: async (expr) => {
      const r = await send("Runtime.evaluate", {
        expression: `(function(){${expr}})()`,
        returnByValue: true, awaitPromise: true
      });
      if (r.result?.exceptionDetails) {
        const d = r.result.exceptionDetails;
        throw new Error(d.exception?.description || d.text || "lỗi không rõ");
      }
      return r.result?.result?.value;
    },
    shot: async (name) => {
      if (!shotDir) return;
      mkdirSync(shotDir, { recursive: true });
      const r = await send("Page.captureScreenshot", { format: "png" });
      writeFileSync(path.join(shotDir, name), Buffer.from(r.result.data, "base64"));
    }
  };
}

/* ---- chạy ---- */
console.log("Build site…");
const b = spawnSync("python", ["-m", "mkdocs", "build", "--strict"],
  { cwd: ROOT, encoding: "utf-8", env: { ...process.env, PYTHONIOENCODING: "utf-8" } });
if (b.status !== 0) { console.error(b.stdout, b.stderr); process.exit(1); }

const server = await serve();
const chrome = findChrome();
const p = await connect(chrome);
const BASE = `http://127.0.0.1:${PORT}`;

try {
  console.log("\nA. Trang nội dung và sơ đồ");
  await p.goto(`${BASE}/`);
  ok("trang chủ dựng được", (await p.ev("return document.title")).includes("DBS201"),
    await p.ev("return document.title"));

  await p.goto(`${BASE}/chuong-1/1-4-mo-hinh-du-lieu-luoc-do-va-the-hien/`);
  /* Material nhét SVG vào shadow DOM đóng nên không đếm được svg từ ngoài;
     bằng chứng render thành công là khối .mermaid có chiều cao thật. */
  await p.doi("var m=document.querySelectorAll('.mermaid');" +
              "return m.length>0 && Array.from(m).every(function(e){return e.offsetHeight>40})");
  const svg = await p.ev(
    "var m=Array.from(document.querySelectorAll('.mermaid'));" +
    "return { m: m.length, ve: m.filter(function(e){return e.offsetHeight>40}).length," +
    " cao: m.map(function(e){return e.offsetHeight}).join('/') }");
  ok("sơ đồ mermaid render thật (có chiều cao)", svg.m > 0 && svg.ve === svg.m,
    `${svg.ve}/${svg.m} sơ đồ · cao ${svg.cao}px`);
  await p.shot("noi-dung.png");

  console.log("\nB. Trắc nghiệm");
  await p.goto(`${BASE}/chuong-1/on-tap/`);
  await p.doi("return document.querySelectorAll('.hl-q').length === 12");
  const n = await p.ev("return document.querySelectorAll('.hl-q').length");
  ok("dựng đủ câu hỏi", n === 12, `${n} câu`);

  const sai = await p.ev(`
    var q = document.querySelectorAll('.hl-q')[0];
    var opts = q.querySelectorAll('.hl-opt');
    var wrong = 0; // câu 1 đáp án đúng là index 1 → chọn 0 cho sai
    opts[wrong].click();
    q.querySelector('.hl-btn').click();
    var fb = q.querySelector('.hl-fb');
    return { cls: fb.className, co_giai_thich: fb.textContent.length > 60,
             to_do: q.querySelectorAll('.hl-wrong').length,
             to_xanh: q.querySelectorAll('.hl-right').length };`);
  ok("chọn sai → phản hồi đỏ kèm giải thích",
    /hl-bad/.test(sai.cls) && sai.co_giai_thich && sai.to_do === 1 && sai.to_xanh === 1);

  const dung = await p.ev(`
    var q = document.querySelectorAll('.hl-q')[1];
    q.querySelectorAll('.hl-opt')[1].click();
    q.querySelector('.hl-btn').click();
    return q.querySelector('.hl-fb').className;`);
  ok("chọn đúng → phản hồi xanh", /hl-good/.test(dung));

  const diem = await p.ev("return document.querySelector('.hl-score').textContent");
  ok("bảng điểm cộng đúng", /1\/12/.test(diem), diem.trim().slice(0, 40));
  await p.shot("trac-nghiem.png");

  console.log("\nC. Nhớ tiến độ và thẻ lật");
  await p.goto(`${BASE}/chuong-1/on-tap/`);
  await p.doi("return document.querySelectorAll('.hl-q').length === 12 && !!document.querySelector('.hl-score')");
  const nho = await p.ev(`
    var q = document.querySelectorAll('.hl-q')[1];
    return { xanh: q.querySelectorAll('.hl-right').length,
             diem: document.querySelector('.hl-score').textContent };`);
  ok("tải lại trang vẫn nhớ kết quả", nho.xanh === 1 && /1\/12/.test(nho.diem));

  const the = await p.ev(`
    var c = document.querySelectorAll('.hl-card');
    c[0].click();
    return { so: c.length, lat: c[0].classList.contains('hl-flip') };`);
  ok("thẻ lật đủ số và lật được", the.so === 6 && the.lat, `${the.so} thẻ`);

  const tick = await p.ev(`
    var r = document.querySelectorAll('.hl-check-row');
    r[0].querySelector('input').click();
    return { so: r.length, danh_dau: r[0].classList.contains('hl-done') };`);
  ok("bảng tự đánh giá tick được", tick.so === 6 && tick.danh_dau, `${tick.so} mục tiêu`);
  await p.shot("the-lat.png");

  console.log("\nD. Chuyển trang tức thời (bẫy navigation.instant)");
  await p.goto(`${BASE}/chuong-1/tom-tat/`);
  const instant = await p.ev(`
    var a = Array.from(document.querySelectorAll('.md-nav a'))
              .find(function(x){ return /on-tap/.test(x.getAttribute('href')||''); });
    if (!a) return { loi: 'không thấy liên kết ôn tập' };
    a.click();
    return { da_bam: true };`);
  await p.doi("return /on-tap/.test(location.pathname) && document.querySelectorAll('.hl-q').length === 12");
  const sau = await p.ev(`
    return { url: location.pathname,
             quiz: document.querySelectorAll('.hl-q').length,
             the: document.querySelectorAll('.hl-card').length };`);
  ok("chuyển trang không tải lại → trắc nghiệm vẫn gắn được",
    /on-tap/.test(sau.url) && sau.quiz === 12 && sau.the === 6,
    `${sau.quiz} câu · ${sau.the} thẻ`);

  console.log("\nE. Nội dung không được lên site");
  await p.goto(`${BASE}/search/search_index.json`);
  const idx = await p.ev("return document.body.innerText");
  ok("không lọt phụ lục dành cho giảng viên",
    !/dành cho giảng viên/i.test(idx) && !/PHỤ LỤC 1A/i.test(idx));
  ok("bài tập giữ nguyên nhãn (a) (b) (c), không bị đổi thành ©",
    !/\(©\)/.test(idx) && /\(c\)/.test(idx));
} catch (e) {
  ok("chạy hết kịch bản", false, e.message);
} finally {
  p.ws.close(); p.child.kill(); server.close();
}

const hong = R.filter((x) => !x).length;
console.log(`\n${R.length - hong}/${R.length} kiểm thử đạt${shotDir ? " · ảnh ở " + shotDir : ""}`);
process.exit(hong ? 1 : 0);
