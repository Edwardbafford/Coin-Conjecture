rm -f package.zip
pip install --upgrade --target ./package -r requirements.txt
cd package || exit
zip -r ../package.zip .
cd .. || exit
zip ./package.zip ./lambda_function.py