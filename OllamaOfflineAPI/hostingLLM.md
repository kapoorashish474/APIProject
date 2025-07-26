# Steps to Fetch LLM from Hugging Face and Host Locally with Ollama (macOS, zsh)

## 1. Install Ollama
```zsh
curl -fsSL https://ollama.ai/install.sh | sh
```

## 2. Start Ollama Service
```zsh
ollama serve
```

## 3. Pull a Model from Hugging Face
```zsh
# Example: Pull Llama 2
ollama pull llama2

# Other models you can try:
ollama pull mistral
ollama pull codellama
ollama pull phi
ollama pull gemma2
```

## 4. (Optional) Create a Custom Model from Hugging Face
1. Create a `Modelfile`:
```zsh
touch Modelfile
```
2. Add configuration to `Modelfile` (example):
```
FROM llama2
PARAMETER temperature 0.7
PARAMETER top_p 0.9
SYSTEM "You are a helpful AI assistant."
```
3. Build your custom model:
```zsh
ollama create mymodel -f Modelfile
```

## 5. Run the Model
```zsh
# Run a pulled model
ollama run llama2

# Or run your custom model
ollama run mymodel
```

## 6. (Optional) Use the API
```zsh
# Ollama API runs by default on localhost:11434
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Hello, how are you?"
}'
```

## 7. Manage Models
```zsh
ollama list         # List installed models
ollama rm modelname # Remove a model
ollama show modelname # Show model info
```

## 8. Troubleshooting
- Ensure you have enough disk space (models can be large)
- If you have issues, check logs: `ollama logs`
- For best performance, use a Mac with Apple Silicon (M1/M2/M3)
