import warnings
from collections import OrderedDict

import pytest

import h


def test_empty_tag():
    assert str(h.tag("b")) == "<b></b>"


def test_void_tag():
    assert str(h.tag("hr")) == "<hr>"


def test_tag_with_children_cant_have_reassigned():
    with pytest.raises(ValueError) as excinfo:
        h.tag("b")["Hi"]["Hi again"]
    assert "Cannot reassign children" in str(excinfo.value)


def test_void_tag_cant_have_children():
    with pytest.raises(ValueError) as excinfo:
        h.tag("hr")["Hi"]
    assert "Void tag <hr> cannot have children" in str(excinfo.value)


def test_shortcut_tag():
    assert str(h.b()) == "<b></b>"


def test_shortcut_void_tag():
    assert str(h.hr()) == "<hr>"


def test_shortcut_tag_del():
    assert str(h.del_()) == "<del></del>"


def test_shortcut_tag_input():
    assert str(h.input_()) == "<input>"


def test_shortcut_tag_map():
    assert str(h.map_()) == "<map></map>"


def test_shortcut_tag_object():
    assert str(h.object_()) == "<object></object>"


def test_tag_with_text_child():
    assert str(h.tag("b")["Hi"]) == "<b>Hi</b>"


def test_tag_with_integer_child():
    assert str(h.tag("b")[1]) == "<b>1</b>"


def test_multiple_children():
    assert (
        str(h.ul()[h.li()["Item 1"], h.li()["Item 2"]])
        == "<ul><li>Item 1</li><li>Item 2</li></ul>"
    )


def test_tag_child_None_ignored():
    assert str(h.b()[None]) == "<b></b>"


def test_tag_class_child_direct():
    assert str(h.b["Hi"]) == "<b>Hi</b>"


def test_attribute():
    assert str(h.a(href="https://example.com")) == '<a href="https://example.com"></a>'


def test_attribute_id():
    assert str(h.h1(id="myheading")) == '<h1 id="myheading"></h1>'


def test_attribute_class():
    assert str(h.b(class_="mybold")) == '<b class="mybold"></b>'


def test_attribute_list():
    assert str(h.b(class_=["foo", "bar"])) == '<b class="foo bar"></b>'


def test_attribute_empty_string():
    assert str(h.a(href="")) == '<a href=""></a>'


def test_attribute_bool_true():
    assert (
        str(h.input_(type="checkbox", checked=True))
        == '<input type="checkbox" checked>'
    )


def test_attribute_bool_false():
    assert str(h.input_(type="checkbox", checked=False)) == '<input type="checkbox">'


def test_attribute_bool_false_solo():
    assert str(h.input_(disabled=False)) == "<input>"


def test_attribute_style_dict():
    assert str(h.b(style={"color": "red"})) == '<b style="color: red"></b>'


def test_attribute_style_ordered_dict():
    assert (
        str(h.b(style=OrderedDict([("color", "red"), ("font-weight", "bold")])))
        == '<b style="color: red; font-weight: bold"></b>'
    )


def test_attribute_and_child():
    assert str(h.b(id="foo")["Hi"]) == '<b id="foo">Hi</b>'


def test_void_tag_attribute():
    assert str(h.hr(id="foo")) == '<hr id="foo">'


def test_nested():
    assert str(h.b()[h.i()["Hi"]]) == "<b><i>Hi</i></b>"


def test_doctype():
    assert str(h.doctype()) == "<!DOCTYPE html>"


def test_doctype_child():
    assert str(h.doctype()[h.html()]) == "<!DOCTYPE html><html></html>"


def test_text():
    assert (
        str(h.text("<script>alert(1)</script>"))
        == "&lt;script&gt;alert(1)&lt;/script&gt;"
    )


def test_unsafe_raw_text():
    assert (
        str(h.unsafe_raw_text("<script>alert(1)</script>"))
        == "<script>alert(1)</script>"
    )


def test_comment():
    assert str(h.comment("Hello world")) == "<!--Hello world-->"


def test_comment_double_dash():
    assert str(h.comment("foo--bar")) == "<!--foo- -bar-->"


def test_comment_trailing_dash():
    assert str(h.comment("foo-")) == "<!--foo- -->"


def test_comment_with_html():
    # HTML comments don't require escaping of < and >
    assert str(h.comment("<script>alert(1)</script>")) == "<!--<script>alert(1)</script>-->"


# Tests for __repr__
def test_repr_empty_tag():
    assert repr(h.div()) == "div()"


def test_repr_tag_with_attrs():
    assert repr(h.div(id_="foo", class_="bar")) == "div(id='foo', class='bar')"


def test_repr_tag_with_children():
    assert repr(h.div()["content"]) == "div()[1 children]"


def test_repr_tag_with_attrs_and_children():
    assert repr(h.div(id_="foo")["content"]) == "div(id='foo')[1 children]"


# Parametrized tests for all HTML5 tags
# Regular (non-void) tags
REGULAR_TAGS = [
    ("a", h.a),
    ("abbr", h.abbr),
    ("address", h.address),
    ("article", h.article),
    ("aside", h.aside),
    ("audio", h.audio),
    ("b", h.b),
    ("bdi", h.bdi),
    ("bdo", h.bdo),
    ("blockquote", h.blockquote),
    ("body", h.body),
    ("button", h.button),
    ("canvas", h.canvas),
    ("caption", h.caption),
    ("cite", h.cite),
    ("code", h.code),
    ("colgroup", h.colgroup),
    ("data", h.data),
    ("datalist", h.datalist),
    ("dd", h.dd),
    ("del", h.del_),
    ("details", h.details),
    ("dfn", h.dfn),
    ("dialog", h.dialog),
    ("div", h.div),
    ("dl", h.dl),
    ("dt", h.dt),
    ("em", h.em),
    ("fencedframe", h.fencedframe),
    ("fieldset", h.fieldset),
    ("figcaption", h.figcaption),
    ("figure", h.figure),
    ("footer", h.footer),
    ("form", h.form),
    ("h1", h.h1),
    ("h2", h.h2),
    ("h3", h.h3),
    ("h4", h.h4),
    ("h5", h.h5),
    ("h6", h.h6),
    ("head", h.head),
    ("header", h.header),
    ("hgroup", h.hgroup),
    ("html", h.html),
    ("i", h.i),
    ("iframe", h.iframe),
    ("ins", h.ins),
    ("kbd", h.kbd),
    ("label", h.label),
    ("legend", h.legend),
    ("li", h.li),
    ("main", h.main),
    ("map", h.map_),
    ("mark", h.mark),
    ("menu", h.menu),
    ("meter", h.meter),
    ("nav", h.nav),
    ("noscript", h.noscript),
    ("object", h.object_),
    ("ol", h.ol),
    ("optgroup", h.optgroup),
    ("option", h.option),
    ("output", h.output),
    ("p", h.p),
    ("picture", h.picture),
    ("pre", h.pre),
    ("progress", h.progress),
    ("q", h.q),
    ("rp", h.rp),
    ("rt", h.rt),
    ("ruby", h.ruby),
    ("s", h.s),
    ("samp", h.samp),
    ("script", h.script),
    ("search", h.search),
    ("section", h.section),
    ("select", h.select),
    ("selectedcontent", h.selectedcontent),
    ("slot", h.slot),
    ("small", h.small),
    ("span", h.span),
    ("strong", h.strong),
    ("style", h.style),
    ("sub", h.sub),
    ("summary", h.summary),
    ("sup", h.sup),
    ("table", h.table),
    ("tbody", h.tbody),
    ("td", h.td),
    ("template", h.template),
    ("textarea", h.textarea),
    ("tfoot", h.tfoot),
    ("th", h.th),
    ("thead", h.thead),
    ("time", h.time),
    ("title", h.title),
    ("tr", h.tr),
    ("u", h.u),
    ("ul", h.ul),
    ("var", h.var),
    ("video", h.video),
]

# Void tags (self-closing, no children allowed)
VOID_TAGS = [
    ("area", h.area),
    ("base", h.base),
    ("br", h.br),
    ("col", h.col),
    ("embed", h.embed),
    ("hr", h.hr),
    ("img", h.img),
    ("input", h.input_),
    ("link", h.link),
    ("meta", h.meta),
    ("source", h.source),
    ("track", h.track),
    ("wbr", h.wbr),
]

# Deprecated tags (emit DeprecationWarning)
DEPRECATED_TAGS = [
    ("acronym", h.acronym),
    ("big", h.big),
    ("center", h.center),
    ("dir", h.dir_),
    ("font", h.font),
    ("frame", h.frame),
    ("frameset", h.frameset),
    ("marquee", h.marquee),
    ("nobr", h.nobr),
    ("noembed", h.noembed),
    ("noframes", h.noframes),
    ("plaintext", h.plaintext),
    ("rb", h.rb),
    ("rtc", h.rtc),
    ("strike", h.strike),
    ("tt", h.tt),
    ("xmp", h.xmp),
]

# Deprecated void tags
DEPRECATED_VOID_TAGS = [
    ("param", h.param),
]


@pytest.mark.parametrize("tag_name,tag_class", REGULAR_TAGS)
def test_regular_tag_renders(tag_name, tag_class):
    """Test that regular tags render with opening and closing tags."""
    assert str(tag_class()) == f"<{tag_name}></{tag_name}>"


@pytest.mark.parametrize("tag_name,tag_class", REGULAR_TAGS)
def test_regular_tag_with_child(tag_name, tag_class):
    """Test that regular tags can have children."""
    assert str(tag_class()["content"]) == f"<{tag_name}>content</{tag_name}>"


@pytest.mark.parametrize("tag_name,tag_class", REGULAR_TAGS)
def test_regular_tag_with_attribute(tag_name, tag_class):
    """Test that regular tags can have attributes."""
    assert str(tag_class(id_="test")) == f'<{tag_name} id="test"></{tag_name}>'


@pytest.mark.parametrize("tag_name,tag_class", REGULAR_TAGS)
def test_regular_tag_class_getitem(tag_name, tag_class):
    """Test that regular tags support class[children] syntax."""
    assert str(tag_class["content"]) == f"<{tag_name}>content</{tag_name}>"


@pytest.mark.parametrize("tag_name,tag_class", VOID_TAGS)
def test_void_tag_renders(tag_name, tag_class):
    """Test that void tags render without closing tag."""
    assert str(tag_class()) == f"<{tag_name}>"


@pytest.mark.parametrize("tag_name,tag_class", VOID_TAGS)
def test_void_tag_with_attribute(tag_name, tag_class):
    """Test that void tags can have attributes."""
    assert str(tag_class(id_="test")) == f'<{tag_name} id="test">'


@pytest.mark.parametrize("tag_name,tag_class", VOID_TAGS)
def test_void_tag_rejects_children(tag_name, tag_class):
    """Test that void tags raise an error when given children."""
    with pytest.raises(ValueError) as excinfo:
        tag_class()["content"]
    assert f"Void tag <{tag_name}> cannot have children" in str(excinfo.value)


# Tests for deprecated tags
@pytest.mark.parametrize("tag_name,tag_class", DEPRECATED_TAGS)
def test_deprecated_tag_emits_warning(tag_name, tag_class):
    """Test that deprecated tags emit a DeprecationWarning."""
    with pytest.warns(DeprecationWarning, match=f"The <{tag_name}> tag is deprecated"):
        tag_class()


@pytest.mark.parametrize("tag_name,tag_class", DEPRECATED_TAGS)
def test_deprecated_tag_renders(tag_name, tag_class):
    """Test that deprecated tags still render correctly."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert str(tag_class()) == f"<{tag_name}></{tag_name}>"


@pytest.mark.parametrize("tag_name,tag_class", DEPRECATED_TAGS)
def test_deprecated_tag_with_child(tag_name, tag_class):
    """Test that deprecated tags can have children."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert str(tag_class()["content"]) == f"<{tag_name}>content</{tag_name}>"


@pytest.mark.parametrize("tag_name,tag_class", DEPRECATED_TAGS)
def test_deprecated_tag_with_attribute(tag_name, tag_class):
    """Test that deprecated tags can have attributes."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert str(tag_class(id_="test")) == f'<{tag_name} id="test"></{tag_name}>'


# Tests for deprecated void tags
@pytest.mark.parametrize("tag_name,tag_class", DEPRECATED_VOID_TAGS)
def test_deprecated_void_tag_emits_warning(tag_name, tag_class):
    """Test that deprecated void tags emit a DeprecationWarning."""
    with pytest.warns(DeprecationWarning, match=f"The <{tag_name}> tag is deprecated"):
        tag_class()


@pytest.mark.parametrize("tag_name,tag_class", DEPRECATED_VOID_TAGS)
def test_deprecated_void_tag_renders(tag_name, tag_class):
    """Test that deprecated void tags still render correctly."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert str(tag_class()) == f"<{tag_name}>"


@pytest.mark.parametrize("tag_name,tag_class", DEPRECATED_VOID_TAGS)
def test_deprecated_void_tag_rejects_children(tag_name, tag_class):
    """Test that deprecated void tags raise an error when given children."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        with pytest.raises(ValueError) as excinfo:
            tag_class()["content"]
        assert f"Void tag <{tag_name}> cannot have children" in str(excinfo.value)
