const {
  SvelteComponent: y,
  add_iframe_resize_listener: b,
  add_render_callback: v,
  attr: m,
  binding_callbacks: h,
  detach: w,
  element: z,
  init: k,
  insert: p,
  noop: o,
  safe_not_equal: C,
  toggle_class: _
} = window.__gradio__svelte__internal, { onMount: E } = window.__gradio__svelte__internal;
function O(l) {
  let e, s;
  return {
    c() {
      e = z("div"), e.textContent = "FOO", m(e, "class", "svelte-84cxb8"), v(() => (
        /*div_elementresize_handler*/
        l[5].call(e)
      )), _(
        e,
        "table",
        /*type*/
        l[0] === "table"
      ), _(
        e,
        "gallery",
        /*type*/
        l[0] === "gallery"
      ), _(
        e,
        "selected",
        /*selected*/
        l[1]
      );
    },
    m(n, i) {
      p(n, e, i), s = b(
        e,
        /*div_elementresize_handler*/
        l[5].bind(e)
      ), l[6](e);
    },
    p(n, [i]) {
      i & /*type*/
      1 && _(
        e,
        "table",
        /*type*/
        n[0] === "table"
      ), i & /*type*/
      1 && _(
        e,
        "gallery",
        /*type*/
        n[0] === "gallery"
      ), i & /*selected*/
      2 && _(
        e,
        "selected",
        /*selected*/
        n[1]
      );
    },
    i: o,
    o,
    d(n) {
      n && w(e), s(), l[6](null);
    }
  };
}
function S(l, e, s) {
  let { value: n } = e, { type: i } = e, { selected: d = !1 } = e, c, a;
  function u(t, r) {
    !t || !r || (a.style.setProperty("--local-text-width", `${r < 150 ? r : 200}px`), s(3, a.style.whiteSpace = "unset", a));
  }
  E(() => {
    u(a, c);
  });
  function f() {
    c = this.clientWidth, s(2, c);
  }
  function g(t) {
    h[t ? "unshift" : "push"](() => {
      a = t, s(3, a);
    });
  }
  return l.$$set = (t) => {
    "value" in t && s(4, n = t.value), "type" in t && s(0, i = t.type), "selected" in t && s(1, d = t.selected);
  }, [i, d, c, a, n, f, g];
}
class q extends y {
  constructor(e) {
    super(), k(this, e, S, O, C, { value: 4, type: 0, selected: 1 });
  }
}
export {
  q as default
};
