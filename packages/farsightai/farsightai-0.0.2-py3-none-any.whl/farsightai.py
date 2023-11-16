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
async def gpt_inference(
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


async def get_generate_prompts(num_prompts, task, context, goals, openai_key):
    system_prompt, user_prompt = get_generate_prompts_prompts(task, context, goals)
    chatCompletion = await gpt_inference(
        user_prompt, openai_key, n=num_prompts, system_prompt=system_prompt
    )
    generated_prompts = []
    for i, choice in enumerate(chatCompletion.choices):
        generated_prompts.append(choice.message.content)
    return generated_prompts


# ---------------------------------------- metrics ---------------------------------------- #


async def get_quality_score(instruction, response, apiKey):
    try:
        prompt = get_quality_prompt(instruction, response)
        chatCompletion = await gpt_inference(prompt, apiKey)
        output = chatCompletion.choices[0].message.content
        output_list = output.split("\n")
        score = int(output_list[0].replace("score: ", "").strip())
        return score
    except Exception as error:
        print("Error in Quality API request:", error)
        return {"score": "error"}


async def get_conciseness_score(inst, resp, openai_key):
    prompt = get_conciseness_prompt(inst, resp)
    try:
        chatCompletion = await gpt_inference(prompt, openai_key)
        output = chatCompletion.choices[0].message.content

        output_list = output.split("\n")
        score = int(output_list[0].replace("score: ", "").strip())
        return score
    except Exception as error:
        return {"Error in Conciseness API request:", error}


async def get_consistency_score(
    instruction,
    response,
    openai_key,
    n=2,
):
    async def process_reference(reference):
        outputs = await gpt_inference(
            get_consistency_prompt(reference, response),
            openai_key,
            "gpt-3.5-turbo",
            0.0,
            1,
        )
        return outputs.choices[0].message.content

    try:
        reference_call = await gpt_inference(instruction, openai_key, "gpt-3.5-turbo", 1.0, n)
        references = [choice.message.content for choice in reference_call.choices]
        consistency_promises = [
            process_reference(reference) for reference in references
        ]
        results = await asyncio.gather(*consistency_promises)
        positives = sum("Yes" in result for result in results)
        consistency_score = positives / len(results)

        return consistency_score
    except Exception as error:
        return ("Error in Consistency API request:", error)


async def get_factuality_score(question, answer, knowledge, openai_key):
    prompt = get_factuality_prompt(question, answer, knowledge)
    try:
        chatCompletion = await gpt_inference(prompt, openai_key)
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


# ---------------------------------------- async -> sync wrappers ----------------------------------------


def quality_score(inst, resp, openai_key):
    score = asyncio.run(get_quality_score(inst, resp, openai_key))
    return score


def conciseness_score(inst, resp, openai_key):
    score = asyncio.run(get_conciseness_score(inst, resp, openai_key))
    return score


def consistency_score(inst, resp, openai_key, n):
    score = asyncio.run(get_consistency_score(inst, resp, openai_key, n))
    return score


def factuality_score(inst, resp, knowledge, openai_key):
    score = asyncio.run(get_factuality_score(inst, resp, knowledge, openai_key))
    return score


def generate_prompts(num_prompts, task, context, goals, openai_key):
    prompts = asyncio.run(
        get_generate_prompts(num_prompts, task, context, goals, openai_key)
    )
    return prompts


# ---------------------------------------- tests ----------------------------------------

def test(openai_key):
    inst = "who is the president of the united states"
    resp = "As of my last knowledge update in January 2022, Joe Biden is the President of the United States. However, keep in mind that my information might be outdated as my training data goes up to that time, and I do not have browsing capabilities to check for the most current information. Please verify with up-to-date sources."
    conciseness = conciseness_score(inst, resp, openai_key)
    print("conciseness_score: ", conciseness)
    quality = quality_score(inst, resp, openai_key)
    print("quality_score: ", quality)
    consistency = consistency_score(inst, resp, openai_key, 2)
    print("consistency_score: ", consistency)
    factuality = factuality_score(inst, resp, "", openai_key)
    print("factuality_score: ", factuality)
    return 

