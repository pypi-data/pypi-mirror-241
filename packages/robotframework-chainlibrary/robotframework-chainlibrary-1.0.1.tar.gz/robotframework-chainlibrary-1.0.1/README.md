# RobotFramework-ChainLibrary

[![GitHub Actions status](https://github.com/crsdet/robotframework-chainlibrary/actions/workflows/checks.yml/badge.svg)](https://github.com/crsdet/robotframework-chainlibrary/actions)

Robot Framework library for running keywords in chain.

This module allows to run 2 or more keywords on a single line where the returned value of the first keyword is the argument of the second keyword and so on in Robot Framework.

## Installation

~~~sh
pip install robotframework-chainlibrary
~~~

## Usage

[ChainLibrary keyword documentation](https://crsdet.github.io/robotframework-chainlibrary)

~~~robotframework
*** Settings ***
Library    String
Library    ChainLibrary


*** Variables ***
${WELCOME_MESSAGE}    Hello __NAME__, welcome to the __LIBRARY__ Library!


*** Test Cases ***
Replace Multiple Strings
    ${new_str}    Replace Strings    ${WELCOME_MESSAGE}    __NAME__=John Doe    __LIBRARY__=Chain
    Should Be Equal    ${new_str}    Hello John Doe, welcome to the Chain Library!

Run Chained Keywords
    ${str}    Chain Keywords    Generate Random String    AND    Set Test Variable    ${RANDOM_STRING}
    Should Be Equal    ${str}    ${RANDOM_STRING}
~~~

You can also specify a different separator:

~~~robotframework
*** Settings ***
Library    String
Library    ChainLibrary    separator=->


*** Test Cases ***
Run Chained Keywords
    ${str}    Chain Keywords    Generate Random String    ->    Set Test Variable    ${RANDOM_STRING}
    Should Be Equal    ${str}    ${RANDOM_STRING}
~~~
