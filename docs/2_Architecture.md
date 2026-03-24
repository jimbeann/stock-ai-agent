# Technical Architecture

## System Overview

The system is designed as a modular AI agent with tool-based architecture and local LLM inference.

## Components

### 1. User Interface

* Web-based UI using HTML/CSS
* Input: Stock symbol
* Output: Analysis + chart

### 2. Backend (FastAPI)

* Handles user requests
* Orchestrates agent workflow

### 3. Agent Layer

Responsible for:

* Calling tools
* Managing data flow
* Constructing LLM prompts

### 4. Tool Layer

#### Financial Tool

* Fetches stock data using Yahoo Finance

#### News Tool

* Fetches recent news using NewsAPI

#### Sentiment Engine

* Performs lightweight sentiment scoring

### 5. RAG Layer

* Stores news embeddings
* Retrieves relevant context using vector search (ChromaDB)

### 6. LLM Layer

* Local model via Ollama (Phi-3 / Mistral)
* Generates final analysis

## Data Flow

User Input → Backend → Agent → Tools → RAG → LLM → Response

## Key Design Principles

* Modular architecture
* Separation of concerns
* Lightweight and scalable
* Local-first AI deployment

## Deployment Model

* Runs on Linux (Lubuntu)
* Minimal hardware requirements (4GB–8GB RAM)
* No dependency on external LLM APIs
