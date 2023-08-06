java -jar openapi-generator-cli-5.0.1-20210110.073014-30.jar generate -i https://testops.katalon.io/v3/api-docs/public -g python --config codegen_config.json

python3 setup.py sdist bdist_wheel