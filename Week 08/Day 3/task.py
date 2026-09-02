import pandas as pd
import re
from transformers import pipeline

# 1. LOAD DATASET

df = pd.read_csv("Week 08/Day 3/ner_dataset.csv")
print("DATASET")
print(df)
print("\nDataset Shape:")
print(df.shape)
print("\nDataset Columns:")
print(df.columns)

# 2. CREATE NER PIPELINE

ner_pipeline = pipeline(
    "token-classification",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

# 3. REGEX PATTERNS

# DATE Pattern
date_pattern = re.compile(
    r"\b(?:\d{1,2}\s+"
    r"(?:January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+\d{4})\b"
)

# TIME Pattern
time_pattern = re.compile(
    r"\b\d{1,2}:\d{2}\s?(?:AM|PM)\b",
    re.IGNORECASE
)

# MONEY Pattern
money_pattern = re.compile(
    r"\$\s?\d+(?:,\d{3})*(?:\.\d+)?(?:\s?(?:million|billion|thousand))?",
    re.IGNORECASE
)

# PERCENT Pattern
percent_pattern = re.compile(
    r"\b\d+(?:\.\d+)?%"
)

# 4. FUNCTION TO EXTRACT REGEX ENTITIES
def extract_regex_entities(text):
    entities = []

    # DATE
    for match in date_pattern.finditer(text):
        entities.append({
            "entity": match.group(),
            "entity_type": "DATE",
            "start": match.start(),
            "end": match.end(),
            "confidence": 1.0
        })

    # TIME
    for match in time_pattern.finditer(text):
        entities.append({
            "entity": match.group(),
            "entity_type": "TIME",
            "start": match.start(),
            "end": match.end(),
            "confidence": 1.0
        })

    # MONEY
    for match in money_pattern.finditer(text):
        entities.append({
            "entity": match.group(),
            "entity_type": "MONEY",
            "start": match.start(),
            "end": match.end(),
            "confidence": 1.0
        })

    # PERCENT
    for match in percent_pattern.finditer(text):
        entities.append({
            "entity": match.group(),
            "entity_type": "PERCENT",
            "start": match.start(),
            "end": match.end(),
            "confidence": 1.0
        })
    return entities

# 5. PROCESS MULTIPLE DOCUMENTS
all_entities = []
for _, row in df.iterrows():
    document_id = row["document_id"]
    text = row["text"]

    # NER MODEL ENTITIES
    ner_results = ner_pipeline(text)
    for entity in ner_results:
        entity_text = entity["word"]
        entity_type = entity["entity_group"]
        # Convert model labels to assignment labels
        if entity_type == "PER":
            entity_type = "PERSON"

        elif entity_type == "ORG":
            entity_type = "ORGANIZATION"

        elif entity_type == "LOC":
            entity_type = "LOCATION"

        else:
            entity_type = "OTHER"

        all_entities.append({
            "document_id": document_id,
            "entity": entity_text,
            "entity_type": entity_type,
            "confidence": round(float(entity["score"]), 4)
        })

    # DATE, TIME, MONEY, PERCENT
    regex_entities = extract_regex_entities(text)
    for entity in regex_entities:
        all_entities.append({
            "document_id": document_id,
            "entity": entity["entity"],
            "entity_type": entity["entity_type"],
            "confidence": entity["confidence"]
        })

# 6. CREATE PANDAS DATAFRAME
entities_df = pd.DataFrame(all_entities)

# 7. SORT RESULTS
entities_df = entities_df.sort_values(
    by=["document_id", "entity_type"]
).reset_index(drop=True)
print("EXTRACTED ENTITIES")
print(entities_df.to_string(index=False))

# 8. ENTITY TYPE COUNTS
entity_type_counts = (
    entities_df["entity_type"]
    .value_counts()
)
print("ENTITY TYPE COUNTS")
print(entity_type_counts)

# 9. FREQUENTLY OCCURRING ENTITIES
entity_frequency = (
    entities_df["entity"]
    .value_counts()
)
print("FREQUENTLY OCCURRING ENTITIES")
print(entity_frequency)

# 10. ENTITY FREQUENCY WITH TYPES
entity_frequency_with_type = (
    entities_df
    .groupby(["entity", "entity_type"])
    .size()
    .reset_index(name="frequency")
    .sort_values(
        by="frequency",
        ascending=False
    )
)
print("ENTITY FREQUENCY WITH ENTITY TYPE")
print(
    entity_frequency_with_type.to_string(index=False)
)

# 11. TOP 10 MOST FREQUENT ENTITIES
top_entities = entity_frequency_with_type.head(10)
print("TOP 10 MOST FREQUENT ENTITIES")
print(
    top_entities.to_string(index=False)
)
# 12. EXPORT ALL RESULTS TO CSV
output_file = "Week 08/Day 3/ner_results.csv"
entities_df.to_csv(
    output_file,
    index=False
)

print("CSV EXPORT")
print(f"NER results exported successfully!")
print(f"File: {output_file}")