/* Học liệu CSDL — ba khối củng cố kiến thức: trắc nghiệm tự chấm, thẻ lật,
   bảng tự đánh giá. Không phụ thuộc thư viện ngoài.

   Lưu ý quan trọng: theme bật navigation.instant nên trang sau được nạp bằng
   XHR, không tải lại tài liệu. Vì vậy phải gắn lại sau MỖI lần chuyển trang
   thông qua document$ của Material, chứ không chạy một lần lúc tải. */
(function () {
  "use strict";

  /* Đường dẫn gốc của site, suy từ chính URL của file script này —
     tính theo document.currentScript nên phải lấy ngay lúc nạp. */
  var SITE_ROOT = (function () {
    var s = document.currentScript && document.currentScript.src;
    if (!s) return "/";
    return s.replace(/assets\/hoclieu\.js.*$/, "");
  })();

  var esc = function (t) {
    return String(t == null ? "" : t).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  };

  /* Cho phép một ít markdown trong câu hỏi và giải thích: `mã`, **đậm**, *nghiêng*.
     Thoát HTML trước rồi mới dựng thẻ, nên nội dung JSON không chèn được mã lạ. */
  var fmt = function (t) {
    return esc(t)
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[^*])\*([^*\n]+)\*/g, "$1<em>$2</em>")
      .replace(/\n/g, "<br>");
  };

  var KEY = "ABCDEFGH".split("");
  /* Nhãn khối bám ma trận đề của Rubric 4: khối A đo CLO2 (60% số câu),
     B1 là tình huống ràng buộc toàn vẹn, B2 là tình huống chuẩn hóa (cộng 40%).
     Nhãn V dành cho câu luyện theo dạng bài kiểm tra viết, không có trong đề
     trắc nghiệm nhưng vẫn là thứ sinh viên phải thi. */
  var NHAN_KHOI = {
    A: "Khối A · khái niệm", B1: "Khối B1 · tình huống",
    B2: "Khối B2 · tình huống", V: "Dạng bài kiểm tra viết"
  };
  var el = function (h) {
    var d = document.createElement("div");
    d.innerHTML = h.trim();
    return d.firstElementChild;
  };

  var luu = function (k, v) {
    try { localStorage.setItem("hl:" + k, JSON.stringify(v)); } catch (e) { }
  };
  var doc = function (k, mac) {
    try {
      var v = localStorage.getItem("hl:" + k);
      return v === null ? mac : JSON.parse(v);
    } catch (e) { return mac; }
  };

  /* ---------------- trắc nghiệm ---------------- */
  function dungQuiz(node, data) {
    var qs = data.questions || [];
    if (!qs.length) { node.innerHTML = ""; return; }
    var ns = "c" + (data.chuong || "x");
    node.innerHTML = "";

    var trangThai = {};
    /* Tạo ô điểm TRƯỚC vòng lặp: khi khôi phục kết quả đã lưu, cham() chạy ngay
       trong vòng lặp và gọi capNhatDiem(), lúc đó ô điểm phải tồn tại rồi. */
    var diem = el('<div class="hl-score"></div>');

    function capNhatDiem() {
      var d = 0, daLam = 0;
      qs.forEach(function (q) {
        var r = doc(ns + ":" + q.id, null);
        if (r && typeof r.pick === "number") { daLam++; if (r.dung) d++; }
      });
      diem.innerHTML = '<span class="hl-num">' + d + "/" + qs.length + "</span> câu đúng" +
        (daLam < qs.length ? " · còn " + (qs.length - daLam) + " câu chưa làm" : " · đã làm hết");
    }

    qs.forEach(function (q, i) {
      var box = el('<div class="hl-q"></div>');
      var khoi = NHAN_KHOI[q.block] || (q.block ? "Khối " + q.block : "");
      box.appendChild(el(
        '<div class="hl-q-head"><span class="hl-badge">Câu ' + (i + 1) + "</span>" +
        (khoi ? "<span>" + esc(khoi) + "</span>" : "") +
        (q.clo ? "<span>" + esc(q.clo) + "</span>" : "") + "</div>"));
      box.appendChild(el('<div class="hl-q-text">' + fmt(q.q) + "</div>"));

      var opts = [];
      (q.options || []).forEach(function (o, n) {
        var b = el('<button type="button" class="hl-opt"><span class="hl-key">' +
          KEY[n] + '</span><span>' + fmt(o) + "</span></button>");
        b.addEventListener("click", function () {
          if (b.classList.contains("hl-lock")) return;
          opts.forEach(function (x) { x.classList.remove("hl-pick"); });
          b.classList.add("hl-pick");
          trangThai[q.id] = n;
        });
        opts.push(b);
        box.appendChild(b);
      });

      var fb = el('<div class="hl-fb"></div>');
      var row = el('<div class="hl-row"></div>');
      var btn = el('<button type="button" class="hl-btn">Kiểm tra</button>');
      var lam = el('<button type="button" class="hl-btn hl-ghost">Làm lại</button>');

      function cham() {
        var pick = trangThai[q.id];
        if (pick === undefined || pick === null) return;
        var dung = pick === q.answer;
        opts.forEach(function (x, n) {
          x.classList.add("hl-lock");
          x.classList.remove("hl-pick");
          if (n === q.answer) x.classList.add("hl-right");
          else if (n === pick) x.classList.add("hl-wrong");
        });
        fb.className = "hl-fb hl-on " + (dung ? "hl-good" : "hl-bad");
        fb.innerHTML = "<b>" + (dung ? "Chính xác." : "Chưa đúng.") + "</b>" +
          fmt(q.explain || "");
        luu(ns + ":" + q.id, { pick: pick, dung: dung });
        capNhatDiem();
      }
      btn.addEventListener("click", cham);
      lam.addEventListener("click", function () {
        trangThai[q.id] = null;
        opts.forEach(function (x) { x.className = "hl-opt"; });
        fb.className = "hl-fb";
        luu(ns + ":" + q.id, null);
        capNhatDiem();
      });
      row.appendChild(btn);
      row.appendChild(lam);
      box.appendChild(row);
      box.appendChild(fb);
      node.appendChild(box);

      /* khôi phục kết quả lần trước */
      var cu = doc(ns + ":" + q.id, null);
      if (cu && typeof cu.pick === "number") {
        trangThai[q.id] = cu.pick;
        cham();
      }
    });

    node.appendChild(diem);
    capNhatDiem();

    var reset = el('<div class="hl-row"><button type="button" class="hl-btn hl-ghost">Xóa toàn bộ kết quả chương này</button></div>');
    reset.firstElementChild.addEventListener("click", function () {
      qs.forEach(function (q) { luu(ns + ":" + q.id, null); });
      dungQuiz(node, data);
    });
    node.appendChild(reset);
  }

  /* ---------------- thẻ lật ---------------- */
  function dungCards(node, data) {
    var cs = data.cards || [];
    if (!cs.length) { node.innerHTML = ""; return; }
    var grid = el('<div class="hl-cards-grid"></div>');
    cs.forEach(function (c) {
      var b = el('<button type="button" class="hl-card"><div class="hl-card-inner">' +
        '<div class="hl-card-face hl-card-front">' + fmt(c.front) + "</div>" +
        '<div class="hl-card-face hl-card-back">' + fmt(c.back) + "</div>" +
        "</div></button>");
      b.addEventListener("click", function () { b.classList.toggle("hl-flip"); });
      grid.appendChild(b);
    });
    node.innerHTML = "";
    node.appendChild(grid);
  }

  /* ---------------- tự đánh giá ---------------- */
  function dungCheck(node, data) {
    var rows = data.selfcheck || [];
    if (!rows.length) { node.innerHTML = ""; return; }
    var ns = "c" + (data.chuong || "x") + ":check";
    node.innerHTML = "";
    rows.forEach(function (r, i) {
      var lab = el('<label class="hl-check-row"><input type="checkbox"><span>' +
        fmt(r.text) + "</span>" +
        (r.clo ? '<span class="hl-clo">' + esc(r.clo) + "</span>" : "") + "</label>");
      var cb = lab.querySelector("input");
      cb.checked = !!doc(ns + ":" + i, false);
      lab.classList.toggle("hl-done", cb.checked);
      cb.addEventListener("change", function () {
        lab.classList.toggle("hl-done", cb.checked);
        luu(ns + ":" + i, cb.checked);
      });
      node.appendChild(lab);
    });
  }

  /* ---------------- gắn vào trang ---------------- */
  var CACHE = {};
  function nap(src) {
    if (CACHE[src]) return CACHE[src];
    CACHE[src] = fetch(SITE_ROOT + src).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    });
    return CACHE[src];
  }

  function gan() {
    var mucs = [
      [".hl-quiz", dungQuiz],
      [".hl-cards", dungCards],
      [".hl-check", dungCheck]
    ];
    mucs.forEach(function (m) {
      document.querySelectorAll(m[0]).forEach(function (node) {
        if (node.dataset.hlDone === "1") return;
        node.dataset.hlDone = "1";
        var src = node.getAttribute("data-src");
        if (!src) return;
        node.innerHTML = '<div class="hl-loading">Đang tải…</div>';
        nap(src).then(function (data) { m[1](node, data); }).catch(function (e) {
          node.innerHTML = '<div class="hl-loading">Không tải được dữ liệu (' +
            esc(e.message) + ").</div>";
        });
      });
    });
  }

  if (typeof document$ !== "undefined" && document$ && document$.subscribe) {
    document$.subscribe(gan);          // Material: chạy lại sau mỗi lần chuyển trang
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", gan);
  } else {
    gan();
  }
})();
