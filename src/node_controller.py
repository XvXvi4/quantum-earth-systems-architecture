from src.pipeline_manager import PipelineManager

class NodeController:
    def __init__(self):
        self.pipeline = PipelineManager()

    def start(self):
        print("Node Controller started.")
        self.pipeline.run_pipeline()

if __name__ == "__main__":
    controller = NodeController()
    controller.start()
