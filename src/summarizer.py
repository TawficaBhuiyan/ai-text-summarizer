import os
from dotenv import load_dotenv


load_dotenv()


USE_LOCAL_MODEL = os.getenv("USE_LOCAL_MODEL", "false").lower() == "true"


if USE_LOCAL_MODEL:
    from transformers import pipeline


    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


    def summarize_text(text: str) -> str:
        result = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return result[0]['summary_text']


else:
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import PromptTemplate
    from langchain_core.output_parsers import StrOutputParser


    def summarize_text(text: str) -> str:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
        prompt = PromptTemplate(
            input_variables=["text"],
            template="Summarize the following text in 3-4 bullet points:\n\n{text}"
        )
        chain = prompt | llm | StrOutputParser()
        summary = chain.invoke({"text": text})
        return summary
