from src.pipeline_manager import PipelineManager

def test_pipeline_manager_initialization():
    pipeline = PipelineManager()
    assert pipeline.quantum_ai is not None
    assert pipeline.multi_agent is not None
    assert pipeline.private_key is not None
    assert pipeline.public_key is not None

def test_pipeline_manager_run_pipeline():
    pipeline = PipelineManager()
    try:
        pipeline.run_pipeline()
        assert True
    except Exception:
        assert False
