from json_schema_for_humans.generation_configuration import GenerationConfiguration


def test_default_values() -> None:
    """Test init GenerationConfiguration with default values"""
    config = GenerationConfiguration()
    assert config.markdown_options == {
        "break-on-newline": True,
        "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
        "tables": None,
    }
    assert config.template_md_options == {"badge_as_image": False}


def test_override_markdown_options() -> None:
    """Test init GenerationConfiguration with default values"""

    # override break-on-newline key
    config = GenerationConfiguration(
        markdown_options={
            "break-on-newline": False,
        }
    )
    assert config.markdown_options == {
        "break-on-newline": False,
        "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
        "tables": None,
    }
    # override fenced-code-blocks key
    config = GenerationConfiguration(
        markdown_options={
            "fenced-code-blocks": {"cssclass": "test"},
        }
    )
    assert config.markdown_options == {
        "break-on-newline": True,
        "fenced-code-blocks": {"cssclass": "test"},
        "tables": None,
    }
    # override tables key
    config = GenerationConfiguration(markdown_options={"tables": ["test"]})
    assert config.markdown_options == {
        "break-on-newline": True,
        "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
        "tables": ["test"],
    }

    # add a new key
    config = GenerationConfiguration(markdown_options={"newKey": "test"})
    assert config.markdown_options == {
        "break-on-newline": True,
        "fenced-code-blocks": {"cssclass": "highlight jumbotron"},
        "tables": None,
        "newKey": "test",
    }
