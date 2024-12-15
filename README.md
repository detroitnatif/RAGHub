### DukeRagHub
## A RAG powered LLM designed to help students find the classes they need. 

Motivation: The goal behind this project is to enable Duke Students to leverage LLMs during the course selection process. Right now there is a series of dropdown menus, filters, and a whole lot of scrolling until students find the classes they want, but more importantly that they need. This project will leverage a foundational model (GPT-4o-mini), a knowledge base (RAG), and a client that allows students to use language to perform queries on the classes at hand.

Design: The design of this project will leverage OpenAI technologies heavily. Through the OpenAI API, users can utilize their model endpoints to use the most powerful foundational models on the market (No, that is not up for debate). This project also uses the OpenAI Vector Storage, which has allowed me to create a knowledge base of Duke classes. The classes are divided into manageable chunks, with each chunk transformed into an embedding. These embeddings capture the meaning of the text, and allow similarity searches. Next, I leverage the OpenAI Assistants API, which allows me to pass a very specific system message to the LLM, specifying the role the LLM is serving and what knowledge base to answer from. 
Data: Using BeautifulSoup, a web scraper python library, I created a script to gather all the course data from Coursicle.com, and compile it into a .txt file. A sample of this data is below:
Course ID | Subject Catalog| Subject Description | Course Description | Attribute Formal | Description
19 AMES 165S THE WORLD OF JAPANESE POP CULT "An examination of modern Japanese culture through a variety of media including literary texts, cultural representations, and films. Different material each year." (CZ) Civilizations
587 ECON 344 HISTORY OF ART MARKETS "Analytical survey of emergence of art markets, interactions between market behavior(s), visual/media culture(s). Addresses questions regarding the nature of art markets, the specificity of art markets and the application of economic and historical methodologies, how and where players in local markets throughout the world shape visual culture(s), effective causes for art consumption, taste, fashion throughout ages, and methodological implications of art market research at interface of Economics, Art History, Law and Visual Studies." (SS) Social Sciences
2606 ECE 353 INTRO TO OPERATING SYSTM "Basic concepts and principles of multiprogrammed operating systems. Processes, interprocess communication, CPU scheduling, mutual exclusion, deadlocks, memory management, I/O devices, file systems, protection mechanisms. Also taught as Electrical and Computer Engineering 353. Prerequisites: Computer Science 201; and either of Computer Science 210D, Computer Science 250D or Electrical and Computer Engineering 250D." (QS) Quantitative Studies





Application: I decided to use StreamLit to design the LLM client as well to host the web application. This client will load the respective OpenAI API key, as well as the vector store from the assistant client so it can perform RAG:
class CourseSearchApp:
   def __init__(self):
       load_dotenv(find_dotenv())
       self.assistant_id = os.getenv("ASSISTANT_ID")
       self.openai_key = os.getenv("OPENAI_API_KEY")
       self.llm = OpenAI()

The call to the OpenAI is simple, and gets a response from the model endpoint: 
stream = self.llm.beta.threads.create_and_run(
               assistant_id=self.assistant_id,
               thread={"messages": [{'role': 'user', 'content': api_message}]},
               stream=True)

I elected to use the “Stream” capability, so the message is streamed as the tokens are received by the client. 
The API creates a thread which the messages are added to, creating context that the user can continue discussing with. 
If the question is outside of the RAG knowledge base, the system message is prompted to return that the class does not exist, rather than hallucinating a class.
The application is using GPT-4o as the base model, which prices at $0.150 / 1M for input tokens, and $0.600 / 1M for output tokens. So cheap I'll provide the key!
