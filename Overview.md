# Overview LingQGPT
## What is this document?
I have decided that from this project onward, I will start writing an overview document for each and every single one of them. 
- This document will have an overview of what I'm making and maybe some thoughts I have while making the program.
- The main part of this document should always be the functional requirements with which I will make the code itself.
- This document should also help me or anyone else pick the project back up where it was left since it will make clear what I want to make and maybe even what I have already made.

## Project Description

An AI project that uses the LingQ API to query and analyse my Japanese learning. It will assist in picking and generating stories based on my progression and interests.

## Requirements
1. LingQ API integrations
	- Query existing stories
	- Query existing LingQs
	- Create new courses
	- Add new content
	- Update existing stories with correct tagging
2. OpenAPI integration for story generation
	- Generate stories based on interests
	- Generate stories based on LingQs
	- Estimate story difficulty 
	- Estimate story tags
	- Write continuations to existing stories
	- Evaluate how much of the story the reader understands
3. Data Analysis
	- Get a list of most common words for both learned and not yet learned
	- View LingQs related to words that are already learned
	- Estimate which words should be retested to see if they are indeed still in known

## Thoughts

I'm still very unsure about whether or not a vector database such as chromadb would be beneficial for this project. I will have to think about it more before I decide, for now I will start implementing without.

I wish I could make this project in something other than Python but I believe it would be best to use Python considering I will use OpenAI API and maybe also ChromaDB. I could also consider using Pinecone API instead since that would make it all go over the internet. 
I'm not 100% sure which programming language I want to use yet, however I will start exploring the API in Python and go from htere.
