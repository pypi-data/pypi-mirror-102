#!/usr/bin/env python

"""Tests for `octis` package."""

import pytest

from click.testing import CliRunner
from octis.evaluation_metrics.topic_significance_metrics import *
from octis.evaluation_metrics.classification_metrics import F1Score
from octis.evaluation_metrics.diversity_metrics import TopicDiversity, InvertedRBO

from octis.evaluation_metrics.coherence_metrics import *
from octis.dataset.dataset import Dataset
from octis.models.LDA import LDA

import os


@pytest.fixture
def root_dir():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def dataset(root_dir):
    dataset = Dataset()
    dataset.load_custom_dataset_from_folder(root_dir + "/../preprocessed_datasets/" + '/M10')
    return dataset


@pytest.fixture
def model_output(dataset):
    model = LDA(num_topics=3, iterations=5)
    output = model.train_model(dataset)
    return output


def test_f1score(dataset, model_output):
    metric = F1Score({'dataset': dataset})
    score = metric.score(model_output)
    assert type(score) == np.float64 or type(score) == float


def test_coherence_measures(dataset, model_output):
    metrics_parameters = {'topk': 10, "texts": dataset.get_corpus()}
    metric = Coherence(metrics_parameters)
    score = metric.score(model_output)
    assert type(score) == np.float64 or type(score) == float


def test_diversity_measures(dataset, model_output):
    metrics_parameters = {'topk': 10}
    metric = TopicDiversity(metrics_parameters)
    score = metric.score(model_output)
    assert type(score) == np.float64 or type(score) == float


def test_irbo(dataset, model_output):
    metrics_parameters = {'topk': 10}
    metric = InvertedRBO(metrics_parameters)
    score = metric.score(model_output)
    assert type(score) == np.float64 or type(score) == float


def test_kl_b(dataset, model_output):
    metric = KL_background()
    score = metric.score(model_output)
    assert type(score) == np.float64 or type(score) == float


def test_kl_v(dataset, model_output):
    metric = KL_vacuous()
    score = metric.score(model_output)
    assert type(score) == np.float64 or type(score) == float


def test_kl_u(dataset, model_output):
    metric = KL_uniform()
    score = metric.score(model_output)
    assert type(score) == np.float64 or type(score) == float
