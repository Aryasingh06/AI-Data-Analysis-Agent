from tools import load_dataset
from agents import CleaningAgent, VisualizationAgent, InsightAgent

print("=== AI Data Analysis Assistant ===")

# Load dataset
df = load_dataset("dataset.csv")

# Initialize agents
cleaner = CleaningAgent()
visualizer = VisualizationAgent()
insight = InsightAgent()

# Multi-agent workflow
clean_df = cleaner.run(df)

visualizer.run(clean_df)

summary = insight.run(clean_df)

print(summary)

query = input("Ask your data question: ")

if "rows" in query.lower():
    print(f"Total Rows: {clean_df.shape[0]}")

elif "columns" in query.lower():
    print(f"Total Columns: {clean_df.shape[1]}")

elif "summary" in query.lower():
    print(clean_df.describe())

else:
    print("Question not recognized.")