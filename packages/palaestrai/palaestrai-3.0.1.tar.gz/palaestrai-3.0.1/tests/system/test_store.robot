*** Settings ***
Documentation   Test results store
...
...             This is a system test that runs the store setup, store migrations, and a dummy experiment
...             to check whether the store works and receives data.

Library     String
Library     Process
Library     OperatingSystem
Library     ${CURDIR}${/}ConfigFileModifier.py

*** Keywords ***
Setup Database Connection
    ${r} =                          generate random string
    set environment variable        PGDB    %{POSTGRES_DB}_${r}
    prepare_for_store_test          ${CURDIR}${/}..${/}..${/}arl-runtime.conf.yaml  ${TEMPDIR}${/}store-test.conf.yml
    log file                        ${TEMPDIR}${/}store-test.conf.yml
    set environment variable        PGPASSWORD      %{POSTGRES_PASSWORD}
    ${result} =                     Run Process     psql    -a  -c  DROP DATABASE IF EXISTS %{PGDB};  -h  %{POSTGRES_HOST}    -U    %{POSTGRES_USER}    postgres
    ${result} =                     Run Process     psql    -a  -c  CREATE DATABASE %{PGDB} WITH OWNER %{POSTGRES_USER}  -h  %{POSTGRES_HOST}    -U     %{POSTGRES_USER}   postgres
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0

Drop Database
    ${result} =                     Run Process     psql    -a  -c  DROP DATABASE %{PGDB}  -h  %{POSTGRES_HOST}    -U     %{POSTGRES_USER}   postgres
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0

*** Test Cases ***
Create database
    [Setup]                         setup database connection
    [Teardown]                      drop database
    ${result} =                     Run Process   palaestrai    -c  ${TEMPDIR}${/}store-test.conf.yml   database-create
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0
    ${result} =                     Run Process     psql    -a  -c  SELECT * FROM pg_tables;  -h  %{POSTGRES_HOST}    -U  %{POSTGRES_USER}    -A    -F    ,     %{PGDB}
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0
    Should Contain                  ${result.stdout}    ,experiment_studies,
    Should Contain                  ${result.stdout}    ,experiments,
    Should Contain                  ${result.stdout}    ,experiment_runs,
    Should Contain                  ${result.stdout}    ,simulation_instances,
    Should Contain                  ${result.stdout}    ,environment_conductors,
    Should Contain                  ${result.stdout}    ,world_states,
    Should Contain                  ${result.stdout}    ,agent_conductors,
    Should Contain                  ${result.stdout}    ,brains,
    Should Contain                  ${result.stdout}    ,muscles,
    Should Contain                  ${result.stdout}    ,muscle_states,
    Should Contain                  ${result.stdout}    ,muscle_actions,
    Should Contain                  ${result.stdout}    ,muscle_sensor_readings,

Verify TimescaleDB Hypertables
    [Setup]                         setup database connection
    [Teardown]                      drop database
    ${result} =                     Run Process   palaestrai    -vv     -c  ${TEMPDIR}${/}store-test.conf.yml   database-create
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0
    ${result} =                     Run Process     psql    -a  -c  SELECT * FROM pg_extension;  -h  %{POSTGRES_HOST}    -U  %{POSTGRES_USER}    -A     -F  ,     %{PGDB}
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0
    Should Contain                  ${result.stdout}    ,timescaledb,
    ${result} =                     Run Process     psql    -a  -c  SELECT table_name FROM _timescaledb_catalog.hypertable;  -h  %{POSTGRES_HOST}    -U  %{POSTGRES_USER}    -A     -F  ,     %{PGDB}
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0
    Should Contain                  ${result.stdout}    world_states
    Should Contain                  ${result.stdout}    muscle_actions
    Should Contain                  ${result.stdout}    muscle_sensor_readings
    Should Contain                  ${result.stdout}    muscle_states

Run dummy experiment and check for data
    [Timeout]                       180
    [Setup]                         setup database connection
    [Teardown]                      drop database
    ${result} =                     Run Process   palaestrai    -c  ${TEMPDIR}${/}store-test.conf.yml   database-create
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0
    ${result} =                     Run Process   palaestrai    -c  ${TEMPDIR}${/}store-test.conf.yml   experiment-start    ${CURDIR}${/}..${/}fixtures${/}dummy_experiment.yml    shell=yes
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0
    ${result} =                     Run Process     psql    -a  -c  SELECT * FROM experiments;  -h  %{POSTGRES_HOST}    -U  %{POSTGRES_USER}    -A  -F  ,     %{PGDB}
    log many                        ${result.stdout}    ${result.stderr}
    Should Be Equal As Integers     ${result.rc}    0
