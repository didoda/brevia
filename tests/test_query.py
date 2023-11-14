"""Query module tests"""
import pytest
from brevia.query import (
    conversation_chain,
    load_qa_prompt,
    load_condense_prompt,
    search_vector_qa,
)
from brevia.collections import create_collection
from langchain.prompts import BasePromptTemplate
from langchain.chains import ConversationalRetrievalChain

FAKE_PROMPT = {
    '_type': 'prompt',
    'input_variables': [],
    'template': 'Fake',
}


def test_load_qa_prompt():
    """Test load_qa_prompt method"""
    result = load_qa_prompt({
        'system': FAKE_PROMPT,
    })
    assert result is not None
    assert isinstance(result, BasePromptTemplate)

    result = load_qa_prompt({
        'human': FAKE_PROMPT,
    })
    assert result is not None
    assert isinstance(result, BasePromptTemplate)


def test_load_condense_prompt():
    """Test load_condense_prompt method"""
    result = load_condense_prompt({
        'few': FAKE_PROMPT,
    })
    assert result is not None
    assert isinstance(result, BasePromptTemplate)

    result = load_condense_prompt({
        'condense': FAKE_PROMPT,
    })
    assert result is not None
    assert isinstance(result, BasePromptTemplate)


def test_search_vector_qa():
    """Test search_vector_qa function"""
    with pytest.raises(ValueError) as exc:
        search_vector_qa(query='test', collection='test')
    assert str(exc.value) == 'Collection not found: test'


def test_conversation_chain():
    """Test conversation_chain function"""
    collection = create_collection('test', {})
    chain = conversation_chain(collection=collection)

    assert chain is not None
    assert isinstance(chain, ConversationalRetrievalChain)