import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *


class GitlabScripts(
    metaclass=jsii.JSIIMeta,
    jsii_type="@gcix/gcix.gitlab.GitlabScripts",
):
    '''GitlabScripts Class Documentation.

    The ``GitlabScripts`` class provides utility methods for performing various Git-related actions in the context of GitLab.
    '''

    @jsii.member(jsii_name="cloneRepository")
    @builtins.classmethod
    def clone_repository(
        cls,
        path: builtins.str,
        branch: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Clones a repository from a remote Git server using the Git command.

        :param path: - The path of the repository to clone. Should start with a forward slash ("/").
        :param branch: - (Optional) The branch name to clone from the remote repository. Currently, only "main" is supported.

        :return: A Git clone command as a string with the provided branch and repository path.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd5b76126699d26330d7dfeb3122212a724ea05dd5a006bbd12e60b24819200)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "cloneRepository", [path, branch]))


__all__ = [
    "GitlabScripts",
]

publication.publish()

def _typecheckingstub__2bd5b76126699d26330d7dfeb3122212a724ea05dd5a006bbd12e60b24819200(
    path: builtins.str,
    branch: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
