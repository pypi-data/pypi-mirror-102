import pytest
from mlserver.settings import ModelParameters, ModelSettings
from mlserver.types import InferenceRequest, RequestInput
from mlserver.utils import to_ndarray

from tempo import Model
from tempo.mlserver import InferenceRuntime
from tempo.serve.loader import save


@pytest.fixture
def model_settings(custom_model: Model) -> ModelSettings:
    save(custom_model, save_env=False)
    pipeline_uri = custom_model.details.local_folder

    return ModelSettings(
        name="sum-model",
        parameters=ModelParameters(uri=pipeline_uri),
    )


@pytest.fixture
def inference_request() -> InferenceRequest:
    return InferenceRequest(inputs=[RequestInput(name="input-0", shape=[4], data=[1, 2, 3, 4], datatype="FP32")])


@pytest.fixture
async def model(model_settings: ModelSettings) -> InferenceRuntime:
    model = InferenceRuntime(model_settings)
    await model.load()

    return model


def test_load(model: InferenceRuntime):
    assert model.ready
    assert isinstance(model._pipeline, Model)


async def test_predict(
    model: InferenceRuntime,
    inference_request: InferenceRequest,
    custom_model: Model,
):
    res = await model.predict(inference_request)

    assert len(res.outputs) == 1

    pipeline_input = to_ndarray(inference_request.inputs[0])
    custom_model.get_tempo().use_remote = False  # ensure direct call to class does not try to do remote
    expected_output = custom_model(pipeline_input)

    pipeline_output = res.outputs[0].data

    assert expected_output.tolist() == pipeline_output
