# DukeRagHub

A **RAG-powered LLM** designed to help Duke students find the classes they need.

---

## **Motivation**

The goal behind this project is to enable Duke students to leverage LLMs during the course selection process. Currently, the process involves navigating through dropdown menus, filters, and extensive scrolling to find the right classes. This project simplifies that by using language-based queries to identify classes students want—and more importantly—**need**.

This project combines:
- A foundational model (**GPT-4o-mini**),
- A knowledge base (**RAG**),
- And a user-friendly client that allows natural language queries on the Duke course catalog.

---

## **Design**

The project is built with heavy reliance on **OpenAI technologies**:
- **OpenAI API**: Provides access to foundational model endpoints, ensuring top-tier performance.
- **OpenAI Vector Storage**: Creates a knowledge base of Duke classes by dividing course data into manageable chunks. Each chunk is transformed into an **embedding** that captures the meaning of the text and enables similarity searches.
- **OpenAI Assistants API**: Allows the LLM to respond to queries with specificity, referencing the knowledge base, and ensuring answers are relevant to Duke classes.

---

### **Data Pipeline**

Using **BeautifulSoup**, a Python web scraping library, a script was built to extract course data from **Coursicle.com**, saving it into a `.txt` file for processing.

Sample of the scraped data:

| Course ID | Subject Catalog | Subject Description          | Course Description                                                                                                                                                                                                                             | Attribute Formal | Attribute Description |
|-----------|------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------------|
| 19        | AMES 165S        | THE WORLD OF JAPANESE POP CULT | "An examination of modern Japanese culture through a variety of media including literary texts, cultural representations, and films. Different material each year."                                                                          | CZ               | Civilizations          |
| 587       | ECON 344         | HISTORY OF ART MARKETS       | "Analytical survey of emergence of art markets, interactions between market behavior(s), visual/media culture(s)... and methodological implications of art market research at interface of Economics, Art History, Law and Visual Studies." | SS               | Social Sciences        |
| 2606      | ECE 353          | INTRO TO OPERATING SYSTM     | "Basic concepts and principles of multiprogrammed operating systems. Processes, interprocess communication, CPU scheduling, mutual exclusion, deadlocks, memory management, I/O devices, file systems, protection mechanisms..."             | QS               | Quantitative Studies   |

---

## **Application**

The application is built using **Streamlit** to create an interactive web-based client. The client:
1. Loads the respective OpenAI API key.
2. Fetches the vector store created from the knowledge base.
3. Provides a user-friendly interface to query Duke courses via natural language.

---

## **Implementation**

### **Main Functionality**

The primary functionality is encapsulated in a `CourseSearchApp` class that loads environment variables for the OpenAI assistant and API key and integrates the model into the application. Below is a simplified explanation:

1. Load `.env` variables.
2. Initialize OpenAI APIs with the keys.
3. Query the model and return real-time responses.

---

## **Future Work**

- Expanding the knowledge base to include additional course attributes like professor ratings or schedule compatibility.
- Integrating a recommendation system to suggest classes based on student preferences and academic history.
- Allowing collaborative features for students to share and discuss courses.

---
