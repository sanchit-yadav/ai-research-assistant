import google.generativeai as genai

genai.configure(api_key="AIzaSyDC8dJv0rbmdVsGiJCVcH6Og3TOKqwCBZQ")

models = genai.list_models()

for m in models:
    print(m.name)