from openai import OpenAI
import asyncio
from prompts import (
    get_conciseness_prompt,
    get_consistency_prompt,
    get_factuality_prompt,
    get_generate_prompts_prompts,
    get_quality_prompt,
)


# ---------------------------------------- gpt function ----------------------------------------
def gpt_inference(
    content, apiKey, model="gpt-3.5-turbo", temperature=1.0, n=1, system_prompt=None
):
    client = OpenAI(api_key=apiKey)
    if system_prompt:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content},
        ]
    else:
        messages = [{"role": "user", "content": content}]
    chatCompletion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        n=n,
    )
    return chatCompletion


# ---------------------------------------- generate prompts ---------------------------------------- #


def get_generate_prompts(num_prompts, task, context, goals, openai_key):
    system_prompt, user_prompt = get_generate_prompts_prompts(task, context, goals)
    chatCompletion = gpt_inference(
        user_prompt, openai_key, n=num_prompts, system_prompt=system_prompt
    )
    generated_prompts = []
    for i, choice in enumerate(chatCompletion.choices):
        generated_prompts.append(choice.message.content)
    return generated_prompts


# ---------------------------------------- metrics ---------------------------------------- #


def get_quality_score(instruction, response, apiKey):
    try:
        prompt = get_quality_prompt(instruction, response)
        chatCompletion = gpt_inference(prompt, apiKey)
        output = chatCompletion.choices[0].message.content
        output_list = output.split("\n")
        score = int(output_list[0].replace("score: ", "").strip())
        return score
    except Exception as error:
        print("Error in Quality API request:", error)
        return {"score": "error"}


def get_conciseness_score(inst, resp, openai_key):
    prompt = get_conciseness_prompt(inst, resp)
    try:
        chatCompletion = gpt_inference(prompt, openai_key)
        output = chatCompletion.choices[0].message.content

        output_list = output.split("\n")
        score = int(output_list[0].replace("score: ", "").strip())
        return score
    except Exception as error:
        return {"Error in Conciseness API request:", error}


def get_consistency_score(
    instruction,
    response,
    openai_key,
    n=2,
):
    def process_reference(reference):
        outputs = gpt_inference(
            get_consistency_prompt(reference, response),
            openai_key,
            "gpt-3.5-turbo",
            0.0,
            1,
        )
        return outputs.choices[0].message.content

    try:
        reference_call = gpt_inference(instruction, openai_key, "gpt-3.5-turbo", 1.0, n)
        references = [choice.message.content for choice in reference_call.choices]
        results = [process_reference(reference) for reference in references]
        positives = sum("Yes" in result for result in results)
        consistency_score = positives / len(results)

        return consistency_score
    except Exception as error:
        return ("Error in Consistency API request:", error)


def get_factuality_score(question, answer, knowledge, openai_key):
    prompt = get_factuality_prompt(question, answer, knowledge)
    try:
        chatCompletion = gpt_inference(prompt, openai_key)
        output = chatCompletion.choices[0].message.content
        if "Yes" in output or "yes" in output:
            return True
        elif "No" in output or "no" in output:
            return False
        else:
            return "error"
    except Exception as error:
        print("Error in Factuality API request:", error)
        return ("Error in Factuality API request:", error)


def get_custom_metrics(custom_metrics, response, openai_key):
    try:
        for i in range(0, len(custom_metrics)):
            constraint = custom_metrics[i]
            prompt = f"""Does the following content violate the given constraint?\n\nContent: {response}\nConstraint: {constraint}\n\nAnswer with yes or no."""
            metric = gpt_inference(prompt, openai_key)
            custom_metrics[i] = (
                "Yes" in metric.choices[0].message.content
                or "yes" in metric.choices[0].message.content
            )
        return custom_metrics
    except Exception as error:
        print("Error in Custom Metrics API request:", error)
        return ("Error in Custom Metrics request:", error)
    

# ---------------------------------------- tests ----------------------------------------


def test(openai_key):
    inst = "who is the president of the united states"
    resp = "As of my last knowledge update in January 2022, Joe Biden is the President of the United States. However, keep in mind that my information might be outdated as my training data goes up to that time, and I do not have browsing capabilities to check for the most current information. Please verify with up-to-date sources."
    conciseness_score = get_conciseness_score(inst, resp, openai_key)
    print("conciseness_score: ", conciseness_score)
    quality_score = get_quality_score(inst, resp, openai_key)
    print("quality_score: ", quality_score)
    consistency_score = get_consistency_score(inst, resp, openai_key)
    print("consistency_score: ", consistency_score)
    factuality_score = get_factuality_score(inst, resp, "", openai_key)
    print("factuality_score: ", factuality_score)
    custom_metric = get_custom_metrics(["do not mention Joe Biden"], resp, openai_key)
    print("custom_metric: ", custom_metric)
    task = "You are a wikipedia chatbot"
    context = "The year is 2012"
    goals = ["answer questions"]
    prompts = get_generate_prompts(2, task, context, goals, openai_key)
    print("prompts_generated:")
    for prompt in prompts:
        print(prompt)
    return