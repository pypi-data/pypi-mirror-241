#    Copyright 2018 - 2023 Aleksei Stepanov aka penguinolog.

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at

#         http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Package specific exceptions."""

from __future__ import annotations

import typing

from exec_helpers import proc_enums

from . import _log_templates

if typing.TYPE_CHECKING:
    from collections.abc import Iterable
    from collections.abc import Sequence

    from exec_helpers import exec_result  # pylint: disable=cyclic-import
    from exec_helpers.proc_enums import ExitCodeT

__all__ = (
    "ExecHelperError",
    "ExecHelperNoKillError",
    "ExecHelperTimeoutError",
    "ExecCalledProcessError",
    "CalledProcessError",
    "ParallelCallProcessError",
    "ParallelCallExceptionsError",
)


class ExecHelperError(Exception):
    """Base class for all exceptions raised inside."""

    __slots__ = ()


class DeserializeValueError(ExecHelperError, ValueError):
    """Deserialize impossible."""

    __slots__ = ()


class ExecCalledProcessError(ExecHelperError):
    """Base class for process call errors."""

    __slots__ = ()


class ExecHelperTimeoutProcessError(ExecCalledProcessError):
    """Timeout based errors."""

    __slots__ = ("result", "timeout")

    def __init__(
        self,
        message: str,
        *,
        result: exec_result.ExecResult,
        timeout: float,
    ) -> None:
        """Exception for error on process calls.

        :param message: exception message
        :type message: str
        :param result: execution result
        :type result: exec_result.ExecResult
        :param timeout: timeout for command
        :type timeout: int | float
        """
        super().__init__(message)
        self.result: exec_result.ExecResult = result
        self.timeout: int | float = timeout

    @property
    def cmd(self) -> str:
        """Failed command.

        :return: command
        """
        return self.result.cmd

    @property
    def stdout(self) -> str:
        """Command stdout.

        :return: command stdout as string
        """
        return self.result.stdout_str

    @property
    def stderr(self) -> str:
        """Command stderr.

        :return: command stderr as string
        """
        return self.result.stderr_str


class ExecHelperNoKillError(ExecHelperTimeoutProcessError):
    """Impossible to kill process.

    .. versionadded:: 3.4.0
    """

    __slots__ = ()

    def __init__(
        self,
        result: exec_result.ExecResult,
        timeout: float,
    ) -> None:
        """Exception for error on process calls.

        :param result: execution result
        :type result: exec_result.ExecResult
        :param timeout: timeout for command
        :type timeout: int | float
        """
        message: str = (
            f"Wait for {result.cmd!r} during {timeout!s}s: "
            f"no return code and no response on SIGTERM + SIGKILL signals!\n"
            f"\tSTDOUT:\n"
            f"{result.stdout_brief}\n"
            f"\tSTDERR:\n"
            f"{result.stderr_brief}"
        )
        super().__init__(message, result=result, timeout=timeout)


class ExecHelperTimeoutError(ExecHelperTimeoutProcessError):
    """Execution timeout.

    .. versionchanged:: 1.3.0 provide full result and timeout inside.
    .. versionchanged:: 1.3.0 subclass ExecCalledProcessError
    """

    __slots__ = ()

    def __init__(
        self,
        result: exec_result.ExecResult,
        timeout: float,
    ) -> None:
        """Exception for error on process calls.

        :param result: execution result
        :type result: exec_result.ExecResult
        :param timeout: timeout for command
        :type timeout: int | float
        """
        message: str = _log_templates.CMD_WAIT_ERROR.format(result=result, timeout=timeout)
        super().__init__(message, result=result, timeout=timeout)


class CalledProcessError(ExecCalledProcessError):
    """Exception for error on process calls."""

    __slots__ = ("result", "expected")

    def __init__(
        self,
        result: exec_result.ExecResult,
        expected: Iterable[ExitCodeT] = (proc_enums.EXPECTED,),
    ) -> None:
        """Exception for error on process calls.

        :param result: execution result
        :type result: exec_result.ExecResult
        :param expected: expected return codes
        :type expected: Iterable[int | proc_enums.ExitCodes]

        .. versionchanged:: 1.1.1 - provide full result
        .. versionchanged:: 3.4.0 Expected is not optional, defaults os dependent
        """
        self.result: exec_result.ExecResult = result
        self.expected: Sequence[ExitCodeT] = proc_enums.exit_codes_to_enums(expected)
        message: str = (
            f"Command {result.cmd!r} returned exit code {result.exit_code} while expected {expected}\n"
            f"\tSTDOUT:\n"
            f"{result.stdout_brief}\n"
            f"\tSTDERR:\n{result.stderr_brief}"
        )
        super().__init__(message)

    @property
    def returncode(self) -> ExitCodeT:
        """Command return code.

        :return: command return code
        """
        return self.result.exit_code

    @property
    def cmd(self) -> str:
        """Failed command.

        :return: command
        """
        return self.result.cmd

    @property
    def stdout(self) -> str:
        """Command stdout.

        :return: command stdout as string
        """
        return self.result.stdout_str

    @property
    def stderr(self) -> str:
        """Command stderr.

        :return: command stderr as string
        """
        return self.result.stderr_str


class ParallelCallProcessError(ExecCalledProcessError):
    """Exception during parallel execution."""

    __slots__ = ("cmd", "errors", "results", "expected")

    def __init__(
        self,
        command: str,
        errors: dict[tuple[str, int], exec_result.ExecResult],
        results: dict[tuple[str, int], exec_result.ExecResult],
        expected: Iterable[ExitCodeT] = (proc_enums.EXPECTED,),
        *,
        _message: str | None = None,
    ) -> None:
        """Exception during parallel execution.

        :param command: command
        :type command: str
        :param errors: results with errors
        :type errors: dict[tuple[str, int], ExecResult]
        :param results: all results
        :type results: dict[tuple[str, int], ExecResult]
        :param expected: expected return codes
        :type expected: Iterable[int | proc_enums.ExitCodes]
        :param _message: message override
        :type _message: str | None

        .. versionchanged:: 3.4.0 Expected is not optional, defaults os dependent
        """
        prep_expected: Sequence[ExitCodeT] = proc_enums.exit_codes_to_enums(expected)
        errors_str: str = "\n\t".join(f"{host}:{port} - {result.exit_code} " for (host, port), result in errors.items())
        message: str = _message or (
            f"Command {command!r} returned unexpected exit codes on several hosts\n"
            f"Expected: {prep_expected}\n"
            f"Got:\n"
            f"\t{errors_str}"
        )
        super().__init__(message)
        self.cmd: str = command
        self.errors: dict[tuple[str, int], exec_result.ExecResult] = errors
        self.results: dict[tuple[str, int], exec_result.ExecResult] = results
        self.expected: Sequence[ExitCodeT] = prep_expected


class ParallelCallExceptionsError(ParallelCallProcessError):
    """Exception raised during parallel call as result of exceptions."""

    __slots__ = ("cmd", "exceptions")

    def __init__(
        self,
        command: str,
        exceptions: dict[tuple[str, int], Exception],
        errors: dict[tuple[str, int], exec_result.ExecResult],
        results: dict[tuple[str, int], exec_result.ExecResult],
        expected: Iterable[ExitCodeT] = (proc_enums.EXPECTED,),
        *,
        _message: str | None = None,
    ) -> None:
        """Exception raised during parallel call as result of exceptions.

        :param command: command
        :type command: str
        :param exceptions: Exceptions on connections
        :type exceptions: dict[tuple[str, int], Exception]
        :param errors: results with errors
        :type errors: dict[tuple[str, int], ExecResult]
        :param results: all results
        :type results: dict[tuple[str, int], ExecResult]
        :param expected: expected return codes
        :type expected: Iterable[int | proc_enums.ExitCodes]
        :param _message: message override
        :type _message: str | None

        .. versionchanged:: 3.4.0 Expected is not optional, defaults os dependent
        """
        exceptions_str: str = "\n\t".join(
            f"{host}:{port} - {str(exc) or repr(exc)}" for (host, port), exc in exceptions.items()
        )
        message: str = _message or f"Command {command!r} during execution raised exceptions: \n\t{exceptions_str}"
        super().__init__(
            command=command,
            errors=errors,
            results=results,
            expected=expected,
            _message=message,
        )
        self.cmd: str = command
        self.exceptions: dict[tuple[str, int], Exception] = exceptions


class StopExecution(Exception):
    """Stop execution without waiting for exit code."""

    def __init__(
        self,
        trigger_line: bytes,
        result: exec_result.ExecResult,
        message: str = "StopExecution raised",
    ) -> None:
        self.__trigger_line = trigger_line
        self.__result = result
        super().__init__(message)

    @property
    def trigger_line(self) -> bytes:
        """Trigger line for exception.

        :return: original line triggered StopExecution as bytes
        :rtype: bytes
        """
        return self.__trigger_line

    @property
    def trigger_string(self) -> str:
        """Decoded trigger line for exception.

        :return: original line triggered StopExecution as str
        :rtype: str
        """
        return self.__trigger_line.decode("utf-8", errors="backslashreplace")

    @property
    def result(self) -> exec_result.ExecResult:
        """Execution result object.

        :return: execution result object
        :rtype: exec_result.ExecResult
        """
        return self.__result


class StopExecutionGraceful(StopExecution):
    """Stop execution without raising exception."""

    def __init__(
        self,
        trigger_line: bytes,
        result: exec_result.ExecResult,
    ) -> None:
        super().__init__(
            trigger_line=trigger_line,
            result=result,
            message="Graceful early stop of execution.",
        )


class StopExecutionError(StopExecution, ExecHelperError):
    """Stop execution and raise exception."""

    def __init__(
        self,
        trigger_line: bytes,
        result: exec_result.ExecResult,
    ) -> None:
        super().__init__(
            trigger_line=trigger_line,
            result=result,
            message="Unexpected command output caused stop of execution.",
        )
