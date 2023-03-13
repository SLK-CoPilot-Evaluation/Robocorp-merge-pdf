*** Settings ***
Documentation       Template robot main suite.

Library             merge.py
Library             RPA.PDF


*** Tasks ***
Minimal task
    Merge Pdf    input_path    output_path
