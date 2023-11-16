from qualtop_llmapi.main import app
import uvicorn

def main():
    uvicorn.run(app,
                host="0.0.0.0",
                port=8070, 
                log_level="debug", 
                workers=1)

if __name__ == "__main__":
    main()
