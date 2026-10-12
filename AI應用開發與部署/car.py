from google import genai
from google.oauth2 import service_account


_PLATE_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "plate": {"type": "string", "description": "車牌號碼，ex: ALJ-0000，若沒有車牌此值為空字串"}
    },
    "required": ["plate"]
}

_genai_client = None


def _get_genai_client(service: str | None = None, api_key: str | None = None):
    genai_client = None
    try:
        if api_key and isinstance(api_key, str):
            genai_client = genai.Client(api_key=api_key)
        elif service and isinstance(service, str):
            credentials = service_account.Credentials.from_service_account_file(
                service,
                scopes=['https://www.googleapis.com/auth/cloud-platform']
            )
            genai_client = genai.Client(
                enterprise=True,
                location='global',
                project=credentials.project_id,
                credentials=credentials
            )
        elif service == None and api_key == None:
            genai_client = genai.Client()
    except Exception as e:
        print(e)

    return genai_client

def recognize_plate(
    image: bytes,
    model: str = 'gemini-3.5-flash-lite',
    service: str | None = None,
    api_key: str | None = None
) -> str | None:
    '''recognize single plate in image
    image   - image in bytes
    model   - model name of Gemini
    service - service account key file name
    api_key - API key of Google AI Studio
    return  - car plate number in image
            - None for error
    '''

    # validate parameters
    if not image or not isinstance(image, bytes):
        return None
    if not model or not isinstance(model, str):
        return None 

    # confirm Gemini client
    global _genai_client
    
    if not _genai_client:
        _genai_client = _get_genai_client(service=service, api_key=api_key)
        if not _genai_client:
            print('no genai client!')
            return None

    # prepare contents
    contents = [
        {
            'role': 'user',
            'parts': [
                {'inline_data': {'data': image, 'mime_type': 'image/jpeg'}}
            ]
        }
    ]

    # configurations
    config = {
        'max_output_tokens': 1_000,
        'thinking_config': {'thinking_level': 'medium'},
        'response_mime_type': 'application/json',
        'response_schema': _PLATE_RESPONSE_SCHEMA
    }
    
    # call Gemini
    try:
        r = _genai_client.models.generate_content(
            model=model,
            config=config,
            contents=contents
        )
        #print(r.usage_metadata)
        if r.candidates[0].finish_reason == 'STOP' and r.parsed:
            return r.parsed.get('plate', '')
        print(r.candidates[0].finish_reason)        
    except Exception as e:
        print(e)
    
    return None