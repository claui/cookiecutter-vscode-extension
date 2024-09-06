"""API to query selected configuration items and state from Git."""


import logging
import subprocess
from typing import Optional


logger = logging.getLogger(__name__)


class UnexpectedGitState(Exception):
    """User-facing error for unexpected Git configurations or states."""


def _git_query(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        capture_output=True,
        check=True,
        text=True
    ).stdout.rstrip()


def _git_commit_hash() -> str:
    try:
        return _git_query("rev-parse", "-q", "@")
    except subprocess.SubprocessError as err:
        raise UnexpectedGitState(
            "Unable to determine commit hash for HEAD"
        ) from err


def _git_current_branch() -> str:
    try:
        return _git_query("symbolic-ref", "--short", "HEAD")
    except subprocess.SubprocessError as err:
        raise UnexpectedGitState(
            "Unable to determine current branch"
        ) from err


def _git_current_remote() -> str:
    branch = _git_current_branch()
    try:
        return _git_query("config", f"branch.{branch}.remote")
    except subprocess.SubprocessError as err:
        raise UnexpectedGitState(
            f"Unable to determine remote for branch `{branch}`"
        ) from err


def _git_current_remote_url() -> str:
    try:
        remote = _git_current_remote()
    except UnexpectedGitState as err:
        logger.warning(err)
        remote = 'origin'
    try:
        return _git_query("config", f"remote.{remote}.url")
    except subprocess.SubprocessError as err:
        raise UnexpectedGitState(
            f"Unable to determine URL for remote `{remote}`"
        ) from err


def commit_hash() -> Optional[str]:
    """Commit SHA of current HEAD."""
    try:
        return _git_commit_hash()
    except UnexpectedGitState as err:
        logger.warning(err)
        return None


def current_remote_url() -> Optional[str]:
    """URL of the Git remote tracked by the current branch."""
    try:
        return _git_current_remote_url()
    except UnexpectedGitState as err:
        logger.warning(err)
        return None
