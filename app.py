from flask import Flask, request
import openai

app = Flask(__name__)

@app.route('/queryCustomGPT')
def hello_world():
    openai.api_key = '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'
    fine_tuned_model = "davinci:ft-personal-2023-12-04-10-36-00"
    new_prompt = request.args.get('query')
    answer = openai.Completion.create(
        model=fine_tuned_model,
        prompt=new_prompt,
        max_tokens=100,
        temperature=0
    )
    print(answer['choices'][0]['text'])
    return answer['choices'][0]['text']

