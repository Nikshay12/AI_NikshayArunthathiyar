from neo4j import GraphDatabase
import spacy

nlp = spacy.load("en_core_web_sm")
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j","neo4jpassword"))

def add_sentence(tx, concept_name, sentence_text):
    tx.run("""
      MERGE (c:Concept {name:$c})
      MERGE (s:Sentence {text:$s})
      MERGE (c)-[:MENTIONED_IN]->(s)
    """, c=concept_name, s=sentence_text)

def ingest_text(concept_name, text):
    doc = nlp(text)
    with driver.session() as session:
        for sent in doc.sents:
            session.write_transaction(add_sentence, concept_name, sent.text)

if __name__ == "__main__":
    sample = "Newton's First Law: An object at rest stays at rest unless acted upon by a force."
    ingest_text("Newton's First Law", sample)
    print("Ingested sample into Neo4j")

