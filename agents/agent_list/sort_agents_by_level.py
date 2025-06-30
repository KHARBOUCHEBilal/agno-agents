import os
import shutil

levels = {
    "level_1": [
        "agent_with_instructions", "agent_with_tools", "basic_agent", "readme_generator",
        "recipe_creator", "translation_agent", "web_extraction_agent", "movie_recommedation",
        "book_recommendation"
    ],
    "level_2": [
        "agent_with_knowledge", "agent_with_storage", "deep_knowledge", "recipe_rag_image",
        "research_agent", "research_agent_exa", "shopping_partner", "youtube_agent"
    ],
    "level_3": [
        "agent_with_memory", "agent_with_reasoning", "finance_agent_with_memory",
        "reasoning_finance_agent", "thinking_finance_agent", "study_partner",
        "meeting_summarizer_agent"
    ],
    "level_4": [
        "agent_team", "agno_support_agent", "media_trend_analysis_agent",
        "social_media_agent", "competitor_analysis_agent", "legal_consultant"
    ],
    "level_5": [
        "agno_assist", "airbnb_mcp", "finance_agent", "deep_research_agent_exa"
    ]
}

# Create level folders if not exist
for level in levels:
    os.makedirs(level, exist_ok=True)

# Move folders to corresponding level
for level, folders in levels.items():
    for folder in folders:
        if os.path.exists(folder):
            shutil.move(folder, os.path.join(level, folder))
            print(f"Moved {folder} -> {level}")
        else:
            print(f"⚠️ Folder not found: {folder}")