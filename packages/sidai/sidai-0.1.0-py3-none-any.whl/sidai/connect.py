import httpx
import json
from typing import Optional, Literal
from dataclasses import dataclass, field
from dataclass_wizard import JSONWizard

@dataclass
class Snippet(JSONWizard):
    score: float
    name: str
    kind: str
    text: str
    predecessors: list[str] = field(default_factory=list)
    successors: list[str] = field(default_factory=list)

@dataclass
class QueryMeta(JSONWizard):
    sync_in_progress: bool

@dataclass
class QueryResponse(JSONWizard):
    results: list[Snippet]
    meta: QueryMeta

@dataclass
class ExampleResult:
    text: str
    snippets: list[Snippet]

@dataclass
class ExampleResponse(JSONWizard):
    result: ExampleResult

@dataclass
class CustomItem(JSONWizard):
    name: str
    text: str

class SIDConnect:
    def __init__(self):
        self.client = httpx.Client()
        self.base_url = 'https://api.sid.ai/v1'

    def __del__(self):
        self.client.close()

    def query(
        self,
        token: str,
        query: str, 
        limit: Optional[int] = None,
        context_size: Optional[int] = None,
        query_processing: Literal['standard', 'extended'] = 'standard',
    ) -> QueryResponse:
        url = f'{self.base_url}/users/me/query'
        data = {
            'query': query,
            'query_processing': query_processing,
        }
        if limit is not None:
            data['limit'] = limit
        if context_size is not None:
            data['context_size'] = context_size

        headers = {
            'Authorization': f'Bearer {token}',
        }

        res_raw = self.client.post(url, json=data, headers=headers)
        if not res_raw.is_success:
            raise Exception(f'Query failed with status code {res_raw.status_code}: {res_raw.text}')
        return QueryResponse.from_json(res_raw.text)

    def example(
        self, 
        token: str,
        usage: Literal['question', 'task'] | str = 'question',
    ) -> ExampleResponse:
        url = f'{self.base_url}/users/me/example'
        data = {
            'usage': usage,
        }
        headers = {
            'Authorization': f'Bearer {token}',
        }
        res_raw =  self.client.post(url, json=data, headers=headers)
        if not res_raw.is_success:
            raise Exception(f'Example failed with status code {res_raw.status_code}: {res_raw.text}')
        return ExampleResponse.from_json(res_raw.text)

    def insert_custom(
        self,
        token: str,
        items: list[CustomItem],
    ):
        url = f'{self.base_url}/users/me/services/me/insert'
        data = {
            'data': [item.to_dict() for item in items],
        }
        headers = {
            'Authorization': f'Bearer {token}',
        }
        res = self.client.post(url, json=data, headers=headers)
        if not res.is_success:
            raise Exception(f'Insert failed with status code {res.status_code}: {res.text}')

    def clear_custom(
        self,
        token: str,
    ):
        url = f'{self.base_url}/users/me/services/me/clear'
        headers = {
            'Authorization': f'Bearer {token}',
        }
        res = self.client.post(url, headers=headers)
        if not res.is_success:
            raise Exception(f'Clear failed with status code {res.status_code}: {res.text}')
    