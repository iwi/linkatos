#!/usr/bin/env bash

py.test --junitxml junit.xml -v tests 2>&1 >/dev/null

cat junit.xml
