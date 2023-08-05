# Thumbor Prometheus Metrics Plugin

Collecting Thumbor runtime metrics using the prometheus_client and exposes them
via an HTTP endpoint on a configurable port.

## Installation

```bash
# latest stable
pip install dffrntlab_tc_prometheus
```

## Configuration

```python
# thumbor.conf
METRICS = 'tc_prometheus.metrics.prometheus_metrics'

# optional with defaults
PROMETHEUS_SCRAPE_PORT = 8000 # Port the prometheus client should listen on
```

# dffrntlab part

## Where it is

https://pypi.org/project/dffrntlab-tc-prometheus/

## Push to PyPi

```
python setup.py sdist bdist_wheel
# install twine if you don't have
# pip install twine
twine upload dist/*
```

Now we use this profile to push packages: https://pypi.org/user/maximka777/ _(need to register dffrntlab one)_.
