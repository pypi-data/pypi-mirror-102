*** Settings ***
Documentation   The most basic system test possible
...
...             This system test serves as the most basic test for the whole
...             ARL core system. It exists to ensure that the infrastructure
...             code works, i.e., that we can run `arlctl', get help,
...             or see debugging output.

Library     OperatingSystem

*** Test Cases ***
Run arlctl for help
    ${rc}    ${output} =            Run and Return RC and Output    palaestrai --help
    Log                             ${output}
    Should Be Equal As Integers     ${rc}    0

Ensure an explicitly given config file is loaded
    File Should Exist               ./tests/fixtures/arl-runtime-debug.conf.yaml
    ${rc}    ${output} =            Run and Return RC and Output    palaestrai -c ./tests/fixtures/arl-runtime-debug.conf.yaml -vv experiment-start --help
    Log                             ${output}
    Should Be Equal As Integers     ${rc}    0
    ${match} =                      Should Match Regexp    ${output}    Initialized logging from RuntimeConfig\\(<RuntimeConfig id=0x[^>]+?> at .*?tests/fixtures/arl-runtime-debug.conf.yaml
