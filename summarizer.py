class AISummarizerPipeline:
    def execute_summary(self, text_payload):
        sentences = text_payload.split('.')
        return {"metrics": [s.strip() for s in sentences[:2]]}

if __name__ == "__main__":
    pipeline = AISummarizerPipeline()
    print(pipeline.execute_summary("The ATmega328P is an MCU. It uses RISC architecture."))

