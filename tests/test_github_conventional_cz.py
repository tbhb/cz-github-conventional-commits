from cz_github_conventional.github_conventional_cz import GitHubConventionalCz


def test_example(config):
    """Just testing a string is returned. not the content."""
    conventional_commits = GitHubConventionalCz(config)
    example = conventional_commits.example()
    assert isinstance(example, str)


def test_schema(config):
    """Just testing a string is returned. not the content."""
    conventional_commits = GitHubConventionalCz(config)
    schema = conventional_commits.schema()
    assert isinstance(schema, str)


def test_info(config):
    """Just testing a string is returned. not the content."""
    conventional_commits = GitHubConventionalCz(config)
    info = conventional_commits.info()
    assert isinstance(info, str)
