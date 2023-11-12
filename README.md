# Responsible Generative AI - Nvidia NeMo Guardrails 

The code demonstration part of the Responsible Generative AI with Guardrails presentation.

## Overview
Generative AI technology offers immense potential, but it also poses unique challenges that require careful consideration. This ReadMe file discusses key issues, recent incidents, and actionable steps for mitigating risks associated with generative AI.

## Challenges
Generative AI has raised concerns related to data protection, unintended output, and data leaks. High-profile incidents, like ChatGPT's hallucination incident in April and a lawyer's reliance on fabricated legal cases in June, underscore the importance of addressing these challenges. Missteps with generative AI can harm reputations and lead to significant financial consequences.

## Areas of Mitigation
### Data Tier: Data Collection, Preprocessing & Assessments
- Data Quality & Quantity
- Data Bias and Toxicity Assessments
- Data Debiasing
- Filtering Harmful Content 

### Model Tier: Model, External Databases
- Vector Databases & Knowledge Graphs
- Agents
- Evaluation and Benchmarking
- Guardrails
- Fine Tuning
- Red Teaming
- Reinforcement Learning for Human Feedback

### Application Tier: User Interface
- Prompting Techniques
- Human Feedback (e.g. from customers)
- Post-Deployment Monitoring

## Guardrails Overview

### Introduction
In conversational AI chatbots, ensuring that the language model interacts with users in a safe and controlled manner is of utmost importance. This is particularly critical when users ask off-topic, harmful, or ambiguous queries, or when the chatbot's responses are incorrect, out of scope, or toxic. To address these challenges, the concept of "guardrails" proves invaluable.

### Guardrails Concept
Guardrails serve as a protective layer between the language model and users, ensuring that the model's outputs align with our expectations. While prompt templates provide a degree of control, they often fall short in handling the complexity and unpredictability of human-language interactions, making them unreliable and clunky for addressing multiple Responsible AI risks or criteria simultaneously.

### Guardrails Application
Guardrails can be applied at two stages:

1. **Prompting Stage:** During this stage, we assess and validate users' inputs to ensure they align with the desired behavior.

2. **Output Stage:** Here, we verify that the generated responses meet our standards and criteria.

These stages involve establishing a set of rules or validators that the model adheres to during interactions.

## NeMo Guardrails
**NeMo Guardrails** offers a structured framework for implementing guardrails effectively. With this framework, we can achieve several essential use cases:
![Image Alt text](/images/examples.png "NeMo Guardrails Examples")
- **Topic Alignment:** Ensure that the language model stays on topic. For example, in a customer support chatbot, if a user asks for legal advice, NeMo Guardrails can steer the conversation back to the company's products and services.

- **Predefined Responses:** Route frequently asked questions to predefined answers, streamlining response generation and eliminating the risk of model hallucination.

- **Retrieval Augmented Generation:** Invoke external agents or APIs to provide information. For instance, if a user requests flight recommendations based on a budget, NeMo Guardrails can execute an API like Kayak to ensure reliable responses.

NeMo Guardrails empower us to create safer and more controlled conversational AI experiences while preserving the flexibility and power of large language models.

### Technical Concepts
NeMo Guardrails offer considerable flexibility, providing precise control over various aspects, including user inputs and Language Model (LLM) outputs.

![Image Alt text](/images/technicalconcepts.png "NeMo Guardrails Technical Concepts")

**Constructing 'Rails' or 'Flows'**
At its core, NeMo Guardrails are designed to establish 'rails' or 'flows' within conversational systems. These pathways offer clear directives to the language model, preventing it from wandering into undesirable topics while seamlessly integrating with other services.

#### Key Components
Setting up NeMo Guardrails involves working with two essential components:

1. **Main Configuration File (YAML):** This file plays a central role in defining a range of parameters, primarily focusing on specifying the deployed language model.

2. **Colang File:** NeMo Guardrails leverage Colang, a modeling language developed by Nvidia. Within this dedicated Colang file, you define the contours of conversational 'rails' or 'flows' and establish the guardrails that guide the conversation in the desired direction.

#### Structure of the Colang File
The Colang file consists of three fundamental message types:

1. **"Define User" Block or "User" Message:** This section enables precise control over user inputs, allowing you to specify topics or specific words for detection. For example, if you wish to steer the conversation away from political discussions, you can define a "user" message called "ask politics" and provide examples of user queries related to this topic.

2. **"Define Bot" Blocks:** These blocks determine the bot's behavior in specific scenarios and govern how the system should validate bot responses. For instance, if you want the bot to avoid discussing politics, you can instruct it on how to respond when a user brings up political topics.

3. **Flows:** Flows define the desired conversation structure and the actions the bot can take. For instance, if a user's query aligns with the "ask politics" user message, the bot responds with a predefined answer labeled "answer politics" and can follow up with further assistance or information.

## Runtime Overview
At runtime, NeMo Guardrails employ an embedding model to encapsulate both user intentions and bot responses, preserving them within a vector database.

All user and bot messages, along with their associated examples, are encoded into this vector database.

![Image Alt text](/images/runtime.png "NeMo Guardrails Runtime Example")

1. **Prompt:** When a user initiates a message, the initial step captures the user's intent. This is achieved by encoding the message into the vector space. The model then assesses its similarity to predefined canonical forms, identifying the most relevant canonical form that explains the user's intent.

   For instance, in a greeting scenario, a user's message like "Hi, how are you?" would be encoded, and the system would ascertain that the closest canonical form is "user express greeting."

2. **Matching Canonical Form:** Once the system identifies the canonical form, it proceeds to locate a flow associated with that canonical form. In our greeting example, the system would correlate "user express greeting" with the flow labeled "greeting."

3. **Executing Flow:** The selected flow is then executed and performs subsequent actions listed in the flow.

4. **Generating Bot's Response:** In our example, the subsequent action is a "bot" message named "express greeting." The system captures the bot's intent and generates a response, getting examples within the vector space.
