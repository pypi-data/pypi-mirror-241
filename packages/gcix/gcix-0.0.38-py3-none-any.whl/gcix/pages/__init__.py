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

from .. import Job as _Job_20682b42
from ..python import (
    PipInstallRequirementsProps as _PipInstallRequirementsProps_47c04e0d
)


@jsii.interface(jsii_type="@gcix/gcix.pages.IPagesAsciiDoctor")
class IPagesAsciiDoctor(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="outFile")
    def out_file(self) -> builtins.str:
        '''Output HTML file.'''
        ...

    @out_file.setter
    def out_file(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        '''Source .adoc files to translate to HTML files.'''
        ...

    @source.setter
    def source(self, value: builtins.str) -> None:
        ...


class _IPagesAsciiDoctorProxy:
    __jsii_type__: typing.ClassVar[str] = "@gcix/gcix.pages.IPagesAsciiDoctor"

    @builtins.property
    @jsii.member(jsii_name="outFile")
    def out_file(self) -> builtins.str:
        '''Output HTML file.'''
        return typing.cast(builtins.str, jsii.get(self, "outFile"))

    @out_file.setter
    def out_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bdd2ac5e1df7128c8e63e71dd62d5e92f65420d3d8182e2db0f8923aa4f122b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outFile", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        '''Source .adoc files to translate to HTML files.'''
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed75dded0af3a29623dcc0d2ee60fb7e0acde4e210845a7992997f431a1cb6c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPagesAsciiDoctor).__jsii_proxy_class__ = lambda : _IPagesAsciiDoctorProxy


@jsii.interface(jsii_type="@gcix/gcix.pages.IPagesPdoc3")
class IPagesPdoc3(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="module")
    def module(self) -> builtins.str:
        '''The Python module name.

        This may be an import path resolvable in the
        current environment, or a file path to a Python module or package.
        '''
        ...

    @module.setter
    def module(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="outputPath")
    def output_path(self) -> builtins.str:
        '''A sub path of the Gitlab Pages ``public`` directory to output generated HTML/markdown files to.

        Defaults to "/".
        '''
        ...

    @output_path.setter
    def output_path(self, value: builtins.str) -> None:
        ...


class _IPagesPdoc3Proxy:
    __jsii_type__: typing.ClassVar[str] = "@gcix/gcix.pages.IPagesPdoc3"

    @builtins.property
    @jsii.member(jsii_name="module")
    def module(self) -> builtins.str:
        '''The Python module name.

        This may be an import path resolvable in the
        current environment, or a file path to a Python module or package.
        '''
        return typing.cast(builtins.str, jsii.get(self, "module"))

    @module.setter
    def module(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3505d679978f6760c611b7ed3ead4ff670fc4c5f5edb38e1051949322cb65ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "module", value)

    @builtins.property
    @jsii.member(jsii_name="outputPath")
    def output_path(self) -> builtins.str:
        '''A sub path of the Gitlab Pages ``public`` directory to output generated HTML/markdown files to.

        Defaults to "/".
        '''
        return typing.cast(builtins.str, jsii.get(self, "outputPath"))

    @output_path.setter
    def output_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd380ff7c01095010a580b362acd3af19eede719cc96995729ba419cc4fe4936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputPath", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPagesPdoc3).__jsii_proxy_class__ = lambda : _IPagesPdoc3Proxy


@jsii.interface(jsii_type="@gcix/gcix.pages.IPagesSphinx")
class IPagesSphinx(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="pip")
    def pip(self) -> typing.Optional[_PipInstallRequirementsProps_47c04e0d]:
        ...

    @pip.setter
    def pip(
        self,
        value: typing.Optional[_PipInstallRequirementsProps_47c04e0d],
    ) -> None:
        ...


class _IPagesSphinxProxy:
    __jsii_type__: typing.ClassVar[str] = "@gcix/gcix.pages.IPagesSphinx"

    @builtins.property
    @jsii.member(jsii_name="pip")
    def pip(self) -> typing.Optional[_PipInstallRequirementsProps_47c04e0d]:
        return typing.cast(typing.Optional[_PipInstallRequirementsProps_47c04e0d], jsii.get(self, "pip"))

    @pip.setter
    def pip(
        self,
        value: typing.Optional[_PipInstallRequirementsProps_47c04e0d],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c66e9c80f1f61d104bb8ce4d6a13387c29e288a8674ddb8613fd9a6f72674fd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pip", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPagesSphinx).__jsii_proxy_class__ = lambda : _IPagesSphinxProxy


@jsii.implements(IPagesAsciiDoctor)
class PagesAsciiDoctor(
    _Job_20682b42,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gcix/gcix.pages.PagesAsciiDoctor",
):
    '''Translate the AsciiDoc source FILE as Gitlab Pages HTML5 file.

    Runs ``asciidoctor {source} -o public{out_file}``and stores the output
    as artifact under the ``public`` directory.

    This subclass of ``Job`` will configure following defaults for the superclass:

    - name: asciidoctor-pages
    - stage: build
    - image: ruby:3-alpine
    - artifacts: Path 'public'
    '''

    def __init__(
        self,
        *,
        out_file: builtins.str,
        source: builtins.str,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param out_file: Output HTML file.
        :param source: Source .adoc files to translate to HTML files.
        :param job_name: The name of the job.
        :param job_stage: The stage of the job.
        '''
        props = PagesAsciiDoctorProps(
            out_file=out_file, source=source, job_name=job_name, job_stage=job_stage
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Returns a representation of any object which implements ``IBase``.

        The rendered representation is used by the ``gcix`` to dump it
        in YAML format as part of the ``.gitlab-ci.yml`` pipeline.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="outFile")
    def out_file(self) -> builtins.str:
        '''Output HTML file.'''
        return typing.cast(builtins.str, jsii.get(self, "outFile"))

    @out_file.setter
    def out_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a2fb5b71b3966b3915f6c900561f642e0a143b7ff417f0a892f3d0e1cb8d423)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outFile", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        '''Source .adoc files to translate to HTML files.'''
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70cd779035214acd8df00cf178ff1567cb093b0e6548fff5a09ebdad50f0185a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)


@jsii.data_type(
    jsii_type="@gcix/gcix.pages.PagesAsciiDoctorProps",
    jsii_struct_bases=[],
    name_mapping={
        "out_file": "outFile",
        "source": "source",
        "job_name": "jobName",
        "job_stage": "jobStage",
    },
)
class PagesAsciiDoctorProps:
    def __init__(
        self,
        *,
        out_file: builtins.str,
        source: builtins.str,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param out_file: Output HTML file.
        :param source: Source .adoc files to translate to HTML files.
        :param job_name: The name of the job.
        :param job_stage: The stage of the job.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__157160701f2290d8c0d363e4b41168e6a8876003e119cf1b7dfd7a5728d877b9)
            check_type(argname="argument out_file", value=out_file, expected_type=type_hints["out_file"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument job_stage", value=job_stage, expected_type=type_hints["job_stage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "out_file": out_file,
            "source": source,
        }
        if job_name is not None:
            self._values["job_name"] = job_name
        if job_stage is not None:
            self._values["job_stage"] = job_stage

    @builtins.property
    def out_file(self) -> builtins.str:
        '''Output HTML file.'''
        result = self._values.get("out_file")
        assert result is not None, "Required property 'out_file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Source .adoc files to translate to HTML files.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job.'''
        result = self._values.get("job_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''The stage of the job.'''
        result = self._values.get("job_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesAsciiDoctorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPagesPdoc3)
class PagesPdoc3(
    _Job_20682b42,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gcix/gcix.pages.PagesPdoc3",
):
    '''Generate a HTML API documentation of you python code as Gitlab Pages.

    Runs ``pdoc3 --html -f --skip-errors --output-dir public{path} {module}`` and stores the output
    as artifact under the ``public`` directory.

    This subclass of ``Job`` will configure following defaults for the superclass:

    - name: pdoc3-pages
    - stage: build
    - artifacts: Path 'public'
    '''

    def __init__(
        self,
        *,
        module: builtins.str,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param module: The Python module name. This may be an import path resolvable in the current environment, or a file path to a Python module or package.
        :param job_name: The name of the job.
        :param job_stage: The stage of the job.
        :param output_path: A sub path of the Gitlab Pages ``public`` directory to output generated HTML/markdown files to. Defaults to "/".
        '''
        props = PagesPdoc3Props(
            module=module,
            job_name=job_name,
            job_stage=job_stage,
            output_path=output_path,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Returns a representation of any object which implements ``IBase``.

        The rendered representation is used by the ``gcix`` to dump it
        in YAML format as part of the ``.gitlab-ci.yml`` pipeline.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="module")
    def module(self) -> builtins.str:
        '''The Python module name.

        This may be an import path resolvable in the
        current environment, or a file path to a Python module or package.
        '''
        return typing.cast(builtins.str, jsii.get(self, "module"))

    @module.setter
    def module(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74494a21f94ad0f9b6e4e3697a7c7c71242bb8d0a1967526cd8b4701e5f61291)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "module", value)

    @builtins.property
    @jsii.member(jsii_name="outputPath")
    def output_path(self) -> builtins.str:
        '''A sub path of the Gitlab Pages ``public`` directory to output generated HTML/markdown files to.

        Defaults to "/".
        '''
        return typing.cast(builtins.str, jsii.get(self, "outputPath"))

    @output_path.setter
    def output_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b33dce8bca7d61db45d5887003dfdb8049fdeac1bac75c9b9d61c0b7c1a33a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputPath", value)


@jsii.data_type(
    jsii_type="@gcix/gcix.pages.PagesPdoc3Props",
    jsii_struct_bases=[],
    name_mapping={
        "module": "module",
        "job_name": "jobName",
        "job_stage": "jobStage",
        "output_path": "outputPath",
    },
)
class PagesPdoc3Props:
    def __init__(
        self,
        *,
        module: builtins.str,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
        output_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param module: The Python module name. This may be an import path resolvable in the current environment, or a file path to a Python module or package.
        :param job_name: The name of the job.
        :param job_stage: The stage of the job.
        :param output_path: A sub path of the Gitlab Pages ``public`` directory to output generated HTML/markdown files to. Defaults to "/".
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2946a74e0efc43a5b40fa6ebbe3c4fec8dd6ab12c5053e5777aedf47b2b92e3e)
            check_type(argname="argument module", value=module, expected_type=type_hints["module"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument job_stage", value=job_stage, expected_type=type_hints["job_stage"])
            check_type(argname="argument output_path", value=output_path, expected_type=type_hints["output_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "module": module,
        }
        if job_name is not None:
            self._values["job_name"] = job_name
        if job_stage is not None:
            self._values["job_stage"] = job_stage
        if output_path is not None:
            self._values["output_path"] = output_path

    @builtins.property
    def module(self) -> builtins.str:
        '''The Python module name.

        This may be an import path resolvable in the
        current environment, or a file path to a Python module or package.
        '''
        result = self._values.get("module")
        assert result is not None, "Required property 'module' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job.'''
        result = self._values.get("job_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''The stage of the job.'''
        result = self._values.get("job_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_path(self) -> typing.Optional[builtins.str]:
        '''A sub path of the Gitlab Pages ``public`` directory to output generated HTML/markdown files to.

        Defaults to "/".
        '''
        result = self._values.get("output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesPdoc3Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPagesSphinx)
class PagesSphinx(
    _Job_20682b42,
    metaclass=jsii.JSIIMeta,
    jsii_type="@gcix/gcix.pages.PagesSphinx",
):
    '''Runs ``sphinx-build -b html -E -a docs public/${CI_COMMIT_REF_NAME}`` and installs project requirements. Uses: (``PythonScripts.PipInstallRequirements()``).

    - Requires a ``docs/requirements.txt`` in your project folder``containing at least``sphinx`
    - Creates artifacts for Gitlab Pages under ``pages``

    This subclass of ``Job`` will configure following defaults for the superclass:

    - name: sphinx-pages
    - stage: build
    - artifacts: Path 'public'
    '''

    def __init__(
        self,
        *,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
        pip: typing.Optional[typing.Union[_PipInstallRequirementsProps_47c04e0d, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param job_name: The name of the job.
        :param job_stage: The stage of the job.
        :param pip: 
        '''
        props = PagesSphinxProps(job_name=job_name, job_stage=job_stage, pip=pip)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="render")
    def render(self) -> typing.Any:
        '''Returns a representation of any object which implements ``IBase``.

        The rendered representation is used by the ``gcix`` to dump it
        in YAML format as part of the ``.gitlab-ci.yml`` pipeline.
        '''
        return typing.cast(typing.Any, jsii.invoke(self, "render", []))

    @builtins.property
    @jsii.member(jsii_name="pip")
    def pip(self) -> typing.Optional[_PipInstallRequirementsProps_47c04e0d]:
        return typing.cast(typing.Optional[_PipInstallRequirementsProps_47c04e0d], jsii.get(self, "pip"))

    @pip.setter
    def pip(
        self,
        value: typing.Optional[_PipInstallRequirementsProps_47c04e0d],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ccdc116062912b4dff5643a2dd8b0c8405184ef0f6b6712015a14757c0bb745)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pip", value)


@jsii.data_type(
    jsii_type="@gcix/gcix.pages.PagesSphinxProps",
    jsii_struct_bases=[],
    name_mapping={"job_name": "jobName", "job_stage": "jobStage", "pip": "pip"},
)
class PagesSphinxProps:
    def __init__(
        self,
        *,
        job_name: typing.Optional[builtins.str] = None,
        job_stage: typing.Optional[builtins.str] = None,
        pip: typing.Optional[typing.Union[_PipInstallRequirementsProps_47c04e0d, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param job_name: The name of the job.
        :param job_stage: The stage of the job.
        :param pip: 
        '''
        if isinstance(pip, dict):
            pip = _PipInstallRequirementsProps_47c04e0d(**pip)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__927b4345e38c4b17bbe35420cef38970ea40ccae04a460ef08a06f727b0d2376)
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument job_stage", value=job_stage, expected_type=type_hints["job_stage"])
            check_type(argname="argument pip", value=pip, expected_type=type_hints["pip"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if job_name is not None:
            self._values["job_name"] = job_name
        if job_stage is not None:
            self._values["job_stage"] = job_stage
        if pip is not None:
            self._values["pip"] = pip

    @builtins.property
    def job_name(self) -> typing.Optional[builtins.str]:
        '''The name of the job.'''
        result = self._values.get("job_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_stage(self) -> typing.Optional[builtins.str]:
        '''The stage of the job.'''
        result = self._values.get("job_stage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pip(self) -> typing.Optional[_PipInstallRequirementsProps_47c04e0d]:
        result = self._values.get("pip")
        return typing.cast(typing.Optional[_PipInstallRequirementsProps_47c04e0d], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PagesSphinxProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IPagesAsciiDoctor",
    "IPagesPdoc3",
    "IPagesSphinx",
    "PagesAsciiDoctor",
    "PagesAsciiDoctorProps",
    "PagesPdoc3",
    "PagesPdoc3Props",
    "PagesSphinx",
    "PagesSphinxProps",
]

publication.publish()

def _typecheckingstub__9bdd2ac5e1df7128c8e63e71dd62d5e92f65420d3d8182e2db0f8923aa4f122b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed75dded0af3a29623dcc0d2ee60fb7e0acde4e210845a7992997f431a1cb6c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3505d679978f6760c611b7ed3ead4ff670fc4c5f5edb38e1051949322cb65ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd380ff7c01095010a580b362acd3af19eede719cc96995729ba419cc4fe4936(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c66e9c80f1f61d104bb8ce4d6a13387c29e288a8674ddb8613fd9a6f72674fd7(
    value: typing.Optional[_PipInstallRequirementsProps_47c04e0d],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a2fb5b71b3966b3915f6c900561f642e0a143b7ff417f0a892f3d0e1cb8d423(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70cd779035214acd8df00cf178ff1567cb093b0e6548fff5a09ebdad50f0185a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__157160701f2290d8c0d363e4b41168e6a8876003e119cf1b7dfd7a5728d877b9(
    *,
    out_file: builtins.str,
    source: builtins.str,
    job_name: typing.Optional[builtins.str] = None,
    job_stage: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74494a21f94ad0f9b6e4e3697a7c7c71242bb8d0a1967526cd8b4701e5f61291(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b33dce8bca7d61db45d5887003dfdb8049fdeac1bac75c9b9d61c0b7c1a33a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2946a74e0efc43a5b40fa6ebbe3c4fec8dd6ab12c5053e5777aedf47b2b92e3e(
    *,
    module: builtins.str,
    job_name: typing.Optional[builtins.str] = None,
    job_stage: typing.Optional[builtins.str] = None,
    output_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ccdc116062912b4dff5643a2dd8b0c8405184ef0f6b6712015a14757c0bb745(
    value: typing.Optional[_PipInstallRequirementsProps_47c04e0d],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__927b4345e38c4b17bbe35420cef38970ea40ccae04a460ef08a06f727b0d2376(
    *,
    job_name: typing.Optional[builtins.str] = None,
    job_stage: typing.Optional[builtins.str] = None,
    pip: typing.Optional[typing.Union[_PipInstallRequirementsProps_47c04e0d, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
