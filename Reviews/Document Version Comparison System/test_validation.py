from document_version_comparison_tool import normalize_text, compare_documents


def test_normalize_text():
    assert normalize_text("  Hello World!  ") == "hello world!"
    assert normalize_text("\nNew Line\n") == "new line"


def test_compare_documents():
    doc_a = "Hello World"
    doc_b = "Hello there World"
    changes = compare_documents(doc_a, doc_b)

    assert 'there' in changes['added']
    assert len(changes['removed']) == 0

    doc_c = "Goodbye World"
    changes = compare_documents(doc_a, doc_c)

    assert 'goodbye' in changes['added']
    assert 'hello' in changes['removed']
