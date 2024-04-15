pytest -s -v -m "sanity" --html=Reports\report.html testCases/ --browser chrome
pytest -s -v -m "sanity" --html=Reports\report.html testCases/ --browser firefox

REM Chrome

REM pytest -s -v -m "sanity" --html=Reports\report.html testCases/ --browser chrome
REM pytest -s -v -m "sanity or regression" --html=Reports\report.html testCases/ --browser chrome
REM pytest -s -v -m "sanity and regression" --html=Reports\report.html testCases/ --browser chrome
REM pytest -s -v -m "regression" --html=Reports\report.html testCases/ --browser chrome

REM Firefox

REM pytest -s -v -m "sanity" --html=Reports\report.html testCases/ --browser firefox
REM pytest -s -v -m "sanity or regression" --html=Reports\report.html testCases/ --browser firefox
REM pytest -s -v -m "sanity and regression" --html=Reports\report.html testCases/ --browser firefox
REM pytest -s -v -m "regression" --html=Reports\report.html testCases/ --browser firefox

REM Edge

REM pytest -s -v -m "sanity" --html=Reports\report.html testCases/ --browser edge
REM pytest -s -v -m "sanity or regression" --html=Reports\report.html testCases/ --browser edge
REM pytest -s -v -m "sanity and regression" --html=Reports\report.html testCases/ --browser edge
REM pytest -s -v -m "regression" --html=Reports\report.html testCases/ --browser edge

