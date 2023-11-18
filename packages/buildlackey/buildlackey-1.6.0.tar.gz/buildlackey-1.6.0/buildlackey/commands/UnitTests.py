
from logging import Logger
from logging import getLogger

from os import sep as osSep
from os import environ as osEnvironment

from warnings import filterwarnings

from enum import Enum

from unittest import TestLoader
from unittest import TestResult
from unittest import TestSuite
from unittest import TextTestRunner

from HtmlTestRunner import HTMLTestRunner
from click import secho

from buildlackey.Environment import Environment
from buildlackey.PythonWarnings import PythonWarnings

from buildlackey.commands.UnitTestVerbosity import UnitTestVerbosity


class ExecutionStatus(Enum):
    ALL_TESTS_PASSED  = 0
    SOME_TESTS_FAILED = 1


class UnitTests(Environment):

    HTML_REPORT_DIRECTORY_NAME: str = 'html_unit_test_reports'
    ENV_VAR_PYTHON_PATH:        str = 'PYTHONPATH'

    def __init__(self, warning: PythonWarnings, verbosity: UnitTestVerbosity, pattern: str, html: bool, reportName: str, sourceSubDirectory: str):
        """

        Args:
            warning:
            verbosity:
            pattern:
            html:
            reportName:
            sourceSubDirectory
        """

        super().__init__()
        self.logger: Logger = getLogger(__name__)

        self._pattern:         str  = pattern
        self._html:            bool = html

        self._executionStatus:    ExecutionStatus   = ExecutionStatus.ALL_TESTS_PASSED
        self._verbosity:          UnitTestVerbosity = verbosity
        self._reportName:         str               = reportName
        self._sourceSubDirectory: str               = sourceSubDirectory

        secho(f'Python Warnings: {warning.value}')
        filterwarnings(warning.value)       # type: ignore

    def execute(self):

        if self.validProjectsBase is True and self.validProjectDirectory() is True:
            self._changeToProjectRoot()

        pythonPath:    str = (f'{self._projectsBase}{osSep}'
                              f'{self._projectDirectory}{osSep}'
                              f'{self._sourceSubDirectory}{osSep}'
                              f'{self._projectDirectory}'           # I am assuming that the project name is the same as the top level package
                              )

        osEnvironment[UnitTests.ENV_VAR_PYTHON_PATH] = f''
        secho('------------------------------------------------------------------')
        secho(f'{pythonPath=}')
        secho('------------------------------------------------------------------')

        secho(f'Test Pattern: {self._pattern}')
        testLoader: TestLoader = TestLoader()
        testSuite:  TestSuite  = testLoader.discover(start_dir='.', pattern=self._pattern, top_level_dir='')

        if self._html is True:
            self._runHtmlTestRunner(testSuite=testSuite)
        else:
            self._runTextTestRunner(testSuite=testSuite)

    @property
    def executionStatus(self) -> int:
        return self._executionStatus.value

    def _runTextTestRunner(self, testSuite: TestSuite):

        unitTestVerbosity: int            = UnitTestVerbosity.toUnitTestValue(self._verbosity)
        runner:            TextTestRunner = TextTestRunner(verbosity=unitTestVerbosity)

        secho(f'Verbosity: {unitTestVerbosity}')
        testResult:        TestResult     = runner.run(testSuite)

        self._setExecutionStatus(testResult)

    def _runHtmlTestRunner(self, testSuite: TestSuite):

        unitTestVerbosity: int            = UnitTestVerbosity.toUnitTestValue(self._verbosity)

        secho(f'Verbosity: {unitTestVerbosity} Report Name: {self._reportName}')

        runner:            HTMLTestRunner = HTMLTestRunner(output=UnitTests.HTML_REPORT_DIRECTORY_NAME,
                                                           report_name=self._reportName,
                                                           verbosity=unitTestVerbosity,
                                                           combine_reports=True,
                                                           add_timestamp=True)

        testResult: TestResult = runner.run(testSuite)

        self._setExecutionStatus(testResult)

    def _setExecutionStatus(self, testResult: TestResult):
        self.logger.info(f'Test Results: {testResult}')

        if len(testResult.failures) != 0:
            self._executionStatus = ExecutionStatus.SOME_TESTS_FAILED
        else:
            self._executionStatus = ExecutionStatus.ALL_TESTS_PASSED
