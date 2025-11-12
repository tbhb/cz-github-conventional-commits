from cz_github_conventional_commits import GitHubConventionalCommitsCz


def test_example(config):
    """Just testing a string is returned. not the content."""
    conventional_commits = GitHubConventionalCommitsCz(config)
    example = conventional_commits.example()
    assert isinstance(example, str)


def test_schema(config):
    """Just testing a string is returned. not the content."""
    conventional_commits = GitHubConventionalCommitsCz(config)
    schema = conventional_commits.schema()
    assert isinstance(schema, str)


def test_info(config):
    """Just testing a string is returned. not the content."""
    conventional_commits = GitHubConventionalCommitsCz(config)
    info = conventional_commits.info()
    assert isinstance(info, str)
