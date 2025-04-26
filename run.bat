@echo off
REM Save as convert_to_html.bat

REM Convert q1.ipynb
jupyter nbconvert --to html --execute "code/q1.ipynb" --output "../output/q1.html"
echo Converted notebook saved to: ../output/q1.html

REM Convert q2_4.ipynb
jupyter nbconvert --to html --execute "code/q2_4.ipynb" --output "../output/q2_4.html"
echo Converted notebook saved to: ../output/q2_4.html

REM Convert q3_5.ipynb
jupyter nbconvert --to html --execute "code/q3_5.ipynb" --output "../output/q3_5.html"
echo Converted notebook saved to: ../output/q3_5.html

REM Convert q6_7.ipynb
jupyter nbconvert --to html --execute "code/q6_7.ipynb" --output "../output/q6_7.html"
echo Converted notebook saved to: ../output/q6_7.html

pause