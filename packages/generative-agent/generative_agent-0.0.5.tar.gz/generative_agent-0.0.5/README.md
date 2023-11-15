# bel-generative-agents
Bel AI Chatbot, developed by Generative Agents Approach

### Workflow of the generative agents
 ![generative-agents-flow](/asset/image/flowchart.png)

### Todo

- [x] Do 6 prompts engineering implementation in Thai language
  - [x] PROMPT_ADDMEM
  - [x] PROMPT_CORE
  - [x] PROMPT_FEELING
  - [x] PROMPT_PLAN
  - [x] PROMPT_REACT
  - [x] PROMP_INTERVIEW
- [x] Time-stamp vector memory
- [x] Guardrails for controlling the generated response
- [x] Keep Chat history and Chat history summary
- [x] Weight-Input for score function (between Time-Importance-Relevant) in TimeWeightedRetriever module
- [x] Save & Load persistent memory for the agent
- [x] Multi-thread and add memory queue for optimized speed performance
- [x] Response with 5 base emotions [Excitement, Joy, Elation, Gratitude, Playfulness] 
- [ ] Ability to react and store new memory based on observation


### Install Dependencies

- ```pip install -r requirements.txt```

### Demo

- Chat in the terminal: ```python main.py```
- Interaction in the Jupyter Notebook: ```demo.ipynb```


### Usage
- Define environment language and Class, Enum importing
    ```python
    import generative_agent
    from generative_agent.tools import Agent_Type
    ```
- Define your LLMs module as you need
    ```python
    # OpenAI GPT
    # Don't forget > Define you OPENAI_API_KEY
    textllm = OpenAI()
    chatllm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0.3)
    embeddings_model = OpenAIEmbeddings() 
    
    # Azure OpenAI GPT
    # Don't forget > Define you OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT and etc.
    textllm = AzureOpenAI()
    chatllm = AzureChatOpenAI(model='gpt-3.5-turbo',temperature=0.3, deployment_name='your-gpt-model-deployment-name')
    embeddings_model = OpenAIEmbeddings(deployment='your-embedding-model-deployment-name')
    
    # Google VertexAI
    textllm = VertexAI(model_name="text-bison@001")
    chatllm = ChatVertexAI(model_name="chat-bison@001",max_output_tokens=1024, stop=[user+':', character_info['name']+':'], temperature=0.3)
    embeddings_model = VertexAIEmbeddings(
        model_name="textembedding-gecko-multilingual@latest"
    )
    ```
- Create Custom Agents
    ```python
    user = 'Name of User'
    agent_type = Agent_Type.TH_Man
    character_file_path = agent_type.value['path']
    knowledge_file_path = 'bel-knowledge.txt'
    name = "Name of Agent"
    age = "Age of Agent"

    with open(character_file_path, 'r') as json_file:
        character_info = json.load(json_file)

    # agent_type
    ## Now, we have only two types (Agent_Type.HUMAN_MALE, Agent_Type.FAIRY_GIRL), 
    ## we plan to implement more in the future.
    # load_memory 
    ## if True -> find the memory state in the database,
    ## else -> create new memory, and new agent
    agent = custom_agent(
        textllm=textllm, 
        chatllm=chatllm, 
        embeddings_model=embeddings_model, 
        name=name,
        age=age, 
        traits=character_info["traits"], 
        summary=character_info["summary"], 
        inappropiates=character_info["inappropiates"], 
        agent_type=agent_type,
        verbose=True,
        load_memory=False
    )
    ```
- Adding Behavior Memory
    - For example:
        ```python
        common_behavior='''เบลใช้เวลาส่วนใหญ่ในพิพิธภัณฑ์วิทยาศาสตร์ของฟอเรสเทียส์
        ส่วนใหญ่แล้วเบลมักจะอยู่รอบๆ พื้นที่จัดแสดง
        เบลชอบที่จะปรับปรุงประสบการณ์ของผู้เยี่ยมชมซึ่งจะช่วยกระจายความสุขและความคิดเชิญบวก
        ...(add more lines as you want)'''
        agent.add_character(common_behavior.split('\n'))
        ```
- Adding Knowledge Memory
  - Knowledge document file, currently, only support ```.txt``` file
  - For example: ```bel-knowledge.txt```, each knowledge in each line.
      ```python
      # Knowledge of agent
      knowledge_file_path = 'bel-knowledge.txt'
      with open(knowledge_file_path, 'r') as f:
          knowledge = f.readlines()
          knowledge = [each_l.replace('\n','') for each_l in knowledge]
      agent.add_knowledge(knowledge)
      ```
- Interact with Agent
  - Interview
    - ```agent.interview(user=user, query='สวัสดี')```
- Save Agent
    - ```agent.save_state_memory()```
      - This function will save 3 files in ```agents/{name of agent}/data``` and 1 json file, then all files will upload to GCP Storage and fileURL will store in GCP Datastore:
        - ```index.faiss```, ```index.pkl```, ```memory_stream.pkl```