const {
  SvelteComponent: Mr,
  assign: Rr,
  create_slot: Dr,
  detach: Ur,
  element: Gr,
  get_all_dirty_from_scope: xr,
  get_slot_changes: Fr,
  get_spread_update: jr,
  init: Vr,
  insert: qr,
  safe_not_equal: zr,
  set_dynamic_element_data: Hn,
  set_style: Q,
  toggle_class: be,
  transition_in: Ui,
  transition_out: Gi,
  update_slot_base: Xr
} = window.__gradio__svelte__internal;
function Zr(e) {
  let t, n, i;
  const r = (
    /*#slots*/
    e[17].default
  ), l = Dr(
    r,
    e,
    /*$$scope*/
    e[16],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      e[7]
    ) },
    { id: (
      /*elem_id*/
      e[2]
    ) },
    {
      class: n = "block " + /*elem_classes*/
      e[3].join(" ") + " svelte-1t38q2d"
    }
  ], a = {};
  for (let s = 0; s < o.length; s += 1)
    a = Rr(a, o[s]);
  return {
    c() {
      t = Gr(
        /*tag*/
        e[14]
      ), l && l.c(), Hn(
        /*tag*/
        e[14]
      )(t, a), be(
        t,
        "hidden",
        /*visible*/
        e[10] === !1
      ), be(
        t,
        "padded",
        /*padding*/
        e[6]
      ), be(
        t,
        "border_focus",
        /*border_mode*/
        e[5] === "focus"
      ), be(t, "hide-container", !/*explicit_call*/
      e[8] && !/*container*/
      e[9]), Q(t, "height", typeof /*height*/
      e[0] == "number" ? (
        /*height*/
        e[0] + "px"
      ) : void 0), Q(t, "width", typeof /*width*/
      e[1] == "number" ? `calc(min(${/*width*/
      e[1]}px, 100%))` : void 0), Q(
        t,
        "border-style",
        /*variant*/
        e[4]
      ), Q(
        t,
        "overflow",
        /*allow_overflow*/
        e[11] ? "visible" : "hidden"
      ), Q(
        t,
        "flex-grow",
        /*scale*/
        e[12]
      ), Q(t, "min-width", `calc(min(${/*min_width*/
      e[13]}px, 100%))`), Q(t, "border-width", "var(--block-border-width)");
    },
    m(s, u) {
      qr(s, t, u), l && l.m(t, null), i = !0;
    },
    p(s, u) {
      l && l.p && (!i || u & /*$$scope*/
      65536) && Xr(
        l,
        r,
        s,
        /*$$scope*/
        s[16],
        i ? Fr(
          r,
          /*$$scope*/
          s[16],
          u,
          null
        ) : xr(
          /*$$scope*/
          s[16]
        ),
        null
      ), Hn(
        /*tag*/
        s[14]
      )(t, a = jr(o, [
        (!i || u & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          s[7]
        ) },
        (!i || u & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          s[2]
        ) },
        (!i || u & /*elem_classes*/
        8 && n !== (n = "block " + /*elem_classes*/
        s[3].join(" ") + " svelte-1t38q2d")) && { class: n }
      ])), be(
        t,
        "hidden",
        /*visible*/
        s[10] === !1
      ), be(
        t,
        "padded",
        /*padding*/
        s[6]
      ), be(
        t,
        "border_focus",
        /*border_mode*/
        s[5] === "focus"
      ), be(t, "hide-container", !/*explicit_call*/
      s[8] && !/*container*/
      s[9]), u & /*height*/
      1 && Q(t, "height", typeof /*height*/
      s[0] == "number" ? (
        /*height*/
        s[0] + "px"
      ) : void 0), u & /*width*/
      2 && Q(t, "width", typeof /*width*/
      s[1] == "number" ? `calc(min(${/*width*/
      s[1]}px, 100%))` : void 0), u & /*variant*/
      16 && Q(
        t,
        "border-style",
        /*variant*/
        s[4]
      ), u & /*allow_overflow*/
      2048 && Q(
        t,
        "overflow",
        /*allow_overflow*/
        s[11] ? "visible" : "hidden"
      ), u & /*scale*/
      4096 && Q(
        t,
        "flex-grow",
        /*scale*/
        s[12]
      ), u & /*min_width*/
      8192 && Q(t, "min-width", `calc(min(${/*min_width*/
      s[13]}px, 100%))`);
    },
    i(s) {
      i || (Ui(l, s), i = !0);
    },
    o(s) {
      Gi(l, s), i = !1;
    },
    d(s) {
      s && Ur(t), l && l.d(s);
    }
  };
}
function Wr(e) {
  let t, n = (
    /*tag*/
    e[14] && Zr(e)
  );
  return {
    c() {
      n && n.c();
    },
    m(i, r) {
      n && n.m(i, r), t = !0;
    },
    p(i, [r]) {
      /*tag*/
      i[14] && n.p(i, r);
    },
    i(i) {
      t || (Ui(n, i), t = !0);
    },
    o(i) {
      Gi(n, i), t = !1;
    },
    d(i) {
      n && n.d(i);
    }
  };
}
function Qr(e, t, n) {
  let { $$slots: i = {}, $$scope: r } = t, { height: l = void 0 } = t, { width: o = void 0 } = t, { elem_id: a = "" } = t, { elem_classes: s = [] } = t, { variant: u = "solid" } = t, { border_mode: f = "base" } = t, { padding: c = !0 } = t, { type: h = "normal" } = t, { test_id: _ = void 0 } = t, { explicit_call: g = !1 } = t, { container: S = !0 } = t, { visible: v = !0 } = t, { allow_overflow: A = !0 } = t, { scale: y = null } = t, { min_width: d = 0 } = t, T = h === "fieldset" ? "fieldset" : "div";
  return e.$$set = (b) => {
    "height" in b && n(0, l = b.height), "width" in b && n(1, o = b.width), "elem_id" in b && n(2, a = b.elem_id), "elem_classes" in b && n(3, s = b.elem_classes), "variant" in b && n(4, u = b.variant), "border_mode" in b && n(5, f = b.border_mode), "padding" in b && n(6, c = b.padding), "type" in b && n(15, h = b.type), "test_id" in b && n(7, _ = b.test_id), "explicit_call" in b && n(8, g = b.explicit_call), "container" in b && n(9, S = b.container), "visible" in b && n(10, v = b.visible), "allow_overflow" in b && n(11, A = b.allow_overflow), "scale" in b && n(12, y = b.scale), "min_width" in b && n(13, d = b.min_width), "$$scope" in b && n(16, r = b.$$scope);
  }, [
    l,
    o,
    a,
    s,
    u,
    f,
    c,
    _,
    g,
    S,
    v,
    A,
    y,
    d,
    T,
    h,
    r,
    i
  ];
}
class Jr extends Mr {
  constructor(t) {
    super(), Vr(this, t, Qr, Wr, zr, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 15,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: Yr,
  append: It,
  attr: ct,
  create_component: Kr,
  destroy_component: $r,
  detach: el,
  element: Bn,
  init: tl,
  insert: nl,
  mount_component: il,
  safe_not_equal: rl,
  set_data: ll,
  space: ol,
  text: sl,
  toggle_class: ge,
  transition_in: al,
  transition_out: ul
} = window.__gradio__svelte__internal;
function fl(e) {
  let t, n, i, r, l, o;
  return i = new /*Icon*/
  e[1]({}), {
    c() {
      t = Bn("label"), n = Bn("span"), Kr(i.$$.fragment), r = ol(), l = sl(
        /*label*/
        e[0]
      ), ct(n, "class", "svelte-9gxdi0"), ct(t, "for", ""), ct(t, "data-testid", "block-label"), ct(t, "class", "svelte-9gxdi0"), ge(t, "hide", !/*show_label*/
      e[2]), ge(t, "sr-only", !/*show_label*/
      e[2]), ge(
        t,
        "float",
        /*float*/
        e[4]
      ), ge(
        t,
        "hide-label",
        /*disable*/
        e[3]
      );
    },
    m(a, s) {
      nl(a, t, s), It(t, n), il(i, n, null), It(t, r), It(t, l), o = !0;
    },
    p(a, [s]) {
      (!o || s & /*label*/
      1) && ll(
        l,
        /*label*/
        a[0]
      ), (!o || s & /*show_label*/
      4) && ge(t, "hide", !/*show_label*/
      a[2]), (!o || s & /*show_label*/
      4) && ge(t, "sr-only", !/*show_label*/
      a[2]), (!o || s & /*float*/
      16) && ge(
        t,
        "float",
        /*float*/
        a[4]
      ), (!o || s & /*disable*/
      8) && ge(
        t,
        "hide-label",
        /*disable*/
        a[3]
      );
    },
    i(a) {
      o || (al(i.$$.fragment, a), o = !0);
    },
    o(a) {
      ul(i.$$.fragment, a), o = !1;
    },
    d(a) {
      a && el(t), $r(i);
    }
  };
}
function cl(e, t, n) {
  let { label: i = null } = t, { Icon: r } = t, { show_label: l = !0 } = t, { disable: o = !1 } = t, { float: a = !0 } = t;
  return e.$$set = (s) => {
    "label" in s && n(0, i = s.label), "Icon" in s && n(1, r = s.Icon), "show_label" in s && n(2, l = s.show_label), "disable" in s && n(3, o = s.disable), "float" in s && n(4, a = s.float);
  }, [i, r, l, o, a];
}
class hl extends Yr {
  constructor(t) {
    super(), tl(this, t, cl, fl, rl, {
      label: 0,
      Icon: 1,
      show_label: 2,
      disable: 3,
      float: 4
    });
  }
}
const {
  SvelteComponent: _l,
  append: Yt,
  attr: Te,
  bubble: ml,
  create_component: dl,
  destroy_component: bl,
  detach: xi,
  element: Kt,
  init: gl,
  insert: Fi,
  listen: pl,
  mount_component: vl,
  safe_not_equal: wl,
  set_data: yl,
  space: El,
  text: Sl,
  toggle_class: pe,
  transition_in: Tl,
  transition_out: Al
} = window.__gradio__svelte__internal;
function kn(e) {
  let t, n;
  return {
    c() {
      t = Kt("span"), n = Sl(
        /*label*/
        e[1]
      ), Te(t, "class", "svelte-xtz2g8");
    },
    m(i, r) {
      Fi(i, t, r), Yt(t, n);
    },
    p(i, r) {
      r & /*label*/
      2 && yl(
        n,
        /*label*/
        i[1]
      );
    },
    d(i) {
      i && xi(t);
    }
  };
}
function Hl(e) {
  let t, n, i, r, l, o, a, s = (
    /*show_label*/
    e[2] && kn(e)
  );
  return r = new /*Icon*/
  e[0]({}), {
    c() {
      t = Kt("button"), s && s.c(), n = El(), i = Kt("div"), dl(r.$$.fragment), Te(i, "class", "svelte-xtz2g8"), pe(
        i,
        "small",
        /*size*/
        e[4] === "small"
      ), pe(
        i,
        "large",
        /*size*/
        e[4] === "large"
      ), Te(
        t,
        "aria-label",
        /*label*/
        e[1]
      ), Te(
        t,
        "title",
        /*label*/
        e[1]
      ), Te(t, "class", "svelte-xtz2g8"), pe(
        t,
        "pending",
        /*pending*/
        e[3]
      ), pe(
        t,
        "padded",
        /*padded*/
        e[5]
      );
    },
    m(u, f) {
      Fi(u, t, f), s && s.m(t, null), Yt(t, n), Yt(t, i), vl(r, i, null), l = !0, o || (a = pl(
        t,
        "click",
        /*click_handler*/
        e[6]
      ), o = !0);
    },
    p(u, [f]) {
      /*show_label*/
      u[2] ? s ? s.p(u, f) : (s = kn(u), s.c(), s.m(t, n)) : s && (s.d(1), s = null), (!l || f & /*size*/
      16) && pe(
        i,
        "small",
        /*size*/
        u[4] === "small"
      ), (!l || f & /*size*/
      16) && pe(
        i,
        "large",
        /*size*/
        u[4] === "large"
      ), (!l || f & /*label*/
      2) && Te(
        t,
        "aria-label",
        /*label*/
        u[1]
      ), (!l || f & /*label*/
      2) && Te(
        t,
        "title",
        /*label*/
        u[1]
      ), (!l || f & /*pending*/
      8) && pe(
        t,
        "pending",
        /*pending*/
        u[3]
      ), (!l || f & /*padded*/
      32) && pe(
        t,
        "padded",
        /*padded*/
        u[5]
      );
    },
    i(u) {
      l || (Tl(r.$$.fragment, u), l = !0);
    },
    o(u) {
      Al(r.$$.fragment, u), l = !1;
    },
    d(u) {
      u && xi(t), s && s.d(), bl(r), o = !1, a();
    }
  };
}
function Bl(e, t, n) {
  let { Icon: i } = t, { label: r = "" } = t, { show_label: l = !1 } = t, { pending: o = !1 } = t, { size: a = "small" } = t, { padded: s = !0 } = t;
  function u(f) {
    ml.call(this, e, f);
  }
  return e.$$set = (f) => {
    "Icon" in f && n(0, i = f.Icon), "label" in f && n(1, r = f.label), "show_label" in f && n(2, l = f.show_label), "pending" in f && n(3, o = f.pending), "size" in f && n(4, a = f.size), "padded" in f && n(5, s = f.padded);
  }, [i, r, l, o, a, s, u];
}
class nt extends _l {
  constructor(t) {
    super(), gl(this, t, Bl, Hl, wl, {
      Icon: 0,
      label: 1,
      show_label: 2,
      pending: 3,
      size: 4,
      padded: 5
    });
  }
}
const {
  SvelteComponent: kl,
  append: Cl,
  attr: Lt,
  binding_callbacks: Pl,
  create_slot: Il,
  detach: Ll,
  element: Cn,
  get_all_dirty_from_scope: Nl,
  get_slot_changes: Ol,
  init: Ml,
  insert: Rl,
  safe_not_equal: Dl,
  toggle_class: ve,
  transition_in: Ul,
  transition_out: Gl,
  update_slot_base: xl
} = window.__gradio__svelte__internal;
function Fl(e) {
  let t, n, i;
  const r = (
    /*#slots*/
    e[5].default
  ), l = Il(
    r,
    e,
    /*$$scope*/
    e[4],
    null
  );
  return {
    c() {
      t = Cn("div"), n = Cn("div"), l && l.c(), Lt(n, "class", "icon svelte-3w3rth"), Lt(t, "class", "empty svelte-3w3rth"), Lt(t, "aria-label", "Empty value"), ve(
        t,
        "small",
        /*size*/
        e[0] === "small"
      ), ve(
        t,
        "large",
        /*size*/
        e[0] === "large"
      ), ve(
        t,
        "unpadded_box",
        /*unpadded_box*/
        e[1]
      ), ve(
        t,
        "small_parent",
        /*parent_height*/
        e[3]
      );
    },
    m(o, a) {
      Rl(o, t, a), Cl(t, n), l && l.m(n, null), e[6](t), i = !0;
    },
    p(o, [a]) {
      l && l.p && (!i || a & /*$$scope*/
      16) && xl(
        l,
        r,
        o,
        /*$$scope*/
        o[4],
        i ? Ol(
          r,
          /*$$scope*/
          o[4],
          a,
          null
        ) : Nl(
          /*$$scope*/
          o[4]
        ),
        null
      ), (!i || a & /*size*/
      1) && ve(
        t,
        "small",
        /*size*/
        o[0] === "small"
      ), (!i || a & /*size*/
      1) && ve(
        t,
        "large",
        /*size*/
        o[0] === "large"
      ), (!i || a & /*unpadded_box*/
      2) && ve(
        t,
        "unpadded_box",
        /*unpadded_box*/
        o[1]
      ), (!i || a & /*parent_height*/
      8) && ve(
        t,
        "small_parent",
        /*parent_height*/
        o[3]
      );
    },
    i(o) {
      i || (Ul(l, o), i = !0);
    },
    o(o) {
      Gl(l, o), i = !1;
    },
    d(o) {
      o && Ll(t), l && l.d(o), e[6](null);
    }
  };
}
function jl(e) {
  let t, n = e[0], i = 1;
  for (; i < e.length; ) {
    const r = e[i], l = e[i + 1];
    if (i += 2, (r === "optionalAccess" || r === "optionalCall") && n == null)
      return;
    r === "access" || r === "optionalAccess" ? (t = n, n = l(n)) : (r === "call" || r === "optionalCall") && (n = l((...o) => n.call(t, ...o)), t = void 0);
  }
  return n;
}
function Vl(e, t, n) {
  let i, { $$slots: r = {}, $$scope: l } = t, { size: o = "small" } = t, { unpadded_box: a = !1 } = t, s;
  function u(c) {
    if (!c)
      return !1;
    const { height: h } = c.getBoundingClientRect(), { height: _ } = jl([
      c,
      "access",
      (g) => g.parentElement,
      "optionalAccess",
      (g) => g.getBoundingClientRect,
      "call",
      (g) => g()
    ]) || { height: h };
    return h > _ + 2;
  }
  function f(c) {
    Pl[c ? "unshift" : "push"](() => {
      s = c, n(2, s);
    });
  }
  return e.$$set = (c) => {
    "size" in c && n(0, o = c.size), "unpadded_box" in c && n(1, a = c.unpadded_box), "$$scope" in c && n(4, l = c.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty & /*el*/
    4 && n(3, i = u(s));
  }, [o, a, s, i, l, r, f];
}
class ql extends kl {
  constructor(t) {
    super(), Ml(this, t, Vl, Fl, Dl, { size: 0, unpadded_box: 1 });
  }
}
const {
  SvelteComponent: zl,
  append: Nt,
  attr: ee,
  detach: Xl,
  init: Zl,
  insert: Wl,
  noop: Ot,
  safe_not_equal: Ql,
  set_style: oe,
  svg_element: ht
} = window.__gradio__svelte__internal;
function Jl(e) {
  let t, n, i, r;
  return {
    c() {
      t = ht("svg"), n = ht("g"), i = ht("path"), r = ht("path"), ee(i, "d", "M18,6L6.087,17.913"), oe(i, "fill", "none"), oe(i, "fill-rule", "nonzero"), oe(i, "stroke-width", "2px"), ee(n, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), ee(r, "d", "M4.364,4.364L19.636,19.636"), oe(r, "fill", "none"), oe(r, "fill-rule", "nonzero"), oe(r, "stroke-width", "2px"), ee(t, "width", "100%"), ee(t, "height", "100%"), ee(t, "viewBox", "0 0 24 24"), ee(t, "version", "1.1"), ee(t, "xmlns", "http://www.w3.org/2000/svg"), ee(t, "xmlns:xlink", "http://www.w3.org/1999/xlink"), ee(t, "xml:space", "preserve"), ee(t, "stroke", "currentColor"), oe(t, "fill-rule", "evenodd"), oe(t, "clip-rule", "evenodd"), oe(t, "stroke-linecap", "round"), oe(t, "stroke-linejoin", "round");
    },
    m(l, o) {
      Wl(l, t, o), Nt(t, n), Nt(n, i), Nt(t, r);
    },
    p: Ot,
    i: Ot,
    o: Ot,
    d(l) {
      l && Xl(t);
    }
  };
}
class Yl extends zl {
  constructor(t) {
    super(), Zl(this, t, null, Jl, Ql, {});
  }
}
const {
  SvelteComponent: Kl,
  append: $l,
  attr: Je,
  detach: eo,
  init: to,
  insert: no,
  noop: Mt,
  safe_not_equal: io,
  svg_element: Pn
} = window.__gradio__svelte__internal;
function ro(e) {
  let t, n;
  return {
    c() {
      t = Pn("svg"), n = Pn("path"), Je(n, "d", "M23,20a5,5,0,0,0-3.89,1.89L11.8,17.32a4.46,4.46,0,0,0,0-2.64l7.31-4.57A5,5,0,1,0,18,7a4.79,4.79,0,0,0,.2,1.32l-7.31,4.57a5,5,0,1,0,0,6.22l7.31,4.57A4.79,4.79,0,0,0,18,25a5,5,0,1,0,5-5ZM23,4a3,3,0,1,1-3,3A3,3,0,0,1,23,4ZM7,19a3,3,0,1,1,3-3A3,3,0,0,1,7,19Zm16,9a3,3,0,1,1,3-3A3,3,0,0,1,23,28Z"), Je(n, "fill", "currentColor"), Je(t, "id", "icon"), Je(t, "xmlns", "http://www.w3.org/2000/svg"), Je(t, "viewBox", "0 0 32 32");
    },
    m(i, r) {
      no(i, t, r), $l(t, n);
    },
    p: Mt,
    i: Mt,
    o: Mt,
    d(i) {
      i && eo(t);
    }
  };
}
class lo extends Kl {
  constructor(t) {
    super(), to(this, t, null, ro, io, {});
  }
}
const {
  SvelteComponent: oo,
  append: so,
  attr: Re,
  detach: ao,
  init: uo,
  insert: fo,
  noop: Rt,
  safe_not_equal: co,
  svg_element: In
} = window.__gradio__svelte__internal;
function ho(e) {
  let t, n;
  return {
    c() {
      t = In("svg"), n = In("path"), Re(n, "fill", "currentColor"), Re(n, "d", "M26 24v4H6v-4H4v4a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2v-4zm0-10l-1.41-1.41L17 20.17V2h-2v18.17l-7.59-7.58L6 14l10 10l10-10z"), Re(t, "xmlns", "http://www.w3.org/2000/svg"), Re(t, "width", "100%"), Re(t, "height", "100%"), Re(t, "viewBox", "0 0 32 32");
    },
    m(i, r) {
      fo(i, t, r), so(t, n);
    },
    p: Rt,
    i: Rt,
    o: Rt,
    d(i) {
      i && ao(t);
    }
  };
}
class _o extends oo {
  constructor(t) {
    super(), uo(this, t, null, ho, co, {});
  }
}
const {
  SvelteComponent: mo,
  append: bo,
  attr: te,
  detach: go,
  init: po,
  insert: vo,
  noop: Dt,
  safe_not_equal: wo,
  svg_element: Ln
} = window.__gradio__svelte__internal;
function yo(e) {
  let t, n;
  return {
    c() {
      t = Ln("svg"), n = Ln("path"), te(n, "d", "M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"), te(t, "xmlns", "http://www.w3.org/2000/svg"), te(t, "width", "100%"), te(t, "height", "100%"), te(t, "viewBox", "0 0 24 24"), te(t, "fill", "none"), te(t, "stroke", "currentColor"), te(t, "stroke-width", "1.5"), te(t, "stroke-linecap", "round"), te(t, "stroke-linejoin", "round"), te(t, "class", "feather feather-edit-2");
    },
    m(i, r) {
      vo(i, t, r), bo(t, n);
    },
    p: Dt,
    i: Dt,
    o: Dt,
    d(i) {
      i && go(t);
    }
  };
}
class Eo extends mo {
  constructor(t) {
    super(), po(this, t, null, yo, wo, {});
  }
}
const {
  SvelteComponent: So,
  append: Ut,
  attr: x,
  detach: To,
  init: Ao,
  insert: Ho,
  noop: Gt,
  safe_not_equal: Bo,
  svg_element: _t
} = window.__gradio__svelte__internal;
function ko(e) {
  let t, n, i, r;
  return {
    c() {
      t = _t("svg"), n = _t("rect"), i = _t("circle"), r = _t("polyline"), x(n, "x", "3"), x(n, "y", "3"), x(n, "width", "18"), x(n, "height", "18"), x(n, "rx", "2"), x(n, "ry", "2"), x(i, "cx", "8.5"), x(i, "cy", "8.5"), x(i, "r", "1.5"), x(r, "points", "21 15 16 10 5 21"), x(t, "xmlns", "http://www.w3.org/2000/svg"), x(t, "width", "100%"), x(t, "height", "100%"), x(t, "viewBox", "0 0 24 24"), x(t, "fill", "none"), x(t, "stroke", "currentColor"), x(t, "stroke-width", "1.5"), x(t, "stroke-linecap", "round"), x(t, "stroke-linejoin", "round"), x(t, "class", "feather feather-image");
    },
    m(l, o) {
      Ho(l, t, o), Ut(t, n), Ut(t, i), Ut(t, r);
    },
    p: Gt,
    i: Gt,
    o: Gt,
    d(l) {
      l && To(t);
    }
  };
}
class ji extends So {
  constructor(t) {
    super(), Ao(this, t, null, ko, Bo, {});
  }
}
const {
  SvelteComponent: Co,
  append: Po,
  attr: se,
  detach: Io,
  init: Lo,
  insert: No,
  noop: xt,
  safe_not_equal: Oo,
  svg_element: Nn
} = window.__gradio__svelte__internal;
function Mo(e) {
  let t, n;
  return {
    c() {
      t = Nn("svg"), n = Nn("polygon"), se(n, "points", "5 3 19 12 5 21 5 3"), se(t, "xmlns", "http://www.w3.org/2000/svg"), se(t, "width", "100%"), se(t, "height", "100%"), se(t, "viewBox", "0 0 24 24"), se(t, "fill", "currentColor"), se(t, "stroke", "currentColor"), se(t, "stroke-width", "1.5"), se(t, "stroke-linecap", "round"), se(t, "stroke-linejoin", "round");
    },
    m(i, r) {
      No(i, t, r), Po(t, n);
    },
    p: xt,
    i: xt,
    o: xt,
    d(i) {
      i && Io(t);
    }
  };
}
class Ro extends Co {
  constructor(t) {
    super(), Lo(this, t, null, Mo, Oo, {});
  }
}
const {
  SvelteComponent: Do,
  append: On,
  attr: Y,
  detach: Uo,
  init: Go,
  insert: xo,
  noop: Ft,
  safe_not_equal: Fo,
  svg_element: jt
} = window.__gradio__svelte__internal;
function jo(e) {
  let t, n, i;
  return {
    c() {
      t = jt("svg"), n = jt("polyline"), i = jt("path"), Y(n, "points", "1 4 1 10 7 10"), Y(i, "d", "M3.51 15a9 9 0 1 0 2.13-9.36L1 10"), Y(t, "xmlns", "http://www.w3.org/2000/svg"), Y(t, "width", "100%"), Y(t, "height", "100%"), Y(t, "viewBox", "0 0 24 24"), Y(t, "fill", "none"), Y(t, "stroke", "currentColor"), Y(t, "stroke-width", "2"), Y(t, "stroke-linecap", "round"), Y(t, "stroke-linejoin", "round"), Y(t, "class", "feather feather-rotate-ccw");
    },
    m(r, l) {
      xo(r, t, l), On(t, n), On(t, i);
    },
    p: Ft,
    i: Ft,
    o: Ft,
    d(r) {
      r && Uo(t);
    }
  };
}
class Vo extends Do {
  constructor(t) {
    super(), Go(this, t, null, jo, Fo, {});
  }
}
const qo = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], Mn = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
qo.reduce(
  (e, { color: t, primary: n, secondary: i }) => ({
    ...e,
    [t]: {
      primary: Mn[t][n],
      secondary: Mn[t][i]
    }
  }),
  {}
);
function zo(e) {
  let t, n = e[0], i = 1;
  for (; i < e.length; ) {
    const r = e[i], l = e[i + 1];
    if (i += 2, (r === "optionalAccess" || r === "optionalCall") && n == null)
      return;
    r === "access" || r === "optionalAccess" ? (t = n, n = l(n)) : (r === "call" || r === "optionalCall") && (n = l((...o) => n.call(t, ...o)), t = void 0);
  }
  return n;
}
class gt extends Error {
  constructor(t) {
    super(t), this.name = "ShareError";
  }
}
async function Xo(e, t) {
  if (window.__gradio_space__ == null)
    throw new gt("Must be on Spaces to share.");
  let n, i, r;
  if (t === "url") {
    const s = await fetch(e);
    n = await s.blob(), i = s.headers.get("content-type") || "", r = s.headers.get("content-disposition") || "";
  } else
    n = Zo(e), i = e.split(";")[0].split(":")[1], r = "file" + i.split("/")[1];
  const l = new File([n], r, { type: i }), o = await fetch("https://huggingface.co/uploads", {
    method: "POST",
    body: l,
    headers: {
      "Content-Type": l.type,
      "X-Requested-With": "XMLHttpRequest"
    }
  });
  if (!o.ok) {
    if (zo([o, "access", (s) => s.headers, "access", (s) => s.get, "call", (s) => s("content-type"), "optionalAccess", (s) => s.includes, "call", (s) => s("application/json")])) {
      const s = await o.json();
      throw new gt(`Upload failed: ${s.error}`);
    }
    throw new gt("Upload failed.");
  }
  return await o.text();
}
function Zo(e) {
  for (var t = e.split(","), n = t[0].match(/:(.*?);/)[1], i = atob(t[1]), r = i.length, l = new Uint8Array(r); r--; )
    l[r] = i.charCodeAt(r);
  return new Blob([l], { type: n });
}
const {
  SvelteComponent: Wo,
  create_component: Qo,
  destroy_component: Jo,
  init: Yo,
  mount_component: Ko,
  safe_not_equal: $o,
  transition_in: es,
  transition_out: ts
} = window.__gradio__svelte__internal, { createEventDispatcher: ns } = window.__gradio__svelte__internal;
function is(e) {
  let t, n;
  return t = new nt({
    props: {
      Icon: lo,
      label: (
        /*i18n*/
        e[2]("common.share")
      ),
      pending: (
        /*pending*/
        e[3]
      )
    }
  }), t.$on(
    "click",
    /*click_handler*/
    e[5]
  ), {
    c() {
      Qo(t.$$.fragment);
    },
    m(i, r) {
      Ko(t, i, r), n = !0;
    },
    p(i, [r]) {
      const l = {};
      r & /*i18n*/
      4 && (l.label = /*i18n*/
      i[2]("common.share")), r & /*pending*/
      8 && (l.pending = /*pending*/
      i[3]), t.$set(l);
    },
    i(i) {
      n || (es(t.$$.fragment, i), n = !0);
    },
    o(i) {
      ts(t.$$.fragment, i), n = !1;
    },
    d(i) {
      Jo(t, i);
    }
  };
}
function rs(e, t, n) {
  const i = ns();
  let { formatter: r } = t, { value: l } = t, { i18n: o } = t, a = !1;
  const s = async () => {
    try {
      n(3, a = !0);
      const u = await r(l);
      i("share", { description: u });
    } catch (u) {
      console.error(u);
      let f = u instanceof gt ? u.message : "Share failed.";
      i("error", f);
    } finally {
      n(3, a = !1);
    }
  };
  return e.$$set = (u) => {
    "formatter" in u && n(0, r = u.formatter), "value" in u && n(1, l = u.value), "i18n" in u && n(2, o = u.i18n);
  }, [r, l, o, a, i, s];
}
class ls extends Wo {
  constructor(t) {
    super(), Yo(this, t, rs, is, $o, { formatter: 0, value: 1, i18n: 2 });
  }
}
new Intl.Collator(0, { numeric: 1 }).compare;
function Vi(e, t, n) {
  if (e == null)
    return null;
  if (Array.isArray(e)) {
    const i = [];
    for (const r of e)
      r == null ? i.push(null) : i.push(Vi(r, t, n));
    return i;
  }
  return e.is_stream ? n == null ? new Vt({
    ...e,
    url: t + "/stream/" + e.path
  }) : new Vt({
    ...e,
    url: "/proxy=" + n + "stream/" + e.path
  }) : new Vt({
    ...e,
    url: ss(e.path, t, n)
  });
}
function os(e) {
  try {
    const t = new URL(e);
    return t.protocol === "http:" || t.protocol === "https:";
  } catch {
    return !1;
  }
}
function ss(e, t, n) {
  return e == null ? n ? `/proxy=${n}file=` : `${t}/file=` : os(e) ? e : n ? `/proxy=${n}file=${e}` : `${t}/file=${e}`;
}
class Vt {
  constructor({
    path: t,
    url: n,
    orig_name: i,
    size: r,
    blob: l,
    is_stream: o,
    mime_type: a,
    alt_text: s
  }) {
    this.path = t, this.url = n, this.orig_name = i, this.size = r, this.blob = n ? void 0 : l, this.is_stream = o, this.mime_type = a, this.alt_text = s;
  }
}
function Be() {
}
function as(e) {
  return e();
}
function us(e) {
  e.forEach(as);
}
function fs(e) {
  return typeof e == "function";
}
function cs(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function hs(e, ...t) {
  if (e == null) {
    for (const i of t)
      i(void 0);
    return Be;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
const qi = typeof window < "u";
let Rn = qi ? () => window.performance.now() : () => Date.now(), zi = qi ? (e) => requestAnimationFrame(e) : Be;
const Ge = /* @__PURE__ */ new Set();
function Xi(e) {
  Ge.forEach((t) => {
    t.c(e) || (Ge.delete(t), t.f());
  }), Ge.size !== 0 && zi(Xi);
}
function _s(e) {
  let t;
  return Ge.size === 0 && zi(Xi), {
    promise: new Promise((n) => {
      Ge.add(t = { c: e, f: n });
    }),
    abort() {
      Ge.delete(t);
    }
  };
}
const De = [];
function ms(e, t) {
  return {
    subscribe: it(e, t).subscribe
  };
}
function it(e, t = Be) {
  let n;
  const i = /* @__PURE__ */ new Set();
  function r(a) {
    if (cs(e, a) && (e = a, n)) {
      const s = !De.length;
      for (const u of i)
        u[1](), De.push(u, e);
      if (s) {
        for (let u = 0; u < De.length; u += 2)
          De[u][0](De[u + 1]);
        De.length = 0;
      }
    }
  }
  function l(a) {
    r(a(e));
  }
  function o(a, s = Be) {
    const u = [a, s];
    return i.add(u), i.size === 1 && (n = t(r, l) || Be), a(e), () => {
      i.delete(u), i.size === 0 && n && (n(), n = null);
    };
  }
  return { set: r, update: l, subscribe: o };
}
function Xe(e, t, n) {
  const i = !Array.isArray(e), r = i ? [e] : e;
  if (!r.every(Boolean))
    throw new Error("derived() expects stores as input, got a falsy value");
  const l = t.length < 2;
  return ms(n, (o, a) => {
    let s = !1;
    const u = [];
    let f = 0, c = Be;
    const h = () => {
      if (f)
        return;
      c();
      const g = t(i ? u[0] : u, o, a);
      l ? o(g) : c = fs(g) ? g : Be;
    }, _ = r.map(
      (g, S) => hs(
        g,
        (v) => {
          u[S] = v, f &= ~(1 << S), s && h();
        },
        () => {
          f |= 1 << S;
        }
      )
    );
    return s = !0, h(), function() {
      us(_), c(), s = !1;
    };
  });
}
function Dn(e) {
  return Object.prototype.toString.call(e) === "[object Date]";
}
function $t(e, t, n, i) {
  if (typeof n == "number" || Dn(n)) {
    const r = i - n, l = (n - t) / (e.dt || 1 / 60), o = e.opts.stiffness * r, a = e.opts.damping * l, s = (o - a) * e.inv_mass, u = (l + s) * e.dt;
    return Math.abs(u) < e.opts.precision && Math.abs(r) < e.opts.precision ? i : (e.settled = !1, Dn(n) ? new Date(n.getTime() + u) : n + u);
  } else {
    if (Array.isArray(n))
      return n.map(
        (r, l) => $t(e, t[l], n[l], i[l])
      );
    if (typeof n == "object") {
      const r = {};
      for (const l in n)
        r[l] = $t(e, t[l], n[l], i[l]);
      return r;
    } else
      throw new Error(`Cannot spring ${typeof n} values`);
  }
}
function Un(e, t = {}) {
  const n = it(e), { stiffness: i = 0.15, damping: r = 0.8, precision: l = 0.01 } = t;
  let o, a, s, u = e, f = e, c = 1, h = 0, _ = !1;
  function g(v, A = {}) {
    f = v;
    const y = s = {};
    return e == null || A.hard || S.stiffness >= 1 && S.damping >= 1 ? (_ = !0, o = Rn(), u = v, n.set(e = f), Promise.resolve()) : (A.soft && (h = 1 / ((A.soft === !0 ? 0.5 : +A.soft) * 60), c = 0), a || (o = Rn(), _ = !1, a = _s((d) => {
      if (_)
        return _ = !1, a = null, !1;
      c = Math.min(c + h, 1);
      const T = {
        inv_mass: c,
        opts: S,
        settled: !0,
        dt: (d - o) * 60 / 1e3
      }, b = $t(T, u, e, f);
      return o = d, u = e, n.set(e = b), T.settled && (a = null), !T.settled;
    })), new Promise((d) => {
      a.promise.then(() => {
        y === s && d();
      });
    }));
  }
  const S = {
    set: g,
    update: (v, A) => g(v(f, e), A),
    subscribe: n.subscribe,
    stiffness: i,
    damping: r,
    precision: l
  };
  return S;
}
function ds(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var bs = function(t) {
  return gs(t) && !ps(t);
};
function gs(e) {
  return !!e && typeof e == "object";
}
function ps(e) {
  var t = Object.prototype.toString.call(e);
  return t === "[object RegExp]" || t === "[object Date]" || ys(e);
}
var vs = typeof Symbol == "function" && Symbol.for, ws = vs ? Symbol.for("react.element") : 60103;
function ys(e) {
  return e.$$typeof === ws;
}
function Es(e) {
  return Array.isArray(e) ? [] : {};
}
function et(e, t) {
  return t.clone !== !1 && t.isMergeableObject(e) ? xe(Es(e), e, t) : e;
}
function Ss(e, t, n) {
  return e.concat(t).map(function(i) {
    return et(i, n);
  });
}
function Ts(e, t) {
  if (!t.customMerge)
    return xe;
  var n = t.customMerge(e);
  return typeof n == "function" ? n : xe;
}
function As(e) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(e).filter(function(t) {
    return Object.propertyIsEnumerable.call(e, t);
  }) : [];
}
function Gn(e) {
  return Object.keys(e).concat(As(e));
}
function Zi(e, t) {
  try {
    return t in e;
  } catch {
    return !1;
  }
}
function Hs(e, t) {
  return Zi(e, t) && !(Object.hasOwnProperty.call(e, t) && Object.propertyIsEnumerable.call(e, t));
}
function Bs(e, t, n) {
  var i = {};
  return n.isMergeableObject(e) && Gn(e).forEach(function(r) {
    i[r] = et(e[r], n);
  }), Gn(t).forEach(function(r) {
    Hs(e, r) || (Zi(e, r) && n.isMergeableObject(t[r]) ? i[r] = Ts(r, n)(e[r], t[r], n) : i[r] = et(t[r], n));
  }), i;
}
function xe(e, t, n) {
  n = n || {}, n.arrayMerge = n.arrayMerge || Ss, n.isMergeableObject = n.isMergeableObject || bs, n.cloneUnlessOtherwiseSpecified = et;
  var i = Array.isArray(t), r = Array.isArray(e), l = i === r;
  return l ? i ? n.arrayMerge(e, t, n) : Bs(e, t, n) : et(t, n);
}
xe.all = function(t, n) {
  if (!Array.isArray(t))
    throw new Error("first argument should be an array");
  return t.reduce(function(i, r) {
    return xe(i, r, n);
  }, {});
};
var ks = xe, Cs = ks;
const Ps = /* @__PURE__ */ ds(Cs);
var en = function(e, t) {
  return en = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(n, i) {
    n.__proto__ = i;
  } || function(n, i) {
    for (var r in i)
      Object.prototype.hasOwnProperty.call(i, r) && (n[r] = i[r]);
  }, en(e, t);
};
function Tt(e, t) {
  if (typeof t != "function" && t !== null)
    throw new TypeError("Class extends value " + String(t) + " is not a constructor or null");
  en(e, t);
  function n() {
    this.constructor = e;
  }
  e.prototype = t === null ? Object.create(t) : (n.prototype = t.prototype, new n());
}
var L = function() {
  return L = Object.assign || function(t) {
    for (var n, i = 1, r = arguments.length; i < r; i++) {
      n = arguments[i];
      for (var l in n)
        Object.prototype.hasOwnProperty.call(n, l) && (t[l] = n[l]);
    }
    return t;
  }, L.apply(this, arguments);
};
function qt(e, t, n) {
  if (n || arguments.length === 2)
    for (var i = 0, r = t.length, l; i < r; i++)
      (l || !(i in t)) && (l || (l = Array.prototype.slice.call(t, 0, i)), l[i] = t[i]);
  return e.concat(l || Array.prototype.slice.call(t));
}
var k;
(function(e) {
  e[e.EXPECT_ARGUMENT_CLOSING_BRACE = 1] = "EXPECT_ARGUMENT_CLOSING_BRACE", e[e.EMPTY_ARGUMENT = 2] = "EMPTY_ARGUMENT", e[e.MALFORMED_ARGUMENT = 3] = "MALFORMED_ARGUMENT", e[e.EXPECT_ARGUMENT_TYPE = 4] = "EXPECT_ARGUMENT_TYPE", e[e.INVALID_ARGUMENT_TYPE = 5] = "INVALID_ARGUMENT_TYPE", e[e.EXPECT_ARGUMENT_STYLE = 6] = "EXPECT_ARGUMENT_STYLE", e[e.INVALID_NUMBER_SKELETON = 7] = "INVALID_NUMBER_SKELETON", e[e.INVALID_DATE_TIME_SKELETON = 8] = "INVALID_DATE_TIME_SKELETON", e[e.EXPECT_NUMBER_SKELETON = 9] = "EXPECT_NUMBER_SKELETON", e[e.EXPECT_DATE_TIME_SKELETON = 10] = "EXPECT_DATE_TIME_SKELETON", e[e.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE = 11] = "UNCLOSED_QUOTE_IN_ARGUMENT_STYLE", e[e.EXPECT_SELECT_ARGUMENT_OPTIONS = 12] = "EXPECT_SELECT_ARGUMENT_OPTIONS", e[e.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE = 13] = "EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE = 14] = "INVALID_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR = 15] = "EXPECT_SELECT_ARGUMENT_SELECTOR", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR = 16] = "EXPECT_PLURAL_ARGUMENT_SELECTOR", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT = 17] = "EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT = 18] = "EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT", e[e.INVALID_PLURAL_ARGUMENT_SELECTOR = 19] = "INVALID_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_PLURAL_ARGUMENT_SELECTOR = 20] = "DUPLICATE_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_SELECT_ARGUMENT_SELECTOR = 21] = "DUPLICATE_SELECT_ARGUMENT_SELECTOR", e[e.MISSING_OTHER_CLAUSE = 22] = "MISSING_OTHER_CLAUSE", e[e.INVALID_TAG = 23] = "INVALID_TAG", e[e.INVALID_TAG_NAME = 25] = "INVALID_TAG_NAME", e[e.UNMATCHED_CLOSING_TAG = 26] = "UNMATCHED_CLOSING_TAG", e[e.UNCLOSED_TAG = 27] = "UNCLOSED_TAG";
})(k || (k = {}));
var R;
(function(e) {
  e[e.literal = 0] = "literal", e[e.argument = 1] = "argument", e[e.number = 2] = "number", e[e.date = 3] = "date", e[e.time = 4] = "time", e[e.select = 5] = "select", e[e.plural = 6] = "plural", e[e.pound = 7] = "pound", e[e.tag = 8] = "tag";
})(R || (R = {}));
var Fe;
(function(e) {
  e[e.number = 0] = "number", e[e.dateTime = 1] = "dateTime";
})(Fe || (Fe = {}));
function xn(e) {
  return e.type === R.literal;
}
function Is(e) {
  return e.type === R.argument;
}
function Wi(e) {
  return e.type === R.number;
}
function Qi(e) {
  return e.type === R.date;
}
function Ji(e) {
  return e.type === R.time;
}
function Yi(e) {
  return e.type === R.select;
}
function Ki(e) {
  return e.type === R.plural;
}
function Ls(e) {
  return e.type === R.pound;
}
function $i(e) {
  return e.type === R.tag;
}
function er(e) {
  return !!(e && typeof e == "object" && e.type === Fe.number);
}
function tn(e) {
  return !!(e && typeof e == "object" && e.type === Fe.dateTime);
}
var tr = /[ \xA0\u1680\u2000-\u200A\u202F\u205F\u3000]/, Ns = /(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;
function Os(e) {
  var t = {};
  return e.replace(Ns, function(n) {
    var i = n.length;
    switch (n[0]) {
      case "G":
        t.era = i === 4 ? "long" : i === 5 ? "narrow" : "short";
        break;
      case "y":
        t.year = i === 2 ? "2-digit" : "numeric";
        break;
      case "Y":
      case "u":
      case "U":
      case "r":
        throw new RangeError("`Y/u/U/r` (year) patterns are not supported, use `y` instead");
      case "q":
      case "Q":
        throw new RangeError("`q/Q` (quarter) patterns are not supported");
      case "M":
      case "L":
        t.month = ["numeric", "2-digit", "short", "long", "narrow"][i - 1];
        break;
      case "w":
      case "W":
        throw new RangeError("`w/W` (week) patterns are not supported");
      case "d":
        t.day = ["numeric", "2-digit"][i - 1];
        break;
      case "D":
      case "F":
      case "g":
        throw new RangeError("`D/F/g` (day) patterns are not supported, use `d` instead");
      case "E":
        t.weekday = i === 4 ? "short" : i === 5 ? "narrow" : "short";
        break;
      case "e":
        if (i < 4)
          throw new RangeError("`e..eee` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][i - 4];
        break;
      case "c":
        if (i < 4)
          throw new RangeError("`c..ccc` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][i - 4];
        break;
      case "a":
        t.hour12 = !0;
        break;
      case "b":
      case "B":
        throw new RangeError("`b/B` (period) patterns are not supported, use `a` instead");
      case "h":
        t.hourCycle = "h12", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "H":
        t.hourCycle = "h23", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "K":
        t.hourCycle = "h11", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "k":
        t.hourCycle = "h24", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "j":
      case "J":
      case "C":
        throw new RangeError("`j/J/C` (hour) patterns are not supported, use `h/H/K/k` instead");
      case "m":
        t.minute = ["numeric", "2-digit"][i - 1];
        break;
      case "s":
        t.second = ["numeric", "2-digit"][i - 1];
        break;
      case "S":
      case "A":
        throw new RangeError("`S/A` (second) patterns are not supported, use `s` instead");
      case "z":
        t.timeZoneName = i < 4 ? "short" : "long";
        break;
      case "Z":
      case "O":
      case "v":
      case "V":
      case "X":
      case "x":
        throw new RangeError("`Z/O/v/V/X/x` (timeZone) patterns are not supported, use `z` instead");
    }
    return "";
  }), t;
}
var Ms = /[\t-\r \x85\u200E\u200F\u2028\u2029]/i;
function Rs(e) {
  if (e.length === 0)
    throw new Error("Number skeleton cannot be empty");
  for (var t = e.split(Ms).filter(function(h) {
    return h.length > 0;
  }), n = [], i = 0, r = t; i < r.length; i++) {
    var l = r[i], o = l.split("/");
    if (o.length === 0)
      throw new Error("Invalid number skeleton");
    for (var a = o[0], s = o.slice(1), u = 0, f = s; u < f.length; u++) {
      var c = f[u];
      if (c.length === 0)
        throw new Error("Invalid number skeleton");
    }
    n.push({ stem: a, options: s });
  }
  return n;
}
function Ds(e) {
  return e.replace(/^(.*?)-/, "");
}
var Fn = /^\.(?:(0+)(\*)?|(#+)|(0+)(#+))$/g, nr = /^(@+)?(\+|#+)?[rs]?$/g, Us = /(\*)(0+)|(#+)(0+)|(0+)/g, ir = /^(0+)$/;
function jn(e) {
  var t = {};
  return e[e.length - 1] === "r" ? t.roundingPriority = "morePrecision" : e[e.length - 1] === "s" && (t.roundingPriority = "lessPrecision"), e.replace(nr, function(n, i, r) {
    return typeof r != "string" ? (t.minimumSignificantDigits = i.length, t.maximumSignificantDigits = i.length) : r === "+" ? t.minimumSignificantDigits = i.length : i[0] === "#" ? t.maximumSignificantDigits = i.length : (t.minimumSignificantDigits = i.length, t.maximumSignificantDigits = i.length + (typeof r == "string" ? r.length : 0)), "";
  }), t;
}
function rr(e) {
  switch (e) {
    case "sign-auto":
      return {
        signDisplay: "auto"
      };
    case "sign-accounting":
    case "()":
      return {
        currencySign: "accounting"
      };
    case "sign-always":
    case "+!":
      return {
        signDisplay: "always"
      };
    case "sign-accounting-always":
    case "()!":
      return {
        signDisplay: "always",
        currencySign: "accounting"
      };
    case "sign-except-zero":
    case "+?":
      return {
        signDisplay: "exceptZero"
      };
    case "sign-accounting-except-zero":
    case "()?":
      return {
        signDisplay: "exceptZero",
        currencySign: "accounting"
      };
    case "sign-never":
    case "+_":
      return {
        signDisplay: "never"
      };
  }
}
function Gs(e) {
  var t;
  if (e[0] === "E" && e[1] === "E" ? (t = {
    notation: "engineering"
  }, e = e.slice(2)) : e[0] === "E" && (t = {
    notation: "scientific"
  }, e = e.slice(1)), t) {
    var n = e.slice(0, 2);
    if (n === "+!" ? (t.signDisplay = "always", e = e.slice(2)) : n === "+?" && (t.signDisplay = "exceptZero", e = e.slice(2)), !ir.test(e))
      throw new Error("Malformed concise eng/scientific notation");
    t.minimumIntegerDigits = e.length;
  }
  return t;
}
function Vn(e) {
  var t = {}, n = rr(e);
  return n || t;
}
function xs(e) {
  for (var t = {}, n = 0, i = e; n < i.length; n++) {
    var r = i[n];
    switch (r.stem) {
      case "percent":
      case "%":
        t.style = "percent";
        continue;
      case "%x100":
        t.style = "percent", t.scale = 100;
        continue;
      case "currency":
        t.style = "currency", t.currency = r.options[0];
        continue;
      case "group-off":
      case ",_":
        t.useGrouping = !1;
        continue;
      case "precision-integer":
      case ".":
        t.maximumFractionDigits = 0;
        continue;
      case "measure-unit":
      case "unit":
        t.style = "unit", t.unit = Ds(r.options[0]);
        continue;
      case "compact-short":
      case "K":
        t.notation = "compact", t.compactDisplay = "short";
        continue;
      case "compact-long":
      case "KK":
        t.notation = "compact", t.compactDisplay = "long";
        continue;
      case "scientific":
        t = L(L(L({}, t), { notation: "scientific" }), r.options.reduce(function(s, u) {
          return L(L({}, s), Vn(u));
        }, {}));
        continue;
      case "engineering":
        t = L(L(L({}, t), { notation: "engineering" }), r.options.reduce(function(s, u) {
          return L(L({}, s), Vn(u));
        }, {}));
        continue;
      case "notation-simple":
        t.notation = "standard";
        continue;
      case "unit-width-narrow":
        t.currencyDisplay = "narrowSymbol", t.unitDisplay = "narrow";
        continue;
      case "unit-width-short":
        t.currencyDisplay = "code", t.unitDisplay = "short";
        continue;
      case "unit-width-full-name":
        t.currencyDisplay = "name", t.unitDisplay = "long";
        continue;
      case "unit-width-iso-code":
        t.currencyDisplay = "symbol";
        continue;
      case "scale":
        t.scale = parseFloat(r.options[0]);
        continue;
      case "integer-width":
        if (r.options.length > 1)
          throw new RangeError("integer-width stems only accept a single optional option");
        r.options[0].replace(Us, function(s, u, f, c, h, _) {
          if (u)
            t.minimumIntegerDigits = f.length;
          else {
            if (c && h)
              throw new Error("We currently do not support maximum integer digits");
            if (_)
              throw new Error("We currently do not support exact integer digits");
          }
          return "";
        });
        continue;
    }
    if (ir.test(r.stem)) {
      t.minimumIntegerDigits = r.stem.length;
      continue;
    }
    if (Fn.test(r.stem)) {
      if (r.options.length > 1)
        throw new RangeError("Fraction-precision stems only accept a single optional option");
      r.stem.replace(Fn, function(s, u, f, c, h, _) {
        return f === "*" ? t.minimumFractionDigits = u.length : c && c[0] === "#" ? t.maximumFractionDigits = c.length : h && _ ? (t.minimumFractionDigits = h.length, t.maximumFractionDigits = h.length + _.length) : (t.minimumFractionDigits = u.length, t.maximumFractionDigits = u.length), "";
      });
      var l = r.options[0];
      l === "w" ? t = L(L({}, t), { trailingZeroDisplay: "stripIfInteger" }) : l && (t = L(L({}, t), jn(l)));
      continue;
    }
    if (nr.test(r.stem)) {
      t = L(L({}, t), jn(r.stem));
      continue;
    }
    var o = rr(r.stem);
    o && (t = L(L({}, t), o));
    var a = Gs(r.stem);
    a && (t = L(L({}, t), a));
  }
  return t;
}
var mt = {
  AX: [
    "H"
  ],
  BQ: [
    "H"
  ],
  CP: [
    "H"
  ],
  CZ: [
    "H"
  ],
  DK: [
    "H"
  ],
  FI: [
    "H"
  ],
  ID: [
    "H"
  ],
  IS: [
    "H"
  ],
  ML: [
    "H"
  ],
  NE: [
    "H"
  ],
  RU: [
    "H"
  ],
  SE: [
    "H"
  ],
  SJ: [
    "H"
  ],
  SK: [
    "H"
  ],
  AS: [
    "h",
    "H"
  ],
  BT: [
    "h",
    "H"
  ],
  DJ: [
    "h",
    "H"
  ],
  ER: [
    "h",
    "H"
  ],
  GH: [
    "h",
    "H"
  ],
  IN: [
    "h",
    "H"
  ],
  LS: [
    "h",
    "H"
  ],
  PG: [
    "h",
    "H"
  ],
  PW: [
    "h",
    "H"
  ],
  SO: [
    "h",
    "H"
  ],
  TO: [
    "h",
    "H"
  ],
  VU: [
    "h",
    "H"
  ],
  WS: [
    "h",
    "H"
  ],
  "001": [
    "H",
    "h"
  ],
  AL: [
    "h",
    "H",
    "hB"
  ],
  TD: [
    "h",
    "H",
    "hB"
  ],
  "ca-ES": [
    "H",
    "h",
    "hB"
  ],
  CF: [
    "H",
    "h",
    "hB"
  ],
  CM: [
    "H",
    "h",
    "hB"
  ],
  "fr-CA": [
    "H",
    "h",
    "hB"
  ],
  "gl-ES": [
    "H",
    "h",
    "hB"
  ],
  "it-CH": [
    "H",
    "h",
    "hB"
  ],
  "it-IT": [
    "H",
    "h",
    "hB"
  ],
  LU: [
    "H",
    "h",
    "hB"
  ],
  NP: [
    "H",
    "h",
    "hB"
  ],
  PF: [
    "H",
    "h",
    "hB"
  ],
  SC: [
    "H",
    "h",
    "hB"
  ],
  SM: [
    "H",
    "h",
    "hB"
  ],
  SN: [
    "H",
    "h",
    "hB"
  ],
  TF: [
    "H",
    "h",
    "hB"
  ],
  VA: [
    "H",
    "h",
    "hB"
  ],
  CY: [
    "h",
    "H",
    "hb",
    "hB"
  ],
  GR: [
    "h",
    "H",
    "hb",
    "hB"
  ],
  CO: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  DO: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  KP: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  KR: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  NA: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  PA: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  PR: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  VE: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  AC: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  AI: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  BW: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  BZ: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CC: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CX: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  DG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  FK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GB: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GI: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IE: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IM: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IO: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  JE: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  LT: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MN: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MS: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NF: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NR: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NU: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  PN: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  SH: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  SX: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  TA: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  ZA: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  "af-ZA": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  AR: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CL: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CR: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CU: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  EA: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-BO": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-BR": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-EC": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-ES": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-GQ": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-PE": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  GT: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  HN: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  IC: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  KG: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  KM: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  LK: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  MA: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  MX: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  NI: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  PY: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  SV: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  UY: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  JP: [
    "H",
    "h",
    "K"
  ],
  AD: [
    "H",
    "hB"
  ],
  AM: [
    "H",
    "hB"
  ],
  AO: [
    "H",
    "hB"
  ],
  AT: [
    "H",
    "hB"
  ],
  AW: [
    "H",
    "hB"
  ],
  BE: [
    "H",
    "hB"
  ],
  BF: [
    "H",
    "hB"
  ],
  BJ: [
    "H",
    "hB"
  ],
  BL: [
    "H",
    "hB"
  ],
  BR: [
    "H",
    "hB"
  ],
  CG: [
    "H",
    "hB"
  ],
  CI: [
    "H",
    "hB"
  ],
  CV: [
    "H",
    "hB"
  ],
  DE: [
    "H",
    "hB"
  ],
  EE: [
    "H",
    "hB"
  ],
  FR: [
    "H",
    "hB"
  ],
  GA: [
    "H",
    "hB"
  ],
  GF: [
    "H",
    "hB"
  ],
  GN: [
    "H",
    "hB"
  ],
  GP: [
    "H",
    "hB"
  ],
  GW: [
    "H",
    "hB"
  ],
  HR: [
    "H",
    "hB"
  ],
  IL: [
    "H",
    "hB"
  ],
  IT: [
    "H",
    "hB"
  ],
  KZ: [
    "H",
    "hB"
  ],
  MC: [
    "H",
    "hB"
  ],
  MD: [
    "H",
    "hB"
  ],
  MF: [
    "H",
    "hB"
  ],
  MQ: [
    "H",
    "hB"
  ],
  MZ: [
    "H",
    "hB"
  ],
  NC: [
    "H",
    "hB"
  ],
  NL: [
    "H",
    "hB"
  ],
  PM: [
    "H",
    "hB"
  ],
  PT: [
    "H",
    "hB"
  ],
  RE: [
    "H",
    "hB"
  ],
  RO: [
    "H",
    "hB"
  ],
  SI: [
    "H",
    "hB"
  ],
  SR: [
    "H",
    "hB"
  ],
  ST: [
    "H",
    "hB"
  ],
  TG: [
    "H",
    "hB"
  ],
  TR: [
    "H",
    "hB"
  ],
  WF: [
    "H",
    "hB"
  ],
  YT: [
    "H",
    "hB"
  ],
  BD: [
    "h",
    "hB",
    "H"
  ],
  PK: [
    "h",
    "hB",
    "H"
  ],
  AZ: [
    "H",
    "hB",
    "h"
  ],
  BA: [
    "H",
    "hB",
    "h"
  ],
  BG: [
    "H",
    "hB",
    "h"
  ],
  CH: [
    "H",
    "hB",
    "h"
  ],
  GE: [
    "H",
    "hB",
    "h"
  ],
  LI: [
    "H",
    "hB",
    "h"
  ],
  ME: [
    "H",
    "hB",
    "h"
  ],
  RS: [
    "H",
    "hB",
    "h"
  ],
  UA: [
    "H",
    "hB",
    "h"
  ],
  UZ: [
    "H",
    "hB",
    "h"
  ],
  XK: [
    "H",
    "hB",
    "h"
  ],
  AG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  AU: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BB: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BS: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  CA: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  DM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  "en-001": [
    "h",
    "hb",
    "H",
    "hB"
  ],
  FJ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  FM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GD: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GU: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GY: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  JM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KI: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KN: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KY: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  LC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  LR: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MH: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MP: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MW: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  NZ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SB: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SL: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SS: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SZ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  TC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  TT: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  UM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  US: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VI: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  ZM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BO: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  EC: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  ES: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  GQ: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  PE: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  AE: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  "ar-001": [
    "h",
    "hB",
    "hb",
    "H"
  ],
  BH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  DZ: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  EG: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  EH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  HK: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  IQ: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  JO: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  KW: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  LB: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  LY: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  MO: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  MR: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  OM: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  PH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  PS: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  QA: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SA: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SD: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SY: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  TN: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  YE: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  AF: [
    "H",
    "hb",
    "hB",
    "h"
  ],
  LA: [
    "H",
    "hb",
    "hB",
    "h"
  ],
  CN: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  LV: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  TL: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  "zu-ZA": [
    "H",
    "hB",
    "hb",
    "h"
  ],
  CD: [
    "hB",
    "H"
  ],
  IR: [
    "hB",
    "H"
  ],
  "hi-IN": [
    "hB",
    "h",
    "H"
  ],
  "kn-IN": [
    "hB",
    "h",
    "H"
  ],
  "ml-IN": [
    "hB",
    "h",
    "H"
  ],
  "te-IN": [
    "hB",
    "h",
    "H"
  ],
  KH: [
    "hB",
    "h",
    "H",
    "hb"
  ],
  "ta-IN": [
    "hB",
    "h",
    "hb",
    "H"
  ],
  BN: [
    "hb",
    "hB",
    "h",
    "H"
  ],
  MY: [
    "hb",
    "hB",
    "h",
    "H"
  ],
  ET: [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "gu-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "mr-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "pa-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  TW: [
    "hB",
    "hb",
    "h",
    "H"
  ],
  KE: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  MM: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  TZ: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  UG: [
    "hB",
    "hb",
    "H",
    "h"
  ]
};
function Fs(e, t) {
  for (var n = "", i = 0; i < e.length; i++) {
    var r = e.charAt(i);
    if (r === "j") {
      for (var l = 0; i + 1 < e.length && e.charAt(i + 1) === r; )
        l++, i++;
      var o = 1 + (l & 1), a = l < 2 ? 1 : 3 + (l >> 1), s = "a", u = js(t);
      for ((u == "H" || u == "k") && (a = 0); a-- > 0; )
        n += s;
      for (; o-- > 0; )
        n = u + n;
    } else
      r === "J" ? n += "H" : n += r;
  }
  return n;
}
function js(e) {
  var t = e.hourCycle;
  if (t === void 0 && // @ts-ignore hourCycle(s) is not identified yet
  e.hourCycles && // @ts-ignore
  e.hourCycles.length && (t = e.hourCycles[0]), t)
    switch (t) {
      case "h24":
        return "k";
      case "h23":
        return "H";
      case "h12":
        return "h";
      case "h11":
        return "K";
      default:
        throw new Error("Invalid hourCycle");
    }
  var n = e.language, i;
  n !== "root" && (i = e.maximize().region);
  var r = mt[i || ""] || mt[n || ""] || mt["".concat(n, "-001")] || mt["001"];
  return r[0];
}
var zt, Vs = new RegExp("^".concat(tr.source, "*")), qs = new RegExp("".concat(tr.source, "*$"));
function C(e, t) {
  return { start: e, end: t };
}
var zs = !!String.prototype.startsWith, Xs = !!String.fromCodePoint, Zs = !!Object.fromEntries, Ws = !!String.prototype.codePointAt, Qs = !!String.prototype.trimStart, Js = !!String.prototype.trimEnd, Ys = !!Number.isSafeInteger, Ks = Ys ? Number.isSafeInteger : function(e) {
  return typeof e == "number" && isFinite(e) && Math.floor(e) === e && Math.abs(e) <= 9007199254740991;
}, nn = !0;
try {
  var $s = or("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  nn = ((zt = $s.exec("a")) === null || zt === void 0 ? void 0 : zt[0]) === "a";
} catch {
  nn = !1;
}
var qn = zs ? (
  // Native
  function(t, n, i) {
    return t.startsWith(n, i);
  }
) : (
  // For IE11
  function(t, n, i) {
    return t.slice(i, i + n.length) === n;
  }
), rn = Xs ? String.fromCodePoint : (
  // IE11
  function() {
    for (var t = [], n = 0; n < arguments.length; n++)
      t[n] = arguments[n];
    for (var i = "", r = t.length, l = 0, o; r > l; ) {
      if (o = t[l++], o > 1114111)
        throw RangeError(o + " is not a valid code point");
      i += o < 65536 ? String.fromCharCode(o) : String.fromCharCode(((o -= 65536) >> 10) + 55296, o % 1024 + 56320);
    }
    return i;
  }
), zn = (
  // native
  Zs ? Object.fromEntries : (
    // Ponyfill
    function(t) {
      for (var n = {}, i = 0, r = t; i < r.length; i++) {
        var l = r[i], o = l[0], a = l[1];
        n[o] = a;
      }
      return n;
    }
  )
), lr = Ws ? (
  // Native
  function(t, n) {
    return t.codePointAt(n);
  }
) : (
  // IE 11
  function(t, n) {
    var i = t.length;
    if (!(n < 0 || n >= i)) {
      var r = t.charCodeAt(n), l;
      return r < 55296 || r > 56319 || n + 1 === i || (l = t.charCodeAt(n + 1)) < 56320 || l > 57343 ? r : (r - 55296 << 10) + (l - 56320) + 65536;
    }
  }
), ea = Qs ? (
  // Native
  function(t) {
    return t.trimStart();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Vs, "");
  }
), ta = Js ? (
  // Native
  function(t) {
    return t.trimEnd();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(qs, "");
  }
);
function or(e, t) {
  return new RegExp(e, t);
}
var ln;
if (nn) {
  var Xn = or("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  ln = function(t, n) {
    var i;
    Xn.lastIndex = n;
    var r = Xn.exec(t);
    return (i = r[1]) !== null && i !== void 0 ? i : "";
  };
} else
  ln = function(t, n) {
    for (var i = []; ; ) {
      var r = lr(t, n);
      if (r === void 0 || sr(r) || la(r))
        break;
      i.push(r), n += r >= 65536 ? 2 : 1;
    }
    return rn.apply(void 0, i);
  };
var na = (
  /** @class */
  function() {
    function e(t, n) {
      n === void 0 && (n = {}), this.message = t, this.position = { offset: 0, line: 1, column: 1 }, this.ignoreTag = !!n.ignoreTag, this.locale = n.locale, this.requiresOtherClause = !!n.requiresOtherClause, this.shouldParseSkeletons = !!n.shouldParseSkeletons;
    }
    return e.prototype.parse = function() {
      if (this.offset() !== 0)
        throw Error("parser can only be used once");
      return this.parseMessage(0, "", !1);
    }, e.prototype.parseMessage = function(t, n, i) {
      for (var r = []; !this.isEOF(); ) {
        var l = this.char();
        if (l === 123) {
          var o = this.parseArgument(t, i);
          if (o.err)
            return o;
          r.push(o.val);
        } else {
          if (l === 125 && t > 0)
            break;
          if (l === 35 && (n === "plural" || n === "selectordinal")) {
            var a = this.clonePosition();
            this.bump(), r.push({
              type: R.pound,
              location: C(a, this.clonePosition())
            });
          } else if (l === 60 && !this.ignoreTag && this.peek() === 47) {
            if (i)
              break;
            return this.error(k.UNMATCHED_CLOSING_TAG, C(this.clonePosition(), this.clonePosition()));
          } else if (l === 60 && !this.ignoreTag && on(this.peek() || 0)) {
            var o = this.parseTag(t, n);
            if (o.err)
              return o;
            r.push(o.val);
          } else {
            var o = this.parseLiteral(t, n);
            if (o.err)
              return o;
            r.push(o.val);
          }
        }
      }
      return { val: r, err: null };
    }, e.prototype.parseTag = function(t, n) {
      var i = this.clonePosition();
      this.bump();
      var r = this.parseTagName();
      if (this.bumpSpace(), this.bumpIf("/>"))
        return {
          val: {
            type: R.literal,
            value: "<".concat(r, "/>"),
            location: C(i, this.clonePosition())
          },
          err: null
        };
      if (this.bumpIf(">")) {
        var l = this.parseMessage(t + 1, n, !0);
        if (l.err)
          return l;
        var o = l.val, a = this.clonePosition();
        if (this.bumpIf("</")) {
          if (this.isEOF() || !on(this.char()))
            return this.error(k.INVALID_TAG, C(a, this.clonePosition()));
          var s = this.clonePosition(), u = this.parseTagName();
          return r !== u ? this.error(k.UNMATCHED_CLOSING_TAG, C(s, this.clonePosition())) : (this.bumpSpace(), this.bumpIf(">") ? {
            val: {
              type: R.tag,
              value: r,
              children: o,
              location: C(i, this.clonePosition())
            },
            err: null
          } : this.error(k.INVALID_TAG, C(a, this.clonePosition())));
        } else
          return this.error(k.UNCLOSED_TAG, C(i, this.clonePosition()));
      } else
        return this.error(k.INVALID_TAG, C(i, this.clonePosition()));
    }, e.prototype.parseTagName = function() {
      var t = this.offset();
      for (this.bump(); !this.isEOF() && ra(this.char()); )
        this.bump();
      return this.message.slice(t, this.offset());
    }, e.prototype.parseLiteral = function(t, n) {
      for (var i = this.clonePosition(), r = ""; ; ) {
        var l = this.tryParseQuote(n);
        if (l) {
          r += l;
          continue;
        }
        var o = this.tryParseUnquoted(t, n);
        if (o) {
          r += o;
          continue;
        }
        var a = this.tryParseLeftAngleBracket();
        if (a) {
          r += a;
          continue;
        }
        break;
      }
      var s = C(i, this.clonePosition());
      return {
        val: { type: R.literal, value: r, location: s },
        err: null
      };
    }, e.prototype.tryParseLeftAngleBracket = function() {
      return !this.isEOF() && this.char() === 60 && (this.ignoreTag || // If at the opening tag or closing tag position, bail.
      !ia(this.peek() || 0)) ? (this.bump(), "<") : null;
    }, e.prototype.tryParseQuote = function(t) {
      if (this.isEOF() || this.char() !== 39)
        return null;
      switch (this.peek()) {
        case 39:
          return this.bump(), this.bump(), "'";
        case 123:
        case 60:
        case 62:
        case 125:
          break;
        case 35:
          if (t === "plural" || t === "selectordinal")
            break;
          return null;
        default:
          return null;
      }
      this.bump();
      var n = [this.char()];
      for (this.bump(); !this.isEOF(); ) {
        var i = this.char();
        if (i === 39)
          if (this.peek() === 39)
            n.push(39), this.bump();
          else {
            this.bump();
            break;
          }
        else
          n.push(i);
        this.bump();
      }
      return rn.apply(void 0, n);
    }, e.prototype.tryParseUnquoted = function(t, n) {
      if (this.isEOF())
        return null;
      var i = this.char();
      return i === 60 || i === 123 || i === 35 && (n === "plural" || n === "selectordinal") || i === 125 && t > 0 ? null : (this.bump(), rn(i));
    }, e.prototype.parseArgument = function(t, n) {
      var i = this.clonePosition();
      if (this.bump(), this.bumpSpace(), this.isEOF())
        return this.error(k.EXPECT_ARGUMENT_CLOSING_BRACE, C(i, this.clonePosition()));
      if (this.char() === 125)
        return this.bump(), this.error(k.EMPTY_ARGUMENT, C(i, this.clonePosition()));
      var r = this.parseIdentifierIfPossible().value;
      if (!r)
        return this.error(k.MALFORMED_ARGUMENT, C(i, this.clonePosition()));
      if (this.bumpSpace(), this.isEOF())
        return this.error(k.EXPECT_ARGUMENT_CLOSING_BRACE, C(i, this.clonePosition()));
      switch (this.char()) {
        case 125:
          return this.bump(), {
            val: {
              type: R.argument,
              // value does not include the opening and closing braces.
              value: r,
              location: C(i, this.clonePosition())
            },
            err: null
          };
        case 44:
          return this.bump(), this.bumpSpace(), this.isEOF() ? this.error(k.EXPECT_ARGUMENT_CLOSING_BRACE, C(i, this.clonePosition())) : this.parseArgumentOptions(t, n, r, i);
        default:
          return this.error(k.MALFORMED_ARGUMENT, C(i, this.clonePosition()));
      }
    }, e.prototype.parseIdentifierIfPossible = function() {
      var t = this.clonePosition(), n = this.offset(), i = ln(this.message, n), r = n + i.length;
      this.bumpTo(r);
      var l = this.clonePosition(), o = C(t, l);
      return { value: i, location: o };
    }, e.prototype.parseArgumentOptions = function(t, n, i, r) {
      var l, o = this.clonePosition(), a = this.parseIdentifierIfPossible().value, s = this.clonePosition();
      switch (a) {
        case "":
          return this.error(k.EXPECT_ARGUMENT_TYPE, C(o, s));
        case "number":
        case "date":
        case "time": {
          this.bumpSpace();
          var u = null;
          if (this.bumpIf(",")) {
            this.bumpSpace();
            var f = this.clonePosition(), c = this.parseSimpleArgStyleIfPossible();
            if (c.err)
              return c;
            var h = ta(c.val);
            if (h.length === 0)
              return this.error(k.EXPECT_ARGUMENT_STYLE, C(this.clonePosition(), this.clonePosition()));
            var _ = C(f, this.clonePosition());
            u = { style: h, styleLocation: _ };
          }
          var g = this.tryParseArgumentClose(r);
          if (g.err)
            return g;
          var S = C(r, this.clonePosition());
          if (u && qn(u == null ? void 0 : u.style, "::", 0)) {
            var v = ea(u.style.slice(2));
            if (a === "number") {
              var c = this.parseNumberSkeletonFromString(v, u.styleLocation);
              return c.err ? c : {
                val: { type: R.number, value: i, location: S, style: c.val },
                err: null
              };
            } else {
              if (v.length === 0)
                return this.error(k.EXPECT_DATE_TIME_SKELETON, S);
              var A = v;
              this.locale && (A = Fs(v, this.locale));
              var h = {
                type: Fe.dateTime,
                pattern: A,
                location: u.styleLocation,
                parsedOptions: this.shouldParseSkeletons ? Os(A) : {}
              }, y = a === "date" ? R.date : R.time;
              return {
                val: { type: y, value: i, location: S, style: h },
                err: null
              };
            }
          }
          return {
            val: {
              type: a === "number" ? R.number : a === "date" ? R.date : R.time,
              value: i,
              location: S,
              style: (l = u == null ? void 0 : u.style) !== null && l !== void 0 ? l : null
            },
            err: null
          };
        }
        case "plural":
        case "selectordinal":
        case "select": {
          var d = this.clonePosition();
          if (this.bumpSpace(), !this.bumpIf(","))
            return this.error(k.EXPECT_SELECT_ARGUMENT_OPTIONS, C(d, L({}, d)));
          this.bumpSpace();
          var T = this.parseIdentifierIfPossible(), b = 0;
          if (a !== "select" && T.value === "offset") {
            if (!this.bumpIf(":"))
              return this.error(k.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, C(this.clonePosition(), this.clonePosition()));
            this.bumpSpace();
            var c = this.tryParseDecimalInteger(k.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, k.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE);
            if (c.err)
              return c;
            this.bumpSpace(), T = this.parseIdentifierIfPossible(), b = c.val;
          }
          var I = this.tryParsePluralOrSelectOptions(t, a, n, T);
          if (I.err)
            return I;
          var g = this.tryParseArgumentClose(r);
          if (g.err)
            return g;
          var M = C(r, this.clonePosition());
          return a === "select" ? {
            val: {
              type: R.select,
              value: i,
              options: zn(I.val),
              location: M
            },
            err: null
          } : {
            val: {
              type: R.plural,
              value: i,
              options: zn(I.val),
              offset: b,
              pluralType: a === "plural" ? "cardinal" : "ordinal",
              location: M
            },
            err: null
          };
        }
        default:
          return this.error(k.INVALID_ARGUMENT_TYPE, C(o, s));
      }
    }, e.prototype.tryParseArgumentClose = function(t) {
      return this.isEOF() || this.char() !== 125 ? this.error(k.EXPECT_ARGUMENT_CLOSING_BRACE, C(t, this.clonePosition())) : (this.bump(), { val: !0, err: null });
    }, e.prototype.parseSimpleArgStyleIfPossible = function() {
      for (var t = 0, n = this.clonePosition(); !this.isEOF(); ) {
        var i = this.char();
        switch (i) {
          case 39: {
            this.bump();
            var r = this.clonePosition();
            if (!this.bumpUntil("'"))
              return this.error(k.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE, C(r, this.clonePosition()));
            this.bump();
            break;
          }
          case 123: {
            t += 1, this.bump();
            break;
          }
          case 125: {
            if (t > 0)
              t -= 1;
            else
              return {
                val: this.message.slice(n.offset, this.offset()),
                err: null
              };
            break;
          }
          default:
            this.bump();
            break;
        }
      }
      return {
        val: this.message.slice(n.offset, this.offset()),
        err: null
      };
    }, e.prototype.parseNumberSkeletonFromString = function(t, n) {
      var i = [];
      try {
        i = Rs(t);
      } catch {
        return this.error(k.INVALID_NUMBER_SKELETON, n);
      }
      return {
        val: {
          type: Fe.number,
          tokens: i,
          location: n,
          parsedOptions: this.shouldParseSkeletons ? xs(i) : {}
        },
        err: null
      };
    }, e.prototype.tryParsePluralOrSelectOptions = function(t, n, i, r) {
      for (var l, o = !1, a = [], s = /* @__PURE__ */ new Set(), u = r.value, f = r.location; ; ) {
        if (u.length === 0) {
          var c = this.clonePosition();
          if (n !== "select" && this.bumpIf("=")) {
            var h = this.tryParseDecimalInteger(k.EXPECT_PLURAL_ARGUMENT_SELECTOR, k.INVALID_PLURAL_ARGUMENT_SELECTOR);
            if (h.err)
              return h;
            f = C(c, this.clonePosition()), u = this.message.slice(c.offset, this.offset());
          } else
            break;
        }
        if (s.has(u))
          return this.error(n === "select" ? k.DUPLICATE_SELECT_ARGUMENT_SELECTOR : k.DUPLICATE_PLURAL_ARGUMENT_SELECTOR, f);
        u === "other" && (o = !0), this.bumpSpace();
        var _ = this.clonePosition();
        if (!this.bumpIf("{"))
          return this.error(n === "select" ? k.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT : k.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT, C(this.clonePosition(), this.clonePosition()));
        var g = this.parseMessage(t + 1, n, i);
        if (g.err)
          return g;
        var S = this.tryParseArgumentClose(_);
        if (S.err)
          return S;
        a.push([
          u,
          {
            value: g.val,
            location: C(_, this.clonePosition())
          }
        ]), s.add(u), this.bumpSpace(), l = this.parseIdentifierIfPossible(), u = l.value, f = l.location;
      }
      return a.length === 0 ? this.error(n === "select" ? k.EXPECT_SELECT_ARGUMENT_SELECTOR : k.EXPECT_PLURAL_ARGUMENT_SELECTOR, C(this.clonePosition(), this.clonePosition())) : this.requiresOtherClause && !o ? this.error(k.MISSING_OTHER_CLAUSE, C(this.clonePosition(), this.clonePosition())) : { val: a, err: null };
    }, e.prototype.tryParseDecimalInteger = function(t, n) {
      var i = 1, r = this.clonePosition();
      this.bumpIf("+") || this.bumpIf("-") && (i = -1);
      for (var l = !1, o = 0; !this.isEOF(); ) {
        var a = this.char();
        if (a >= 48 && a <= 57)
          l = !0, o = o * 10 + (a - 48), this.bump();
        else
          break;
      }
      var s = C(r, this.clonePosition());
      return l ? (o *= i, Ks(o) ? { val: o, err: null } : this.error(n, s)) : this.error(t, s);
    }, e.prototype.offset = function() {
      return this.position.offset;
    }, e.prototype.isEOF = function() {
      return this.offset() === this.message.length;
    }, e.prototype.clonePosition = function() {
      return {
        offset: this.position.offset,
        line: this.position.line,
        column: this.position.column
      };
    }, e.prototype.char = function() {
      var t = this.position.offset;
      if (t >= this.message.length)
        throw Error("out of bound");
      var n = lr(this.message, t);
      if (n === void 0)
        throw Error("Offset ".concat(t, " is at invalid UTF-16 code unit boundary"));
      return n;
    }, e.prototype.error = function(t, n) {
      return {
        val: null,
        err: {
          kind: t,
          message: this.message,
          location: n
        }
      };
    }, e.prototype.bump = function() {
      if (!this.isEOF()) {
        var t = this.char();
        t === 10 ? (this.position.line += 1, this.position.column = 1, this.position.offset += 1) : (this.position.column += 1, this.position.offset += t < 65536 ? 1 : 2);
      }
    }, e.prototype.bumpIf = function(t) {
      if (qn(this.message, t, this.offset())) {
        for (var n = 0; n < t.length; n++)
          this.bump();
        return !0;
      }
      return !1;
    }, e.prototype.bumpUntil = function(t) {
      var n = this.offset(), i = this.message.indexOf(t, n);
      return i >= 0 ? (this.bumpTo(i), !0) : (this.bumpTo(this.message.length), !1);
    }, e.prototype.bumpTo = function(t) {
      if (this.offset() > t)
        throw Error("targetOffset ".concat(t, " must be greater than or equal to the current offset ").concat(this.offset()));
      for (t = Math.min(t, this.message.length); ; ) {
        var n = this.offset();
        if (n === t)
          break;
        if (n > t)
          throw Error("targetOffset ".concat(t, " is at invalid UTF-16 code unit boundary"));
        if (this.bump(), this.isEOF())
          break;
      }
    }, e.prototype.bumpSpace = function() {
      for (; !this.isEOF() && sr(this.char()); )
        this.bump();
    }, e.prototype.peek = function() {
      if (this.isEOF())
        return null;
      var t = this.char(), n = this.offset(), i = this.message.charCodeAt(n + (t >= 65536 ? 2 : 1));
      return i ?? null;
    }, e;
  }()
);
function on(e) {
  return e >= 97 && e <= 122 || e >= 65 && e <= 90;
}
function ia(e) {
  return on(e) || e === 47;
}
function ra(e) {
  return e === 45 || e === 46 || e >= 48 && e <= 57 || e === 95 || e >= 97 && e <= 122 || e >= 65 && e <= 90 || e == 183 || e >= 192 && e <= 214 || e >= 216 && e <= 246 || e >= 248 && e <= 893 || e >= 895 && e <= 8191 || e >= 8204 && e <= 8205 || e >= 8255 && e <= 8256 || e >= 8304 && e <= 8591 || e >= 11264 && e <= 12271 || e >= 12289 && e <= 55295 || e >= 63744 && e <= 64975 || e >= 65008 && e <= 65533 || e >= 65536 && e <= 983039;
}
function sr(e) {
  return e >= 9 && e <= 13 || e === 32 || e === 133 || e >= 8206 && e <= 8207 || e === 8232 || e === 8233;
}
function la(e) {
  return e >= 33 && e <= 35 || e === 36 || e >= 37 && e <= 39 || e === 40 || e === 41 || e === 42 || e === 43 || e === 44 || e === 45 || e >= 46 && e <= 47 || e >= 58 && e <= 59 || e >= 60 && e <= 62 || e >= 63 && e <= 64 || e === 91 || e === 92 || e === 93 || e === 94 || e === 96 || e === 123 || e === 124 || e === 125 || e === 126 || e === 161 || e >= 162 && e <= 165 || e === 166 || e === 167 || e === 169 || e === 171 || e === 172 || e === 174 || e === 176 || e === 177 || e === 182 || e === 187 || e === 191 || e === 215 || e === 247 || e >= 8208 && e <= 8213 || e >= 8214 && e <= 8215 || e === 8216 || e === 8217 || e === 8218 || e >= 8219 && e <= 8220 || e === 8221 || e === 8222 || e === 8223 || e >= 8224 && e <= 8231 || e >= 8240 && e <= 8248 || e === 8249 || e === 8250 || e >= 8251 && e <= 8254 || e >= 8257 && e <= 8259 || e === 8260 || e === 8261 || e === 8262 || e >= 8263 && e <= 8273 || e === 8274 || e === 8275 || e >= 8277 && e <= 8286 || e >= 8592 && e <= 8596 || e >= 8597 && e <= 8601 || e >= 8602 && e <= 8603 || e >= 8604 && e <= 8607 || e === 8608 || e >= 8609 && e <= 8610 || e === 8611 || e >= 8612 && e <= 8613 || e === 8614 || e >= 8615 && e <= 8621 || e === 8622 || e >= 8623 && e <= 8653 || e >= 8654 && e <= 8655 || e >= 8656 && e <= 8657 || e === 8658 || e === 8659 || e === 8660 || e >= 8661 && e <= 8691 || e >= 8692 && e <= 8959 || e >= 8960 && e <= 8967 || e === 8968 || e === 8969 || e === 8970 || e === 8971 || e >= 8972 && e <= 8991 || e >= 8992 && e <= 8993 || e >= 8994 && e <= 9e3 || e === 9001 || e === 9002 || e >= 9003 && e <= 9083 || e === 9084 || e >= 9085 && e <= 9114 || e >= 9115 && e <= 9139 || e >= 9140 && e <= 9179 || e >= 9180 && e <= 9185 || e >= 9186 && e <= 9254 || e >= 9255 && e <= 9279 || e >= 9280 && e <= 9290 || e >= 9291 && e <= 9311 || e >= 9472 && e <= 9654 || e === 9655 || e >= 9656 && e <= 9664 || e === 9665 || e >= 9666 && e <= 9719 || e >= 9720 && e <= 9727 || e >= 9728 && e <= 9838 || e === 9839 || e >= 9840 && e <= 10087 || e === 10088 || e === 10089 || e === 10090 || e === 10091 || e === 10092 || e === 10093 || e === 10094 || e === 10095 || e === 10096 || e === 10097 || e === 10098 || e === 10099 || e === 10100 || e === 10101 || e >= 10132 && e <= 10175 || e >= 10176 && e <= 10180 || e === 10181 || e === 10182 || e >= 10183 && e <= 10213 || e === 10214 || e === 10215 || e === 10216 || e === 10217 || e === 10218 || e === 10219 || e === 10220 || e === 10221 || e === 10222 || e === 10223 || e >= 10224 && e <= 10239 || e >= 10240 && e <= 10495 || e >= 10496 && e <= 10626 || e === 10627 || e === 10628 || e === 10629 || e === 10630 || e === 10631 || e === 10632 || e === 10633 || e === 10634 || e === 10635 || e === 10636 || e === 10637 || e === 10638 || e === 10639 || e === 10640 || e === 10641 || e === 10642 || e === 10643 || e === 10644 || e === 10645 || e === 10646 || e === 10647 || e === 10648 || e >= 10649 && e <= 10711 || e === 10712 || e === 10713 || e === 10714 || e === 10715 || e >= 10716 && e <= 10747 || e === 10748 || e === 10749 || e >= 10750 && e <= 11007 || e >= 11008 && e <= 11055 || e >= 11056 && e <= 11076 || e >= 11077 && e <= 11078 || e >= 11079 && e <= 11084 || e >= 11085 && e <= 11123 || e >= 11124 && e <= 11125 || e >= 11126 && e <= 11157 || e === 11158 || e >= 11159 && e <= 11263 || e >= 11776 && e <= 11777 || e === 11778 || e === 11779 || e === 11780 || e === 11781 || e >= 11782 && e <= 11784 || e === 11785 || e === 11786 || e === 11787 || e === 11788 || e === 11789 || e >= 11790 && e <= 11798 || e === 11799 || e >= 11800 && e <= 11801 || e === 11802 || e === 11803 || e === 11804 || e === 11805 || e >= 11806 && e <= 11807 || e === 11808 || e === 11809 || e === 11810 || e === 11811 || e === 11812 || e === 11813 || e === 11814 || e === 11815 || e === 11816 || e === 11817 || e >= 11818 && e <= 11822 || e === 11823 || e >= 11824 && e <= 11833 || e >= 11834 && e <= 11835 || e >= 11836 && e <= 11839 || e === 11840 || e === 11841 || e === 11842 || e >= 11843 && e <= 11855 || e >= 11856 && e <= 11857 || e === 11858 || e >= 11859 && e <= 11903 || e >= 12289 && e <= 12291 || e === 12296 || e === 12297 || e === 12298 || e === 12299 || e === 12300 || e === 12301 || e === 12302 || e === 12303 || e === 12304 || e === 12305 || e >= 12306 && e <= 12307 || e === 12308 || e === 12309 || e === 12310 || e === 12311 || e === 12312 || e === 12313 || e === 12314 || e === 12315 || e === 12316 || e === 12317 || e >= 12318 && e <= 12319 || e === 12320 || e === 12336 || e === 64830 || e === 64831 || e >= 65093 && e <= 65094;
}
function sn(e) {
  e.forEach(function(t) {
    if (delete t.location, Yi(t) || Ki(t))
      for (var n in t.options)
        delete t.options[n].location, sn(t.options[n].value);
    else
      Wi(t) && er(t.style) || (Qi(t) || Ji(t)) && tn(t.style) ? delete t.style.location : $i(t) && sn(t.children);
  });
}
function oa(e, t) {
  t === void 0 && (t = {}), t = L({ shouldParseSkeletons: !0, requiresOtherClause: !0 }, t);
  var n = new na(e, t).parse();
  if (n.err) {
    var i = SyntaxError(k[n.err.kind]);
    throw i.location = n.err.location, i.originalMessage = n.err.message, i;
  }
  return t != null && t.captureLocation || sn(n.val), n.val;
}
function Xt(e, t) {
  var n = t && t.cache ? t.cache : ha, i = t && t.serializer ? t.serializer : ca, r = t && t.strategy ? t.strategy : aa;
  return r(e, {
    cache: n,
    serializer: i
  });
}
function sa(e) {
  return e == null || typeof e == "number" || typeof e == "boolean";
}
function ar(e, t, n, i) {
  var r = sa(i) ? i : n(i), l = t.get(r);
  return typeof l > "u" && (l = e.call(this, i), t.set(r, l)), l;
}
function ur(e, t, n) {
  var i = Array.prototype.slice.call(arguments, 3), r = n(i), l = t.get(r);
  return typeof l > "u" && (l = e.apply(this, i), t.set(r, l)), l;
}
function gn(e, t, n, i, r) {
  return n.bind(t, e, i, r);
}
function aa(e, t) {
  var n = e.length === 1 ? ar : ur;
  return gn(e, this, n, t.cache.create(), t.serializer);
}
function ua(e, t) {
  return gn(e, this, ur, t.cache.create(), t.serializer);
}
function fa(e, t) {
  return gn(e, this, ar, t.cache.create(), t.serializer);
}
var ca = function() {
  return JSON.stringify(arguments);
};
function pn() {
  this.cache = /* @__PURE__ */ Object.create(null);
}
pn.prototype.get = function(e) {
  return this.cache[e];
};
pn.prototype.set = function(e, t) {
  this.cache[e] = t;
};
var ha = {
  create: function() {
    return new pn();
  }
}, Zt = {
  variadic: ua,
  monadic: fa
}, je;
(function(e) {
  e.MISSING_VALUE = "MISSING_VALUE", e.INVALID_VALUE = "INVALID_VALUE", e.MISSING_INTL_API = "MISSING_INTL_API";
})(je || (je = {}));
var At = (
  /** @class */
  function(e) {
    Tt(t, e);
    function t(n, i, r) {
      var l = e.call(this, n) || this;
      return l.code = i, l.originalMessage = r, l;
    }
    return t.prototype.toString = function() {
      return "[formatjs Error: ".concat(this.code, "] ").concat(this.message);
    }, t;
  }(Error)
), Zn = (
  /** @class */
  function(e) {
    Tt(t, e);
    function t(n, i, r, l) {
      return e.call(this, 'Invalid values for "'.concat(n, '": "').concat(i, '". Options are "').concat(Object.keys(r).join('", "'), '"'), je.INVALID_VALUE, l) || this;
    }
    return t;
  }(At)
), _a = (
  /** @class */
  function(e) {
    Tt(t, e);
    function t(n, i, r) {
      return e.call(this, 'Value for "'.concat(n, '" must be of type ').concat(i), je.INVALID_VALUE, r) || this;
    }
    return t;
  }(At)
), ma = (
  /** @class */
  function(e) {
    Tt(t, e);
    function t(n, i) {
      return e.call(this, 'The intl string context variable "'.concat(n, '" was not provided to the string "').concat(i, '"'), je.MISSING_VALUE, i) || this;
    }
    return t;
  }(At)
), W;
(function(e) {
  e[e.literal = 0] = "literal", e[e.object = 1] = "object";
})(W || (W = {}));
function da(e) {
  return e.length < 2 ? e : e.reduce(function(t, n) {
    var i = t[t.length - 1];
    return !i || i.type !== W.literal || n.type !== W.literal ? t.push(n) : i.value += n.value, t;
  }, []);
}
function ba(e) {
  return typeof e == "function";
}
function pt(e, t, n, i, r, l, o) {
  if (e.length === 1 && xn(e[0]))
    return [
      {
        type: W.literal,
        value: e[0].value
      }
    ];
  for (var a = [], s = 0, u = e; s < u.length; s++) {
    var f = u[s];
    if (xn(f)) {
      a.push({
        type: W.literal,
        value: f.value
      });
      continue;
    }
    if (Ls(f)) {
      typeof l == "number" && a.push({
        type: W.literal,
        value: n.getNumberFormat(t).format(l)
      });
      continue;
    }
    var c = f.value;
    if (!(r && c in r))
      throw new ma(c, o);
    var h = r[c];
    if (Is(f)) {
      (!h || typeof h == "string" || typeof h == "number") && (h = typeof h == "string" || typeof h == "number" ? String(h) : ""), a.push({
        type: typeof h == "string" ? W.literal : W.object,
        value: h
      });
      continue;
    }
    if (Qi(f)) {
      var _ = typeof f.style == "string" ? i.date[f.style] : tn(f.style) ? f.style.parsedOptions : void 0;
      a.push({
        type: W.literal,
        value: n.getDateTimeFormat(t, _).format(h)
      });
      continue;
    }
    if (Ji(f)) {
      var _ = typeof f.style == "string" ? i.time[f.style] : tn(f.style) ? f.style.parsedOptions : i.time.medium;
      a.push({
        type: W.literal,
        value: n.getDateTimeFormat(t, _).format(h)
      });
      continue;
    }
    if (Wi(f)) {
      var _ = typeof f.style == "string" ? i.number[f.style] : er(f.style) ? f.style.parsedOptions : void 0;
      _ && _.scale && (h = h * (_.scale || 1)), a.push({
        type: W.literal,
        value: n.getNumberFormat(t, _).format(h)
      });
      continue;
    }
    if ($i(f)) {
      var g = f.children, S = f.value, v = r[S];
      if (!ba(v))
        throw new _a(S, "function", o);
      var A = pt(g, t, n, i, r, l), y = v(A.map(function(b) {
        return b.value;
      }));
      Array.isArray(y) || (y = [y]), a.push.apply(a, y.map(function(b) {
        return {
          type: typeof b == "string" ? W.literal : W.object,
          value: b
        };
      }));
    }
    if (Yi(f)) {
      var d = f.options[h] || f.options.other;
      if (!d)
        throw new Zn(f.value, h, Object.keys(f.options), o);
      a.push.apply(a, pt(d.value, t, n, i, r));
      continue;
    }
    if (Ki(f)) {
      var d = f.options["=".concat(h)];
      if (!d) {
        if (!Intl.PluralRules)
          throw new At(`Intl.PluralRules is not available in this environment.
Try polyfilling it using "@formatjs/intl-pluralrules"
`, je.MISSING_INTL_API, o);
        var T = n.getPluralRules(t, { type: f.pluralType }).select(h - (f.offset || 0));
        d = f.options[T] || f.options.other;
      }
      if (!d)
        throw new Zn(f.value, h, Object.keys(f.options), o);
      a.push.apply(a, pt(d.value, t, n, i, r, h - (f.offset || 0)));
      continue;
    }
  }
  return da(a);
}
function ga(e, t) {
  return t ? L(L(L({}, e || {}), t || {}), Object.keys(e).reduce(function(n, i) {
    return n[i] = L(L({}, e[i]), t[i] || {}), n;
  }, {})) : e;
}
function pa(e, t) {
  return t ? Object.keys(e).reduce(function(n, i) {
    return n[i] = ga(e[i], t[i]), n;
  }, L({}, e)) : e;
}
function Wt(e) {
  return {
    create: function() {
      return {
        get: function(t) {
          return e[t];
        },
        set: function(t, n) {
          e[t] = n;
        }
      };
    }
  };
}
function va(e) {
  return e === void 0 && (e = {
    number: {},
    dateTime: {},
    pluralRules: {}
  }), {
    getNumberFormat: Xt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.NumberFormat).bind.apply(t, qt([void 0], n, !1)))();
    }, {
      cache: Wt(e.number),
      strategy: Zt.variadic
    }),
    getDateTimeFormat: Xt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.DateTimeFormat).bind.apply(t, qt([void 0], n, !1)))();
    }, {
      cache: Wt(e.dateTime),
      strategy: Zt.variadic
    }),
    getPluralRules: Xt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.PluralRules).bind.apply(t, qt([void 0], n, !1)))();
    }, {
      cache: Wt(e.pluralRules),
      strategy: Zt.variadic
    })
  };
}
var wa = (
  /** @class */
  function() {
    function e(t, n, i, r) {
      var l = this;
      if (n === void 0 && (n = e.defaultLocale), this.formatterCache = {
        number: {},
        dateTime: {},
        pluralRules: {}
      }, this.format = function(o) {
        var a = l.formatToParts(o);
        if (a.length === 1)
          return a[0].value;
        var s = a.reduce(function(u, f) {
          return !u.length || f.type !== W.literal || typeof u[u.length - 1] != "string" ? u.push(f.value) : u[u.length - 1] += f.value, u;
        }, []);
        return s.length <= 1 ? s[0] || "" : s;
      }, this.formatToParts = function(o) {
        return pt(l.ast, l.locales, l.formatters, l.formats, o, void 0, l.message);
      }, this.resolvedOptions = function() {
        return {
          locale: l.resolvedLocale.toString()
        };
      }, this.getAst = function() {
        return l.ast;
      }, this.locales = n, this.resolvedLocale = e.resolveLocale(n), typeof t == "string") {
        if (this.message = t, !e.__parse)
          throw new TypeError("IntlMessageFormat.__parse must be set to process `message` of type `string`");
        this.ast = e.__parse(t, {
          ignoreTag: r == null ? void 0 : r.ignoreTag,
          locale: this.resolvedLocale
        });
      } else
        this.ast = t;
      if (!Array.isArray(this.ast))
        throw new TypeError("A message must be provided as a String or AST.");
      this.formats = pa(e.formats, i), this.formatters = r && r.formatters || va(this.formatterCache);
    }
    return Object.defineProperty(e, "defaultLocale", {
      get: function() {
        return e.memoizedDefaultLocale || (e.memoizedDefaultLocale = new Intl.NumberFormat().resolvedOptions().locale), e.memoizedDefaultLocale;
      },
      enumerable: !1,
      configurable: !0
    }), e.memoizedDefaultLocale = null, e.resolveLocale = function(t) {
      var n = Intl.NumberFormat.supportedLocalesOf(t);
      return n.length > 0 ? new Intl.Locale(n[0]) : new Intl.Locale(typeof t == "string" ? t : t[0]);
    }, e.__parse = oa, e.formats = {
      number: {
        integer: {
          maximumFractionDigits: 0
        },
        currency: {
          style: "currency"
        },
        percent: {
          style: "percent"
        }
      },
      date: {
        short: {
          month: "numeric",
          day: "numeric",
          year: "2-digit"
        },
        medium: {
          month: "short",
          day: "numeric",
          year: "numeric"
        },
        long: {
          month: "long",
          day: "numeric",
          year: "numeric"
        },
        full: {
          weekday: "long",
          month: "long",
          day: "numeric",
          year: "numeric"
        }
      },
      time: {
        short: {
          hour: "numeric",
          minute: "numeric"
        },
        medium: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric"
        },
        long: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric",
          timeZoneName: "short"
        },
        full: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric",
          timeZoneName: "short"
        }
      }
    }, e;
  }()
);
function ya(e, t) {
  if (t == null)
    return;
  if (t in e)
    return e[t];
  const n = t.split(".");
  let i = e;
  for (let r = 0; r < n.length; r++)
    if (typeof i == "object") {
      if (r > 0) {
        const l = n.slice(r, n.length).join(".");
        if (l in i) {
          i = i[l];
          break;
        }
      }
      i = i[n[r]];
    } else
      i = void 0;
  return i;
}
const ye = {}, Ea = (e, t, n) => n && (t in ye || (ye[t] = {}), e in ye[t] || (ye[t][e] = n), n), fr = (e, t) => {
  if (t == null)
    return;
  if (t in ye && e in ye[t])
    return ye[t][e];
  const n = Ht(t);
  for (let i = 0; i < n.length; i++) {
    const r = n[i], l = Ta(r, e);
    if (l)
      return Ea(e, t, l);
  }
};
let vn;
const rt = it({});
function Sa(e) {
  return vn[e] || null;
}
function cr(e) {
  return e in vn;
}
function Ta(e, t) {
  if (!cr(e))
    return null;
  const n = Sa(e);
  return ya(n, t);
}
function Aa(e) {
  if (e == null)
    return;
  const t = Ht(e);
  for (let n = 0; n < t.length; n++) {
    const i = t[n];
    if (cr(i))
      return i;
  }
}
function Ha(e, ...t) {
  delete ye[e], rt.update((n) => (n[e] = Ps.all([n[e] || {}, ...t]), n));
}
Xe(
  [rt],
  ([e]) => Object.keys(e)
);
rt.subscribe((e) => vn = e);
const vt = {};
function Ba(e, t) {
  vt[e].delete(t), vt[e].size === 0 && delete vt[e];
}
function hr(e) {
  return vt[e];
}
function ka(e) {
  return Ht(e).map((t) => {
    const n = hr(t);
    return [t, n ? [...n] : []];
  }).filter(([, t]) => t.length > 0);
}
function an(e) {
  return e == null ? !1 : Ht(e).some(
    (t) => {
      var n;
      return (n = hr(t)) == null ? void 0 : n.size;
    }
  );
}
function Ca(e, t) {
  return Promise.all(
    t.map((i) => (Ba(e, i), i().then((r) => r.default || r)))
  ).then((i) => Ha(e, ...i));
}
const Ye = {};
function _r(e) {
  if (!an(e))
    return e in Ye ? Ye[e] : Promise.resolve();
  const t = ka(e);
  return Ye[e] = Promise.all(
    t.map(
      ([n, i]) => Ca(n, i)
    )
  ).then(() => {
    if (an(e))
      return _r(e);
    delete Ye[e];
  }), Ye[e];
}
const Pa = {
  number: {
    scientific: { notation: "scientific" },
    engineering: { notation: "engineering" },
    compactLong: { notation: "compact", compactDisplay: "long" },
    compactShort: { notation: "compact", compactDisplay: "short" }
  },
  date: {
    short: { month: "numeric", day: "numeric", year: "2-digit" },
    medium: { month: "short", day: "numeric", year: "numeric" },
    long: { month: "long", day: "numeric", year: "numeric" },
    full: { weekday: "long", month: "long", day: "numeric", year: "numeric" }
  },
  time: {
    short: { hour: "numeric", minute: "numeric" },
    medium: { hour: "numeric", minute: "numeric", second: "numeric" },
    long: {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZoneName: "short"
    },
    full: {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZoneName: "short"
    }
  }
}, Ia = {
  fallbackLocale: null,
  loadingDelay: 200,
  formats: Pa,
  warnOnMissingMessages: !0,
  handleMissingMessage: void 0,
  ignoreTag: !0
}, La = Ia;
function Ve() {
  return La;
}
const Qt = it(!1);
var Na = Object.defineProperty, Oa = Object.defineProperties, Ma = Object.getOwnPropertyDescriptors, Wn = Object.getOwnPropertySymbols, Ra = Object.prototype.hasOwnProperty, Da = Object.prototype.propertyIsEnumerable, Qn = (e, t, n) => t in e ? Na(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, Ua = (e, t) => {
  for (var n in t || (t = {}))
    Ra.call(t, n) && Qn(e, n, t[n]);
  if (Wn)
    for (var n of Wn(t))
      Da.call(t, n) && Qn(e, n, t[n]);
  return e;
}, Ga = (e, t) => Oa(e, Ma(t));
let un;
const wt = it(null);
function Jn(e) {
  return e.split("-").map((t, n, i) => i.slice(0, n + 1).join("-")).reverse();
}
function Ht(e, t = Ve().fallbackLocale) {
  const n = Jn(e);
  return t ? [.../* @__PURE__ */ new Set([...n, ...Jn(t)])] : n;
}
function Pe() {
  return un ?? void 0;
}
wt.subscribe((e) => {
  un = e ?? void 0, typeof window < "u" && e != null && document.documentElement.setAttribute("lang", e);
});
const xa = (e) => {
  if (e && Aa(e) && an(e)) {
    const { loadingDelay: t } = Ve();
    let n;
    return typeof window < "u" && Pe() != null && t ? n = window.setTimeout(
      () => Qt.set(!0),
      t
    ) : Qt.set(!0), _r(e).then(() => {
      wt.set(e);
    }).finally(() => {
      clearTimeout(n), Qt.set(!1);
    });
  }
  return wt.set(e);
}, lt = Ga(Ua({}, wt), {
  set: xa
}), Bt = (e) => {
  const t = /* @__PURE__ */ Object.create(null);
  return (i) => {
    const r = JSON.stringify(i);
    return r in t ? t[r] : t[r] = e(i);
  };
};
var Fa = Object.defineProperty, yt = Object.getOwnPropertySymbols, mr = Object.prototype.hasOwnProperty, dr = Object.prototype.propertyIsEnumerable, Yn = (e, t, n) => t in e ? Fa(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, wn = (e, t) => {
  for (var n in t || (t = {}))
    mr.call(t, n) && Yn(e, n, t[n]);
  if (yt)
    for (var n of yt(t))
      dr.call(t, n) && Yn(e, n, t[n]);
  return e;
}, Ze = (e, t) => {
  var n = {};
  for (var i in e)
    mr.call(e, i) && t.indexOf(i) < 0 && (n[i] = e[i]);
  if (e != null && yt)
    for (var i of yt(e))
      t.indexOf(i) < 0 && dr.call(e, i) && (n[i] = e[i]);
  return n;
};
const tt = (e, t) => {
  const { formats: n } = Ve();
  if (e in n && t in n[e])
    return n[e][t];
  throw new Error(`[svelte-i18n] Unknown "${t}" ${e} format.`);
}, ja = Bt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ze(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format numbers');
    return i && (r = tt("number", i)), new Intl.NumberFormat(n, r);
  }
), Va = Bt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ze(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format dates');
    return i ? r = tt("date", i) : Object.keys(r).length === 0 && (r = tt("date", "short")), new Intl.DateTimeFormat(n, r);
  }
), qa = Bt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = Ze(t, ["locale", "format"]);
    if (n == null)
      throw new Error(
        '[svelte-i18n] A "locale" must be set to format time values'
      );
    return i ? r = tt("time", i) : Object.keys(r).length === 0 && (r = tt("time", "short")), new Intl.DateTimeFormat(n, r);
  }
), za = (e = {}) => {
  var t = e, {
    locale: n = Pe()
  } = t, i = Ze(t, [
    "locale"
  ]);
  return ja(wn({ locale: n }, i));
}, Xa = (e = {}) => {
  var t = e, {
    locale: n = Pe()
  } = t, i = Ze(t, [
    "locale"
  ]);
  return Va(wn({ locale: n }, i));
}, Za = (e = {}) => {
  var t = e, {
    locale: n = Pe()
  } = t, i = Ze(t, [
    "locale"
  ]);
  return qa(wn({ locale: n }, i));
}, Wa = Bt(
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  (e, t = Pe()) => new wa(e, t, Ve().formats, {
    ignoreTag: Ve().ignoreTag
  })
), Qa = (e, t = {}) => {
  var n, i, r, l;
  let o = t;
  typeof e == "object" && (o = e, e = o.id);
  const {
    values: a,
    locale: s = Pe(),
    default: u
  } = o;
  if (s == null)
    throw new Error(
      "[svelte-i18n] Cannot format a message without first setting the initial locale."
    );
  let f = fr(e, s);
  if (!f)
    f = (l = (r = (i = (n = Ve()).handleMissingMessage) == null ? void 0 : i.call(n, { locale: s, id: e, defaultValue: u })) != null ? r : u) != null ? l : e;
  else if (typeof f != "string")
    return console.warn(
      `[svelte-i18n] Message with id "${e}" must be of type "string", found: "${typeof f}". Gettin its value through the "$format" method is deprecated; use the "json" method instead.`
    ), f;
  if (!a)
    return f;
  let c = f;
  try {
    c = Wa(f, s).format(a);
  } catch (h) {
    h instanceof Error && console.warn(
      `[svelte-i18n] Message "${e}" has syntax error:`,
      h.message
    );
  }
  return c;
}, Ja = (e, t) => Za(t).format(e), Ya = (e, t) => Xa(t).format(e), Ka = (e, t) => za(t).format(e), $a = (e, t = Pe()) => fr(e, t);
Xe([lt, rt], () => Qa);
Xe([lt], () => Ja);
Xe([lt], () => Ya);
Xe([lt], () => Ka);
Xe([lt, rt], () => $a);
const {
  SvelteComponent: eu,
  append: Kn,
  attr: tu,
  check_outros: $n,
  create_component: yn,
  destroy_component: En,
  detach: nu,
  element: iu,
  group_outros: ei,
  init: ru,
  insert: lu,
  mount_component: Sn,
  safe_not_equal: ou,
  set_style: ti,
  space: ni,
  toggle_class: ii,
  transition_in: _e,
  transition_out: Ae
} = window.__gradio__svelte__internal, { createEventDispatcher: su } = window.__gradio__svelte__internal;
function ri(e) {
  let t, n;
  return t = new nt({
    props: {
      Icon: Eo,
      label: (
        /*i18n*/
        e[3]("common.edit")
      )
    }
  }), t.$on(
    "click",
    /*click_handler*/
    e[5]
  ), {
    c() {
      yn(t.$$.fragment);
    },
    m(i, r) {
      Sn(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r & /*i18n*/
      8 && (l.label = /*i18n*/
      i[3]("common.edit")), t.$set(l);
    },
    i(i) {
      n || (_e(t.$$.fragment, i), n = !0);
    },
    o(i) {
      Ae(t.$$.fragment, i), n = !1;
    },
    d(i) {
      En(t, i);
    }
  };
}
function li(e) {
  let t, n;
  return t = new nt({
    props: {
      Icon: Vo,
      label: (
        /*i18n*/
        e[3]("common.undo")
      )
    }
  }), t.$on(
    "click",
    /*click_handler_1*/
    e[6]
  ), {
    c() {
      yn(t.$$.fragment);
    },
    m(i, r) {
      Sn(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r & /*i18n*/
      8 && (l.label = /*i18n*/
      i[3]("common.undo")), t.$set(l);
    },
    i(i) {
      n || (_e(t.$$.fragment, i), n = !0);
    },
    o(i) {
      Ae(t.$$.fragment, i), n = !1;
    },
    d(i) {
      En(t, i);
    }
  };
}
function au(e) {
  let t, n, i, r, l, o = (
    /*editable*/
    e[0] && ri(e)
  ), a = (
    /*undoable*/
    e[1] && li(e)
  );
  return r = new nt({
    props: {
      Icon: Yl,
      label: (
        /*i18n*/
        e[3]("common.clear")
      )
    }
  }), r.$on(
    "click",
    /*click_handler_2*/
    e[7]
  ), {
    c() {
      t = iu("div"), o && o.c(), n = ni(), a && a.c(), i = ni(), yn(r.$$.fragment), tu(t, "class", "svelte-1wj0ocy"), ii(t, "not-absolute", !/*absolute*/
      e[2]), ti(
        t,
        "position",
        /*absolute*/
        e[2] ? "absolute" : "static"
      );
    },
    m(s, u) {
      lu(s, t, u), o && o.m(t, null), Kn(t, n), a && a.m(t, null), Kn(t, i), Sn(r, t, null), l = !0;
    },
    p(s, [u]) {
      /*editable*/
      s[0] ? o ? (o.p(s, u), u & /*editable*/
      1 && _e(o, 1)) : (o = ri(s), o.c(), _e(o, 1), o.m(t, n)) : o && (ei(), Ae(o, 1, 1, () => {
        o = null;
      }), $n()), /*undoable*/
      s[1] ? a ? (a.p(s, u), u & /*undoable*/
      2 && _e(a, 1)) : (a = li(s), a.c(), _e(a, 1), a.m(t, i)) : a && (ei(), Ae(a, 1, 1, () => {
        a = null;
      }), $n());
      const f = {};
      u & /*i18n*/
      8 && (f.label = /*i18n*/
      s[3]("common.clear")), r.$set(f), (!l || u & /*absolute*/
      4) && ii(t, "not-absolute", !/*absolute*/
      s[2]), u & /*absolute*/
      4 && ti(
        t,
        "position",
        /*absolute*/
        s[2] ? "absolute" : "static"
      );
    },
    i(s) {
      l || (_e(o), _e(a), _e(r.$$.fragment, s), l = !0);
    },
    o(s) {
      Ae(o), Ae(a), Ae(r.$$.fragment, s), l = !1;
    },
    d(s) {
      s && nu(t), o && o.d(), a && a.d(), En(r);
    }
  };
}
function uu(e, t, n) {
  let { editable: i = !1 } = t, { undoable: r = !1 } = t, { absolute: l = !0 } = t, { i18n: o } = t;
  const a = su(), s = () => a("edit"), u = () => a("undo"), f = (c) => {
    a("clear"), c.stopPropagation();
  };
  return e.$$set = (c) => {
    "editable" in c && n(0, i = c.editable), "undoable" in c && n(1, r = c.undoable), "absolute" in c && n(2, l = c.absolute), "i18n" in c && n(3, o = c.i18n);
  }, [
    i,
    r,
    l,
    o,
    a,
    s,
    u,
    f
  ];
}
class fu extends eu {
  constructor(t) {
    super(), ru(this, t, uu, au, ou, {
      editable: 0,
      undoable: 1,
      absolute: 2,
      i18n: 3
    });
  }
}
var oi = Object.prototype.hasOwnProperty;
function si(e, t, n) {
  for (n of e.keys())
    if ($e(n, t))
      return n;
}
function $e(e, t) {
  var n, i, r;
  if (e === t)
    return !0;
  if (e && t && (n = e.constructor) === t.constructor) {
    if (n === Date)
      return e.getTime() === t.getTime();
    if (n === RegExp)
      return e.toString() === t.toString();
    if (n === Array) {
      if ((i = e.length) === t.length)
        for (; i-- && $e(e[i], t[i]); )
          ;
      return i === -1;
    }
    if (n === Set) {
      if (e.size !== t.size)
        return !1;
      for (i of e)
        if (r = i, r && typeof r == "object" && (r = si(t, r), !r) || !t.has(r))
          return !1;
      return !0;
    }
    if (n === Map) {
      if (e.size !== t.size)
        return !1;
      for (i of e)
        if (r = i[0], r && typeof r == "object" && (r = si(t, r), !r) || !$e(i[1], t.get(r)))
          return !1;
      return !0;
    }
    if (n === ArrayBuffer)
      e = new Uint8Array(e), t = new Uint8Array(t);
    else if (n === DataView) {
      if ((i = e.byteLength) === t.byteLength)
        for (; i-- && e.getInt8(i) === t.getInt8(i); )
          ;
      return i === -1;
    }
    if (ArrayBuffer.isView(e)) {
      if ((i = e.byteLength) === t.byteLength)
        for (; i-- && e[i] === t[i]; )
          ;
      return i === -1;
    }
    if (!n || typeof e == "object") {
      i = 0;
      for (n in e)
        if (oi.call(e, n) && ++i && !oi.call(t, n) || !(n in t) || !$e(e[n], t[n]))
          return !1;
      return Object.keys(t).length === i;
    }
  }
  return e !== e && t !== t;
}
async function cu(e) {
  return e ? `<div style="display: flex; flex-wrap: wrap; gap: 16px">${(await Promise.all(
    e.map(async ([n, i]) => n === null || !n.url ? "" : await Xo(n.url, "url"))
  )).map((n) => `<img src="${n}" style="height: 400px" />`).join("")}</div>` : "";
}
const {
  SvelteComponent: hu,
  add_iframe_resize_listener: _u,
  add_render_callback: br,
  append: j,
  attr: w,
  binding_callbacks: ai,
  bubble: we,
  check_outros: ke,
  create_component: Ie,
  destroy_component: Le,
  destroy_each: gr,
  detach: X,
  element: F,
  empty: mu,
  ensure_array_like: Et,
  globals: du,
  group_outros: Ce,
  init: bu,
  insert: Z,
  listen: le,
  mount_component: Ne,
  run_all: pr,
  safe_not_equal: gu,
  set_data: vr,
  set_style: ae,
  space: re,
  src_url_equal: he,
  text: wr,
  toggle_class: ue,
  transition_in: N,
  transition_out: G
} = window.__gradio__svelte__internal, { window: yr } = du, { createEventDispatcher: pu, onMount: vu } = window.__gradio__svelte__internal, { tick: wu } = window.__gradio__svelte__internal;
function ui(e, t, n) {
  const i = e.slice();
  return i[47] = t[n], i[49] = n, i;
}
function fi(e, t, n) {
  const i = e.slice();
  return i[50] = t[n], i[51] = t, i[49] = n, i;
}
function ci(e) {
  let t, n;
  return t = new hl({
    props: {
      show_label: (
        /*show_label*/
        e[1]
      ),
      Icon: ji,
      label: (
        /*label*/
        e[2] || "Gallery"
      )
    }
  }), {
    c() {
      Ie(t.$$.fragment);
    },
    m(i, r) {
      Ne(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[0] & /*show_label*/
      2 && (l.show_label = /*show_label*/
      i[1]), r[0] & /*label*/
      4 && (l.label = /*label*/
      i[2] || "Gallery"), t.$set(l);
    },
    i(i) {
      n || (N(t.$$.fragment, i), n = !0);
    },
    o(i) {
      G(t.$$.fragment, i), n = !1;
    },
    d(i) {
      Le(t, i);
    }
  };
}
function yu(e) {
  let t, n, i, r, l, o, a = (
    /*selected_index*/
    e[0] !== null && /*allow_preview*/
    e[7] && hi(e)
  ), s = (
    /*show_share_button*/
    e[9] && gi(e)
  ), u = Et(
    /*_value*/
    e[12]
  ), f = [];
  for (let c = 0; c < u.length; c += 1)
    f[c] = vi(ui(e, u, c));
  return {
    c() {
      a && a.c(), t = re(), n = F("div"), i = F("div"), s && s.c(), r = re();
      for (let c = 0; c < f.length; c += 1)
        f[c].c();
      w(i, "class", "grid-container svelte-16l5kkn"), ae(
        i,
        "--grid-cols",
        /*columns*/
        e[4]
      ), ae(
        i,
        "--grid-rows",
        /*rows*/
        e[5]
      ), ae(
        i,
        "--object-fit",
        /*object_fit*/
        e[8]
      ), ae(
        i,
        "height",
        /*height*/
        e[6]
      ), ue(
        i,
        "pt-6",
        /*show_label*/
        e[1]
      ), w(n, "class", "grid-wrap svelte-16l5kkn"), br(() => (
        /*div1_elementresize_handler*/
        e[41].call(n)
      )), ue(n, "fixed-height", !/*height*/
      e[6] || /*height*/
      e[6] == "auto");
    },
    m(c, h) {
      a && a.m(c, h), Z(c, t, h), Z(c, n, h), j(n, i), s && s.m(i, null), j(i, r);
      for (let _ = 0; _ < f.length; _ += 1)
        f[_] && f[_].m(i, null);
      l = _u(
        n,
        /*div1_elementresize_handler*/
        e[41].bind(n)
      ), o = !0;
    },
    p(c, h) {
      if (/*selected_index*/
      c[0] !== null && /*allow_preview*/
      c[7] ? a ? (a.p(c, h), h[0] & /*selected_index, allow_preview*/
      129 && N(a, 1)) : (a = hi(c), a.c(), N(a, 1), a.m(t.parentNode, t)) : a && (Ce(), G(a, 1, 1, () => {
        a = null;
      }), ke()), /*show_share_button*/
      c[9] ? s ? (s.p(c, h), h[0] & /*show_share_button*/
      512 && N(s, 1)) : (s = gi(c), s.c(), N(s, 1), s.m(i, r)) : s && (Ce(), G(s, 1, 1, () => {
        s = null;
      }), ke()), h[0] & /*_value, selected_index*/
      4097) {
        u = Et(
          /*_value*/
          c[12]
        );
        let _;
        for (_ = 0; _ < u.length; _ += 1) {
          const g = ui(c, u, _);
          f[_] ? f[_].p(g, h) : (f[_] = vi(g), f[_].c(), f[_].m(i, null));
        }
        for (; _ < f.length; _ += 1)
          f[_].d(1);
        f.length = u.length;
      }
      (!o || h[0] & /*columns*/
      16) && ae(
        i,
        "--grid-cols",
        /*columns*/
        c[4]
      ), (!o || h[0] & /*rows*/
      32) && ae(
        i,
        "--grid-rows",
        /*rows*/
        c[5]
      ), (!o || h[0] & /*object_fit*/
      256) && ae(
        i,
        "--object-fit",
        /*object_fit*/
        c[8]
      ), (!o || h[0] & /*height*/
      64) && ae(
        i,
        "height",
        /*height*/
        c[6]
      ), (!o || h[0] & /*show_label*/
      2) && ue(
        i,
        "pt-6",
        /*show_label*/
        c[1]
      ), (!o || h[0] & /*height*/
      64) && ue(n, "fixed-height", !/*height*/
      c[6] || /*height*/
      c[6] == "auto");
    },
    i(c) {
      o || (N(a), N(s), o = !0);
    },
    o(c) {
      G(a), G(s), o = !1;
    },
    d(c) {
      c && (X(t), X(n)), a && a.d(c), s && s.d(), gr(f, c), l();
    }
  };
}
function Eu(e) {
  let t, n;
  return t = new ql({
    props: {
      unpadded_box: !0,
      size: "large",
      $$slots: { default: [Bu] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      Ie(t.$$.fragment);
    },
    m(i, r) {
      Ne(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[1] & /*$$scope*/
      2097152 && (l.$$scope = { dirty: r, ctx: i }), t.$set(l);
    },
    i(i) {
      n || (N(t.$$.fragment, i), n = !0);
    },
    o(i) {
      G(t.$$.fragment, i), n = !1;
    },
    d(i) {
      Le(t, i);
    }
  };
}
function hi(e) {
  var T;
  let t, n, i, r, l, o, a, s, u, f, c, h = (
    /*show_download_button*/
    e[10] && _i(e)
  );
  r = new fu({
    props: { i18n: (
      /*i18n*/
      e[11]
    ), absolute: !1 }
  }), r.$on(
    "clear",
    /*clear_handler*/
    e[33]
  );
  function _(b, I) {
    return (
      /*_value*/
      b[12][
        /*selected_index*/
        b[0]
      ].image.mime_type === "video/mp4" ? Tu : Su
    );
  }
  let g = _(e), S = g(e), v = (
    /*_value*/
    ((T = e[12][
      /*selected_index*/
      e[0]
    ]) == null ? void 0 : T.caption) && mi(e)
  ), A = Et(
    /*_value*/
    e[12]
  ), y = [];
  for (let b = 0; b < A.length; b += 1)
    y[b] = bi(fi(e, A, b));
  const d = (b) => G(y[b], 1, 1, () => {
    y[b] = null;
  });
  return {
    c() {
      t = F("button"), n = F("div"), h && h.c(), i = re(), Ie(r.$$.fragment), l = re(), S.c(), o = re(), v && v.c(), a = re(), s = F("div");
      for (let b = 0; b < y.length; b += 1)
        y[b].c();
      w(n, "class", "icon-buttons svelte-16l5kkn"), w(s, "class", "thumbnails scroll-hide svelte-16l5kkn"), w(s, "data-testid", "container_el"), w(t, "class", "preview svelte-16l5kkn");
    },
    m(b, I) {
      Z(b, t, I), j(t, n), h && h.m(n, null), j(n, i), Ne(r, n, null), j(t, l), S.m(t, null), j(t, o), v && v.m(t, null), j(t, a), j(t, s);
      for (let M = 0; M < y.length; M += 1)
        y[M] && y[M].m(s, null);
      e[37](s), u = !0, f || (c = le(
        t,
        "keydown",
        /*on_keydown*/
        e[19]
      ), f = !0);
    },
    p(b, I) {
      var U;
      /*show_download_button*/
      b[10] ? h ? (h.p(b, I), I[0] & /*show_download_button*/
      1024 && N(h, 1)) : (h = _i(b), h.c(), N(h, 1), h.m(n, i)) : h && (Ce(), G(h, 1, 1, () => {
        h = null;
      }), ke());
      const M = {};
      if (I[0] & /*i18n*/
      2048 && (M.i18n = /*i18n*/
      b[11]), r.$set(M), g === (g = _(b)) && S ? S.p(b, I) : (S.d(1), S = g(b), S && (S.c(), S.m(t, o))), /*_value*/
      (U = b[12][
        /*selected_index*/
        b[0]
      ]) != null && U.caption ? v ? v.p(b, I) : (v = mi(b), v.c(), v.m(t, a)) : v && (v.d(1), v = null), I[0] & /*_value, el, selected_index, thumbnailUrl*/
      28673) {
        A = Et(
          /*_value*/
          b[12]
        );
        let O;
        for (O = 0; O < A.length; O += 1) {
          const V = fi(b, A, O);
          y[O] ? (y[O].p(V, I), N(y[O], 1)) : (y[O] = bi(V), y[O].c(), N(y[O], 1), y[O].m(s, null));
        }
        for (Ce(), O = A.length; O < y.length; O += 1)
          d(O);
        ke();
      }
    },
    i(b) {
      if (!u) {
        N(h), N(r.$$.fragment, b);
        for (let I = 0; I < A.length; I += 1)
          N(y[I]);
        u = !0;
      }
    },
    o(b) {
      G(h), G(r.$$.fragment, b), y = y.filter(Boolean);
      for (let I = 0; I < y.length; I += 1)
        G(y[I]);
      u = !1;
    },
    d(b) {
      b && X(t), h && h.d(), Le(r), S.d(), v && v.d(), gr(y, b), e[37](null), f = !1, c();
    }
  };
}
function _i(e) {
  let t, n, i, r;
  return n = new nt({
    props: {
      Icon: _o,
      label: (
        /*i18n*/
        e[11]("common.download")
      )
    }
  }), {
    c() {
      t = F("a"), Ie(n.$$.fragment), w(t, "href", i = fn(
        /*value*/
        e[3][
          /*selected_index*/
          e[0]
        ]
      )), w(t, "target", window.__is_colab__ ? "_blank" : null), w(t, "download", "image"), w(t, "class", "svelte-16l5kkn");
    },
    m(l, o) {
      Z(l, t, o), Ne(n, t, null), r = !0;
    },
    p(l, o) {
      const a = {};
      o[0] & /*i18n*/
      2048 && (a.label = /*i18n*/
      l[11]("common.download")), n.$set(a), (!r || o[0] & /*value, selected_index*/
      9 && i !== (i = fn(
        /*value*/
        l[3][
          /*selected_index*/
          l[0]
        ]
      ))) && w(t, "href", i);
    },
    i(l) {
      r || (N(n.$$.fragment, l), r = !0);
    },
    o(l) {
      G(n.$$.fragment, l), r = !1;
    },
    d(l) {
      l && X(t), Le(n);
    }
  };
}
function Su(e) {
  let t, n, i, r, l, o, a;
  return {
    c() {
      t = F("button"), n = F("img"), w(n, "data-testid", "detailed-image"), he(n.src, i = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].image.url) || w(n, "src", i), w(n, "alt", r = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].caption || ""), w(n, "title", l = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].caption || null), w(n, "loading", "lazy"), w(n, "class", "svelte-16l5kkn"), ue(n, "with-caption", !!/*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].caption), w(t, "class", "image-button svelte-16l5kkn"), ae(t, "height", "calc(100% - " + /*_value*/
      (e[12][
        /*selected_index*/
        e[0]
      ].caption ? "80px" : "60px") + ")"), w(t, "aria-label", "detailed view of selected image");
    },
    m(s, u) {
      Z(s, t, u), j(t, n), o || (a = le(
        t,
        "click",
        /*click_handler*/
        e[34]
      ), o = !0);
    },
    p(s, u) {
      u[0] & /*_value, selected_index*/
      4097 && !he(n.src, i = /*_value*/
      s[12][
        /*selected_index*/
        s[0]
      ].image.url) && w(n, "src", i), u[0] & /*_value, selected_index*/
      4097 && r !== (r = /*_value*/
      s[12][
        /*selected_index*/
        s[0]
      ].caption || "") && w(n, "alt", r), u[0] & /*_value, selected_index*/
      4097 && l !== (l = /*_value*/
      s[12][
        /*selected_index*/
        s[0]
      ].caption || null) && w(n, "title", l), u[0] & /*_value, selected_index*/
      4097 && ue(n, "with-caption", !!/*_value*/
      s[12][
        /*selected_index*/
        s[0]
      ].caption), u[0] & /*_value, selected_index*/
      4097 && ae(t, "height", "calc(100% - " + /*_value*/
      (s[12][
        /*selected_index*/
        s[0]
      ].caption ? "80px" : "60px") + ")");
    },
    d(s) {
      s && X(t), o = !1, a();
    }
  };
}
function Tu(e) {
  let t, n, i, r, l, o;
  return {
    c() {
      t = F("video"), n = F("track"), w(n, "kind", "captions"), w(t, "class", "detailed-video svelte-16l5kkn"), w(t, "data-testid", "detailed-video"), t.controls = !0, he(t.src, i = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].image.path) || w(t, "src", i), w(t, "title", r = /*_value*/
      e[12][
        /*selected_index*/
        e[0]
      ].image.alt_text), w(t, "preload", "auto");
    },
    m(a, s) {
      Z(a, t, s), j(t, n), l || (o = [
        le(
          t,
          "play",
          /*play_handler*/
          e[29]
        ),
        le(
          t,
          "pause",
          /*pause_handler*/
          e[30]
        ),
        le(
          t,
          "ended",
          /*ended_handler*/
          e[31]
        )
      ], l = !0);
    },
    p(a, s) {
      s[0] & /*_value, selected_index*/
      4097 && !he(t.src, i = /*_value*/
      a[12][
        /*selected_index*/
        a[0]
      ].image.path) && w(t, "src", i), s[0] & /*_value, selected_index*/
      4097 && r !== (r = /*_value*/
      a[12][
        /*selected_index*/
        a[0]
      ].image.alt_text) && w(t, "title", r);
    },
    d(a) {
      a && X(t), l = !1, pr(o);
    }
  };
}
function mi(e) {
  let t, n = (
    /*_value*/
    e[12][
      /*selected_index*/
      e[0]
    ].caption + ""
  ), i;
  return {
    c() {
      t = F("caption"), i = wr(n), w(t, "class", "caption svelte-16l5kkn");
    },
    m(r, l) {
      Z(r, t, l), j(t, i);
    },
    p(r, l) {
      l[0] & /*_value, selected_index*/
      4097 && n !== (n = /*_value*/
      r[12][
        /*selected_index*/
        r[0]
      ].caption + "") && vr(i, n);
    },
    d(r) {
      r && X(t);
    }
  };
}
function di(e) {
  let t, n, i;
  return n = new Ro({}), {
    c() {
      t = F("div"), Ie(n.$$.fragment), w(t, "class", "thumbnail-play svelte-16l5kkn");
    },
    m(r, l) {
      Z(r, t, l), Ne(n, t, null), i = !0;
    },
    i(r) {
      i || (N(n.$$.fragment, r), i = !0);
    },
    o(r) {
      G(n.$$.fragment, r), i = !1;
    },
    d(r) {
      r && X(t), Le(n);
    }
  };
}
function bi(e) {
  let t, n, i, r, l, o, a, s = (
    /*i*/
    e[49]
  ), u, f, c, h = (
    /*media*/
    e[50].image.mime_type === "video/mp4" && di()
  );
  const _ = () => (
    /*button_binding*/
    e[35](t, s)
  ), g = () => (
    /*button_binding*/
    e[35](null, s)
  );
  function S() {
    return (
      /*click_handler_1*/
      e[36](
        /*i*/
        e[49]
      )
    );
  }
  return {
    c() {
      t = F("button"), n = F("img"), l = re(), h && h.c(), o = re(), he(n.src, i = /*thumbnailUrl*/
      e[13]) || w(n, "src", i), w(n, "title", r = /*media*/
      e[50].caption || null), w(n, "data-testid", "thumbnail " + /*i*/
      (e[49] + 1)), w(n, "alt", ""), w(n, "loading", "lazy"), w(n, "class", "svelte-16l5kkn"), w(t, "class", "thumbnail-item thumbnail-small svelte-16l5kkn"), w(t, "aria-label", a = "Thumbnail " + /*i*/
      (e[49] + 1) + " of " + /*_value*/
      e[12].length), ue(
        t,
        "selected",
        /*selected_index*/
        e[0] === /*i*/
        e[49]
      );
    },
    m(v, A) {
      Z(v, t, A), j(t, n), j(t, l), h && h.m(t, null), j(t, o), _(), u = !0, f || (c = le(t, "click", S), f = !0);
    },
    p(v, A) {
      e = v, (!u || A[0] & /*thumbnailUrl*/
      8192 && !he(n.src, i = /*thumbnailUrl*/
      e[13])) && w(n, "src", i), (!u || A[0] & /*_value*/
      4096 && r !== (r = /*media*/
      e[50].caption || null)) && w(n, "title", r), /*media*/
      e[50].image.mime_type === "video/mp4" ? h ? A[0] & /*_value*/
      4096 && N(h, 1) : (h = di(), h.c(), N(h, 1), h.m(t, o)) : h && (Ce(), G(h, 1, 1, () => {
        h = null;
      }), ke()), (!u || A[0] & /*_value*/
      4096 && a !== (a = "Thumbnail " + /*i*/
      (e[49] + 1) + " of " + /*_value*/
      e[12].length)) && w(t, "aria-label", a), s !== /*i*/
      e[49] && (g(), s = /*i*/
      e[49], _()), (!u || A[0] & /*selected_index*/
      1) && ue(
        t,
        "selected",
        /*selected_index*/
        e[0] === /*i*/
        e[49]
      );
    },
    i(v) {
      u || (N(h), u = !0);
    },
    o(v) {
      G(h), u = !1;
    },
    d(v) {
      v && X(t), h && h.d(), g(), f = !1, c();
    }
  };
}
function gi(e) {
  let t, n, i;
  return n = new ls({
    props: {
      i18n: (
        /*i18n*/
        e[11]
      ),
      value: (
        /*_value*/
        e[12]
      ),
      formatter: cu
    }
  }), n.$on(
    "share",
    /*share_handler*/
    e[38]
  ), n.$on(
    "error",
    /*error_handler*/
    e[39]
  ), {
    c() {
      t = F("div"), Ie(n.$$.fragment), w(t, "class", "icon-button svelte-16l5kkn");
    },
    m(r, l) {
      Z(r, t, l), Ne(n, t, null), i = !0;
    },
    p(r, l) {
      const o = {};
      l[0] & /*i18n*/
      2048 && (o.i18n = /*i18n*/
      r[11]), l[0] & /*_value*/
      4096 && (o.value = /*_value*/
      r[12]), n.$set(o);
    },
    i(r) {
      i || (N(n.$$.fragment, r), i = !0);
    },
    o(r) {
      G(n.$$.fragment, r), i = !1;
    },
    d(r) {
      r && X(t), Le(n);
    }
  };
}
function Au(e) {
  let t, n, i;
  return {
    c() {
      t = F("img"), w(t, "alt", n = /*entry*/
      e[47].caption || ""), he(t.src, i = typeof /*entry*/
      e[47].image == "string" ? (
        /*entry*/
        e[47].image
      ) : (
        /*entry*/
        e[47].image.url
      )) || w(t, "src", i), w(t, "loading", "lazy"), w(t, "class", "svelte-16l5kkn");
    },
    m(r, l) {
      Z(r, t, l);
    },
    p(r, l) {
      l[0] & /*_value*/
      4096 && n !== (n = /*entry*/
      r[47].caption || "") && w(t, "alt", n), l[0] & /*_value*/
      4096 && !he(t.src, i = typeof /*entry*/
      r[47].image == "string" ? (
        /*entry*/
        r[47].image
      ) : (
        /*entry*/
        r[47].image.url
      )) && w(t, "src", i);
    },
    d(r) {
      r && X(t);
    }
  };
}
function Hu(e) {
  let t, n, i, r, l, o;
  return {
    c() {
      t = F("video"), n = F("track"), w(n, "kind", "captions"), w(t, "class", "detailed-video svelte-16l5kkn"), w(t, "data-testid", "detailed-video"), t.controls = !0, he(t.src, i = /*entry*/
      e[47].image.path) || w(t, "src", i), w(t, "title", r = /*entry*/
      e[47].image.alt_text), w(t, "preload", "auto");
    },
    m(a, s) {
      Z(a, t, s), j(t, n), l || (o = [
        le(
          t,
          "play",
          /*play_handler_1*/
          e[26]
        ),
        le(
          t,
          "pause",
          /*pause_handler_1*/
          e[27]
        ),
        le(
          t,
          "ended",
          /*ended_handler_1*/
          e[28]
        )
      ], l = !0);
    },
    p(a, s) {
      s[0] & /*_value*/
      4096 && !he(t.src, i = /*entry*/
      a[47].image.path) && w(t, "src", i), s[0] & /*_value*/
      4096 && r !== (r = /*entry*/
      a[47].image.alt_text) && w(t, "title", r);
    },
    d(a) {
      a && X(t), l = !1, pr(o);
    }
  };
}
function pi(e) {
  let t, n = (
    /*entry*/
    e[47].caption + ""
  ), i;
  return {
    c() {
      t = F("div"), i = wr(n), w(t, "class", "caption-label svelte-16l5kkn");
    },
    m(r, l) {
      Z(r, t, l), j(t, i);
    },
    p(r, l) {
      l[0] & /*_value*/
      4096 && n !== (n = /*entry*/
      r[47].caption + "") && vr(i, n);
    },
    d(r) {
      r && X(t);
    }
  };
}
function vi(e) {
  let t, n, i, r, l, o;
  function a(h, _) {
    return (
      /*entry*/
      h[47].image.mime_type === "video/mp4" ? Hu : Au
    );
  }
  let s = a(e), u = s(e), f = (
    /*entry*/
    e[47].caption && pi(e)
  );
  function c() {
    return (
      /*click_handler_2*/
      e[40](
        /*i*/
        e[49]
      )
    );
  }
  return {
    c() {
      t = F("button"), u.c(), n = re(), f && f.c(), i = re(), w(t, "class", "thumbnail-item thumbnail-lg svelte-16l5kkn"), w(t, "aria-label", r = "Thumbnail " + /*i*/
      (e[49] + 1) + " of " + /*_value*/
      e[12].length), ue(
        t,
        "selected",
        /*selected_index*/
        e[0] === /*i*/
        e[49]
      );
    },
    m(h, _) {
      Z(h, t, _), u.m(t, null), j(t, n), f && f.m(t, null), j(t, i), l || (o = le(t, "click", c), l = !0);
    },
    p(h, _) {
      e = h, s === (s = a(e)) && u ? u.p(e, _) : (u.d(1), u = s(e), u && (u.c(), u.m(t, n))), /*entry*/
      e[47].caption ? f ? f.p(e, _) : (f = pi(e), f.c(), f.m(t, i)) : f && (f.d(1), f = null), _[0] & /*_value*/
      4096 && r !== (r = "Thumbnail " + /*i*/
      (e[49] + 1) + " of " + /*_value*/
      e[12].length) && w(t, "aria-label", r), _[0] & /*selected_index*/
      1 && ue(
        t,
        "selected",
        /*selected_index*/
        e[0] === /*i*/
        e[49]
      );
    },
    d(h) {
      h && X(t), u.d(), f && f.d(), l = !1, o();
    }
  };
}
function Bu(e) {
  let t, n;
  return t = new ji({}), {
    c() {
      Ie(t.$$.fragment);
    },
    m(i, r) {
      Ne(t, i, r), n = !0;
    },
    i(i) {
      n || (N(t.$$.fragment, i), n = !0);
    },
    o(i) {
      G(t.$$.fragment, i), n = !1;
    },
    d(i) {
      Le(t, i);
    }
  };
}
function ku(e) {
  let t, n, i, r, l, o, a;
  br(
    /*onwindowresize*/
    e[32]
  );
  let s = (
    /*show_label*/
    e[1] && ci(e)
  );
  const u = [Eu, yu], f = [];
  function c(h, _) {
    return (
      /*value*/
      h[3] === null || /*_value*/
      h[12] === null || /*_value*/
      h[12].length === 0 ? 0 : 1
    );
  }
  return n = c(e), i = f[n] = u[n](e), {
    c() {
      s && s.c(), t = re(), i.c(), r = mu();
    },
    m(h, _) {
      s && s.m(h, _), Z(h, t, _), f[n].m(h, _), Z(h, r, _), l = !0, o || (a = le(
        yr,
        "resize",
        /*onwindowresize*/
        e[32]
      ), o = !0);
    },
    p(h, _) {
      /*show_label*/
      h[1] ? s ? (s.p(h, _), _[0] & /*show_label*/
      2 && N(s, 1)) : (s = ci(h), s.c(), N(s, 1), s.m(t.parentNode, t)) : s && (Ce(), G(s, 1, 1, () => {
        s = null;
      }), ke());
      let g = n;
      n = c(h), n === g ? f[n].p(h, _) : (Ce(), G(f[g], 1, 1, () => {
        f[g] = null;
      }), ke(), i = f[n], i ? i.p(h, _) : (i = f[n] = u[n](h), i.c()), N(i, 1), i.m(r.parentNode, r));
    },
    i(h) {
      l || (N(s), N(i), l = !0);
    },
    o(h) {
      G(s), G(i), l = !1;
    },
    d(h) {
      h && (X(t), X(r)), s && s.d(h), f[n].d(h), o = !1, a();
    }
  };
}
function Ke(e, t) {
  return e ?? t();
}
function Se(e) {
  let t, n = e[0], i = 1;
  for (; i < e.length; ) {
    const r = e[i], l = e[i + 1];
    if (i += 2, (r === "optionalAccess" || r === "optionalCall") && n == null)
      return;
    r === "access" || r === "optionalAccess" ? (t = n, n = l(n)) : (r === "call" || r === "optionalCall") && (n = l((...o) => n.call(t, ...o)), t = void 0);
  }
  return n;
}
function Cu(e) {
  return typeof e == "object" && e !== null && "data" in e;
}
function fn(e) {
  return Cu(e) ? e.path : typeof e == "string" ? e : Array.isArray(e) ? fn(e[0]) : "";
}
function Pu(e, t, n) {
  let i, r, { show_label: l = !0 } = t, { label: o } = t, { root: a = "" } = t, { proxy_url: s = null } = t, { value: u = null } = t, { columns: f = [2] } = t, { rows: c = void 0 } = t, { height: h = "auto" } = t, { preview: _ } = t, { allow_preview: g = !0 } = t, { object_fit: S = "cover" } = t, { show_share_button: v = !1 } = t, { show_download_button: A = !1 } = t, { i18n: y } = t, { selected_index: d = null } = t, T = "";
  const b = pu();
  vu(() => {
    const m = document.createElement("video");
    m.style.position = "absolute", m.style.left = "-9999px", m.src = u[0].image.url, m.crossOrigin = "anonymous", m.muted = !0, m.addEventListener("loadedmetadata", () => {
      m.currentTime = 0.1;
    }), m.addEventListener("seeked", () => {
      I(m);
    }), document.body.appendChild(m), m.load();
  });
  function I(m) {
    const J = document.createElement("canvas");
    J.width = m.videoWidth, J.height = m.videoHeight, J.getContext("2d").drawImage(m, 0, 0, J.width, J.height), n(13, T = J.toDataURL("image/jpeg")), document.body.removeChild(m);
  }
  let M = !0, U = null, O = u;
  d === null && _ && Se([u, "optionalAccess", (m) => m.length]) && (d = 0);
  let V = d;
  function de(m) {
    const J = m.target, ft = m.clientX, Pt = J.offsetWidth / 2;
    ft < Pt ? n(0, d = i) : n(0, d = r);
  }
  function Oe(m) {
    switch (m.code) {
      case "Escape":
        m.preventDefault(), n(0, d = null);
        break;
      case "ArrowLeft":
        m.preventDefault(), n(0, d = i);
        break;
      case "ArrowRight":
        m.preventDefault(), n(0, d = r);
        break;
    }
  }
  let q = [], z;
  async function p(m) {
    if (typeof m != "number" || (await wu(), q[m] === void 0))
      return;
    Se([
      q,
      "access",
      (Qe) => Qe[m],
      "optionalAccess",
      (Qe) => Qe.focus,
      "call",
      (Qe) => Qe()
    ]);
    const { left: J, width: ft } = z.getBoundingClientRect(), { left: Tn, width: Pt } = q[m].getBoundingClientRect(), An = Tn - J + Pt / 2 - ft / 2 + z.scrollLeft;
    z && typeof z.scrollTo == "function" && z.scrollTo({
      left: An < 0 ? 0 : An,
      behavior: "smooth"
    });
  }
  let Me = 0, ot = 0;
  function st(m) {
    we.call(this, e, m);
  }
  function at(m) {
    we.call(this, e, m);
  }
  function ut(m) {
    we.call(this, e, m);
  }
  function kt(m) {
    we.call(this, e, m);
  }
  function Ct(m) {
    we.call(this, e, m);
  }
  function E(m) {
    we.call(this, e, m);
  }
  function Ar() {
    n(17, ot = yr.innerHeight);
  }
  const Hr = () => n(0, d = null), Br = (m) => de(m);
  function kr(m, J) {
    ai[m ? "unshift" : "push"](() => {
      q[J] = m, n(14, q);
    });
  }
  const Cr = (m) => n(0, d = m);
  function Pr(m) {
    ai[m ? "unshift" : "push"](() => {
      z = m, n(15, z);
    });
  }
  function Ir(m) {
    we.call(this, e, m);
  }
  function Lr(m) {
    we.call(this, e, m);
  }
  const Nr = (m) => n(0, d = m);
  function Or() {
    Me = this.clientHeight, n(16, Me);
  }
  return e.$$set = (m) => {
    "show_label" in m && n(1, l = m.show_label), "label" in m && n(2, o = m.label), "root" in m && n(20, a = m.root), "proxy_url" in m && n(21, s = m.proxy_url), "value" in m && n(3, u = m.value), "columns" in m && n(4, f = m.columns), "rows" in m && n(5, c = m.rows), "height" in m && n(6, h = m.height), "preview" in m && n(22, _ = m.preview), "allow_preview" in m && n(7, g = m.allow_preview), "object_fit" in m && n(8, S = m.object_fit), "show_share_button" in m && n(9, v = m.show_share_button), "show_download_button" in m && n(10, A = m.show_download_button), "i18n" in m && n(11, y = m.i18n), "selected_index" in m && n(0, d = m.selected_index);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*value, was_reset*/
    8388616 && n(23, M = u == null || u.length == 0 ? !0 : M), e.$$.dirty[0] & /*value, root, proxy_url*/
    3145736 && n(12, U = u === null ? null : u.map((m) => ({
      image: Vi(m.image, a, s),
      caption: m.caption
    }))), e.$$.dirty[0] & /*prevValue, value, was_reset, preview, selected_index*/
    29360137 && ($e(O, u) || (M ? (n(0, d = _ && Se([u, "optionalAccess", (m) => m.length]) ? 0 : null), n(23, M = !1)) : n(
      0,
      d = d !== null && u !== null && d < u.length ? d : null
    ), b("change"), n(24, O = u))), e.$$.dirty[0] & /*selected_index, _value*/
    4097 && (i = (Ke(d, () => 0) + Ke(Se([U, "optionalAccess", (m) => m.length]), () => 0) - 1) % Ke(Se([U, "optionalAccess", (m) => m.length]), () => 0)), e.$$.dirty[0] & /*selected_index, _value*/
    4097 && (r = (Ke(d, () => 0) + 1) % Ke(Se([U, "optionalAccess", (m) => m.length]), () => 0)), e.$$.dirty[0] & /*selected_index, old_selected_index, _value*/
    33558529 && d !== V && (n(25, V = d), d !== null && b("select", {
      index: d,
      value: Se([U, "optionalAccess", (m) => m[d]])
    })), e.$$.dirty[0] & /*allow_preview, selected_index*/
    129 && g && p(d);
  }, [
    d,
    l,
    o,
    u,
    f,
    c,
    h,
    g,
    S,
    v,
    A,
    y,
    U,
    T,
    q,
    z,
    Me,
    ot,
    de,
    Oe,
    a,
    s,
    _,
    M,
    O,
    V,
    st,
    at,
    ut,
    kt,
    Ct,
    E,
    Ar,
    Hr,
    Br,
    kr,
    Cr,
    Pr,
    Ir,
    Lr,
    Nr,
    Or
  ];
}
class Iu extends hu {
  constructor(t) {
    super(), bu(
      this,
      t,
      Pu,
      ku,
      gu,
      {
        show_label: 1,
        label: 2,
        root: 20,
        proxy_url: 21,
        value: 3,
        columns: 4,
        rows: 5,
        height: 6,
        preview: 22,
        allow_preview: 7,
        object_fit: 8,
        show_share_button: 9,
        show_download_button: 10,
        i18n: 11,
        selected_index: 0
      },
      null,
      [-1, -1]
    );
  }
}
function Ue(e) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], n = 0;
  for (; e > 1e3 && n < t.length - 1; )
    e /= 1e3, n++;
  let i = t[n];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + i;
}
const {
  SvelteComponent: Lu,
  append: ne,
  attr: P,
  component_subscribe: wi,
  detach: Nu,
  element: Ou,
  init: Mu,
  insert: Ru,
  noop: yi,
  safe_not_equal: Du,
  set_style: dt,
  svg_element: ie,
  toggle_class: Ei
} = window.__gradio__svelte__internal, { onMount: Uu } = window.__gradio__svelte__internal;
function Gu(e) {
  let t, n, i, r, l, o, a, s, u, f, c, h;
  return {
    c() {
      t = Ou("div"), n = ie("svg"), i = ie("g"), r = ie("path"), l = ie("path"), o = ie("path"), a = ie("path"), s = ie("g"), u = ie("path"), f = ie("path"), c = ie("path"), h = ie("path"), P(r, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), P(r, "fill", "#FF7C00"), P(r, "fill-opacity", "0.4"), P(r, "class", "svelte-43sxxs"), P(l, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), P(l, "fill", "#FF7C00"), P(l, "class", "svelte-43sxxs"), P(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), P(o, "fill", "#FF7C00"), P(o, "fill-opacity", "0.4"), P(o, "class", "svelte-43sxxs"), P(a, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), P(a, "fill", "#FF7C00"), P(a, "class", "svelte-43sxxs"), dt(i, "transform", "translate(" + /*$top*/
      e[1][0] + "px, " + /*$top*/
      e[1][1] + "px)"), P(u, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), P(u, "fill", "#FF7C00"), P(u, "fill-opacity", "0.4"), P(u, "class", "svelte-43sxxs"), P(f, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), P(f, "fill", "#FF7C00"), P(f, "class", "svelte-43sxxs"), P(c, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), P(c, "fill", "#FF7C00"), P(c, "fill-opacity", "0.4"), P(c, "class", "svelte-43sxxs"), P(h, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), P(h, "fill", "#FF7C00"), P(h, "class", "svelte-43sxxs"), dt(s, "transform", "translate(" + /*$bottom*/
      e[2][0] + "px, " + /*$bottom*/
      e[2][1] + "px)"), P(n, "viewBox", "-1200 -1200 3000 3000"), P(n, "fill", "none"), P(n, "xmlns", "http://www.w3.org/2000/svg"), P(n, "class", "svelte-43sxxs"), P(t, "class", "svelte-43sxxs"), Ei(
        t,
        "margin",
        /*margin*/
        e[0]
      );
    },
    m(_, g) {
      Ru(_, t, g), ne(t, n), ne(n, i), ne(i, r), ne(i, l), ne(i, o), ne(i, a), ne(n, s), ne(s, u), ne(s, f), ne(s, c), ne(s, h);
    },
    p(_, [g]) {
      g & /*$top*/
      2 && dt(i, "transform", "translate(" + /*$top*/
      _[1][0] + "px, " + /*$top*/
      _[1][1] + "px)"), g & /*$bottom*/
      4 && dt(s, "transform", "translate(" + /*$bottom*/
      _[2][0] + "px, " + /*$bottom*/
      _[2][1] + "px)"), g & /*margin*/
      1 && Ei(
        t,
        "margin",
        /*margin*/
        _[0]
      );
    },
    i: yi,
    o: yi,
    d(_) {
      _ && Nu(t);
    }
  };
}
function xu(e, t, n) {
  let i, r, { margin: l = !0 } = t;
  const o = Un([0, 0]);
  wi(e, o, (h) => n(1, i = h));
  const a = Un([0, 0]);
  wi(e, a, (h) => n(2, r = h));
  let s;
  async function u() {
    await Promise.all([o.set([125, 140]), a.set([-125, -140])]), await Promise.all([o.set([-125, 140]), a.set([125, -140])]), await Promise.all([o.set([-125, 0]), a.set([125, -0])]), await Promise.all([o.set([125, 0]), a.set([-125, 0])]);
  }
  async function f() {
    await u(), s || f();
  }
  async function c() {
    await Promise.all([o.set([125, 0]), a.set([-125, 0])]), f();
  }
  return Uu(() => (c(), () => s = !0)), e.$$set = (h) => {
    "margin" in h && n(0, l = h.margin);
  }, [l, i, r, o, a];
}
class Fu extends Lu {
  constructor(t) {
    super(), Mu(this, t, xu, Gu, Du, { margin: 0 });
  }
}
const {
  SvelteComponent: ju,
  append: He,
  attr: fe,
  binding_callbacks: Si,
  check_outros: Er,
  create_component: Vu,
  create_slot: qu,
  destroy_component: zu,
  destroy_each: Sr,
  detach: H,
  element: me,
  empty: We,
  ensure_array_like: St,
  get_all_dirty_from_scope: Xu,
  get_slot_changes: Zu,
  group_outros: Tr,
  init: Wu,
  insert: B,
  mount_component: Qu,
  noop: cn,
  safe_not_equal: Ju,
  set_data: $,
  set_style: Ee,
  space: ce,
  text: D,
  toggle_class: K,
  transition_in: qe,
  transition_out: ze,
  update_slot_base: Yu
} = window.__gradio__svelte__internal, { tick: Ku } = window.__gradio__svelte__internal, { onDestroy: $u } = window.__gradio__svelte__internal, ef = (e) => ({}), Ti = (e) => ({});
function Ai(e, t, n) {
  const i = e.slice();
  return i[38] = t[n], i[40] = n, i;
}
function Hi(e, t, n) {
  const i = e.slice();
  return i[38] = t[n], i;
}
function tf(e) {
  let t, n = (
    /*i18n*/
    e[1]("common.error") + ""
  ), i, r, l;
  const o = (
    /*#slots*/
    e[29].error
  ), a = qu(
    o,
    e,
    /*$$scope*/
    e[28],
    Ti
  );
  return {
    c() {
      t = me("span"), i = D(n), r = ce(), a && a.c(), fe(t, "class", "error svelte-14miwb5");
    },
    m(s, u) {
      B(s, t, u), He(t, i), B(s, r, u), a && a.m(s, u), l = !0;
    },
    p(s, u) {
      (!l || u[0] & /*i18n*/
      2) && n !== (n = /*i18n*/
      s[1]("common.error") + "") && $(i, n), a && a.p && (!l || u[0] & /*$$scope*/
      268435456) && Yu(
        a,
        o,
        s,
        /*$$scope*/
        s[28],
        l ? Zu(
          o,
          /*$$scope*/
          s[28],
          u,
          ef
        ) : Xu(
          /*$$scope*/
          s[28]
        ),
        Ti
      );
    },
    i(s) {
      l || (qe(a, s), l = !0);
    },
    o(s) {
      ze(a, s), l = !1;
    },
    d(s) {
      s && (H(t), H(r)), a && a.d(s);
    }
  };
}
function nf(e) {
  let t, n, i, r, l, o, a, s, u, f = (
    /*variant*/
    e[8] === "default" && /*show_eta_bar*/
    e[18] && /*show_progress*/
    e[6] === "full" && Bi(e)
  );
  function c(d, T) {
    if (
      /*progress*/
      d[7]
    )
      return of;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    )
      return lf;
    if (
      /*queue_position*/
      d[2] === 0
    )
      return rf;
  }
  let h = c(e), _ = h && h(e), g = (
    /*timer*/
    e[5] && Pi(e)
  );
  const S = [ff, uf], v = [];
  function A(d, T) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(l = A(e)) && (o = v[l] = S[l](e));
  let y = !/*timer*/
  e[5] && Di(e);
  return {
    c() {
      f && f.c(), t = ce(), n = me("div"), _ && _.c(), i = ce(), g && g.c(), r = ce(), o && o.c(), a = ce(), y && y.c(), s = We(), fe(n, "class", "progress-text svelte-14miwb5"), K(
        n,
        "meta-text-center",
        /*variant*/
        e[8] === "center"
      ), K(
        n,
        "meta-text",
        /*variant*/
        e[8] === "default"
      );
    },
    m(d, T) {
      f && f.m(d, T), B(d, t, T), B(d, n, T), _ && _.m(n, null), He(n, i), g && g.m(n, null), B(d, r, T), ~l && v[l].m(d, T), B(d, a, T), y && y.m(d, T), B(d, s, T), u = !0;
    },
    p(d, T) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? f ? f.p(d, T) : (f = Bi(d), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), h === (h = c(d)) && _ ? _.p(d, T) : (_ && _.d(1), _ = h && h(d), _ && (_.c(), _.m(n, i))), /*timer*/
      d[5] ? g ? g.p(d, T) : (g = Pi(d), g.c(), g.m(n, null)) : g && (g.d(1), g = null), (!u || T[0] & /*variant*/
      256) && K(
        n,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!u || T[0] & /*variant*/
      256) && K(
        n,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let b = l;
      l = A(d), l === b ? ~l && v[l].p(d, T) : (o && (Tr(), ze(v[b], 1, 1, () => {
        v[b] = null;
      }), Er()), ~l ? (o = v[l], o ? o.p(d, T) : (o = v[l] = S[l](d), o.c()), qe(o, 1), o.m(a.parentNode, a)) : o = null), /*timer*/
      d[5] ? y && (y.d(1), y = null) : y ? y.p(d, T) : (y = Di(d), y.c(), y.m(s.parentNode, s));
    },
    i(d) {
      u || (qe(o), u = !0);
    },
    o(d) {
      ze(o), u = !1;
    },
    d(d) {
      d && (H(t), H(n), H(r), H(a), H(s)), f && f.d(d), _ && _.d(), g && g.d(), ~l && v[l].d(d), y && y.d(d);
    }
  };
}
function Bi(e) {
  let t, n = `translateX(${/*eta_level*/
  (e[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = me("div"), fe(t, "class", "eta-bar svelte-14miwb5"), Ee(t, "transform", n);
    },
    m(i, r) {
      B(i, t, r);
    },
    p(i, r) {
      r[0] & /*eta_level*/
      131072 && n !== (n = `translateX(${/*eta_level*/
      (i[17] || 0) * 100 - 100}%)`) && Ee(t, "transform", n);
    },
    d(i) {
      i && H(t);
    }
  };
}
function rf(e) {
  let t;
  return {
    c() {
      t = D("processing |");
    },
    m(n, i) {
      B(n, t, i);
    },
    p: cn,
    d(n) {
      n && H(t);
    }
  };
}
function lf(e) {
  let t, n = (
    /*queue_position*/
    e[2] + 1 + ""
  ), i, r, l, o;
  return {
    c() {
      t = D("queue: "), i = D(n), r = D("/"), l = D(
        /*queue_size*/
        e[3]
      ), o = D(" |");
    },
    m(a, s) {
      B(a, t, s), B(a, i, s), B(a, r, s), B(a, l, s), B(a, o, s);
    },
    p(a, s) {
      s[0] & /*queue_position*/
      4 && n !== (n = /*queue_position*/
      a[2] + 1 + "") && $(i, n), s[0] & /*queue_size*/
      8 && $(
        l,
        /*queue_size*/
        a[3]
      );
    },
    d(a) {
      a && (H(t), H(i), H(r), H(l), H(o));
    }
  };
}
function of(e) {
  let t, n = St(
    /*progress*/
    e[7]
  ), i = [];
  for (let r = 0; r < n.length; r += 1)
    i[r] = Ci(Hi(e, n, r));
  return {
    c() {
      for (let r = 0; r < i.length; r += 1)
        i[r].c();
      t = We();
    },
    m(r, l) {
      for (let o = 0; o < i.length; o += 1)
        i[o] && i[o].m(r, l);
      B(r, t, l);
    },
    p(r, l) {
      if (l[0] & /*progress*/
      128) {
        n = St(
          /*progress*/
          r[7]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const a = Hi(r, n, o);
          i[o] ? i[o].p(a, l) : (i[o] = Ci(a), i[o].c(), i[o].m(t.parentNode, t));
        }
        for (; o < i.length; o += 1)
          i[o].d(1);
        i.length = n.length;
      }
    },
    d(r) {
      r && H(t), Sr(i, r);
    }
  };
}
function ki(e) {
  let t, n = (
    /*p*/
    e[38].unit + ""
  ), i, r, l = " ", o;
  function a(f, c) {
    return (
      /*p*/
      f[38].length != null ? af : sf
    );
  }
  let s = a(e), u = s(e);
  return {
    c() {
      u.c(), t = ce(), i = D(n), r = D(" | "), o = D(l);
    },
    m(f, c) {
      u.m(f, c), B(f, t, c), B(f, i, c), B(f, r, c), B(f, o, c);
    },
    p(f, c) {
      s === (s = a(f)) && u ? u.p(f, c) : (u.d(1), u = s(f), u && (u.c(), u.m(t.parentNode, t))), c[0] & /*progress*/
      128 && n !== (n = /*p*/
      f[38].unit + "") && $(i, n);
    },
    d(f) {
      f && (H(t), H(i), H(r), H(o)), u.d(f);
    }
  };
}
function sf(e) {
  let t = Ue(
    /*p*/
    e[38].index || 0
  ) + "", n;
  return {
    c() {
      n = D(t);
    },
    m(i, r) {
      B(i, n, r);
    },
    p(i, r) {
      r[0] & /*progress*/
      128 && t !== (t = Ue(
        /*p*/
        i[38].index || 0
      ) + "") && $(n, t);
    },
    d(i) {
      i && H(n);
    }
  };
}
function af(e) {
  let t = Ue(
    /*p*/
    e[38].index || 0
  ) + "", n, i, r = Ue(
    /*p*/
    e[38].length
  ) + "", l;
  return {
    c() {
      n = D(t), i = D("/"), l = D(r);
    },
    m(o, a) {
      B(o, n, a), B(o, i, a), B(o, l, a);
    },
    p(o, a) {
      a[0] & /*progress*/
      128 && t !== (t = Ue(
        /*p*/
        o[38].index || 0
      ) + "") && $(n, t), a[0] & /*progress*/
      128 && r !== (r = Ue(
        /*p*/
        o[38].length
      ) + "") && $(l, r);
    },
    d(o) {
      o && (H(n), H(i), H(l));
    }
  };
}
function Ci(e) {
  let t, n = (
    /*p*/
    e[38].index != null && ki(e)
  );
  return {
    c() {
      n && n.c(), t = We();
    },
    m(i, r) {
      n && n.m(i, r), B(i, t, r);
    },
    p(i, r) {
      /*p*/
      i[38].index != null ? n ? n.p(i, r) : (n = ki(i), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(i) {
      i && H(t), n && n.d(i);
    }
  };
}
function Pi(e) {
  let t, n = (
    /*eta*/
    e[0] ? `/${/*formatted_eta*/
    e[19]}` : ""
  ), i, r;
  return {
    c() {
      t = D(
        /*formatted_timer*/
        e[20]
      ), i = D(n), r = D("s");
    },
    m(l, o) {
      B(l, t, o), B(l, i, o), B(l, r, o);
    },
    p(l, o) {
      o[0] & /*formatted_timer*/
      1048576 && $(
        t,
        /*formatted_timer*/
        l[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && n !== (n = /*eta*/
      l[0] ? `/${/*formatted_eta*/
      l[19]}` : "") && $(i, n);
    },
    d(l) {
      l && (H(t), H(i), H(r));
    }
  };
}
function uf(e) {
  let t, n;
  return t = new Fu({
    props: { margin: (
      /*variant*/
      e[8] === "default"
    ) }
  }), {
    c() {
      Vu(t.$$.fragment);
    },
    m(i, r) {
      Qu(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[0] & /*variant*/
      256 && (l.margin = /*variant*/
      i[8] === "default"), t.$set(l);
    },
    i(i) {
      n || (qe(t.$$.fragment, i), n = !0);
    },
    o(i) {
      ze(t.$$.fragment, i), n = !1;
    },
    d(i) {
      zu(t, i);
    }
  };
}
function ff(e) {
  let t, n, i, r, l, o = `${/*last_progress_level*/
  e[15] * 100}%`, a = (
    /*progress*/
    e[7] != null && Ii(e)
  );
  return {
    c() {
      t = me("div"), n = me("div"), a && a.c(), i = ce(), r = me("div"), l = me("div"), fe(n, "class", "progress-level-inner svelte-14miwb5"), fe(l, "class", "progress-bar svelte-14miwb5"), Ee(l, "width", o), fe(r, "class", "progress-bar-wrap svelte-14miwb5"), fe(t, "class", "progress-level svelte-14miwb5");
    },
    m(s, u) {
      B(s, t, u), He(t, n), a && a.m(n, null), He(t, i), He(t, r), He(r, l), e[30](l);
    },
    p(s, u) {
      /*progress*/
      s[7] != null ? a ? a.p(s, u) : (a = Ii(s), a.c(), a.m(n, null)) : a && (a.d(1), a = null), u[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      s[15] * 100}%`) && Ee(l, "width", o);
    },
    i: cn,
    o: cn,
    d(s) {
      s && H(t), a && a.d(), e[30](null);
    }
  };
}
function Ii(e) {
  let t, n = St(
    /*progress*/
    e[7]
  ), i = [];
  for (let r = 0; r < n.length; r += 1)
    i[r] = Ri(Ai(e, n, r));
  return {
    c() {
      for (let r = 0; r < i.length; r += 1)
        i[r].c();
      t = We();
    },
    m(r, l) {
      for (let o = 0; o < i.length; o += 1)
        i[o] && i[o].m(r, l);
      B(r, t, l);
    },
    p(r, l) {
      if (l[0] & /*progress_level, progress*/
      16512) {
        n = St(
          /*progress*/
          r[7]
        );
        let o;
        for (o = 0; o < n.length; o += 1) {
          const a = Ai(r, n, o);
          i[o] ? i[o].p(a, l) : (i[o] = Ri(a), i[o].c(), i[o].m(t.parentNode, t));
        }
        for (; o < i.length; o += 1)
          i[o].d(1);
        i.length = n.length;
      }
    },
    d(r) {
      r && H(t), Sr(i, r);
    }
  };
}
function Li(e) {
  let t, n, i, r, l = (
    /*i*/
    e[40] !== 0 && cf()
  ), o = (
    /*p*/
    e[38].desc != null && Ni(e)
  ), a = (
    /*p*/
    e[38].desc != null && /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null && Oi()
  ), s = (
    /*progress_level*/
    e[14] != null && Mi(e)
  );
  return {
    c() {
      l && l.c(), t = ce(), o && o.c(), n = ce(), a && a.c(), i = ce(), s && s.c(), r = We();
    },
    m(u, f) {
      l && l.m(u, f), B(u, t, f), o && o.m(u, f), B(u, n, f), a && a.m(u, f), B(u, i, f), s && s.m(u, f), B(u, r, f);
    },
    p(u, f) {
      /*p*/
      u[38].desc != null ? o ? o.p(u, f) : (o = Ni(u), o.c(), o.m(n.parentNode, n)) : o && (o.d(1), o = null), /*p*/
      u[38].desc != null && /*progress_level*/
      u[14] && /*progress_level*/
      u[14][
        /*i*/
        u[40]
      ] != null ? a || (a = Oi(), a.c(), a.m(i.parentNode, i)) : a && (a.d(1), a = null), /*progress_level*/
      u[14] != null ? s ? s.p(u, f) : (s = Mi(u), s.c(), s.m(r.parentNode, r)) : s && (s.d(1), s = null);
    },
    d(u) {
      u && (H(t), H(n), H(i), H(r)), l && l.d(u), o && o.d(u), a && a.d(u), s && s.d(u);
    }
  };
}
function cf(e) {
  let t;
  return {
    c() {
      t = D(" /");
    },
    m(n, i) {
      B(n, t, i);
    },
    d(n) {
      n && H(t);
    }
  };
}
function Ni(e) {
  let t = (
    /*p*/
    e[38].desc + ""
  ), n;
  return {
    c() {
      n = D(t);
    },
    m(i, r) {
      B(i, n, r);
    },
    p(i, r) {
      r[0] & /*progress*/
      128 && t !== (t = /*p*/
      i[38].desc + "") && $(n, t);
    },
    d(i) {
      i && H(n);
    }
  };
}
function Oi(e) {
  let t;
  return {
    c() {
      t = D("-");
    },
    m(n, i) {
      B(n, t, i);
    },
    d(n) {
      n && H(t);
    }
  };
}
function Mi(e) {
  let t = (100 * /*progress_level*/
  (e[14][
    /*i*/
    e[40]
  ] || 0)).toFixed(1) + "", n, i;
  return {
    c() {
      n = D(t), i = D("%");
    },
    m(r, l) {
      B(r, n, l), B(r, i, l);
    },
    p(r, l) {
      l[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (r[14][
        /*i*/
        r[40]
      ] || 0)).toFixed(1) + "") && $(n, t);
    },
    d(r) {
      r && (H(n), H(i));
    }
  };
}
function Ri(e) {
  let t, n = (
    /*p*/
    (e[38].desc != null || /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null) && Li(e)
  );
  return {
    c() {
      n && n.c(), t = We();
    },
    m(i, r) {
      n && n.m(i, r), B(i, t, r);
    },
    p(i, r) {
      /*p*/
      i[38].desc != null || /*progress_level*/
      i[14] && /*progress_level*/
      i[14][
        /*i*/
        i[40]
      ] != null ? n ? n.p(i, r) : (n = Li(i), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(i) {
      i && H(t), n && n.d(i);
    }
  };
}
function Di(e) {
  let t, n;
  return {
    c() {
      t = me("p"), n = D(
        /*loading_text*/
        e[9]
      ), fe(t, "class", "loading svelte-14miwb5");
    },
    m(i, r) {
      B(i, t, r), He(t, n);
    },
    p(i, r) {
      r[0] & /*loading_text*/
      512 && $(
        n,
        /*loading_text*/
        i[9]
      );
    },
    d(i) {
      i && H(t);
    }
  };
}
function hf(e) {
  let t, n, i, r, l;
  const o = [nf, tf], a = [];
  function s(u, f) {
    return (
      /*status*/
      u[4] === "pending" ? 0 : (
        /*status*/
        u[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(n = s(e)) && (i = a[n] = o[n](e)), {
    c() {
      t = me("div"), i && i.c(), fe(t, "class", r = "wrap " + /*variant*/
      e[8] + " " + /*show_progress*/
      e[6] + " svelte-14miwb5"), K(t, "hide", !/*status*/
      e[4] || /*status*/
      e[4] === "complete" || /*show_progress*/
      e[6] === "hidden"), K(
        t,
        "translucent",
        /*variant*/
        e[8] === "center" && /*status*/
        (e[4] === "pending" || /*status*/
        e[4] === "error") || /*translucent*/
        e[11] || /*show_progress*/
        e[6] === "minimal"
      ), K(
        t,
        "generating",
        /*status*/
        e[4] === "generating"
      ), K(
        t,
        "border",
        /*border*/
        e[12]
      ), Ee(
        t,
        "position",
        /*absolute*/
        e[10] ? "absolute" : "static"
      ), Ee(
        t,
        "padding",
        /*absolute*/
        e[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(u, f) {
      B(u, t, f), ~n && a[n].m(t, null), e[31](t), l = !0;
    },
    p(u, f) {
      let c = n;
      n = s(u), n === c ? ~n && a[n].p(u, f) : (i && (Tr(), ze(a[c], 1, 1, () => {
        a[c] = null;
      }), Er()), ~n ? (i = a[n], i ? i.p(u, f) : (i = a[n] = o[n](u), i.c()), qe(i, 1), i.m(t, null)) : i = null), (!l || f[0] & /*variant, show_progress*/
      320 && r !== (r = "wrap " + /*variant*/
      u[8] + " " + /*show_progress*/
      u[6] + " svelte-14miwb5")) && fe(t, "class", r), (!l || f[0] & /*variant, show_progress, status, show_progress*/
      336) && K(t, "hide", !/*status*/
      u[4] || /*status*/
      u[4] === "complete" || /*show_progress*/
      u[6] === "hidden"), (!l || f[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && K(
        t,
        "translucent",
        /*variant*/
        u[8] === "center" && /*status*/
        (u[4] === "pending" || /*status*/
        u[4] === "error") || /*translucent*/
        u[11] || /*show_progress*/
        u[6] === "minimal"
      ), (!l || f[0] & /*variant, show_progress, status*/
      336) && K(
        t,
        "generating",
        /*status*/
        u[4] === "generating"
      ), (!l || f[0] & /*variant, show_progress, border*/
      4416) && K(
        t,
        "border",
        /*border*/
        u[12]
      ), f[0] & /*absolute*/
      1024 && Ee(
        t,
        "position",
        /*absolute*/
        u[10] ? "absolute" : "static"
      ), f[0] & /*absolute*/
      1024 && Ee(
        t,
        "padding",
        /*absolute*/
        u[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(u) {
      l || (qe(i), l = !0);
    },
    o(u) {
      ze(i), l = !1;
    },
    d(u) {
      u && H(t), ~n && a[n].d(), e[31](null);
    }
  };
}
let bt = [], Jt = !1;
async function _f(e, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (bt.push(e), !Jt)
      Jt = !0;
    else
      return;
    await Ku(), requestAnimationFrame(() => {
      let n = [0, 0];
      for (let i = 0; i < bt.length; i++) {
        const l = bt[i].getBoundingClientRect();
        (i === 0 || l.top + window.scrollY <= n[0]) && (n[0] = l.top + window.scrollY, n[1] = i);
      }
      window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), Jt = !1, bt = [];
    });
  }
}
function mf(e, t, n) {
  let i, { $$slots: r = {}, $$scope: l } = t, { i18n: o } = t, { eta: a = null } = t, { queue: s = !1 } = t, { queue_position: u } = t, { queue_size: f } = t, { status: c } = t, { scroll_to_output: h = !1 } = t, { timer: _ = !0 } = t, { show_progress: g = "full" } = t, { message: S = null } = t, { progress: v = null } = t, { variant: A = "default" } = t, { loading_text: y = "Loading..." } = t, { absolute: d = !0 } = t, { translucent: T = !1 } = t, { border: b = !1 } = t, { autoscroll: I } = t, M, U = !1, O = 0, V = 0, de = null, Oe = 0, q = null, z, p = null, Me = !0;
  const ot = () => {
    n(25, O = performance.now()), n(26, V = 0), U = !0, st();
  };
  function st() {
    requestAnimationFrame(() => {
      n(26, V = (performance.now() - O) / 1e3), U && st();
    });
  }
  function at() {
    n(26, V = 0), U && (U = !1);
  }
  $u(() => {
    U && at();
  });
  let ut = null;
  function kt(E) {
    Si[E ? "unshift" : "push"](() => {
      p = E, n(16, p), n(7, v), n(14, q), n(15, z);
    });
  }
  function Ct(E) {
    Si[E ? "unshift" : "push"](() => {
      M = E, n(13, M);
    });
  }
  return e.$$set = (E) => {
    "i18n" in E && n(1, o = E.i18n), "eta" in E && n(0, a = E.eta), "queue" in E && n(21, s = E.queue), "queue_position" in E && n(2, u = E.queue_position), "queue_size" in E && n(3, f = E.queue_size), "status" in E && n(4, c = E.status), "scroll_to_output" in E && n(22, h = E.scroll_to_output), "timer" in E && n(5, _ = E.timer), "show_progress" in E && n(6, g = E.show_progress), "message" in E && n(23, S = E.message), "progress" in E && n(7, v = E.progress), "variant" in E && n(8, A = E.variant), "loading_text" in E && n(9, y = E.loading_text), "absolute" in E && n(10, d = E.absolute), "translucent" in E && n(11, T = E.translucent), "border" in E && n(12, b = E.border), "autoscroll" in E && n(24, I = E.autoscroll), "$$scope" in E && n(28, l = E.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*eta, old_eta, queue, timer_start*/
    169869313 && (a === null ? n(0, a = de) : s && n(0, a = (performance.now() - O) / 1e3 + a), a != null && (n(19, ut = a.toFixed(1)), n(27, de = a))), e.$$.dirty[0] & /*eta, timer_diff*/
    67108865 && n(17, Oe = a === null || a <= 0 || !V ? null : Math.min(V / a, 1)), e.$$.dirty[0] & /*progress*/
    128 && v != null && n(18, Me = !1), e.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (v != null ? n(14, q = v.map((E) => {
      if (E.index != null && E.length != null)
        return E.index / E.length;
      if (E.progress != null)
        return E.progress;
    })) : n(14, q = null), q ? (n(15, z = q[q.length - 1]), p && (z === 0 ? n(16, p.style.transition = "0", p) : n(16, p.style.transition = "150ms", p))) : n(15, z = void 0)), e.$$.dirty[0] & /*status*/
    16 && (c === "pending" ? ot() : at()), e.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && M && h && (c === "pending" || c === "complete") && _f(M, I), e.$$.dirty[0] & /*status, message*/
    8388624, e.$$.dirty[0] & /*timer_diff*/
    67108864 && n(20, i = V.toFixed(1));
  }, [
    a,
    o,
    u,
    f,
    c,
    _,
    g,
    v,
    A,
    y,
    d,
    T,
    b,
    M,
    q,
    z,
    p,
    Oe,
    Me,
    ut,
    i,
    s,
    h,
    S,
    I,
    O,
    V,
    de,
    l,
    r,
    kt,
    Ct
  ];
}
class df extends ju {
  constructor(t) {
    super(), Wu(
      this,
      t,
      mf,
      hf,
      Ju,
      {
        i18n: 1,
        eta: 0,
        queue: 21,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: bf,
  add_flush_callback: gf,
  assign: pf,
  bind: vf,
  binding_callbacks: wf,
  create_component: hn,
  destroy_component: _n,
  detach: yf,
  get_spread_object: Ef,
  get_spread_update: Sf,
  init: Tf,
  insert: Af,
  mount_component: mn,
  safe_not_equal: Hf,
  space: Bf,
  transition_in: dn,
  transition_out: bn
} = window.__gradio__svelte__internal, { createEventDispatcher: kf } = window.__gradio__svelte__internal;
function Cf(e) {
  let t, n, i, r, l;
  const o = [
    {
      autoscroll: (
        /*gradio*/
        e[21].autoscroll
      )
    },
    { i18n: (
      /*gradio*/
      e[21].i18n
    ) },
    /*loading_status*/
    e[1]
  ];
  let a = {};
  for (let f = 0; f < o.length; f += 1)
    a = pf(a, o[f]);
  t = new df({ props: a });
  function s(f) {
    e[22](f);
  }
  let u = {
    label: (
      /*label*/
      e[3]
    ),
    value: (
      /*value*/
      e[9]
    ),
    show_label: (
      /*show_label*/
      e[2]
    ),
    root: (
      /*root*/
      e[4]
    ),
    proxy_url: (
      /*proxy_url*/
      e[5]
    ),
    columns: (
      /*columns*/
      e[13]
    ),
    rows: (
      /*rows*/
      e[14]
    ),
    height: (
      /*height*/
      e[15]
    ),
    preview: (
      /*preview*/
      e[16]
    ),
    object_fit: (
      /*object_fit*/
      e[18]
    ),
    allow_preview: (
      /*allow_preview*/
      e[17]
    ),
    show_share_button: (
      /*show_share_button*/
      e[19]
    ),
    show_download_button: (
      /*show_download_button*/
      e[20]
    ),
    i18n: (
      /*gradio*/
      e[21].i18n
    )
  };
  return (
    /*selected_index*/
    e[0] !== void 0 && (u.selected_index = /*selected_index*/
    e[0]), i = new Iu({ props: u }), wf.push(() => vf(i, "selected_index", s)), i.$on(
      "change",
      /*change_handler*/
      e[23]
    ), i.$on(
      "select",
      /*select_handler*/
      e[24]
    ), i.$on(
      "share",
      /*share_handler*/
      e[25]
    ), i.$on(
      "error",
      /*error_handler*/
      e[26]
    ), {
      c() {
        hn(t.$$.fragment), n = Bf(), hn(i.$$.fragment);
      },
      m(f, c) {
        mn(t, f, c), Af(f, n, c), mn(i, f, c), l = !0;
      },
      p(f, c) {
        const h = c & /*gradio, loading_status*/
        2097154 ? Sf(o, [
          c & /*gradio*/
          2097152 && {
            autoscroll: (
              /*gradio*/
              f[21].autoscroll
            )
          },
          c & /*gradio*/
          2097152 && { i18n: (
            /*gradio*/
            f[21].i18n
          ) },
          c & /*loading_status*/
          2 && Ef(
            /*loading_status*/
            f[1]
          )
        ]) : {};
        t.$set(h);
        const _ = {};
        c & /*label*/
        8 && (_.label = /*label*/
        f[3]), c & /*value*/
        512 && (_.value = /*value*/
        f[9]), c & /*show_label*/
        4 && (_.show_label = /*show_label*/
        f[2]), c & /*root*/
        16 && (_.root = /*root*/
        f[4]), c & /*proxy_url*/
        32 && (_.proxy_url = /*proxy_url*/
        f[5]), c & /*columns*/
        8192 && (_.columns = /*columns*/
        f[13]), c & /*rows*/
        16384 && (_.rows = /*rows*/
        f[14]), c & /*height*/
        32768 && (_.height = /*height*/
        f[15]), c & /*preview*/
        65536 && (_.preview = /*preview*/
        f[16]), c & /*object_fit*/
        262144 && (_.object_fit = /*object_fit*/
        f[18]), c & /*allow_preview*/
        131072 && (_.allow_preview = /*allow_preview*/
        f[17]), c & /*show_share_button*/
        524288 && (_.show_share_button = /*show_share_button*/
        f[19]), c & /*show_download_button*/
        1048576 && (_.show_download_button = /*show_download_button*/
        f[20]), c & /*gradio*/
        2097152 && (_.i18n = /*gradio*/
        f[21].i18n), !r && c & /*selected_index*/
        1 && (r = !0, _.selected_index = /*selected_index*/
        f[0], gf(() => r = !1)), i.$set(_);
      },
      i(f) {
        l || (dn(t.$$.fragment, f), dn(i.$$.fragment, f), l = !0);
      },
      o(f) {
        bn(t.$$.fragment, f), bn(i.$$.fragment, f), l = !1;
      },
      d(f) {
        f && yf(n), _n(t, f), _n(i, f);
      }
    }
  );
}
function Pf(e) {
  let t, n;
  return t = new Jr({
    props: {
      visible: (
        /*visible*/
        e[8]
      ),
      variant: "solid",
      padding: !1,
      elem_id: (
        /*elem_id*/
        e[6]
      ),
      elem_classes: (
        /*elem_classes*/
        e[7]
      ),
      container: (
        /*container*/
        e[10]
      ),
      scale: (
        /*scale*/
        e[11]
      ),
      min_width: (
        /*min_width*/
        e[12]
      ),
      allow_overflow: !1,
      height: typeof /*height*/
      e[15] == "number" ? (
        /*height*/
        e[15]
      ) : void 0,
      $$slots: { default: [Cf] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      hn(t.$$.fragment);
    },
    m(i, r) {
      mn(t, i, r), n = !0;
    },
    p(i, [r]) {
      const l = {};
      r & /*visible*/
      256 && (l.visible = /*visible*/
      i[8]), r & /*elem_id*/
      64 && (l.elem_id = /*elem_id*/
      i[6]), r & /*elem_classes*/
      128 && (l.elem_classes = /*elem_classes*/
      i[7]), r & /*container*/
      1024 && (l.container = /*container*/
      i[10]), r & /*scale*/
      2048 && (l.scale = /*scale*/
      i[11]), r & /*min_width*/
      4096 && (l.min_width = /*min_width*/
      i[12]), r & /*height*/
      32768 && (l.height = typeof /*height*/
      i[15] == "number" ? (
        /*height*/
        i[15]
      ) : void 0), r & /*$$scope, label, value, show_label, root, proxy_url, columns, rows, height, preview, object_fit, allow_preview, show_share_button, show_download_button, gradio, selected_index, loading_status*/
      272622143 && (l.$$scope = { dirty: r, ctx: i }), t.$set(l);
    },
    i(i) {
      n || (dn(t.$$.fragment, i), n = !0);
    },
    o(i) {
      bn(t.$$.fragment, i), n = !1;
    },
    d(i) {
      _n(t, i);
    }
  };
}
function If(e, t, n) {
  let { loading_status: i } = t, { show_label: r } = t, { label: l } = t, { root: o } = t, { proxy_url: a } = t, { elem_id: s = "" } = t, { elem_classes: u = [] } = t, { visible: f = !0 } = t, { value: c = null } = t, { container: h = !0 } = t, { scale: _ = null } = t, { min_width: g = void 0 } = t, { columns: S = [2] } = t, { rows: v = void 0 } = t, { height: A = "auto" } = t, { preview: y } = t, { allow_preview: d = !0 } = t, { selected_index: T = null } = t, { object_fit: b = "cover" } = t, { show_share_button: I = !1 } = t, { show_download_button: M = !1 } = t, { gradio: U } = t;
  const O = kf();
  function V(p) {
    T = p, n(0, T);
  }
  const de = () => U.dispatch("change", c), Oe = (p) => U.dispatch("select", p.detail), q = (p) => U.dispatch("share", p.detail), z = (p) => U.dispatch("error", p.detail);
  return e.$$set = (p) => {
    "loading_status" in p && n(1, i = p.loading_status), "show_label" in p && n(2, r = p.show_label), "label" in p && n(3, l = p.label), "root" in p && n(4, o = p.root), "proxy_url" in p && n(5, a = p.proxy_url), "elem_id" in p && n(6, s = p.elem_id), "elem_classes" in p && n(7, u = p.elem_classes), "visible" in p && n(8, f = p.visible), "value" in p && n(9, c = p.value), "container" in p && n(10, h = p.container), "scale" in p && n(11, _ = p.scale), "min_width" in p && n(12, g = p.min_width), "columns" in p && n(13, S = p.columns), "rows" in p && n(14, v = p.rows), "height" in p && n(15, A = p.height), "preview" in p && n(16, y = p.preview), "allow_preview" in p && n(17, d = p.allow_preview), "selected_index" in p && n(0, T = p.selected_index), "object_fit" in p && n(18, b = p.object_fit), "show_share_button" in p && n(19, I = p.show_share_button), "show_download_button" in p && n(20, M = p.show_download_button), "gradio" in p && n(21, U = p.gradio);
  }, e.$$.update = () => {
    e.$$.dirty & /*selected_index*/
    1 && O("prop_change", { selected_index: T });
  }, [
    T,
    i,
    r,
    l,
    o,
    a,
    s,
    u,
    f,
    c,
    h,
    _,
    g,
    S,
    v,
    A,
    y,
    d,
    b,
    I,
    M,
    U,
    V,
    de,
    Oe,
    q,
    z
  ];
}
class Nf extends bf {
  constructor(t) {
    super(), Tf(this, t, If, Pf, Hf, {
      loading_status: 1,
      show_label: 2,
      label: 3,
      root: 4,
      proxy_url: 5,
      elem_id: 6,
      elem_classes: 7,
      visible: 8,
      value: 9,
      container: 10,
      scale: 11,
      min_width: 12,
      columns: 13,
      rows: 14,
      height: 15,
      preview: 16,
      allow_preview: 17,
      selected_index: 0,
      object_fit: 18,
      show_share_button: 19,
      show_download_button: 20,
      gradio: 21
    });
  }
}
export {
  Iu as BaseGallery,
  Nf as default
};
