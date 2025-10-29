import openai

def task_agent(prompt):
    openai.api_key = "YOUR_API_KEY"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a helpful automation agent."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

print(task_agent("Summarize the benefits of Hacktoberfest in 5 lines."))
