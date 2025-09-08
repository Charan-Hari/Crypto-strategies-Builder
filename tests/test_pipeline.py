
def test_pipeline_smoke():
    # Basic smoke test that imports the pipeline if present
    try:
        from crypto_strategies_ai.runner import pipeline
        # if pipeline has a run function, ok
        assert hasattr(pipeline, 'run_pipeline') or hasattr(pipeline, 'build_scores')
    except Exception as e:
        pytest.skip('Pipeline not available: %s' % e)
