*** Settings ***
Documentation       Template robot main suite.

Library             RPA.PDF


*** Variables ***
${TESTDATA_DIR} =       D:\\OneDrive - SLK Software Services Pvt Ltd\\Desktop\\PDF files


*** Tasks ***
Merge
    Merge pdfs


*** Keywords ***
Merge pdfs
    ${files}=    Create List
    ...    ${TESTDATA_DIR}${/}newdoc.pdf:
    ...    ${TESTDATA_DIR}${/}newdoc.pdf:

    Add Files To Pdf    ${files}    ${TESTDATA_DIR}${/}newdoc2.pdf
