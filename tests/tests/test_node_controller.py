from src.node_controller import NodeController

def test_node_controller_initialization():
    controller = NodeController()
    assert controller.pipeline is not None
