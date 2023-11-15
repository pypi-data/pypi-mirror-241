from enum import Enum

from prompts import DynamicSchema, PromptRole, Template, TurboSchema
from prompts.schemas import TurboSchema
from pydantic import BaseModel
from redb.core import BaseDocument
from redb.interface.fields import Field

from melting_schemas.completion.chat import ChatModelSettings
from melting_schemas.meta import Creator

# ====== Create Schemas ======


class ChatPromptTemplate(TurboSchema):
    settings: ChatModelSettings
    class Config:
        examples = {
            "Minimal Prompt Template": {
                "value": {
                    "assistant_templates": "<text>",
                    "description": "Single of its kind, example app, teia org.",
                    "name": "teia.example_app.single.example01",
                    "system_templates": "<text>",
                    "user_templates": "<text>",
                    "settings": {"model": "gpt-3.5-turbo"},
                }
            },
            "Time-aware Prompt Template": {
                "value": {
                    "assistant_templates": "<text>",
                    "description": "Single of its kind, example app, teia org.",
                    "name": "teia.example.1",
                    "system_templates": "Current timestamp: <now>\nYou are a helpful chatbot.",
                    "user_templates": "<text>",
                    "settings": {
                        "model": "gpt-3.5-turbo",
                    },
                }
            },
            "Many Templates": {
                "value": {
                    "name": "teia.example.2",
                    "description": "A development example.",
                    "settings": {
                        "model": "gpt-3.5-turbo",
                        "max_tokens": 200,
                        "temperature": 0.25,
                    },
                    "system_templates": [
                        {"template_name": "plugin_prompt", "template": "<plugin_data>"},
                    ],
                    "user_templates": [
                        {"template_name": "user_prompt", "template": "<question>"}
                    ],
                    "assistant_templates": [
                        {"template_name": "assistant_prompt", "template": "<message>"}
                    ],
                }
            },
        }


class CreateCompletionPrompt(DynamicSchema):
    pass


# ====== Get Schemas ======


class GeneratedFields(BaseModel):
    created_at: str
    created_by: Creator
    id: str = Field(alias="_id")


class ChatPrompt(GeneratedFields, TurboSchema):
    pass


class GetCompletionPrompt(GeneratedFields, DynamicSchema):
    pass


# ====== Update Schemas ======


class UpdateChatTemplateData(BaseDocument):
    name: str | None = None
    role: PromptRole | None = None
    replacements: dict[str, str] | None = None


class UpdateSettings(BaseDocument):
    model: str | None = None
    max_tokens: int | None = None
    stop: list[str] | None = None
    temperature: float | None = None
    top_p: float | None = None
    frequency_penalty: float | None = None
    presence_penalty: float | None = None


class BaseUpdatePrompt(BaseDocument):
    class Config:
        json_encoders = {Enum: lambda e: e.value}

    # Prompt fields
    description: str | None = None
    settings: UpdateSettings | None = None

    # Prompt start
    initial_template_data: str | list[UpdateChatTemplateData] | None = None


class UpdateChatPrompt(BaseUpdatePrompt):
    # Templates
    assistant_templates: list[Template] | None = None
    system_templates: list[Template] | None = None
    user_templates: list[Template] | None = None


class UpdateCompletionPrompt(BaseUpdatePrompt):
    # Template
    template: str | None = None
