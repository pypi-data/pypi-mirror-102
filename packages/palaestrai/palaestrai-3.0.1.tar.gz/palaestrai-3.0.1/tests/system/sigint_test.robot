*** Settings ***
Documentation   Test handling of Ctrl+C (SIGINT)
...
...             This runs the system with the dummy experiment, but hits Ctrl+C after a short amount of time.
...             The test then monitors that everything exists smoothly.
...             There are several test cases that interrupt the running process after different amounts of time.

Library     OperatingSystem

*** Test Cases ***

Interrupt palaestrai-experiment with the dummy test after 3 seconds.
    ${rc}    ${output} =            Run and Return RC and Output    bash ${CURDIR}/sigint_test_runner.sh 3
    Log                             ${output}
    ${match} =                      Should Match Regexp    ${output}    Executor has received signal Signals.SIGINT, shutting down
    Should Be Equal As Integers     ${rc}    254

Interrupt palaestrai-experiment with the dummy test after 6 seconds.
    ${rc}    ${output} =            Run and Return RC and Output    bash ${CURDIR}/sigint_test_runner.sh 6
    Log                             ${output}
    ${match} =                      Should Match Regexp    ${output}    Executor has received signal Signals.SIGINT, shutting down
    Should Be Equal As Integers     ${rc}    254

Interrupt palaestrai-experiment with the dummy test after 12 seconds.
    ${rc}    ${output} =            Run and Return RC and Output    bash ${CURDIR}/sigint_test_runner.sh 12
    Log                             ${output}
    ${match} =                      Should Match Regexp    ${output}    Executor has received signal Signals.SIGINT, shutting down
    Should Be Equal As Integers     ${rc}    254
