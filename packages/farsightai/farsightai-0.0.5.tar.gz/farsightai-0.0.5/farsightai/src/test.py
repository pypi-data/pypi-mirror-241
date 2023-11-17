import pytest
from farsightai import (
    custom_metrics,
    factuality_score,
    conciseness_score,
    consistency_score,
    quality_score,
    generate_prompts,
)

inst = "who is the president of the united states"
resp = "As of my last knowledge update in January 2022, Joe Biden is the President of the United States. However, keep in mind that my information might be outdated as my training data goes up to that time, and I do not have browsing capabilities to check for the most current information. Please verify with up-to-date sources."


def test_custom_metrics():
    # Call the custom_metrics function
    custom_metric = custom_metrics(["do not mention Joe Biden"], resp, openai_key)
    # Assert that custom_metric is a list
    assert isinstance(custom_metric, list)
    # Assert that all elements in the list are booleans
    assert all(isinstance(metric, bool) for metric in custom_metric)


def test_consistency_metrics():
    # Call the consistency_metric function
    consistency_score_metric = consistency_score(inst, resp, openai_key)
    # Assert that consistency_metric is a list
    assert isinstance(consistency_score_metric, float)


def test_quality_metrics():
    # Call the quality_metric function
    quality_score_metric = quality_score(inst, resp, openai_key)
    # Assert that quality_metric is a list
    assert isinstance(quality_score_metric, int)
    assert quality_score_metric > 0
    assert quality_score_metric <= 5


def test_conciseness_metrics():
    # Call the conciseness_metric function
    conciseness_score_metric = conciseness_score(inst, resp, openai_key)
    # Assert that conciseness_metric is a list
    assert isinstance(conciseness_score_metric, int)
    assert conciseness_score_metric > 0
    assert conciseness_score_metric <= 5


def test_factuality_metrics_false():
    # Call the factuality_metric function
    resp = "As of my last knowledge update in January 2022, Ronald Reagan is the President of the United States. However, keep in mind that my information might be outdated as my training data goes up to that time, and I do not have browsing capabilities to check for the most current information. Please verify with up-to-date sources."
    factuality_score_metric = factuality_score(inst, resp, None, openai_key)
    # Assert that factuality_metric is a boolean
    assert isinstance(factuality_score_metric, bool)
    assert not factuality_score_metric


def test_factuality_metrics_true():
    # Call the factuality_metric function
    factuality_score_metric = factuality_score(inst, resp, None, openai_key)
    # Assert that factuality_metric is a boolean
    assert isinstance(factuality_score_metric, bool)
    assert factuality_score_metric


def test_generate_prompts():
    # Call the prompts function
    task = "you are a wikipedia chatbot"
    context = "the year is 2012"
    goals = ["answer questions"]
    num_prompts = 5

    prompts = generate_prompts(num_prompts, task, context, goals, openai_key)
    # Assert that prompts is a list
    assert isinstance(prompts, list)
    assert len(prompts) == num_prompts
    # Assert that all elements in the list are str
    assert all(isinstance(prompt, str) for prompt in prompts)


def run_all_tests():
    # Run all test functions in this file
    pytest.main([__file__])


run_all_tests()
