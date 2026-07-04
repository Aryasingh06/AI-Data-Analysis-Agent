from tools import load_dataset, clean_data, dataset_summary, create_chart

class CleaningAgent:

    def run(self, df):

        print("[Cleaning Agent] Cleaning dataset...")
        return clean_data(df)

class VisualizationAgent:

    def run(self, df):

        print("[Visualization Agent] Creating charts...")
        create_chart(df)

class InsightAgent:

    def run(self, df):

        print("[Insight Agent] Generating insights...")
        return dataset_summary(df)